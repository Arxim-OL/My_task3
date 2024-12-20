# Задание "Раз, два, три, четыре, пять .... Это не всё?"

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(data_s):
    result = 0
    if isinstance(data_s, int) or isinstance(data_s, float):
        result += data_s
    else:
        for i in data_s:
            if (isinstance(i, list) or isinstance(i, tuple) or isinstance(i, set)):
                result += calculate_structure_sum(i)
            elif isinstance(i, dict):
                result += calculate_structure_sum(i)
                for j in i:
                    result += calculate_structure_sum(i[j])
            else:
                if isinstance(i, str):
                    result += len (i)
                else:
                    result += i
    return result

result = calculate_structure_sum(data_structure)
print(result)

