import json
import requests


favorites_companies = [
    'VK, Вконтакте',
    'Т-Банк',
    'Ozon Информационные технологии',
    'Яндекс',
    'RUTUBE',
    'Сбер. ИТ',
    'Лаборатория Касперского',
    'Доктор Веб',
    'ПАО ВТБ',
    'Альфа-Банк',
]
vacancies = []


#   Реализуем подключение к API hh.ru
def connect_to_api():
    for company in favorites_companies:

        url = 'https://api.hh.ru/vacancies'  # прописываем адрес для подключения к сервису API
        params = {
            'text': company,
            'per_page': 100
        }    # Используется для настройки поискового запроса
        data = requests.get(url, params=params)

        if data.status_code == 200:
            json_data = data.json()
            for item in json_data['items']:
                job_title = item['name']
                link_to_vacancy = item['alternate_url']
                salary = item['salary']

                salary_from = None
                salary_to = None

                if salary:
                    salary_from = salary.get('from')
                    salary_to = salary.get('to')

                description = item['snippet']['responsibility']
                requirement = item['snippet']['requirement']

                vacancies.append({
                    "company": company,
                    "job_title": job_title,
                    "link_to_vacancy": link_to_vacancy,
                    "salary": salary,
                    "salary_from": salary_from,
                    "salary_to": salary_to,
                    "description": description,
                    "requirement": requirement,
                })
        else:
            print(f'Ошибка {data.status_code}')
    return vacancies


if __name__ == '__main__':
    vacancies = connect_to_api()
    filename = 'vacancy_json.json'
    with open(filename, 'w', encoding='utf-8') as outfile:
        json.dump(vacancies, outfile, ensure_ascii=False, indent=4)
