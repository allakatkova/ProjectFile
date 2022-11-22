import os


def read_content_file():
    content = {}
    with open('recipes.txt') as file:
        for line in file:
            recipes_name = line.strip()
            recipe = {recipes_name: []}
            ingredients_count = file.readline()
            for i in range(int(ingredients_count)):
                compound = file.readline()
                ingredient_name, quantity, measure = compound.split(' | ')
                products = {'ingredient_name': ingredient_name, 'quantity': int(quantity), 'measure': measure.strip()}
                recipe[recipes_name].append(products)
            file.readline()
            content.update(recipe)
    return content


def get_shop_list_by_dishes(dishes, person_count):
    result_list = {}
    cook_book = read_content_file()
    for dish in dishes:
        ingredients_dish = cook_book.get(dish)
        for ingredient in ingredients_dish:
            ingredient_name = ingredient.pop('ingredient_name')
            required_quantity = ingredient.pop('quantity') * person_count
            ingredient.update({'quantity': required_quantity})
            result_list.update({ingredient_name: ingredient})
    return result_list


if __name__ == '__main__':
    # task 1
    cook_book = read_content_file()
    for key, value in cook_book.items():
        print(key, value)

    print()
    print('---------------------------------------')
    print()

    # task 2
    ingredients = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
    for key, value in ingredients.items():
        print(key, value)

    print()
    print('---------------------------------------')
    print()

    # task 3
    current_directory = os.getcwd()
    folder = 'sorted'
    files = ['1.txt', '2.txt', '3.txt']
    result_file = 'result.txt'
    list_content = []
    line_count = 0
    for file_txt in files:
        full_path = os.path.join(current_directory, folder, file_txt)
        with open(full_path, 'r') as file:
            content = file.readlines()
            content.insert(0, file_txt + '\n' + str(len(content)) + '\n')
            if line_count > len(content):
                list_content.insert(0, content)
            else:
                list_content.insert(len(list_content), content)
            line_count = len(content)

    full_path = os.path.join(current_directory, folder, result_file)

    with open(full_path, 'w') as file:
        for element in list_content:
            for line in element:
                file.writelines(line)

    print(f'Результат слияния файлов записан в файл {full_path}')