"""
CineAI — Configuration
"""
from __future__ import annotations
import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).parent


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False,
    )

    # API Keys
    groq_api_key: str = ""
    omdb_api_key: str = ""
    tmdb_api_key: str = ""

    # LLM config
    groq_model: str = "llama-3.1-8b-instant"
    ollama_model: str = "mistral"
    ollama_base_url: str = "http://localhost:11434"

    # Server
    host: str = "0.0.0.0"
    port: int = 8000
    debug: bool = False
    log_level: str = "INFO"

    # Limits
    max_input_chars: int = 500
    rate_limit_ip_max_requests: int = 30
    rate_limit_ip_window_seconds: int = 60

    # Cache
    cache_dir: str = str(BASE_DIR / "cache")
    cache_ttl_seconds: int = 3600
    data_dir: str = str(BASE_DIR / "data")

    # Similarity
    similarity_min_threshold: float = 20.0


PATHS = {
    "base": BASE_DIR,
    "cache": BASE_DIR / "cache",
    "data": BASE_DIR / "data",
}

settings = Settings()

# Ensure directories exist
Path(settings.cache_dir).mkdir(parents=True, exist_ok=True)
Path(settings.data_dir).mkdir(parents=True, exist_ok=True)
