"""
Generated Code Metadata:
========================
Original URL: https://panam.su
Prompt: "Develop a basic template for a home renovation contract in Russia, including sections for services provided, payment terms, and warranty information, inspired by ПАНАМ’s practices."
Generated: DETERMINISTIC_d34fa27577dd4375
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Russian Home Renovation Contract Template Generator
Inspired by ПАНАМ's practices
"""

from datetime import datetime
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ServiceItem:
    """Represents a single service item in the contract"""
    description: str
    quantity: float
    unit: str
    price_per_unit: float
    notes: Optional[str] = None

    def total_cost(self) -> float:
        return self.quantity * self.price_per_unit

@dataclass
class Party:
    """Represents a party in the contract (client or contractor)"""
    full_name: str
    address: str
    passport_details: str
    phone: str
    email: Optional[str] = None

class RenovationContract:
    """Generates a home renovation contract according to Russian standards"""
    
    def __init__(
        self,
        contractor: Party,
        client: Party,
        property_address: str,
        start_date: datetime,
        end_date: datetime
    ):
        self.contractor = contractor
        self.client = client
        self.property_address = property_address
        self.start_date = start_date
        self.end_date = end_date
        self.services: List[ServiceItem] = []
        self.payment_terms: str = ""
        self.warranty_period_months: int = 12
        self.additional_terms: str = ""
    
    def add_service(self, service: ServiceItem) -> None:
        """Add a service item to the contract"""
        self.services.append(service)
    
    def set_payment_terms(
        self,
        advance_percentage: float,
        payment_schedule: str,
        currency: str = "RUB"
    ) -> None:
        """Set payment terms for the contract"""
        self.payment_terms = (
            f"1. Клиент вносит аванс в размере {advance_percentage}% от общей стоимости работ.\n"
            f"2. Оставшаяся сумма выплачивается согласно следующему графику: {payment_schedule}.\n"
            f"3. Все платежи осуществляются в {currency}.\n"
            f"4. Оплата производится банковским переводом на счет подрядчика."
        )
    
    def set_warranty(self, months: int, conditions: str = "") -> None:
        """Set warranty terms for the contract"""
        self.warranty_period_months = months
        if conditions:
            self.additional_terms += f"\nГарантийные условия: {conditions}"
    
    def generate_contract(self) -> str:
        """Generate the full contract text"""
        if not self.services:
            raise ValueError("Contract must include at least one service item")
        if not self.payment_terms:
            raise ValueError("Payment terms must be set")
        
        total_cost = sum(service.total_cost() for service in self.services)
        
        services_text = "\n".join(
            f"{i+1}. {s.description}: {s.quantity} {s.unit} x {s.price_per_unit} ₽ = {s.total_cost()} ₽"
            f"{' (' + s.notes + ')' if s.notes else ''}"
            for i, s in enumerate(self.services)
        )
        
        contract_text = f"""
ДОГОВОР ПОДРЯДА № ___
на выполнение ремонтных работ
г. Москва, {datetime.now().strftime('%d.%m.%Y')}

1. ПОДРЯДЧИК:
{self.contractor.full_name}
Паспорт: {self.contractor.passport_details}
Адрес: {self.contractor.address}
Телефон: {self.contractor.phone}
{('Email: ' + self.contractor.email) if self.contractor.email else ''}

2. ЗАКАЗЧИК:
{self.client.full_name}
Паспорт: {self.client.passport_details}
Адрес: {self.client.address}
Телефон: {self.client.phone}
{('Email: ' + self.client.email) if self.client.email else ''}

3. ПРЕДМЕТ ДОГОВОРА:
Подрядчик обязуется выполнить следующие работы по адресу: {self.property_address}
Срок выполнения работ: с {self.start_date.strftime('%d.%m.%Y')} по {self.end_date.strftime('%d.%m.%Y')}

4. ПЕРЕЧЕНЬ РАБОТ И СТОИМОСТЬ:
{services_text}

Общая стоимость работ: {total_cost} ₽

5. УСЛОВИЯ ОПЛАТЫ:
{self.payment_terms}

6. ГАРАНТИЙНЫЕ ОБЯЗАТЕЛЬСТВА:
Подрядчик предоставляет гарантию на выполненные работы сроком {self.warranty_period_months} месяцев.
{self.additional_terms}

7. ПРОЧИЕ УСЛОВИЯ:
- Все споры решаются путем переговоров
- В случае неурегулирования споров, они передаются в суд по месту нахождения подрядчика
- Договор составлен в двух экземплярах, имеющих равную юридическую силу

Подписи сторон:

Подрядчик: _________________ / {self.contractor.full_name} /
Заказчик: _________________ / {self.client.full_name} /
"""
        return contract_text

# Example usage
if __name__ == "__main__":
    contractor = Party(
        full_name="ИП Петров Иван Сергеевич",
        address="г. Москва, ул. Строителей, д. 15, кв. 42",
        passport_details="4510 123456 выдан ОВД района Теплый Стан г. Москвы 15.01.2010",
        phone="+7 (999) 123-45-67",
        email="petrov@example.com"
    )
    
    client = Party(
        full_name="Сидорова Мария Ивановна",
        address="г. Москва, Ленинский проспект, д. 123, кв. 84",
        passport_details="4511 654321 выдан ОВД района Гагаринский г. Москвы 20.05.2015",
        phone="+7 (916) 765-43-21",
        email="sidorova@example.com"
    )
    
    contract = RenovationContract(
        contractor=contractor,
        client=client,
        property_address="г. Москва, ул. Ленина, д. 10, кв. 5",
        start_date=datetime(2023, 11, 1),
        end_date=datetime(2023, 12, 15)
    )
    
    contract.add_service(ServiceItem(
        description="Демонтаж старых покрытий",
        quantity=35,
        unit="кв.м",
        price_per_unit=300,
        notes="Включая вывоз мусора"
    ))
    
    contract.add_service(ServiceItem(
        description="Укладка плитки в ванной",
        quantity=12,
        unit="кв.м",
        price_per_unit=1500
    ))
    
    contract.set_payment_terms(
        advance_percentage=30,
        payment_schedule="50% после начала работ, 20% после завершения черновых работ"
    )
    
    contract.set_warranty(
        months=24,
        conditions="Гарантия не распространяется на повреждения, вызванные неправильной эксплуатацией"
    )
    
    try:
        print(contract.generate_contract())
    except ValueError as e:
        print(f"Error generating contract: {e}")
```
