from pydantic_settings import BaseSettings
from pydantic import Field


class Settings(BaseSettings):
    # Application metadata
    app_name: str = "SaaS Backend"

    # Environment type
    environment: str = Field(default="development",  alias="ENVIRONMENT")

    # Security
    secret_key: str

    # Database
    database_url: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


# Create a single settings instance
settings = Settings()