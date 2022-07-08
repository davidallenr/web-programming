from mongita import MongitaClientDisk
client = MongitaClientDisk(host="./.mongita")

shopping_db = client.shopping_db
shopping_list = shopping_db.shopping_list
shopping_list.delete_many({})

shopping_list.insert_one({"description":"apple"})
shopping_list.insert_one({"description":"cheese"})
shopping_list.insert_one({"description":"milk"})




items = list(shopping_list.find({}))
items = [item['description'] for item in items]

print(items)
shopping_list.insert_one({"description":"banana"})

items = list(shopping_list.find({}))
items = [item['description'] for item in items]

print(items)

shopping_list.delete_one({"description" : "banana"})

items = list(shopping_list.find({}))
items = [item['description'] for item in items]

print(items)

shopping_list.update_one({"description" : "apple"}, {'$set':{'description':'pear'}})
items = list(shopping_list.find({}))
items = [item['description'] for item in items]

print(items)

pear_item = shopping_list.find_one({'description':'pear'})

print(pear_item)