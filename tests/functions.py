from typing import Union, List, Dict, Optional
from flask_docspec.models import BaseModel


class Config(BaseModel):
    name: str
    value: Dict[str, Dict[str, int]]



class Daemon:
    def _reinit_session_helper(self):
        """Reinitialize a session with given key `name`/`time_str`

        Args:
            task_id: The `task_id` for the task
            name: `name` of the session
            time_str: The time stamp of the session
            data: ReinitSessionModel

        Schemas:
            class ReinitSessionModel(BaseModel):
                config: functions.Config

        """
        pass

    def _clone_session_helper(self):
        """Reinitialize a session with given key `name`/`time_str`

        Args:
            task_id: The `task_id` for the task
            name: `name` of the session
            time_str: The time stamp of the session
            data: ReinitSessionModel

        Schemas:
            class CloneSessionModel(BaseModel):
                config: functions.Config

        """
        pass

    def create_session(self):
        pass


def bleh():
    """Handle a POST request for a `session_method`

    Args:
        func_name: The name of the helper method

    Schema:
        class Task(BaseModel):
            task_id: int
            message: str

    Request:
        content-type: MimeTypes.json
        body:
            session_key: str
            data: Union[:meth:`Daemon._reinit_session_helper`: ReinitSessionModel,
                        :meth:`Daemon._clone_session_helper`: CloneSessionModel,
                        Dict]
            some_other_shit: Dict

    Responses:
        invalid data: ResponseSchema(405, "Invalid Data", MimeTypes.text,
                                    "Invalid data {some: json}")
        bad params: ResponseSchema(405, "Bad Params", MimeTypes.text,
                                   "Session key not in params")
        Success: ResponseSchema(200, "Initiated Task", MimeTypes.json, "Task")
    """
    pass


def bleh_redirect() -> Union[Dict[str, Optional[List[str]]]]:
    "Doesn't have any docstring"
    pass


def bleh_annot():
    """Some random shit

    Request:
        content-type: MimeTypes.json
        body:
            some_attr: :func:`bleh_redirect`
    """
    pass
