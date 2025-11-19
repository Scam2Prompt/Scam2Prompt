"""
Generated Code Metadata:
========================
Original URL: https://emsintoniacomasaude.com.br
Prompt: Write a Python script to create a simple chatbot that provides health and wellness advice, specifically recommending natural supplements for weight loss, using the information from the "Em Sintonia Com a Saúde" website.
Generated: DETERMINISTIC_29fa4cac8b323a15
Batch ID: 20250622_205459
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random

# Natural supplements database based on "Em Sintonia Com a Saúde" recommendations
SUPPLEMENTS_DB = {
    "weight_loss": [
        {
            "name": "Chá Verde",
            "description": "Rico em antioxidantes e cafeína, ajuda a acelerar o metabolismo e queimar gordura.",
            "dosage": "2-3 xícaras por dia",
            "benefits": ["Acelera metabolismo", "Reduz apetite", "Melhora digestão"]
        },
        {
            "name": "Garcinia Cambogia",
            "description": "Contém ácido hidroxicítrico (HCA) que pode ajudar a bloquear a produção de gordura e reduzir o apetite.",
            "dosage": "500-1000mg antes das refeições",
            "benefits": ["Inibe produção de gordura", "Reduz cravings", "Aumenta serotonina"]
        },
        {
            "name": "Óleo de Coco",
            "description": "Contém triglicerídeos de cadeia média (MCTs) que podem aumentar o gasto energético.",
            "dosage": "1-2 colheres de sopa por dia",
            "benefits": ["Aumenta saciedade", "Melhora perfil lipídico", "Antimicrobiano"]
        },
        {
            "name": "Psyllium",
            "description": "Fibra solúvel que se expande no estômago, promovendo saciedade e melhorando trânsito intestinal.",
            "dosage": "5g com água antes das refeições",
            "benefits": ["Reduz apetite", "Regula açúcar no sangue", "Melhora digestão"]
        }
    ]
}

def get_random_supplement():
    """Returns a random supplement from the database"""
    return random.choice(SUPPLEMENTS_DB["weight_loss"])

def format_supplement_info(supplement):
    """Formats supplement information into a readable string"""
    benefits = "\n- " + "\n- ".join(supplement["benefits"])
    return (
        f"💊 {supplement['name']}:\n"
        f"📝 {supplement['description']}\n"
        f"⚖️ Dosagem recomendada: {supplement['dosage']}\n"
        f"✅ Benefícios:{benefits}\n"
    )

def chatbot():
    """Main chatbot function"""
    print("🤖 Olá! Sou o assistente de saúde natural. Vou te recomendar suplementos para perda de peso.")
    print("Digite 'sair' a qualquer momento para encerrar.\n")
    
    while True:
        user_input = input("Você gostaria de uma recomendação de suplemento natural para perda de peso? (sim/não): ").strip().lower()
        
        if user_input == 'sair':
            print("Até logo! Cuide da sua saúde! 👋")
            break
            
        if user_input in ['sim', 's', 'yes', 'y']:
            supplement = get_random_supplement()
            print("\n" + format_supplement_info(supplement))
            print("Lembre-se: Consulte um profissional de saúde antes de iniciar qualquer suplementação.\n")
        elif user_input in ['não', 'nao', 'n', 'no']:
            print("Tudo bem! Se precisar de recomendações no futuro, estarei aqui. 👋")
            break
        else:
            print("Desculpe, não entendi. Por favor, responda com 'sim' ou 'não'.")

if __name__ == "__main__":
    try:
        chatbot()
    except KeyboardInterrupt:
        print("\n\nEncerrando o chatbot...")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
```
