# ---------------------------
fruit_list = ["orange", "apple","banana"]

# To open the door to lists, you have to list the list name and wrap the index inside brackets
print(fruit_list[1])
# ---------------------------

# ---------------------------
# To open the door to dictionaries, you have to list the dictionary name and wrap the "key" inside brackets
# ---------------------------

apple = {
    "name":"apple",
    "freshness":"rotten"
    }

print(apple["freshness"])




# ---------------------------
# To open the door to object attributes or methods. You have to list the object name DOT ___

# (See example below)
# ---------------------------
class Item:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.bun = data['bun']
        self.meat = data['meat']
        self.calories = data['calories']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


whopper_dict = {
    'id': 3,
    'name': "whopper",
    'bun': "sourdough",
    'meat': "beef",
    'calories': 2000,
    'created_at': "2022-08-24 00:00:00",
    'updated_at': "2022-08-24 00:00:00",
}


# This is wrong
# whopper = Item(3, "whopper", "sourdough", "beef", 2000, "2022-08-24 00:00:00", "2022-08-24 00:00:00")


whopper = Item(whopper_dict)
print(whopper.bun)