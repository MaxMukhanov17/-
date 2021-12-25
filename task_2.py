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

def get_shop_list_by_dishes(dishes, person_count):
    cook_book = read_file('recipes.txt')
    order = {}
    for dish in dishes:
        if dish in cook_book.keys():
            list_ingridient = cook_book.get(dish)
            for ingredients in list_ingridient:
                q_m = {}
                q_m['quantity'] = int(ingredients[list(ingredients.keys())[1]])*person_count
                q_m['measure'] = ingredients[list(ingredients.keys())[2]]
                order[ingredients.get('ingredient_name')] = q_m
        else:
            print('Такого блюда нет в меню!')
    return order
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


