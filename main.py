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
        #print(ingredients_dish)
        for ingredient in ingredients_dish:
            #print(ingredient)
            ingredient_name = ingredient.pop('ingredient_name')
            #print(ingredient_name)
            required_quantity = ingredient.pop('quantity') * person_count
            ingredient.update({'quantity': required_quantity})
            #print(ingredient)
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
    # ingredients = get_shop_list_by_dishes(['Омлет'], 2)
    for key, value in ingredients.items():
        print(key, value)

    print()
    print('---------------------------------------')
    print()

