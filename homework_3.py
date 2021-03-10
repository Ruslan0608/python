# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None. Подумайте, как и где лучше хранить информацию, необходимую для
# перевода: какой тип данных выбрать, в теле функции или снаружи.

dictionary_of_numbers = {'zero': "ноль", 'one': "один", "two": "два", "three": "три", 'four': "четыре",
                         "five ": "пять",
                         "six": "шесть", "seven": "семь", 'eight': "восемь", "nine": "девять",
                         "ten": "десять", "one hundred thousand": 'сто тысяч'}


def num_translate(key):
    for i in dictionary_of_numbers:
        if i == key:
            print(dictionary_of_numbers[key])
    return


print('Задача №1 ')
num_translate('zero')
num_translate('one')
num_translate('nine')
num_translate('six')
num_translate('four')


# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с
# соответствующей буквы. Например:
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# } Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?


def thesaurus(*args):
    zz = {}
    for i in sorted(args):
        a = i[0]
        if a in zz:
            zz[a] += [i]
        else:
            zz[a] = [i]
    return zz


print("Задача №2 ")
print(thesaurus("Иван", "Мария", "Петр", "Илья", "Даниил"))

# долго промудохался с  тем что список создал отдельно и вывод так и не получился, если вставлять имя списка а не
# сам список. Почему так и не понял

# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из двух случайных слов, взятых из трёх списков:
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]


from random import randrange, choice

nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes(n, repeat=False):
    list_1 = []
    while n and len(nouns):
        mmm = randrange(len(adjectives))
        if repeat:
            list_1.append(f"{nouns.pop(mmm)} {adverbs.pop(mmm)} {adjectives.pop(mmm)}")
        else:
            list_1.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
        n -= 1
    return list_1


print("Задача №3 ")
print(get_jokes(5))
