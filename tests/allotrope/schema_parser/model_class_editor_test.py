from io import StringIO

from allotropy.allotrope.schema_parser.model_class_editor import (
    _parse_field_types,
    ClassLines,
    create_class_lines,
    DataclassField,
    DataClassLines,
    get_manifest_from_schema_path,
    ModelClassEditor,
)


def lines_from_multistring(lines: str) -> list[str]:
    return list(StringIO(lines.strip("\n") + "\n").readlines())


def class_lines_from_multistring(lines: str) -> ClassLines:
    return create_class_lines(lines_from_multistring(lines))


def data_class_lines_from_multistring(lines: str) -> DataClassLines:
    class_lines = create_class_lines(lines_from_multistring(lines))
    assert isinstance(class_lines, DataClassLines)
    return class_lines


def validate_lines_against_multistring(class_lines: ClassLines, lines: str) -> None:
    assert class_lines == class_lines_from_multistring(lines)


def test_parse_field_types() -> None:
    assert _parse_field_types("str") == {"str"}
    assert _parse_field_types("Union[str,int]") == {"int", "str"}
    assert _parse_field_types("Union[str,str,str]") == {"str"}
    assert _parse_field_types("Union[List[str],int]") == {"int", "List[str]"}
    assert _parse_field_types("List[Union[str,str,str]]") == {"List[str]"}
    assert _parse_field_types("list[str,str,str]") == {"list[str]"}
    assert _parse_field_types("tuple[str,int]") == {"tuple[Union[int,str]]"}
    assert _parse_field_types("set[int,int]") == {"set[int]"}
    assert _parse_field_types("dict[str,Any]") == {"dict[str,Any]"}
    assert _parse_field_types("dict[str,list[str,str]]") == {"dict[str,list[str]]"}
    assert _parse_field_types("dict[Union[int,float],str]") == {
        "dict[Union[int,float],str]"
    }
    assert _parse_field_types("List[Union[Type1,Type2,Type3,]]") == {
        "List[Union[Type1,Type2,Type3]]"
    }


def test_get_manifest_from_schema_path() -> None:
    schema_path = "src/allotropy/allotrope/schemas/cell_counting/BENCHLING/2023/09/cell-counting.json"
    expected = "http://purl.allotrope.org/manifests/cell_counting/BENCHLING/2023/09/cell-counting.manifest"
    assert get_manifest_from_schema_path(schema_path) == expected


def test_modify_file_removes_skipped_and_unused_classes() -> None:
    classes_to_skip = {"ClassA"}
    imports_to_add = {"definitions": {"Thing1", "Thing2"}}
    editor = ModelClassEditor("fake_manifest", classes_to_skip, imports_to_add)

    model_file_contents = """
import json
from typing import Union


@dataclass(frozen=True)
class ClassA:
    key: str
    value: str


@dataclass(frozen=True)
class ClassB:
    key: str
    value: str


@dataclass(frozen=True)
class UnusedClass:
    value: int


@dataclass(frozen=True)
class Model:
    key: str
    value: str
    b_thing: ClassB
"""

    expected = """
import json
from typing import Union

from allotropy.allotrope.models.shared.definitions import Thing1, Thing2


@dataclass(frozen=True)
class ClassB:
    key: str
    value: str


@dataclass(frozen=True)
class Model:
    key: str
    value: str
    b_thing: ClassB
    manifest: str=\"fake_manifest\"
"""
    assert editor.modify_file(model_file_contents) == expected


def test_class_lines_dataclass_parent_classes() -> None:
    class_lines = class_lines_from_multistring(
        """
@dataclass(frozen=True)
class ClassA:
    key: str
    value: str
"""
    )
    assert class_lines.class_name == "ClassA"
    assert isinstance(class_lines, DataClassLines)
    assert class_lines.parent_class_names == []

    class_lines = class_lines_from_multistring(
        """
@dataclass(frozen=True)
class ClassB(ClassA):
    key: str
    value: str
"""
    )
    assert class_lines.class_name == "ClassB"
    assert isinstance(class_lines, DataClassLines)
    assert class_lines.parent_class_names == ["ClassA"]

    class_lines = class_lines_from_multistring(
        """
@dataclass(frozen=True)
class ClassB(ClassA, ClassC):
    key: str
    value: str
"""
    )
    assert class_lines.class_name == "ClassB"
    assert isinstance(class_lines, DataClassLines)
    assert class_lines.parent_class_names == ["ClassA", "ClassC"]

    class_lines = class_lines_from_multistring(
        """
@dataclass(frozen=True)
class ClassB(
    ClassA,
    ClassC
):
    key: str
    value: str
"""
    )
    assert class_lines.class_name == "ClassB"
    assert isinstance(class_lines, DataClassLines)
    assert class_lines.parent_class_names == ["ClassA", "ClassC"]


def test_class_lines_dataclass_field_parsing() -> None:
    class_lines = data_class_lines_from_multistring(
        """
@dataclass
class Test:
    key: str
    value: str
"""
    )
    assert class_lines.has_required_fields()
    assert not class_lines.has_optional_fields()
    assert class_lines.fields == {
        "key": DataclassField(
            "key", is_required=True, default_value=None, field_types={"str"}
        ),
        "value": DataclassField(
            "value", is_required=True, default_value=None, field_types={"str"}
        ),
    }

    class_lines = data_class_lines_from_multistring(
        """
@dataclass
class Test:
    key: Optional[str]
    value: Optional[str]="something"
    int_value:Optional[int]=1
"""
    )
    assert not class_lines.has_required_fields()
    assert class_lines.has_optional_fields()
    assert class_lines.fields == {
        "key": DataclassField(
            "key", is_required=False, default_value=None, field_types={"str"}
        ),
        "value": DataclassField(
            "value", is_required=False, default_value='"something"', field_types={"str"}
        ),
        "int_value": DataclassField(
            "int_value", is_required=False, default_value="1", field_types={"int"}
        ),
    }

    class_lines = data_class_lines_from_multistring(
        """
@dataclass
class Test:
    key: str
    item: Union[
        Item1,
        str
    ]
    value: Optional[
        str
    ]
    other_key: Optional[str]=None
"""
    )
    assert class_lines.has_required_fields()
    assert class_lines.has_optional_fields()
    assert class_lines.fields == {
        "key": DataclassField(
            "key", is_required=True, default_value=None, field_types={"str"}
        ),
        "item": DataclassField(
            "item", is_required=True, default_value=None, field_types={"Item1", "str"}
        ),
        "value": DataclassField(
            "value", is_required=False, default_value=None, field_types={"str"}
        ),
        "other_key": DataclassField(
            "other_key", is_required=False, default_value="None", field_types={"str"}
        ),
    }


def test_class_lines_merge_parent() -> None:
    parent_class = data_class_lines_from_multistring(
        """
@dataclass
class ClassA:
    a_required: str
    a_optional: Optional[str]
"""
    )
    child_class = data_class_lines_from_multistring(
        """
@dataclass
class ClassB(ClassA):
    b_required: str
    b_optional: Optional[str]
"""
    )

    validate_lines_against_multistring(
        child_class.merge_parent(parent_class),
        """
@dataclass
class ClassB:
    b_required: str
    a_required: str
    b_optional: Optional[str]
    a_optional: Optional[str]
""",
    )


def test_class_lines_merge_parent_multiple() -> None:
    parent_class = data_class_lines_from_multistring(
        """
@dataclass
class ClassA:
    a_required: str
    a_optional: Optional[str]
"""
    )
    child_class = data_class_lines_from_multistring(
        """
@dataclass
class ClassB(ClassA, ClassC):
    b_required: str
    b_optional: Optional[
        str
    ]
"""
    )
    validate_lines_against_multistring(
        child_class.merge_parent(parent_class),
        """
@dataclass
class ClassB(ClassC):
    b_required: str
    a_required: str
    b_optional: Optional[str]
    a_optional: Optional[str]
""",
    )


def test_class_lines_dataclass_eq() -> None:
    class_lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item:
    key: Union[str, int]
"""
    )

    other_lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: Union[
        str,
        int
    ]
"""
    )
    assert class_lines == other_lines


def test_class_lines_typedef_eq() -> None:
    lines = class_lines_from_multistring(
        """
TDateTimeStampValue1 = Union[str, TDateTimeStampValue2]
"""
    )
    other_lines = class_lines_from_multistring(
        """
TDateTimeStampValue = Union[str, TDateTimeStampValue3]
"""
    )
    assert lines != other_lines

    lines = class_lines_from_multistring(
        """
TDateTimeStampValue1 = Union[str, TDateTimeStampValue2]
"""
    )
    other_lines = class_lines_from_multistring(
        """
TDateTimeStampValue = Union[str, TDateTimeStampValue2]
"""
    )
    assert lines == other_lines


def test_class_lines_dataclass_should_merge() -> None:
    lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item:
    key: str
    special: Optional[int]
"""
    )
    other_lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: str
    other_special: Optional[int]
"""
    )
    assert lines.should_merge(other_lines)

    # Extra required key will not match
    other_lines_extra_required_key = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: str
    other_special: int
"""
    )
    assert not lines.should_merge(other_lines_extra_required_key)

    # Missing required key will not match
    other_lines_missing_required_key = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    other_special: Optional[int]
"""
    )
    assert not lines.should_merge(other_lines_missing_required_key)

    # Shared key that does not agree on optional/required will not match
    other_lines_non_matching_shared_key = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: Optional[str]
"""
    )
    assert not lines.should_merge(other_lines_non_matching_shared_key)


def test_class_lines_merge_similar() -> None:
    lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item:
    key: str
    other_key: str
    special: Optional[int]
"""
    )

    other_lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: str
    other_key: Union[
        int,
        float,
    ]
    other_special: Optional[str]
"""
    )

    validate_lines_against_multistring(
        lines.merge_similar(other_lines),
        """
@dataclass(frozen=True)
class Item:
    key: str
    other_key: Union[float,int,str]
    special: Optional[int]
    other_special: Optional[str]
""",
    )


def test_class_lines_merge_similar_with_lists() -> None:
    lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item:
    key: list[str]
"""
    )

    other_lines = data_class_lines_from_multistring(
        """
@dataclass(frozen=True)
class Item1:
    key: list[int]
"""
    )

    validate_lines_against_multistring(
        lines.merge_similar(other_lines),
        """
@dataclass(frozen=True)
class Item:
    key: Union[list[int],list[str]]
""",
    )


def test_modify_file_handles_merging_parent_classes_and_removing_unused_parents() -> None:
    editor = ModelClassEditor("fake_manifest", classes_to_skip=set(), imports_to_add={})

    model_file_contents = """
import json
from typing import Union


@dataclass(frozen=True)
class OptionalFieldParentClass:
    optional_parent: Optional[str]


@dataclass(frozen=True)
class RequiredFieldChildClass(OptionalFieldParentClass):
    required_child: str


@dataclass(frozen=True)
class Model:
    key: str
    value: str
    b_thing: RequiredFieldChildClass
"""

    expected = """
import json
from typing import Union


@dataclass(frozen=True)
class RequiredFieldChildClass:
    required_child: str
    optional_parent: Optional[str]


@dataclass(frozen=True)
class Model:
    key: str
    value: str
    b_thing: RequiredFieldChildClass
    manifest: str=\"fake_manifest\"
"""
    assert editor.modify_file(model_file_contents) == expected


def test_modify_file_handles_does_not_merge_parents_when_not_required() -> None:
    editor = ModelClassEditor("fake_manifest", classes_to_skip=set(), imports_to_add={})

    model_file_contents = """
import json
from typing import Union


@dataclass(frozen=True)
class RequiredFieldParentClass:
    required_parent: str


@dataclass(frozen=True)
class OptionalFieldParentClass:
    optional_parent: Optional[str]


@dataclass(frozen=True)
class RequiredFieldChildClassUsingRequiredParent(RequiredFieldParentClass):
    required_child: str


@dataclass(frozen=True)
class RequiredFieldChildUsingOptionalParent(OptionalFieldParentClass):
    required_child: str


@dataclass(frozen=True)
class OptionalFieldChildClass(OptionalFieldParentClass):
    optional_child: Optional[str]


@dataclass(frozen=True)
class Model:
    key: str
    thing1: RequiredFieldChildClassUsingRequiredParent
    thing2: RequiredFieldChildUsingOptionalParent
    thing3: OptionalFieldChildClass
"""

    expected = """
import json
from typing import Union


@dataclass(frozen=True)
class RequiredFieldParentClass:
    required_parent: str


@dataclass(frozen=True)
class OptionalFieldParentClass:
    optional_parent: Optional[str]


@dataclass(frozen=True)
class RequiredFieldChildClassUsingRequiredParent(RequiredFieldParentClass):
    required_child: str


@dataclass(frozen=True)
class RequiredFieldChildUsingOptionalParent:
    required_child: str
    optional_parent: Optional[str]


@dataclass(frozen=True)
class OptionalFieldChildClass(OptionalFieldParentClass):
    optional_child: Optional[str]


@dataclass(frozen=True)
class Model:
    key: str
    thing1: RequiredFieldChildClassUsingRequiredParent
    thing2: RequiredFieldChildUsingOptionalParent
    thing3: OptionalFieldChildClass
    manifest: str = \"fake_manifest\"
"""
    assert editor.modify_file(model_file_contents) == expected


def test_modify_file_removes_identical_classes() -> None:
    editor = ModelClassEditor("fake_manifest", classes_to_skip=set(), imports_to_add={})

    model_file_contents = """
import json


@dataclass(frozen=True)
class Item:
    key: str


@dataclass(frozen=True)
class Item1:
    key: str


@dataclass(frozen=True)
class Item2:
    key: str


@dataclass(frozen=True)
class Item12:
    value: str


@dataclass(frozen=True)
class ParentItem:
    item: Item1
    other_item: Optional[Item2]


@dataclass(frozen=True)
class Model:
    item: Item
    thing: ParentItem
    other_item: Optional[Item12]
"""

    expected = """
import json


@dataclass(frozen=True)
class Item:
    key: str


@dataclass(frozen=True)
class Item12:
    value: str


@dataclass(frozen=True)
class ParentItem:
    item: Item
    other_item: Optional[Item]


@dataclass(frozen=True)
class Model:
    item: Item
    thing: ParentItem
    manifest: str=\"fake_manifest\"
    other_item: Optional[Item12]
"""
    assert editor.modify_file(model_file_contents) == expected


def test_modify_file_merges_similar_classes() -> None:
    editor = ModelClassEditor("fake_manifest", classes_to_skip=set(), imports_to_add={})

    model_file_contents = """
import json


@dataclass(frozen=True)
class Item:
    key: str
    disagree: int


@dataclass(frozen=True)
class Item1:
    key: str
    disagree: str
    extra_key: Optional[str]="test"


@dataclass(frozen=True)
class Item2:
    key: str
    disagree: str
    extra_key: str


@dataclass(frozen=True)
class Model:
    item: Item
    item1: Item1
    item2: Item2
"""

    expected = """
import json


@dataclass(frozen=True)
class Item:
    key: str
    disagree: Union[int,str]
    extra_key: Optional[str]="test"


@dataclass(frozen=True)
class Item2:
    key: str
    disagree: str
    extra_key: str


@dataclass(frozen=True)
class Model:
    item: Item
    item1: Item
    item2: Item2
    manifest: str=\"fake_manifest\"
"""
    assert editor.modify_file(model_file_contents) == expected
