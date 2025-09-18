from pydantic import BaseModel
from typing import Optional

# --- Pydantic models ---
class User(BaseModel):
    username: str

class Token(BaseModel):
    access_token: str
    token_type: str
    