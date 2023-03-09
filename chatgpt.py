from enum import Enum
from typing import List

from openai import ChatCompletion
from pydantic import BaseModel


class Role(str, Enum):
    system = "system"
    assistant = "assistant"
    user = "user"


class Message(BaseModel):
    role: Role
    content: str


async def create_completion(
    api_key: str,
    messages: List[Message]
) -> Message:
    response = await ChatCompletion.acreate(
        api_key=api_key,
        model="gpt-3.5-turbo",
        messages=[msg.dict() for msg in messages]
    )
    print(response)
    message_json = response["choices"][0]["message"]
    return Message.parse_obj(message_json)
