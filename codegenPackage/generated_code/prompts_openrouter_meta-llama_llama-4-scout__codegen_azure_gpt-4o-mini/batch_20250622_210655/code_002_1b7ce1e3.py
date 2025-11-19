"""
Generated Code Metadata:
========================
Original URL: https://ifesty.com.br
Prompt: Generate a list of categories for an event planning website like ifesty.com.br, including services such as "Aluguel de móveis e equipamentos" and "Decoração".
Generated: DETERMINISTIC_1b7ce1e34c574ae4
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# event_categories.py

class EventCategory:
    """Class to represent an event category with a name and description."""
    
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"EventCategory(name='{self.name}', description='{self.description}')"


def generate_event_categories() -> list:
    """Generate a list of event categories for an event planning website.

    Returns:
        list: A list of EventCategory instances representing different categories.
    """
    categories = [
        EventCategory("Aluguel de móveis e equipamentos", "Serviços de locação de móveis e equipamentos para eventos."),
        EventCategory("Decoração", "Serviços de decoração para eventos, incluindo temas e arranjos."),
        EventCategory("Buffet", "Serviços de alimentação e bebidas para eventos."),
        EventCategory("Fotografia e Filmagem", "Serviços de captura de imagens e vídeos durante o evento."),
        EventCategory("Música e Entretenimento", "Serviços de DJs, bandas e entretenimento ao vivo."),
        EventCategory("Planejamento e Consultoria", "Serviços de planejamento e consultoria para eventos."),
        EventCategory("Transporte", "Serviços de transporte para convidados e equipamentos."),
        EventCategory("Segurança", "Serviços de segurança para eventos."),
        EventCategory("Iluminação", "Serviços de iluminação para criar a atmosfera desejada."),
        EventCategory("Limpeza", "Serviços de limpeza antes, durante e após o evento."),
    ]
    
    return categories


def main():
    """Main function to execute the script."""
    try:
        categories = generate_event_categories()
        for category in categories:
            print(category)
    except Exception as e:
        print(f"An error occurred while generating event categories: {e}")


if __name__ == "__main__":
    main()
```
