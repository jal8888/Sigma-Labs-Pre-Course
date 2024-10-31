def num_obj(s):
    list = []
    for num in s:
        dict = {str(num):str(chr(num))}
        list.append(dict)
    return list
