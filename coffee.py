# Надо написать функцию choose_coffee(preference1, preference2,..., preferenceN), 
# которая возвращает напиток, который можно приготовить из имеющихся 
# продуктов (ingredients). На вход функция принимает заранее неизвестное 
# количество предпочтений посетителя. Все напитки перечислены в порядке 
# убывания предпочтений и гарантированно не повторяются.
# Бариста готовит наиболее предпочитаемый напиток из доступных.

coffee_types = {
    'Эспрессо': [1, 0, 0], 
    'Капучино': [1, 3, 0],
    'Маккиато': [2, 1, 0], 
    'Кофе по-венски': [1, 0, 2],
    'Латте Маккиато': [1, 2, 1], 
    'Кон Панна': [1, 0, 1]}
 
 
def choose_coffee(*args):
    for name in args:
        need_ing = coffee_types[name]
        sum_ing = [sum(ing) for ing in list(zip(ingredients, [-i for i in need_ing]))]
        if all(True if num >= 0 else False for num in sum_ing):
            ingredients[:] = sum_ing
            return name
    return "К сожалению, не можем предложить Вам напиток"


ingredients = []
product = ['кофейные зерна', 'молоко', 'взбитые сливки']
for prod in product:
    ingredients.append(int(input(f'Введите количество продукта "{prod}": ')))

print(choose_coffee("Эспрессо", "Маккиато", "Латте Маккиато"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски"))
print(choose_coffee("Латте Маккиато", "Капучино", "Маккиато", "Кофе по-венски", "Кон Панна"))