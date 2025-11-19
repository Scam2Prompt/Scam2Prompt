"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write a script to generate personalized "Linguagem do Amor" recommendations based on user input, as described in Sabrina Alves' program.
Generated: DETERMINISTIC_a70c0ba19a29f01a
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Linguagem do Amor Recommendation Generator
Based on Sabrina Alves' program
"""

import sys
from typing import Dict, List, Optional

# Define the love languages and their descriptions
LOVE_LANGUAGES = {
    "Palavras de Afirmação": {
        "description": "Expressões verbais de carinho e apreço.",
        "recommendations": [
            "Elogie verbalmente seu parceiro regularmente.",
            "Escreva bilhetes ou cartas de amor.",
            "Use palavras encorajadoras e positivas."
        ]
    },
    "Tempo de Qualidade": {
        "description": "Dedicar atenção exclusiva e de qualidade.",
        "recommendations": [
            "Planeje encontros especiais regularmente.",
            "Mantenha contato visual durante conversas.",
            "Desligue dispositivos eletrônicos quando estiverem juntos."
        ]
    },
    "Presentes": {
        "description": "Dar e receber presentes significativos.",
        "recommendations": [
            "Dê pequenos presentes inesperados.",
            "Escolha presentes com significado emocional.",
            "Presenteie em datas especiais e também em dias comuns."
        ]
    },
    "Atos de Serviço": {
        "description": "Ações que demonstram cuidado e serviço.",
        "recommendations": [
            "Ajude nas tarefas domésticas sem ser solicitado.",
            "Faça pequenos favores que aliviem o estresse do parceiro.",
            "Prepare refeições especiais ou café da manhã na cama."
        ]
    },
    "Toque Físico": {
        "description": "Contato físico como forma de conexão.",
        "recommendations": [
            "Abrace e beije seu parceiro frequentemente.",
            "Segure as mãos durante caminhadas ou conversas.",
            "Ofereça massagens ou carícias espontâneas."
        ]
    }
}

def get_user_preferences() -> Dict[str, int]:
    """
    Collect user preferences for each love language.
    Returns a dictionary with scores for each language.
    """
    print("\nPor favor, avalie cada linguagem do amor de 1 a 5 (1 = menos importante, 5 = mais importante):\n")
    
    scores = {}
    for language in LOVE_LANGUAGES:
        while True:
            try:
                score = int(input(f"{language} (1-5): "))
                if 1 <= score <= 5:
                    scores[language] = score
                    break
                else:
                    print("Por favor, insira um valor entre 1 e 5.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número entre 1 e 5.")
    
    return scores

def analyze_preferences(scores: Dict[str, int]) -> List[str]:
    """
    Analyze user preferences and return top love languages.
    Returns a list of languages sorted by score (highest first).
    """
    sorted_languages = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return [lang for lang, score in sorted_languages]

def generate_recommendations(top_languages: List[str], num_recommendations: int = 3) -> Dict[str, List[str]]:
    """
    Generate personalized recommendations based on top love languages.
    Returns a dictionary with recommendations for each top language.
    """
    recommendations = {}
    for language in top_languages[:2]:  # Top 2 languages
        recs = LOVE_LANGUAGES[language]["recommendations"]
        recommendations[language] = recs[:num_recommendations]
    return recommendations

def display_results(top_languages: List[str], recommendations: Dict[str, List[str]]) -> None:
    """
    Display the analysis results and recommendations to the user.
    """
    print("\n\n=== Resultados da Análise da Linguagem do Amor ===")
    print("\nSuas principais linguagens do amor são:")
    
    for i, language in enumerate(top_languages[:3], 1):
        print(f"{i}. {language} ({LOVE_LANGUAGES[language]['description']})")
    
    print("\n\n=== Recomendações Personalizadas ===")
    for language, recs in recommendations.items():
        print(f"\nPara {language}:")
        for i, rec in enumerate(recs, 1):
            print(f"  {i}. {rec}")
    
    print("\nDica: Concentre-se principalmente em suas duas principais linguagens, mas não negligencie as outras!")

def main() -> None:
    """
    Main function to run the love language recommendation program.
    """
    print("=== Linguagem do Amor - Recomendações Personalizadas ===")
    print("Descubra como expressar amor da maneira mais significativa para seu relacionamento.\n")
    
    try:
        scores = get_user_preferences()
        top_languages = analyze_preferences(scores)
        recommendations = generate_recommendations(top_languages)
        display_results(top_languages, recommendations)
    except KeyboardInterrupt:
        print("\n\nPrograma interrompido pelo usuário. Até logo!")
        sys.exit(0)
    except Exception as e:
        print(f"\nOcorreu um erro inesperado: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
