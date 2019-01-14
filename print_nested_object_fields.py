class Person:
   def __init__(self, first_name, last_name, father):
    self.first_name = first_name
    self.last_name = last_name
    self.father = father
 
p1 = Person("parent_fn", "parent_ln", None)
p2 = Person("child_fn", "child_ln", p1)
 
nested_dict = {
  "key_1": 1,
  "key_2": {
    "key_3": 2,
    "key_4": {
      "key_5": 3,
      "key_6": p2
    }
  }
}

def convert_obj_values_in_dict(dict_with_obj):
  if not isinstance(dict_with_obj, dict):
    raise ValueError("Not python dictionary")
  for key, val in dict_with_obj.items():
    if isinstance(val, dict):
      dict_with_obj[key] = convert_obj_values_in_dict(val)
    elif hasattr(val, '__dict__'):
      val_dict = convert_obj_values_in_dict(val.__dict__)
      dict_with_obj[key] = val_dict
  return dict_with_obj
 
def print_nested_depth(dic, depth=1):
  for key, val in dic.items():
    print(key, depth)
    if isinstance(val, dict):
      print_nested_depth(val, depth+1)
 
def print_depth(data):
  nested_dict = convert_obj_values_in_dict(data)
  print_nested_depth(nested_dict)
 
print_depth(nested_dict)
