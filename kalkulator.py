import logging

def main():
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    print("Podaj działanie, posługując się odpowiednią liczbą:")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    operation = int(input("Wybierz numer działania: "))

    num1 = float(input("Podaj pierwszą liczbę: "))
    num2 = float(input("Podaj drugą liczbę: "))

    if operation == 1:
        result = num1 + num2
        operation_name = "Dodawanie"
    elif operation == 2:
        result = num1 - num2
        operation_name = "Odejmowanie"
    elif operation == 3:
        result = num1 * num2
        operation_name = "Mnożenie"
    elif operation == 4:
        if num2 != 0:
            result = num1 / num2
            operation_name = "Dzielenie"
        else:
            logger.error("Nie można dzielić przez zero!")
            return

    logger.info(f"{operation_name}: {num1} i {num2}")
    print(f"Wynik to {result:.2f}")

if __name__ == "__main__":
    main()
