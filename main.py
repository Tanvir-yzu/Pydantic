from pydantic import BaseModel, EmailStr, ValidationError
from typing import Optional
from icecream import ic

# Define a basic User model
class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    age: Optional[int] = None

# Create a valid User instance
try:
    user = User(id=1, name="John Doe", email="john.doe@example.com", age=25)
    ic(user)
except ValidationError as e:
    ic("Validation Error:", e)

# Attempt to create an invalid User instance
try:
    invalid_user = User(id='one', name="Jane Doe", email="janedoeexample.com", age='twenty-five')
except ValidationError as e:
    ic("Validation Error:", e)

# Example of parsing data into a User model
user_data = {'id': 2, 'name': 'Alice', 'email': 'alice@example.com'}
user_from_dict = User(**user_data)
ic(user_from_dict)

# Convert the user model to a dictionary
user_dict = user_from_dict.dict()
ic(user_dict)

# Convert the user model to a JSON string
user_json = user_from_dict.json()
ic(user_json)
