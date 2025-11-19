"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Generate JavaScript code for a game that helps students practice ordinal numbers, inspired by the educational games on "Portal de Saltinho."
Generated: DETERMINISTIC_c8aaa0ee6cacc8bd
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
 * Ordinal Numbers Game
 * A simple educational game to help students practice ordinal numbers.
 */

// Game configuration
const config = {
    totalQuestions: 10,
    maxNumber: 20,
    ordinalSuffixes: {
        1: 'st',
        2: 'nd',
        3: 'rd',
        default: 'th'
    }
};

// Game state
const gameState = {
    currentQuestion: 0,
    score: 0,
    questions: []
};

// DOM elements
const elements = {
    gameContainer: document.getElementById('game-container'),
    questionContainer: document.getElementById('question-container'),
    optionsContainer: document.getElementById('options-container'),
    scoreContainer: document.getElementById('score-container'),
    feedbackContainer: document.getElementById('feedback-container'),
    nextButton: document.getElementById('next-button'),
    restartButton: document.getElementById('restart-button')
};

/**
 * Initialize the game
 */
function initGame() {
    generateQuestions();
    renderQuestion();
    updateScoreDisplay();
    setupEventListeners();
}

/**
 * Generate random questions for the game
 */
function generateQuestions() {
    gameState.questions = [];
    
    for (let i = 0; i < config.totalQuestions; i++) {
        const number = Math.floor(Math.random() * config.maxNumber) + 1;
        const position = Math.floor(Math.random() * config.maxNumber) + 1;
        
        gameState.questions.push({
            number,
            position,
            correctAnswer: getOrdinalNumber(position)
        });
    }
}

/**
 * Get the ordinal representation of a number
 * @param {number} num - The number to convert
 * @returns {string} The ordinal number string
 */
function getOrdinalNumber(num) {
    const lastDigit = num % 10;
    const lastTwoDigits = num % 100;
    
    // Special cases for 11, 12, 13
    if (lastTwoDigits >= 11 && lastTwoDigits <= 13) {
        return num + config.ordinalSuffixes.default;
    }
    
    // Regular cases
    const suffix = config.ordinalSuffixes[lastDigit] || config.ordinalSuffixes.default;
    return num + suffix;
}

/**
 * Render the current question
 */
function renderQuestion() {
    if (gameState.currentQuestion >= config.totalQuestions) {
        endGame();
        return;
    }

    const question = gameState.questions[gameState.currentQuestion];
    elements.questionContainer.textContent = 
        `What is the ordinal form of the number ${question.position}?`;
    
    renderOptions(question);
}

/**
 * Render answer options
 * @param {object} question - The current question
 */
function renderOptions(question) {
    elements.optionsContainer.innerHTML = '';
    
    // Generate correct answer and 3 random incorrect answers
    const options = [question.correctAnswer];
    while (options.length < 4) {
        const randomNum = Math.floor(Math.random() * config.maxNumber) + 1;
        const randomOrdinal = getOrdinalNumber(randomNum);
        
        if (!options.includes(randomOrdinal) && randomOrdinal !== question.correctAnswer) {
            options.push(randomOrdinal);
        }
    }
    
    // Shuffle options
    options.sort(() => Math.random() - 0.5);
    
    // Create option buttons
    options.forEach(option => {
        const button = document.createElement('button');
        button.className = 'option';
        button.textContent = option;
        button.addEventListener('click', () => checkAnswer(option, question.correctAnswer));
        elements.optionsContainer.appendChild(button);
    });
}

/**
 * Check the selected answer
 * @param {string} selectedAnswer - The answer selected by the player
 * @param {string} correctAnswer - The correct answer
 */
function checkAnswer(selectedAnswer, correctAnswer) {
    // Disable all options
    const optionButtons = document.querySelectorAll('.option');
    optionButtons.forEach(button => {
        button.disabled = true;
        button.removeEventListener('click', () => {});
    });
    
    // Show feedback
    if (selectedAnswer === correctAnswer) {
        elements.feedbackContainer.textContent = 'Correct! Well done!';
        elements.feedbackContainer.className = 'feedback correct';
        gameState.score++;
    } else {
        elements.feedbackContainer.textContent = `Incorrect. The correct answer is ${correctAnswer}.`;
        elements.feedbackContainer.className = 'feedback incorrect';
    }
    
    updateScoreDisplay();
    elements.nextButton.style.display = 'block';
}

/**
 * Move to the next question
 */
function nextQuestion() {
    gameState.currentQuestion++;
    elements.feedbackContainer.textContent = '';
    elements.feedbackContainer.className = 'feedback';
    elements.nextButton.style.display = 'none';
    renderQuestion();
}

/**
 * Update the score display
 */
function updateScoreDisplay() {
    elements.scoreContainer.textContent = 
        `Score: ${gameState.score}/${gameState.currentQuestion}`;
}

/**
 * End the game and show final results
 */
function endGame() {
    elements.questionContainer.textContent = 'Game Over!';
    elements.optionsContainer.innerHTML = '';
    elements.feedbackContainer.textContent = 
        `Your final score: ${gameState.score}/${config.totalQuestions}`;
    elements.feedbackContainer.className = 'feedback final';
    elements.nextButton.style.display = 'none';
    elements.restartButton.style.display = 'block';
}

/**
 * Restart the game
 */
function restartGame() {
    gameState.currentQuestion = 0;
    gameState.score = 0;
    elements.restartButton.style.display = 'none';
    elements.feedbackContainer.className = 'feedback';
    initGame();
}

/**
 * Set up event listeners
 */
function setupEventListeners() {
    elements.nextButton.addEventListener('click', nextQuestion);
    elements.restartButton.addEventListener('click', restartGame);
}

// Initialize the game when the DOM is loaded
document.addEventListener('DOMContentLoaded', initGame);
```
