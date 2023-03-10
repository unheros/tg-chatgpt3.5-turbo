from pydantic import BaseSettings


class Config(BaseSettings):
    OPENAI_TOKEN: str
    TG_BOT_TOKEN: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"