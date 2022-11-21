# def read_content_file():
#     content = []
#     with open('recipes.txt') as file:
#         for line in file:
#             recipes_name = line.strip()
#             recipe = {'name': recipes_name, 'compound': []}
#             ingredients_count = file.readline()
#             print(recipe)
#             for i in range(int(ingredients_count)):
#                 compound = file.readline()
#                 ingredient_name, quantity, measure = compound.split(' | ')
#                 products = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
#                 recipe['compound'].append(products)
#                 print(products)
#             file.readline()
#             content.append(recipe)
#     return content

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
                products = {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure.strip()}
                recipe[recipes_name].append(products)
            file.readline()
            content.update(recipe)
    return content


if __name__ == '__main__':
    cook_book = read_content_file()
    print(cook_book)
