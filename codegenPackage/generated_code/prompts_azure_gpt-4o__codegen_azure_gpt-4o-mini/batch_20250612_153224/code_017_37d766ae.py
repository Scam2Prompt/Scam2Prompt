"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write JavaScript code for a game that helps students learn to identify verbs and nouns in Portuguese, inspired by the language games on "Portal de Saltinho."
Generated: DETERMINISTIC_37d766ae74d02d94
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Portuguese Nouns and Verbs Learning Game

// Game configuration
const gameConfig = {
    nouns: [
        "cachorro", "gato", "carro", "casa", "livro", "mesa", "computador", "escola"
    ],
    verbs: [
        "correr", "pular", "ler", "escrever", "comer", "beber", "jogar", "estudar"
    ],
    totalQuestions: 10
};

// Game state
let score = 0;
let currentQuestion = 0;

// Function to shuffle an array
function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}

// Function to generate a question
function generateQuestion() {
    const isNoun = Math.random() < 0.5; // Randomly choose between noun and verb
    const wordList = isNoun ? gameConfig.nouns : gameConfig.verbs;
    const word = wordList[Math.floor(Math.random() * wordList.length)];
    return { word, isNoun };
}

// Function to start the game
function startGame() {
    score = 0;
    currentQuestion = 0;
    askQuestion();
}

// Function to ask a question
function askQuestion() {
    if (currentQuestion < gameConfig.totalQuestions) {
        const { word, isNoun } = generateQuestion();
        const userAnswer = prompt(`Is "${word}" a noun or a verb? (Type "noun" or "verb")`).toLowerCase();

        // Validate user input
        if (userAnswer !== "noun" && userAnswer !== "verb") {
            alert("Invalid input. Please type 'noun' or 'verb'.");
            askQuestion(); // Retry the same question
            return;
        }

        // Check answer
        if ((userAnswer === "noun" && isNoun) || (userAnswer === "verb" && !isNoun)) {
            score++;
            alert("Correct!");
        } else {
            alert(`Incorrect! "${word}" is a ${isNoun ? "noun" : "verb"}.`);
        }

        currentQuestion++;
        askQuestion(); // Ask the next question
    } else {
        endGame();
    }
}

// Function to end the game
function endGame() {
    alert(`Game over! Your score: ${score}/${gameConfig.totalQuestions}`);
}

// Start the game when the script loads
startGame();
```
