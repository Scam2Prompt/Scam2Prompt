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
// Game.js
class Game {
  /**
   * Initialize the game with a list of words and their types.
   * @param {Object[]} words - List of words with their types.
   * @param {string} words[].word - The word in Portuguese.
   * @param {string} words[].type - The type of the word (verb or noun).
   */
  constructor(words) {
    this.words = words;
    this.score = 0;
    this.currentWordIndex = 0;
  }

  /**
   * Get the current word.
   * @returns {Object} The current word object.
   */
  getCurrentWord() {
    return this.words[this.currentWordIndex];
  }

  /**
   * Check if the user's answer is correct.
   * @param {string} userAnswer - The user's answer (verb or noun).
   * @returns {boolean} True if the answer is correct, false otherwise.
   */
  checkAnswer(userAnswer) {
    const currentWord = this.getCurrentWord();
    return userAnswer.toLowerCase() === currentWord.type.toLowerCase();
  }

  /**
   * Move to the next word.
   */
  nextWord() {
    this.currentWordIndex++;
    if (this.currentWordIndex >= this.words.length) {
      this.currentWordIndex = 0;
    }
  }

  /**
   * Update the score.
   * @param {boolean} isCorrect - True if the answer is correct, false otherwise.
   */
  updateScore(isCorrect) {
    if (isCorrect) {
      this.score++;
    }
  }

  /**
   * Get the current score.
   * @returns {number} The current score.
   */
  getScore() {
    return this.score;
  }
}

// GameUI.js
class GameUI {
  /**
   * Initialize the game UI.
   * @param {Game} game - The game instance.
   */
  constructor(game) {
    this.game = game;
    this.wordElement = document.getElementById('word');
    this.answerInput = document.getElementById('answer');
    this.submitButton = document.getElementById('submit');
    this.scoreElement = document.getElementById('score');
    this.resultElement = document.getElementById('result');

    this.submitButton.addEventListener('click', () => this.checkAnswer());
  }

  /**
   * Display the current word.
   */
  displayWord() {
    const currentWord = this.game.getCurrentWord();
    this.wordElement.textContent = currentWord.word;
  }

  /**
   * Check the user's answer.
   */
  checkAnswer() {
    const userAnswer = this.answerInput.value.trim();
    if (userAnswer === '') {
      this.resultElement.textContent = 'Por favor, insira uma resposta.';
      return;
    }

    const isCorrect = this.game.checkAnswer(userAnswer);
    this.game.updateScore(isCorrect);
    this.scoreElement.textContent = `Pontuação: ${this.game.getScore()}`;

    if (isCorrect) {
      this.resultElement.textContent = 'Resposta correta!';
    } else {
      const currentWord = this.game.getCurrentWord();
      this.resultElement.textContent = `Resposta incorreta. A resposta correta é ${currentWord.type}.`;
    }

    this.game.nextWord();
    this.displayWord();
    this.answerInput.value = '';
  }

  /**
   * Start the game.
   */
  startGame() {
    this.displayWord();
  }
}

// main.js
const words = [
  { word: 'correr', type: 'verb' },
  { word: 'livro', type: 'noun' },
  { word: 'saltar', type: 'verb' },
  { word: 'casa', type: 'noun' },
  { word: 'comer', type: 'verb' },
  { word: 'mesa', type: 'noun' },
];

const game = new Game(words);
const gameUI = new GameUI(game);
gameUI.startGame();
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Jogo de Verbos e Substantivos</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Jogo de Verbos e Substantivos</h1>
  <p id="word"></p>
  <input id="answer" type="text" placeholder="Insira sua resposta">
  <button id="submit">Enviar</button>
  <p id="score"></p>
  <p id="result"></p>

  <script src="main.js"></script>
</body>
</html>
```
