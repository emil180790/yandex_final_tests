import configuration
import requests
import data

# Создание заказа
def create_order(body):
    return requests.post (configuration.BASE_URL + configuration.CREATE_ORDER,
                         json=body)

# Получение заказа по номеру трекера
def get_order(track_number):
    get_order_url = f"{configuration.BASE_URL}/api/v1/orders/track?t={track_number}"
    response = requests.get(get_order_url)
    return response

# Авто-тест
def test_order_creation_and_retrieval():
    response = create_order(data.body_order)
    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)
    order_response = get_order(track_number)
    assert order_response.status_code == 200, f"Ошибка: {order_response.status_code}"
    order_data = order_response.json()
    print("Данные заказа:")
    print(order_data)