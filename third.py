def dict(dict1, dict2):
    mergeDict = dict1.copy()

    for key, value in dict2.items():
        if key in mergeDict:
            mergeDict[key] += value
        else:
            mergeDict[key] = value

    return mergeDict
dict1_input = input("")
dict2_input = input("")

dict1 = eval(dict1_input)
dict2 = eval(dict2_input)

result = dict(dict1, dict2)
print(result)


# +++++++++++++++++++++++++++++++++++++++NOTE++++++++++++++++++++++++++++++++++++++++
# you can  input in this format for dictionaries {'a': 4, 'b': 8, 'c': 2}
