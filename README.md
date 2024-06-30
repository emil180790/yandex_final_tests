﻿# Final_Sprint

Описание проекта

# 1. Работа с базой данных. 

Запросы расположены в файле SQL.txt.

## Задание 1.

Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true):

	SELECT
    		c.login,
    		COUNT(o.id) AS orders_in_delivery
	FROM
    		"Couriers" c
	JOIN
    		"Orders" o ON c.id = o."courierId"
	WHERE
    		o."inDelivery" = true
	GROUP BY
    		c.login;

Скрин результатов запроса - skrin1.png

## Задание 2

Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.

	SELECT 
    		id AS "order_id",
    	CASE 
        	WHEN finished = true THEN 2
        	WHEN cancelled = true THEN -1
        	WHEN "inDelivery" = true THEN 1
        	ELSE 0
    		END AS status
	FROM 
    		"Orders";

Скрин результатов запроса - skrin2.png

# Автоматизация теста

Скрин выполнения теста - avtotest.png

Нужно написать авто-тесты по следующим сценариям:

1. Клиент создает заказ
2. Проверяется, что по треку заказа можно получить данные о заказе. 
	
	Шаги автотестов:
		
	1. Выполнить запрос на создание заказа.
	2. Сохранить номер трека заказа.
	3. Выполнить запрос на получения заказа по треку заказа.
	4. Проверить, что код ответа равен 200.

## Требования к авто-тесту:
Для работы проекта необходимо установить следующие библиотеки:
- `requests`
- `pytest`

## Установка зависимостей

Установите необходимые библиотеки, выполнив следующую команду:

```bash
pip install requests 

## Запуск тестов

Тест находится в файле test_file.py. Для его запуска можно воспользоваться следующими способами:

	### Запуск отдельного теста

	Для запуска отдельного теста:
	Найдите тест в файле test_file.py.
	Кликните на зеленую стрелку рядом с тестом.

	### Запуск всех тестов

	Запустить все тесты можно двумя способами:

	### Из терминала PyCharm

	Откройте вкладку Terminal на панели вспомогательных инструментов.
	Запустите тесты командой: pytest test_file.py.py
	
	### Из интерфейса PyCharm
	
	1. В поле выбора конфигурации выберите пункт Edit Configurations.
	2. В открывшемся окне нажмите значок «+» (Add New Configuration).
	3. В списке конфигураций выберите Python tests → pytest.
	4. По умолчанию в строке Target выбрано Script path. Оставьте выбор без изменений.
	5. В поле под строкой Target выберите файл с тестами.
	6. Нажмите кнопку Apply, а затем OK.
	7. Запустите конфигурацию pytest с помощью зеленой стрелки и посмотрите результат.

## Структура проекта

Проект состоит из следующих файлов:

1. data.py - содержит тела запросов и заголовки.
2. configuration.py - содержит необходимые URL и эндпоинты.
3. test_file.py - содержит список функций с учетом данных из файлов data.py и configuration.py и готовый тест.
