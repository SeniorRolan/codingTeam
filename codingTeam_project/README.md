<h1 align="center">Тестовое задание для <a href="https://codingteam.ru/" target="_blank">codingTeam</a> 
</h1>

#Задание
  **Стек Django\DRF**

  *Даны модели "Категория Блюд" и "Блюдо" для ресторана.*
  
  *Даны сериализаторы.*
  
  *В выборку попадают только Блюда у которых is_publish=True.
  Если в категории нет блюд (или все блюда данной категории 
  имеют is_publish=False) - не включаем ее в выборку.*
  
  *Запрос в БД сделать любым удобным способом:
  Django ORM (предпочтительно), Raw SQL, Sqlalchemy...*

*Написать View который вернет для API 127.0.0.1/api/v1/foods/* 

  JSON следующего формата:

  `[
      {
         "id":1,
         "name_ru":"Напитки",
         "name_en":null,
         "name_ch":null,
         "order_id":10,
         "foods":[
            {
               "internal_code":100,
               "code":1,
               "name_ru":"Чай",
               "description_ru":"Чай 100 гр",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
                  200
               ]
            },
            {
               "internal_code":200,
               "code":2,
               "name_ru":"Кола",
               "description_ru":"Кола",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
               ]
            },
            {
               "internal_code":300,
               "code":3,
               "name_ru":"Спрайт",
               "description_ru":"Спрайт",
               "description_en":null,
               "description_ch":null,
               "is_vegan":false,
               "is_special":false,
               "cost":"123.00",
               "additional":[
               ]
            }
   ]`
  
# Установка

*%git clone https://github.com/SeniorRolan/codingTeam.git*

*%cd codingTeam*

*%pip install -r requirements.txt*

#Запуск

*%cd codingTeam_project*

*% ./manage.py runserver 8000*