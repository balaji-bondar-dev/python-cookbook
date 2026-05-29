from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime


class User(BaseModel):
    """A sample User model using Pydantic."""
    
    id: int
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = None
    age: Optional[int] = Field(None, ge=0, le=150)
    is_active: bool = True
    created_at: datetime = Field(default_factory=datetime.now)
    
    class Config:
        json_schema_extra = {
            "example": {
                "id": 1,
                "username": "johndoe",
                "email": "john@example.com",
                "full_name": "John Doe",
                "age": 30,
                "is_active": True,
                "created_at": "2026-05-28T10:00:00"
            }
        }


# Example usage
if __name__ == "__main__":
    # Create a user instance
    user = User(
        id=1,
        username="jane_smith",
        email="jane@example.com",
        full_name="Jane Smith",
        age=28
    )
    
    print("User created successfully:")
    print(user.model_dump_json(indent=2))
    
    # Validate data
    user_data = {
        "id": 2,
        "username": "bob_wilson",
        "email": "bob@example.com",
        "full_name": "Bob Wilson",
        "age": 35
    }
    
    validated_user = User(**user_data)
    print("\nValidated user:")
    print(validated_user)
