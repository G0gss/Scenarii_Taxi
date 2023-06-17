import datetime # Добавил модуль datatime для дальнейшего его использования в деконаторе

def taxi_payment(distance): 
   
    distance_meters = distance * 1000
   
    num_blocks = distance_meters // 140

    total_payment = 4 + num_blocks * 0.25
    return total_payment


def log_calls(func):
    def wrapper(*args, **kwargs):
       
        now = datetime.datetime.now()
        print(f"Функция {func.__name__}, текущая дата и время {now}")
        print(f"Аргумент: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

# декоратор к функции taxi_payment
@log_calls
def taxi_payment_decorated(distance):
    return taxi_payment(distance)

# Пример вызова функции
distance_km = 6.2
total_payment = taxi_payment(distance_km)
print(f"Общая сумма оплаты за поездку на такси составляет ${total_payment:.2f} расстояние поездки составляет {distance_km} км")

# Пример вызова декорированной функции
distance_km = 6.2
total_payment = taxi_payment_decorated(distance_km)
