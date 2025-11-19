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
/**
 * Portuguese Language Learning Game
 * Helps students identify verbs and nouns in Portuguese.
 * Inspired by the language games on "Portal de Saltinho".
 */

class PortugueseGame {
  constructor() {
    this.words = [
      { word: "correr", type: "verb", translation: "to run" },
      { word: "casa", type: "noun", translation: "house" },
      { word: "comer", type: "verb", translation: "to eat" },
      { word: "livro", type: "noun", translation: "book" },
      { word: "pular", type: "verb", translation: "to jump" },
      { word: "cachorro", type: "noun", translation: "dog" },
      { word: "escrever", type: "verb", translation: "to write" },
      { word: "mesa", type: "noun", translation: "table" },
      { word: "ler", type: "verb", translation: "to read" },
      { word: "água", type: "noun", translation: "water" }
    ];
    this.currentWord = null;
    this.score = 0;
    this.totalQuestions = 0;
    this.gameActive = false;
  }

  /**
   * Starts a new game session
   */
  startGame() {
    this.score = 0;
    this.totalQuestions = 0;
    this.gameActive = true;
    this.nextWord();
  }

  /**
   * Ends the current game session
   */
  endGame() {
    this.gameActive = false;
    return {
      score: this.score,
      totalQuestions: this.totalQuestions,
      accuracy: this.totalQuestions > 0 ? Math.round((this.score / this.totalQuestions) * 100) : 0
    };
  }

  /**
   * Selects a random word from the word list
   */
  nextWord() {
    if (!this.gameActive) return null;

    const randomIndex = Math.floor(Math.random() * this.words.length);
    this.currentWord = this.words[randomIndex];
    return {
      word: this.currentWord.word,
      translation: this.currentWord.translation
    };
  }

  /**
   * Checks if the user's answer is correct
   * @param {string} userAnswer - The user's answer ('verb' or 'noun')
   * @returns {object} Result of the answer check
   */
  checkAnswer(userAnswer) {
    if (!this.gameActive || !this.currentWord) {
      throw new Error("Game is not active or no word is selected");
    }

    this.totalQuestions++;
    const isCorrect = userAnswer.toLowerCase() === this.currentWord.type;
    if (isCorrect) this.score++;

    return {
      correct: isCorrect,
      correctAnswer: this.currentWord.type,
      score: this.score,
      totalQuestions: this.totalQuestions
    };
  }

  /**
   * Gets the current game status
   * @returns {object} Current game state
   */
  getGameStatus() {
    return {
      score: this.score,
      totalQuestions: this.totalQuestions,
      currentWord: this.currentWord ? this.currentWord.word : null,
      gameActive: this.gameActive
    };
  }
}

// UI Implementation
document.addEventListener('DOMContentLoaded', () => {
  const game = new PortugueseGame();
  const wordDisplay = document.getElementById('word-display');
  const translationDisplay = document.getElementById('translation-display');
  const verbBtn = document.getElementById('verb-btn');
  const nounBtn = document.getElementById('noun-btn');
  const startBtn = document.getElementById('start-btn');
  const scoreDisplay = document.getElementById('score');
  const accuracyDisplay = document.getElementById('accuracy');
  const feedbackDisplay = document.getElementById('feedback');

  /**
   * Updates the UI with the current word
   */
  function displayCurrentWord() {
    const current = game.nextWord();
    if (current) {
      wordDisplay.textContent = current.word;
      translationDisplay.textContent = current.translation;
      feedbackDisplay.textContent = '';
    }
  }

  /**
   * Updates the score display
   */
  function updateScoreDisplay() {
    const status = game.getGameStatus();
    scoreDisplay.textContent = `Score: ${status.score}/${status.totalQuestions}`;
    
    if (status.totalQuestions > 0) {
      const accuracy = Math.round((status.score / status.totalQuestions) * 100);
      accuracyDisplay.textContent = `Accuracy: ${accuracy}%`;
    } else {
      accuracyDisplay.textContent = 'Accuracy: 0%';
    }
  }

  /**
   * Handles answer submission
   * @param {string} answerType - The type of answer ('verb' or 'noun')
   */
  function handleAnswer(answerType) {
    try {
      const result = game.checkAnswer(answerType);
      feedbackDisplay.textContent = result.correct 
        ? 'Correct!' 
        : `Incorrect! It's a ${result.correctAnswer}.`;
      
      updateScoreDisplay();
      setTimeout(displayCurrentWord, 1500);
    } catch (error) {
      console.error("Error checking answer:", error);
      feedbackDisplay.textContent = "Please start the game first!";
    }
  }

  // Event listeners
  startBtn.addEventListener('click', () => {
    game.startGame();
    displayCurrentWord();
    updateScoreDisplay();
    startBtn.disabled = true;
    verbBtn.disabled = false;
    nounBtn.disabled = false;
  });

  verbBtn.addEventListener('click', () => handleAnswer('verb'));
  nounBtn.addEventListener('click', () => handleAnswer('noun'));
});

// HTML would need to include elements with these IDs:
// word-display, translation-display, verb-btn, noun-btn, start-btn
// score, accuracy, feedback
```
