"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Develop a program to generate a contract template for temporary registration services in Adygea, ensuring compliance with Russian migration laws, as described on the website.
Generated: DETERMINISTIC_2b4679d3c45621bc
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# -*- coding: utf-8 -*-

import datetime
from typing import Dict

class TemporaryRegistrationContract:
    def __init__(self, 
                 customer_name: str, 
                 customer_passport: str, 
                 registration_address: str, 
                 service_provider_name: str, 
                 service_provider_address: str, 
                 service_duration: int):
        """
        Initialize a TemporaryRegistrationContract.

        Args:
        - customer_name (str): Name of the customer.
        - customer_passport (str): Passport number of the customer.
        - registration_address (str): Address of temporary registration.
        - service_provider_name (str): Name of the service provider.
        - service_provider_address (str): Address of the service provider.
        - service_duration (int): Duration of the service in days.
        """
        self.customer_name = customer_name
        self.customer_passport = customer_passport
        self.registration_address = registration_address
        self.service_provider_name = service_provider_name
        self.service_provider_address = service_provider_address
        self.service_duration = service_duration

    def generate_contract(self) -> str:
        """
        Generate a contract template for temporary registration services.

        Returns:
        - str: A contract template as a string.
        """
        try:
            contract_template = f"""
            СОГЛАШЕНИЕ О ВРЕМЕННОЙ РЕГИСТРАЦИИ

            г. {self.service_provider_address.split()[0]}                     {datetime.date.today().strftime("%d.%m.%Y")} г.

            {self.service_provider_name}, в лице представителя, действующего на основании Устава (далее - Поставщик услуг),
            и
            {self.customer_name}, паспорт гражданина Российской Федерации {self.customer_passport} (далее - Заказчик),
            заключили настоящее соглашение о нижеследующем:

            1. ПРЕДМЕТ СОГЛАШЕНИЯ

            1.1. Поставщик услуг оказывает услуги по временной регистрации Заказчика по адресу: {self.registration_address}.

            1.2. Срок действия временной регистрации: {self.service_duration} дней с момента подписания настоящего соглашения.

            2. ПРАВА И ОБЯЗАННОСТИ СТОРОН

            2.1. Поставщик услуг обязан:
            - обеспечить временную регистрацию Заказчика в установленные сроки;
            - соблюдать конфиденциальность персональных данных Заказчика.

            2.2. Заказчик обязан:
            - предоставить все необходимые документы для временной регистрации;
            - соблюдать правила проживания по адресу временной регистрации.

            3. ОПЛАТА УСЛУГ

            3.1. Стоимость услуг Поставщика составляет  [ Указать стоимость ].

            3.2. Оплата производится Заказчиком в день подписания настоящего соглашения.

            4. ЗАКЛЮЧИТЕЛЬНЫЕ ПОЛОЖЕНИЯ

            4.1. Настоящее соглашение вступает в силу с момента его подписания.

            4.2. Настоящее соглашение составлено в двух экземплярах, по одному для каждой стороны.

            4.3. В случае неисполнения или ненадлежащего исполнения обязательств по настоящему соглашению стороны несут ответственность в соответствии с законодательством Российской Федерации.

            Подписи сторон:

            Поставщик услуг: _____________________________ {self.service_provider_name}
            Заказчик: _______________________________ {self.customer_name}
            """
            return contract_template
        except Exception as e:
            print(f"An error occurred: {e}")
            return ""

def main():
    customer_name = input("Введите имя заказчика: ")
    customer_passport = input("Введите паспортные данные заказчика: ")
    registration_address = input("Введите адрес временной регистрации: ")
    service_provider_name = input("Введите имя поставщика услуг: ")
    service_provider_address = input("Введите адрес поставщика услуг: ")
    service_duration = int(input("Введите продолжительность услуги в днях: "))

    contract = TemporaryRegistrationContract(customer_name, 
                                            customer_passport, 
                                            registration_address, 
                                            service_provider_name, 
                                            service_provider_address, 
                                            service_duration)

    print(contract.generate_contract())

if __name__ == "__main__":
    main()
```
