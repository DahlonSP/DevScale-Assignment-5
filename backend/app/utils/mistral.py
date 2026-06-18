from mistralai.client import Mistral

from app.core.settings import settings

def get_mistral_client() -> Mistral:
    if settings.mistral_api_key is None:
        raise ValueError("Mistral API key is not set in settings.")
    
    return Mistral(api_key=settings.mistral_api_key)