def read_file(file_name):
    cook_book = {}
    with open(file_name, encoding = 'utf-8') as file:
        for line in file:
            name = line.strip()
            count = int(file.readline().strip())
            dish_list = []
            for ingredients in range(count):
                ingredient_name, quantity, measure = file.readline().strip().split('|')
                composition = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}
                dish_list.append(composition)
            cook_book[name] = dish_list
            file.readline()
    return cook_book
    
print(read_file('recipes.txt'))