import pytest
from typing import Union, List, Callable, Dict, Optional, Any
from flask_docspec.models import BaseModel
from flask_docspec.util import dget



def test_callable_structure():
    class NoArgs(BaseModel):
        meh: int
        func: Callable
    schema = NoArgs.schema()
    assert "properties" in dget(schema, "properties", "func")
    assert dget(schema, "properties", "func", "type") == "object"
    assert dget(schema, "properties", "func", "x-type") == "function"



def test_callable_no_args():
    class NoArgs(BaseModel):
        meh: int
        func: Callable
    schema = NoArgs.schema()
    assert "properties" in dget(schema, "properties", "func")
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"



def test_nullable_in_object():
    class NullableInObject(BaseModel):
        func: Dict[str, Dict[str, Union[List[Optional[int]], int, bool, None]]]
    schema = NullableInObject.schema()
    assert "properties" in schema
    union = dget(schema, "properties", "func", "additionalProperties",
                 "additionalProperties", "anyOf")
    assert "nullable" in [*filter(lambda x: x["type"] == "array", union)][0]["items"]



def test_nullable_in_array():
    class NullableInArray(BaseModel):
        func: Dict[str, Union[List[Union[int, str, None]], int, bool]]
    schema = NullableInArray.schema()
    assert len(dget(schema, "properties", "func", "additionalProperties", "anyOf")) == 3
    bleh = dget(schema, "properties", "func", "additionalProperties", "anyOf")
    assert [*filter(lambda x: x["type"] == "array", bleh)][0]["items"]["nullable"]



def test_callable_with_nullable_no_args():
    class NoArgs(BaseModel):
        meh: int
        func: Callable
    schema = NoArgs.schema()
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")



def test_callable_with_nullable_empty_args():
    class EmptyArgs(BaseModel):
        func: Callable[[], None]
    schema = EmptyArgs.schema()
    assert "args" not in dget(schema, "properties", "func", "properties")
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")



def test_callable_with_nullable_any_args():
    class AnyArgs(BaseModel):
        func: Callable[..., None]
    schema = AnyArgs.schema()
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")



def test_callable_with_nullable_simple_args():
    class SimpleArgs(BaseModel):
        func: Callable[[int, int], None]
    schema = SimpleArgs.schema()
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"
    assert dget(schema, "properties", "func",
                "properties", "args", "properties").keys() == {0, 1}
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")



def test_callable_with_nullable_args_inside_strucutre():
    class DictArgs(BaseModel):
        func: Dict[str, Callable[[Optional[int]], None]]
    schema = DictArgs.schema()
    assert dget(schema, "properties", "func", "additionalProperties")
    func = dget(schema, "properties", "func", "additionalProperties")
    assert "x-type" in func and func["x-type"] == "function"
    assert dget(func, "properties", "args", "type") == "object"
    assert 0 in dget(func, "properties", "args", "properties")
    assert dget(func, "properties", "args", "properties", 0, "nullable")
    assert dget(func, "properties", "args", "properties", 0, "type") == "integer"
    assert dget(func, "properties", "retval", "nullable")



def test_callable_with_one_any_arg():
    class DictArgs(BaseModel):
        func: Callable[[Any], None]
    schema = DictArgs.schema()
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"
    assert dget(schema, "properties", "func",
                "properties", "args", "properties").keys() == {0}
    assert dget(schema, "properties", "func",
                "properties", "args", "properties", 0, "nullable")
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")


def test_callable_with_nullable_recurse_args():
    class RecurseArgs(BaseModel):
        func: Callable[[int, int, Callable[[int], None]], None]
    schema = RecurseArgs.schema()
    assert dget(schema, "properties", "func", "properties", "args", "type") == "object"
    assert dget(schema, "properties", "func", "properties", "retval", "nullable")
    assert dget(schema, "properties", "func",
                "properties", "args", "properties").keys() == {0, 1, 2}
    func_arg = dget(schema, "properties", "func",
                    "properties", "args", "properties")[2]
    assert "args" in func_arg["properties"]
    assert dget(func_arg, "properties", "args", "properties",
                0, "type") == "integer"
    assert dget(func_arg, "properties", "retval", "nullable")

# importlib.reload(models)
# class UpdateFunctionsParams(models.BaseModel):
#     models: List[str]
#     criteria_map: Dict[str, str]
#     checks: Dict[str, Callable[[Optional[int]], bool]]
#     logs: List[str]
# yaml.dump(UpdateFunctionsParams.schema(), sys.stdout)

# importlib.reload(models)
# class UpdateFunctionsParams(models.BaseModel):
#     models: List[str]
#     criteria_map: Dict[str, str]
#     checks: Dict[str, Dict[int, Optional[bool]]]
#     logs: List[Optional[str]]
# yaml.dump(UpdateFunctionsParams.schema(), sys.stdout)
