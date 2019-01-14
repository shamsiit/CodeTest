def print_depth(data):
    if not isinstance(data, dict):
        raise ValueError("Not a dictionary")
    Ddepth = 1
    obj = [(data.get(k), Ddepth + 1) for k in data.keys() if isinstance(data.get(k), dict)]
    not_dict = [k for k in data.keys()]
    for key in not_dict:
        print(key + "    " + str(Ddepth))
    max_depth = 0

    while obj:
        n, Ddepth = obj.pop()
        max_depth = max(max_depth, Ddepth)
        if isinstance(n, dict):
            obj = obj + [(n.get(k), Ddepth + 1) for k in n.keys() if isinstance(n.get(k), dict)]
            not_dict = [k for k in n.keys()]
            for key in not_dict:
                print(key + "    " + str(Ddepth))

myDict = {
    "key1": 1,
    "key2": {
        "key3": 1,
        "key4": {
            "key5": 4
            }
        }
    }

print_depth(myDict)  