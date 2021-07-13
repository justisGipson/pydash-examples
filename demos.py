from pydash import py_

# flatten array
a = [[1, 2], [3, 4, 5]]
print(py_.flatten(a))

# Flatten-Deep array
a = [[1, 2, [4, 5]], [6, 7]]
print(py_.flatten_deep(a))

# chunk array elements (list, # in chunk)
a = [1, 2, 3, 4, 5,]
print(py_.chunk(a, 2))

# omit dict attrs
fruits = {"name": "apple",
          "color": "red",
          "taste": "sweet"}
print(py_.omit(fruits, "name"))

# access deep nested dictionary
apple = {
  "price": {
    "in_season": {"store": {"Walmart": [2, 4], "Aldi": 1}},
    "out_of_season": {"store": {"Walmart": [3, 5], "Aldi": 2}},
  }
}

print(py_.get(apple, "price.in_season.store.Walmart[0]"))

# find item index with a function
fruits = [
  {"name": "apple", "price": 2},
  {"name": "orange", "price": 2},
  {"name": "grapes", "price": 4},
]

filter_fruits = lambda fruit: fruit["name"] == "apple"
print(py_.find_index(fruits, filter_fruits))

# find objects with matching style
fruits = [
  {"name": "apple", "price": 2},
  {"name": "orange", "price": 2},
  {"name": "grapes", "price": 4},
]

print(py_.filter_(fruits, {"name": "apple"}))

# nested obj value
fruits = [
    {"name": "apple", "attributes": {"color": "red", "taste": "sweet"}},
    {"name": "orange", "attributes": {"color": "orange", "taste": "sweet"}},
    {"name": "lemon", "attributes": {"color": "yellow", "taste": "sour"}},
]

print(py_.map_(fruits, "attributes.taste"))

# execute a function n times
print(py_.times(4, lambda i: f"I have just bought {i} apple"))

# chaining - lazy evaluation
fruits = ["apple", "orange", "grapes"]
print(py_.chain(fruits).without("grapes").reject(lambda fruit: fruit.startswith("a")).value())

# custom methods
fruits = ["apple", "orange", "grapes"]
def get_price(fruit):
  prices = {"apple": 2, "orange": 2, "grapes": 4}
  return prices[fruit]

total_price = py_.chain(fruits).map(get_price).sum()
print(total_price.value())

# planting a value
print(total_price.plant(["apple", "orange"]).value())
