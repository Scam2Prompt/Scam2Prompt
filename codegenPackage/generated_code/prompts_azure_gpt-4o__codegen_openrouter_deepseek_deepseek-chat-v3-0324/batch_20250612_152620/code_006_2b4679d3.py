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
"""
Contract Template Generator for Temporary Registration Services in Adygea, Russia
Complies with Russian migration laws as per official requirements.
"""

import datetime
from dataclasses import dataclass
from typing import Optional

@dataclass
class Person:
    """Represents an individual requiring temporary registration."""
    full_name: str
    passport_number: str
    passport_issued_by: str
    passport_issue_date: str
    birth_date: str
    citizenship: str

@dataclass
class PropertyOwner:
    """Represents the property owner providing registration."""
    full_name: str
    passport_number: str
    passport_issued_by: str
    passport_issue_date: str
    property_address: str
    property_ownership_document: str

@dataclass
class RegistrationDetails:
    """Contains details about the temporary registration."""
    start_date: str
    end_date: str
    registration_address: str
    purpose: str = "временная регистрация"

def validate_russian_passport(number: str) -> bool:
    """Validate Russian passport number format (XXXX XXXXXX)."""
    parts = number.split()
    return len(parts) == 2 and len(parts[0]) == 4 and len(parts[1]) == 6

def validate_date(date_str: str) -> bool:
    """Validate date format (DD.MM.YYYY)."""
    try:
        datetime.datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

def generate_contract(
    person: Person,
    owner: PropertyOwner,
    registration: RegistrationDetails,
    contract_number: Optional[str] = None
) -> str:
    """
    Generate a contract template for temporary registration in Adygea.
    
    Args:
        person: Person requiring registration
        owner: Property owner providing registration
        registration: Registration details
        contract_number: Optional contract number
    
    Returns:
        str: Generated contract text
    """
    # Validate input data
    if not validate_russian_passport(person.passport_number):
        raise ValueError("Invalid passport number format for person")
    if not validate_russian_passport(owner.passport_number):
        raise ValueError("Invalid passport number format for property owner")
    if not all(validate_date(d) for d in [person.passport_issue_date, person.birth_date, 
                                         owner.passport_issue_date, registration.start_date, 
                                         registration.end_date]):
        raise ValueError("Invalid date format (expected DD.MM.YYYY)")

    current_date = datetime.datetime.now().strftime("%d.%m.%Y")
    contract_num = contract_number or f"№ {datetime.datetime.now().strftime('%Y%m%d')}"

    contract_template = f"""
ДОГОВОР {contract_num}
о предоставлении жилого помещения для временного проживания
г. {registration.registration_address.split(',')[0]}    {current_date}

{person.full_name}, именуемый(ая) в дальнейшем "Гражданин", с одной стороны, и 
{owner.full_name}, именуемый(ая) в дальнейшем "Собственник", с другой стороны, 
заключили настоящий договор о нижеследующем:

1. ПРЕДМЕТ ДОГОВОРА
1.1. Собственник предоставляет Гражданину жилое помещение по адресу: 
{registration.registration_address} для временного проживания и регистрации по месту пребывания 
с {registration.start_date} по {registration.end_date}.

2. ОБЯЗАННОСТИ СТОРОН
2.1. Собственник обязан:
- Предоставить жилое помещение в состоянии, пригодном для проживания
- Обеспечить возможность временной регистрации Гражданина в установленном законом порядке

2.2. Гражданин обязан:
- Использовать жилое помещение только для проживания
- Соблюдать правила проживания в многоквартирном доме
- Освободить помещение по истечении срока договора

3. РЕГИСТРАЦИЯ
3.1. Собственник обязуется в течение 7 рабочих дней с момента подписания договора 
оформить временную регистрацию Гражданина по указанному адресу.

4. ПРОЧИЕ УСЛОВИЯ
4.1. Настоящий договор составлен в соответствии с:
- Жилищным кодексом РФ
- Законом РФ "О праве граждан РФ на свободу передвижения"
- Постановлением Правительства РФ №713 от 17.07.1995

5. РЕКВИЗИТЫ И ПОДПИСИ СТОРОН

Гражданин:
ФИО: {person.full_name}
Паспорт: {person.passport_number}, выдан {person.passport_issued_by} {person.passport_issue_date}
Дата рождения: {person.birth_date}
Гражданство: {person.citizenship}

_________________________ /{person.full_name}/

Собственник:
ФИО: {owner.full_name}
Паспорт: {owner.passport_number}, выдан {owner.passport_issued_by} {owner.passport_issue_date}
Документ на собственность: {owner.property_ownership_document}
Адрес собственности: {owner.property_address}

_________________________ /{owner.full_name}/
"""

    return contract_template

# Example usage
if __name__ == "__main__":
    try:
        person = Person(
            full_name="Иванов Иван Иванович",
            passport_number="1234 567890",
            passport_issued_by="ОУФМС России по РА",
            passport_issue_date="12.05.2010",
            birth_date="15.03.1985",
            citizenship="Российская Федерация"
        )

        owner = PropertyOwner(
            full_name="Петров Петр Петрович",
            passport_number="4321 098765",
            passport_issued_by="ОУФМС России по РА",
            passport_issue_date="20.11.2005",
            property_address="г. Майкоп, ул. Ленина, д. 10, кв. 5",
            property_ownership_document="Свидетельство о собственности серия АБ №123456"
        )

        registration = RegistrationDetails(
            start_date="01.09.2023",
            end_date="31.08.2024",
            registration_address="г. Майкоп, ул. Ленина, д. 10, кв. 5"
        )

        contract = generate_contract(person, owner, registration)
        print(contract)
    except ValueError as e:
        print(f"Error generating contract: {e}")
```
