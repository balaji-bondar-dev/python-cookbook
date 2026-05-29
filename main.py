# Class introduction
class User:
    def __init__(self, name, age=0):
        self.name = name
        self.age = age


john = User("John Doe", 30)
print(f"User Name: {john.name}, Age: {john.age}")


class APIConfig:
    def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100, base_url=None):
+        self.model = model
        self.max_tokens = max_tokens
        self.base_url = base_url


dev_config = APIConfig(
    api_key="xxxxxxxxxx",
    # model="gpt-3.5-turbo",
    max_tokens=50,
    base_url="https://api.openai.com",
)
print(f"Dev Config: {dev_config.__dict__}")
print(f"Dev Config Model: {dev_config.model}")

prod_config = APIConfig(
    api_key="yyyyyyyyyy",
    model="gpt-4",
    max_tokens=200,
    base_url="https://api.openai.com",
)
print(f"Prod Config: {prod_config.__dict__}")
