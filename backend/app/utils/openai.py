from openai import OpenAI

from app.core.settings import settings

def get_openai_client() -> OpenAI:
    if settings.openai_api_key is None:
        raise ValueError("OpenAI API key is not set in settings.")
    
    return OpenAI(api_key=settings.openai_api_key)