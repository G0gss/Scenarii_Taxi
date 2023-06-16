import datetime # Добавил модуль datatime для дальнейшего его использования в деконаторе

def taxi_payment(distance): #Создал функцию taxi_payment которая принимает расстояние в киллометрах
    # Конвертируем расстояние в километрах в расстояние в метрах
    distance_meters = distance * 1000
    # Считаем количество блоков по 140 метров (это нужно для того чтобы в легче было расчитывать стоймость поездки, так как за каждые 140 метров к стоймости добавляется 0.25$ )
    num_blocks = distance_meters // 140
    # Считаем итоговую стоимость
    total_payment = 4 + num_blocks * 0.25
    return total_payment

# Создал декоратор для логирования вызовов функции
def log_calls(func):
    def wrapper(*args, **kwargs):
        # Получаем текущую дату и время с помощбю комманд модуля datetime
        now = datetime.datetime.now()
        # Выводим информацию о вызове функции
        print(f"Function {func.__name__}, текущая дата и время {now}")
        print(f"Arguments: {args}, {kwargs}")
        # Вызываем функцию и сохраняем результат
        result = func(*args, **kwargs)
        # Выводим результат
        print(f"Result: {result}")
        return result
    return wrapper

# Добавил декоратор к функции taxi_payment
@log_calls
def taxi_payment_decorated(distance):
    return taxi_payment(distance)

# Пример вызова функции
distance_km = 6.2
total_payment = taxi_payment(distance_km)
print(f"Общая сумма оплаты за поездку на такси составляет ${total_payment:.2f} расстояние поездки составляет {distance_km} км")

# Пример вызова декорированной функции
distance_km = 10.2
total_payment = taxi_payment_decorated(distance_km)