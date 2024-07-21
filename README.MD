
# Pydantic Data Validation Example

## Description

This project is a Python application demonstrating how to use Pydantic for data validation and settings management. It includes examples of defining data models, validating data, handling validation errors, and managing settings using environment variables.

## Features

- **Data Model Definition**: Define and validate data models using Pydantic.
- **Error Handling**: Catch and handle validation errors effectively.
- **Data Conversion**: Convert Pydantic models to dictionaries and JSON.
- **Settings Management**: Use environment variables for configuration.

## Installation

### Prerequisites

- Python 3.7 or later. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up the Project

1. **Clone the repository:**

   ```sh
   https://github.com/Tanvir-yzu/Pydantic.git
   cd main.py
   ```

2. **Create and activate a virtual environment:**

   - **On Windows:**

     ```sh
     python -m venv myenv
     ```
     ```sh
     myenv\Scripts\activate
     ```

  

3. **Install the required dependencies:**

   ```sh
   pip freeze > requirements.txt
   ```

   If `requirements.txt` does not exist, you can manually install the required packages:

   ```sh
   pip install pydantic email-validator icecream
   ```

## Usage

### Running the Application

To run the application or script, execute:

```sh
python main.py
```

Replace `main.py` with the name of your script if different.

### Example

Here's an example of how to use the code:

```python
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
```

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. **Fork the repository**.
2. **Create a new branch** (`git checkout -b feature-branch`).
3. **Make your changes**.
4. **Commit your changes** (`git commit -am 'Add new feature'`).
5. **Push to the branch** (`git push origin feature-branch`).
6. **Create a pull request**.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, you can contact me at [2020tanvir1971@gmail.com](mailto:2020tanvir@gmial.com).
```

