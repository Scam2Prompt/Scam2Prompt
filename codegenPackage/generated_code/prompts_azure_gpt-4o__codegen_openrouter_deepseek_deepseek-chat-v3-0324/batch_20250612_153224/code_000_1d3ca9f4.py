"""
Generated Code Metadata:
========================
Original URL: https://sabrinaalves.com
Prompt: Write code to create a web-based "Teste do Perfil de Dependência Emocional" quiz as described in Sabrina Alves' methodology, including scoring logic and personalized feedback.
Generated: DETERMINISTIC_1d3ca9f4d561bd5e
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Teste do Perfil de Dependência Emocional</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .question {
            background-color: white;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .options {
            margin-top: 10px;
        }
        .option {
            margin-bottom: 10px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            display: block;
            margin: 30px auto;
        }
        button:hover {
            background-color: #2980b9;
        }
        #result {
            display: none;
            background-color: white;
            padding: 30px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        .result-title {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 20px;
        }
        .result-description {
            margin-bottom: 20px;
        }
        .score {
            font-weight: bold;
            text-align: center;
            font-size: 18px;
            margin-bottom: 20px;
        }
        .progress-container {
            width: 100%;
            background-color: #f1f1f1;
            border-radius: 5px;
            margin-bottom: 30px;
        }
        .progress-bar {
            height: 20px;
            background-color: #3498db;
            border-radius: 5px;
            width: 0%;
            transition: width 0.5s;
        }
    </style>
</head>
<body>
    <h1>Teste do Perfil de Dependência Emocional</h1>
    
    <div id="quiz-container">
        <div class="progress-container">
            <div id="progress-bar" class="progress-bar"></div>
        </div>
        
        <div id="questions">
            <!-- Questions will be inserted here by JavaScript -->
        </div>
        
        <button id="submit-btn" onclick="calculateScore()">Ver Resultado</button>
    </div>
    
    <div id="result">
        <h2 class="result-title">Seu Resultado</h2>
        <div class="score">Sua pontuação: <span id="final-score">0</span>/100</div>
        <div id="result-description" class="result-description"></div>
        <button onclick="resetQuiz()">Fazer o Teste Novamente</button>
    </div>

    <script>
        // Questions and options for the quiz
        const questions = [
            {
                question: "1. Com que frequência você sente que precisa da aprovação de outras pessoas para se sentir bem consigo mesmo?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "2. Quando está em um relacionamento, você tem dificuldade em tomar decisões sem consultar seu parceiro(a)?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "3. Você sente que sua felicidade depende principalmente de outras pessoas?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "4. Com que frequência você evita expressar suas opiniões por medo de desagradar os outros?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "5. Você tem dificuldade em terminar relacionamentos, mesmo quando sabe que não são saudáveis?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "6. Quando está sozinho(a), você sente uma forte necessidade de estar com alguém?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "7. Você frequentemente se preocupa com a possibilidade de ser abandonado(a) por pessoas importantes para você?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "8. Você já deixou de fazer coisas que gostava para agradar ou não desapontar alguém?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "9. Você sente que precisa constantemente de demonstrações de amor e afeto para se sentir seguro(a) em um relacionamento?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            },
            {
                question: "10. Você tem dificuldade em dizer 'não' mesmo quando isso vai contra seus interesses ou necessidades?",
                options: [
                    { text: "Nunca", value: 0 },
                    { text: "Raramente", value: 1 },
                    { text: "Às vezes", value: 2 },
                    { text: "Frequentemente", value: 3 },
                    { text: "Sempre", value: 4 }
                ]
            }
        ];

        // Results descriptions based on score ranges
        const results = [
            {
                minScore: 0,
                maxScore: 15,
                title: "Baixa Dependência Emocional",
                description: "Você demonstra uma boa independência emocional e consegue manter sua identidade e autoestima sem depender excessivamente dos outros. Continue cultivando sua autonomia e autoconfiança!"
            },
            {
                minScore: 16,
                maxScore: 25,
                title: "Dependência Emocional Moderada",
                description: "Você apresenta alguns sinais de dependência emocional,
