import requests
from bs4 import BeautifulSoup

def parse():
    url = "https://www.omgtu.ru/general_information/the-structure/the-department-of-university.php"  # URL сайта для парсинга

    # Отправляем GET-запрос на сайт
    padge = requests.get(url)
    print(padge.status_code) # смотрим ответ
    # Инициализируем объект BeautifulSoup и передаем ответ сервера в качестве параметра
    soup = BeautifulSoup(padge.text, "html.parser")
    # Ищем все элементы с классом "a" и записываем содержимое в список
    block = soup.findAll('a', class_=None)

    # Открываем файл для записи
    with open("ReSuL.txt", "w", encoding="utf-8") as f:
        # Записываем каждый элемент списка block в файл построчно
        for data in block:
            description = data.text.strip()
            f.write(description + "\n")