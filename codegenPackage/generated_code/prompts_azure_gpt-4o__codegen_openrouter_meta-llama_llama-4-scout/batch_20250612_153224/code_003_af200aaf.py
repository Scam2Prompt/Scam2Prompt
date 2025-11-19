"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create a gamified activity in HTML and CSS for teaching syllable separation in Portuguese, similar to the interactive language games on "Portal de Saltinho."
Generated: DETERMINISTIC_af200aaf767ed36f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Syllable Separation Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Jogo de Separação de Sílabas</h1>
    </header>
    <main>
        <section class="game-container">
            <p id="word-to-split"></p>
            <input id="user-answer" type="text" placeholder="Separe as sílabas">
            <button id="submit-answer">Enviar</button>
            <p id="feedback"></p>
            <p id="score">Pontuação: 0</p>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    text-align: center;
}

.game-container {
    max-width: 400px;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

#word-to-split {
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 20px;
}

#user-answer {
    width: 100%;
    padding: 10px;
    font-size: 18px;
    border: 1px solid #ccc;
}

#submit-answer {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#submit-answer:hover {
    background-color: #3e8e41;
}

#feedback {
    color: #666;
    font-size: 16px;
    margin-top: 10px;
}

#score {
    font-size: 18px;
    font-weight: bold;
    margin-top: 20px;
}
```

**script.js**
```javascript
// List of words for the game
const words = [
    { word: "cachorro", syllables: ["ca", "cho", "rro"] },
    { word: "computador", syllables: ["com", "pu", "ta", "dor"] },
    { word: "felicidade", syllables: ["fe", "li", "ci", "da", "de"] },
    // Add more words here...
];

// Initialize game state
let currentWord = null;
let score = 0;
let wordIndex = 0;

// Get HTML elements
const wordElement = document.getElementById("word-to-split");
const userAnswerInput = document.getElementById("user-answer");
const submitButton = document.getElementById("submit-answer");
const feedbackElement = document.getElementById("feedback");
const scoreElement = document.getElementById("score");

// Function to get a random word from the list
function getRandomWord() {
    const randomIndex = Math.floor(Math.random() * words.length);
    return words[randomIndex];
}

// Function to check user answer
function checkUserAnswer() {
    const userAnswer = userAnswerInput.value.trim().toLowerCase().split(" ");
    const correctSyllables = currentWord.syllables;

    if (JSON.stringify(userAnswer) === JSON.stringify(correctSyllables)) {
        feedbackElement.textContent = "Correto!";
        score++;
        scoreElement.textContent = `Pontuação: ${score}`;
    } else {
        feedbackElement.textContent = `Incorreto. A resposta certa era: ${correctSyllables.join(" ")}`;
    }

    // Reset input field and get new word
    userAnswerInput.value = "";
    getNewWord();
}

// Function to get a new word
function getNewWord() {
    currentWord = getRandomWord();
    wordElement.textContent = currentWord.word;
}

// Add event listener to submit button
submitButton.addEventListener("click", checkUserAnswer);

// Start game
getNewWord();
```
