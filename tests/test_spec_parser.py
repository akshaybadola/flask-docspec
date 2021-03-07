import pytest
from typing import Union, List, Callable, Dict, Tuple, Optional, Any
from pydantic import BaseModel as PydanticBaseModel, Field
from flask_docspec.models import (BaseModel, ModelNoTitleNoRequiredNoPropTitle,
                                  add_nullable, remove_attr, remove_prop_titles)
