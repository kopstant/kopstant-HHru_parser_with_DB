Nadelayev.D.A 

**В рамках этого проекта была поставлена задача на получение данных о работодателях и их вакансиях с сайта hh.ru, с исполь
зованием библиотеки requests, и хранением полученных данных в базе данных с использованием библиотеки psycopg2 .**

1) В файле func.py мы импортируем библиотеку json и requests, прописываем в список  - _favorites_companies_, интересующих
нас работодателей и прописываем логику для работы с API/hh.ru и сохранением результатов в _.json_ формате


2) В файле create_bd.py прописываем логику для проектирования таблицы в DB PostgesSQL и дальнейшим ее заполнением с использованием данных с файла json.


3) В файле dbmanager.py прописан класс DBManager(), необходимый для вывода данных из БД. Имеются методы для:
-    get_companies_and_vacancies() - получение списка всех компаний и количества вакансий у каждой компании.
-    get_all_vacancies() - получение списка всех вакансий с указанием названия компаний, названия вакансий и зарплаты и ссылки на вакансии.
-    get_avg_salary() - получение средней зарплаты по вакансием.
-    get_vacancies_with_higher_salary() - получение списка всех вакансий, у которых зарплата выше средней по всем вакансиям.
-    get_vacancies_with_keyword() - получение списка всех вакансий, в названии которых содержится переданные в метод слова.
4)  В файле db_config прописана функция для подключения к базе данных, используются данные из файла database.ini, который не импортируется и включен в список исключений .gitgnore, так как содержит конфиденциальную информацию.

    database.ini  внутри себя имееет данные в следующей типовой форме:

     [postgresql] - название базы данных
 
     host=localhost - имя хоста

     user=username - имя пользователя, использованное для регистрации

     password=password - пароль указанный при регистрации

     port=5432 - стандартный порт
 


    


5) В файле main.py прописана основная логика, сюда импортируется class DBManager и config from db_config.

    Первым делом происходит подключение к базе данных используя функцию
    
    Далее пользователю предлагается выбрать интересующий его метод, введя соответствующую цифру.

    Исходя из ответа пользователя выводится информация в консоль
