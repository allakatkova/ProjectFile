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


def read_files_from_dir(directory):
    dict_len_files = {}
    for file_name in os.listdir(directory):
        with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
            text = file.readlines()
            dict_len_files[file_name] = len(text)
    return dict_len_files


def write_result_file(directory, result_file, file_dict):
    full_path = os.path.join(directory, result_file)
    for file_name in file_dict.keys():
        with open(os.path.join(directory, file_name), 'r', encoding='utf-8') as file:
            text_from_file = file.readlines()
        with open(full_path, 'a', encoding='utf-8') as file:
            file.writelines(text_from_file)
    print(f'Результат слияния файлов записан в файл {full_path}')


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
    directory = 'sorted'
    file_dict = read_files_from_dir(directory)

    # сортируем словарь по возрастанию значений
    result_file_dict = dict(sorted(file_dict.items(), key=lambda item: item[1]))

    result_file = 'result.txt'
    write_result_file(directory, result_file, result_file_dict)
