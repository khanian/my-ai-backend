from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # 환경변수에서 자동으로 매핑됨 (자바의 @Value("${...}") 역할)
    OPENAI_API_KEY: str
    
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

settings = Settings()

# from dotenv import load_dotenv
# load_dotenv()
