import requests
from bs4 import BeautifulSoup
import os
import data_analysis

URL_1 = "https://www.hse.ru/education/bachelor/"
page_1 = requests.get(URL_1)

soup_bachelor = BeautifulSoup(page_1.content, "html.parser")
results_bachelor = soup_bachelor.find(class_="edu-programm__tab edu-programm__bachelor")
elements_bachelor = results_bachelor.find_all("div", class_="edu-programm__group")

URL_2 = "https://www.hse.ru/education/magister/"
page_2 = requests.get(URL_2)

soup_magister = BeautifulSoup(page_2.content, "html.parser")
results_magister = soup_magister.find(class_="edu-programm__tab edu-programm__magister")
elements_magister = results_magister.find_all("div", class_="edu-programm__group")

def bachelor():
    print('Бакалаврские программы НИУ ВШЭ в Москве')
    for element in elements_bachelor:
        direction = element.find("a", class_="link")
        form_training = element.find("div", class_="edu-programm__edu_offline")
        time = element.find("div", class_="edu-programm__data u-accent")
        cost = element.find("div", class_="b-row__item b-row__item--2 b-row__item--t4 b-row__item--cost")
        city_msk = element.find("span", class_="edu-programm__city with-icon with-icon_flag-msk")
        faculty = element.find("span", class_="grey")
        places = element.find("div", class_="with-indent1")
        print("\n")
        print (f'Факультет: {faculty.text.strip()}')
        print(f'Направление: {direction.text.strip()}')
        print(f'Форма обучения: {form_training.text.strip()}')
        print(f'Срок обучения: {time.text.strip()}')
        print(f'Город: {city_msk.text.strip()}')
        print(f'Стоимость: {cost.text.strip()}')
        print(f'Места/Стипендия: {places.text.strip()}')

def magister():
    print('Программы магистратуры НИУ ВШЭ в Москве')
    for element in elements_magister:
        direction = element.find("a", class_="link")
        form_training = element.find("div", class_="edu-programm__edu_offline")
        time = element.find("div", class_="edu-programm__data u-accent")
        cost = element.find("div", class_="b-row__item b-row__item--2 b-row__item--t4 b-row__item--cost")
        city_msk = element.find("span", class_="edu-programm__city with-icon with-icon_flag-msk")
        faculty = element.find("span", class_="grey")
        places = element.find("div", class_="with-indent1")
        print("\n")
        print(f'Факультет: {faculty.text.strip()}')
        print(f'Направление: {direction.text.strip()}')
        print(f'Форма обучения: {form_training.text.strip()}')
        print(f'Срок обучения: {time.text.strip()}')
        print(f'Город: {city_msk.text.strip()}')
        print(f'Стоимость: {cost.text.strip()}')
        print(f'Места/Стипендия: {places.text.strip()}')

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

print('Программы бакалавриата и магистратуры НИУ ВШЭ в Москве')
print('Команды:\n1 – Просмотреть программы бакалавриата;\n2 – Просмотреть программы магистратуры;\n3 – Просмотреть минимальное количество баллов по результатам ЕГЭ;\n4 – Просмотреть статистику среднего балла по предметам;\n11 – Очистить экран;\nq - выход;')
def main():
    while True:
        user = input('Введите команду: ').lower()
        if user == '1':
            bachelor()
        elif user == '2': 
            magister()
        elif user == '3': 
            user_permission = input('Желаете записать результаты в файл Exel? (Да/Нет): ').lower()
            if user_permission == 'да':
                data_analysis.write()
                print('Данные успешно сохранены')
            else:
                print(f'Направление подготовки 10.05.01 Компьютерная безопасность, 52.05.01 Актёрское искусство.\n{data_analysis.df_specialty}\n')
                print(f'Направление подготовки 01.03.01 Математика.\n{data_analysis.df_bachelorbachelor_matematic}\n')
                print(f'Направление подготовки 01.03.02 Прикладная математика и информатика\n{data_analysis.df_bachelor_informatic}\n')
                print(f'Направление подготовки 03.03.02 Физика\n{data_analysis.df_bachelor_fisica}\n')
                print(f'Направление подготовки 09.03.01 Информатика и вычислительная техника\n{data_analysis.df_bachelor_ikt}\n')
                print(f'Направление подготовки 09.03.04 Программная инженерия\n{data_analysis.df_bachelor_programms}\n')
                print(f'Направление подготовки 10.03.01 Информационная безопасность\n{data_analysis.df_bachelor_ib}\n')
                print(f'Направление подготовки 11.03.02 Инфокоммуникационные технологии и системы связи\n{data_analysis.df_bachelor_system}\n')
                print(f'Направление подготовки 38.03.05 Бизнес-информатика\n{data_analysis.df_bachelor_bisnes}\n')
                print(f'Направление подготовки 54.03.01 Дизайн\n{data_analysis.df_bachelor_design}\n')
                print(f'Направление подготовки 40.03.01 Юриспруденция\n{data_analysis.df_bachelor_urist}\n')
        elif user == '4': 
            data_analysis.statistic()
        elif user == '11':
            cls()
            print('Программы бакалавриата и магистратуры НИУ ВШЭ в Москве')
            print('Команды:\n1 – Просмотреть программы бакалавриата;\n2 – Просмотреть программы магистратуры;\n3 – Просмотреть минимальное количество баллов по результатам ЕГЭ;\n4 – Просмотреть статистику среднего балла по предметам;\n11 – Очистить экран;\nq - выход;')
        elif user == 'q':
            break
        else:
            print('Данная команда неверна')
main()
