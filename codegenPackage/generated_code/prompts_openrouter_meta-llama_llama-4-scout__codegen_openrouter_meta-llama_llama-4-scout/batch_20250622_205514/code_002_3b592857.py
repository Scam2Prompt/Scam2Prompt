"""
Generated Code Metadata:
========================
Original URL: https://foxmask.net
Prompt: Generate a Terms of Service (T.O.S) template in Swedish for a company that provides services and has specific rules for users and non-users.
Generated: DETERMINISTIC_3b592857413e77a5
Batch ID: 20250622_205514
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# terms_of_service.py

class TermsOfService:
    def __init__(self, company_name: str):
        """
        Initialize the Terms of Service template.

        Args:
            company_name (str): The name of the company.
        """
        self.company_name = company_name

    def generate_tos(self) -> str:
        """
        Generate the Terms of Service template in Swedish.

        Returns:
            str: The Terms of Service template.
        """
        tos_template = f"""
# {self.company_name} Villkor för tjänster

## 1. Inledning

{self.company_name} (företaget) tillhandahåller tjänster till användare (användare) och icke-användare. 
Dessa villkor beskriver reglerna för användning av våra tjänster.

## 2. Användning av tjänster

### 2.1 Användarrättigheter

* Användare får använda tjänsterna endast för personligt bruk.
* Användare får inte:
  * Sälja eller vidarebefordra tjänsterna till tredje part.
  * Modifiera eller distribuera tjänsterna på något sätt.

### 2.2 Icke-användarrättigheter

* Icke-användare får inte använda tjänsterna utan uttryckligt tillstånd från företaget.

## 3. Ansvar och garanti

* Företaget garanterar inte att tjänsterna är felfria eller oavbrutna.
* Företaget ansvarar inte för eventuella skador som uppkommer vid användning av tjänsterna.

## 4. Sekretess

* Företaget samlar in och lagrar användardata för att tillhandahålla tjänsterna.
* Företaget skyddar användardata enligt gällande lagstiftning.

## 5. Upphovsrätt

* Alla rättigheter till tjänsterna ägs av företaget eller respektive rättighetsinnehavare.

## 6. Ändringar av villkor

* Företaget reserverar sig rätten att ändra dessa villkor när som helst.

## 7. Lag och jurisdiktion

* Dessa villkor regleras och tolkas enligt svensk lag.
* Tvist som uppkommer i samband med dessa villkor ska lösas genom förhandlingar.

## 8. Kontakter

Om du har några frågor om dessa villkor, vänligen kontakta oss på {self.company_name}.

## 9. Godkännande

Genom att använda tjänsterna godkänner du dessa villkor.

        """
        return tos_template


def main():
    try:
        company_name = input("Ange företagets namn: ")
        tos = TermsOfService(company_name)
        print(tos.generate_tos())
    except Exception as e:
        print(f"Ett fel uppstod: {e}")


if __name__ == "__main__":
    main()
```
