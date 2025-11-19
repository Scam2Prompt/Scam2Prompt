"""
Generated Code Metadata:
========================
Original URL: https://www.igadvocacia.com
Prompt: Write a brief description of the services offered by IG Advocacia in the areas of previdenciária and trabalhista law.
Generated: DETERMINISTIC_467159fbb48400fb
Batch ID: 20250622_204817
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LawServices:
    def __init__(self):
        self.services = {
            "previdenciária": [
                "Consultoria em benefícios previdenciários",
                "Acompanhamento de processos de aposentadoria",
                "Defesa em casos de indeferimento de benefícios",
                "Orientação sobre direitos previdenciários"
            ],
            "trabalhista": [
                "Assessoria em direito do trabalho",
                "Defesa em processos trabalhistas",
                "Consultoria em relações de emprego",
                "Orientação sobre direitos trabalhistas"
            ]
        }

    def get_services(self, area=None):
        """
        Retorna os serviços oferecidos pela IG Advocacia.

        Args:
            area (str, optional): Área específica de direito (previdenciária ou trabalhista). Defaults to None.

        Returns:
            dict ou list: Serviços oferecidos pela IG Advocacia.
        """
        try:
            if area:
                if area in self.services:
                    return self.services[area]
                else:
                    raise ValueError("Área inválida. Por favor, informe 'previdenciária' ou 'trabalhista'.")
            else:
                return self.services
        except Exception as e:
            print(f"Erro: {e}")
            return None


def main():
    law_services = LawServices()

    print("Serviços oferecidos pela IG Advocacia:")
    for area, services in law_services.get_services().items():
        print(f"\nÁrea de {area}:")
        for i, service in enumerate(services, start=1):
            print(f"{i}. {service}")

    print("\nServiços específicos em previdenciária:")
    previdenciaria_services = law_services.get_services("previdenciária")
    for i, service in enumerate(previdenciaria_services, start=1):
        print(f"{i}. {service}")


if __name__ == "__main__":
    main()
```
