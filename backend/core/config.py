from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    api_name: str = "VM Tools API"
    api_version: str = "1.0"
    data_base_url: str = "postgresql+asyncpg://postgres:postgres@localhost/vm_tools"

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()