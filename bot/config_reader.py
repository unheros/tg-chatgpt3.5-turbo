from pydantic import BaseSettings


class Config(BaseSettings):
    OPENAI_TOKEN: str
    TG_BOT_TOKEN: str
    chat_id: int

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"