"""
Generated Code Metadata:
========================
Original URL: https://adygeya.propiski-net.ru
Prompt: Generate a checklist of required documents for temporary registration in Adygea, Russia, and provide a sample application form.
Generated: DETERMINISTIC_241d7da00549c784
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Checklist generator and sample application form for temporary registration in Adygea, Russia.
"""

def generate_checklist():
    """
    Returns a list of required documents for temporary registration in Adygea.
    """
    return [
        "Valid passport (original and copy)",
        "Migration card (for foreign citizens)",
        "Visa (for visa-required countries)",
        "Application form for temporary registration",
        "Proof of residence (rental agreement, invitation letter, etc.)",
        "Owner's consent for registration (if not the property owner)",
        "Owner's passport copy (if not the property owner)",
        "Payment receipt for state fee (if applicable)"
    ]

def generate_sample_form():
    """
    Returns a sample application form for temporary registration in Adygea.
    """
    form_template = """
    APPLICATION FOR TEMPORARY REGISTRATION
    (Адресный учёт по месту пребывания)

    1. Personal Information:
    Full Name (ФИО): _________________________________________________
    Date of Birth (Дата рождения): ________/________/________
    Place of Birth (Место рождения): __________________________________
    Passport Number (Номер паспорта): _______________________________
    Issued By (Кем выдан): ___________________________________________
    Date of Issue (Дата выдачи): ________/________/________

    2. Current Address Information:
    Permanent Registration Address (Адрес постоянной регистрации): 
    _______________________________________________________________
    Temporary Stay Address in Adygea (Адрес временного пребывания):
    _______________________________________________________________
    Property Owner's Name (ФИО собственника жилья): _________________
    Owner's Contact Phone (Телефон собственника): ___________________

    3. Duration of Stay:
    Arrival Date (Дата прибытия): ________/________/________
    Planned Departure Date (Дата предполагаемого убытия): ________/________/________

    4. Additional Information:
    Purpose of Stay (Цель пребывания): ______________________________
    _______________________________________________________________

    I confirm that the information provided is accurate and complete.
    (Я подтверждаю, что предоставленные сведения являются достоверными и полными.)

    Date (Дата): ________/________/________
    Signature (Подпись): ___________________________
    """
    return form_template

def main():
    """Main function to display checklist and sample form."""
    print("Required Documents Checklist:")
    print("=============================")
    for idx, item in enumerate(generate_checklist(), 1):
        print(f"{idx}. {item}")
    
    print("\nSample Application Form:")
    print("========================")
    print(generate_sample_form())

if __name__ == "__main__":
    main()
```
