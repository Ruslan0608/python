# 1. Не используя библиотеки для парсинга, распарсить (получить определённые данные)
# файл логов web-сервера nginx_logs.txt
# (https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs) — получить
# список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). Например:
#
# [
# ...
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('141.138.90.60', 'GET', '/downloads/product_2'),
# ('173.255.199.22', 'GET', '/downloads/product_2'),
# ...
# ]

# Сделал сам

# import requests
#
# url = 'https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
# r = requests.get(url)
# with open('nginx_logs.txt', 'w') as output_file:
#     output_file.write(r.text)
#
# with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
#     pro = ((line.split()[0], line.split()[5], line.split()[6]) for line in f)
#     for i in pro:
#         print(i)


# 3. Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
# Известно, что при хранении данных используется принцип: одна строка — один пользователь,
# разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов и формирующий
# из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь в файл.
# Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше записей, чем в файле с ФИО,
# задаём в словаре значение None. Если наоборот — выходим из скрипта с кодом «1».
# При решении задачи считать, что объём данных в файлах во много раз меньше объема ОЗУ.
# Фрагмент файла с данными о пользователях (users.csv):
# Иванов,Иван,Иванович
# Петров,Петр,Петрович
# Фрагмент файла с данными о хобби (hobby.csv):
# скалолазание,охота
# горные лыжи

# from json import dump
# from itertools import zip_longest
#
# with open('users.csv', 'r', encoding="utf-8") as users:
#     with open('hobbyy.csv', 'r', encoding="utf-8") as hobbyy:
#
#         if len(users.readlines()) > len(hobbyy.readlines()):
#             with open("itog.json", 'w', encoding="utf-8") as f:
#                 ddd = zip_longest(users, hobbyy, fillvalue=None)
#                 my_dic = {str(aa[0]).strip(): (aa[1].strip()) for aa in ddd}
#
#                 dump(my_dic, f, ensure_ascii=False, indent=4)
#
#             print(my_dic)
#         else:
#             exit(1)
# Traceback (most recent call last):
#   File "C:\Project\PPython\homework_6.py", line 46, in <module>
#     if len(users.readlines()) > len(hobbyy.readlines()):
#   File "C:\Users\Руслан\AppData\Local\Programs\Python\Python39\lib\codecs.py", line 322, in decode
#     (result, consumed) = self._buffer_decode(data, self.errors, final)
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc8 in position 0: invalid continuation byte

# Не понял как убрать эту ошибку, незачет.


# 6. Реализовать простую систему хранения данных о суммах продаж булочной.
# Должно быть два скрипта с интерфейсом командной строки: для записи данных и для вывода на экран записанных данных.
# При записи передавать из командной строки значение суммы продаж.
# Для чтения данных реализовать в командной строке следующую логику:
# просто запуск скрипта — выводить все записи;
# запуск скрипта с одним параметром-числом — выводить все записи с номера, равного этому числу, до конца;
# запуск скрипта с двумя числами — выводить записи, начиная с номера, равного первому числу,
# по номер, равный второму числу, включительно.


# 7. Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
# Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1. Примеры запуска скриптов:
#
# python add_sale.py 5978,5
# python add_sale.py 8914,3
# python add_sale.py 7879,1
# python add_sale.py 1573,7
# python show_sales.py
# 5978,5
# 8914,3
# 7879,1
# 1573,7
# python show_sales.py 3
# 7879,1
# 1573,7
# python show_sales.py 1 3
# 5978,5
# 8914,3
# 7879,1
