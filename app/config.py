from pydantic_settings import BaseSettings
from typing import Literal


class Settings(BaseSettings):
    MODE: Literal["TEST", "PROD"]
    LOG_LEVEL: str = "INFO"
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str

    class Config:
        env_file = ".env"
    @property
    def db_url(self):
        return f"postgresql+asyncpg://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}"


settings = Settings()
