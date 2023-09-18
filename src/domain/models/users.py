# pylint: disable=redefined-builtin
# pylint: disable=invalid-name

class Users:
    def __init__(self, id: int, first_name: str, last_name: str, age: int) -> None:
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


user_1 = Users(12, 'ola', 'aqui', 61)
print(user_1.first_name)
