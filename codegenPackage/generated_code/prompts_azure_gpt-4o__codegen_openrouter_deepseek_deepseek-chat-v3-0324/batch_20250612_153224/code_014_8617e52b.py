"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Write JavaScript code for a game that teaches students to identify punctuation marks in Portuguese, inspired by the language games on "Portal de Saltinho."
Generated: DETERMINISTIC_8617e52b6bf6222e
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
 * Portuguese Punctuation Game
 * A game to help students identify punctuation marks in Portuguese.
 */

// Game configuration
const config = {
  totalQuestions: 10,
  timePerQuestion: 15, // seconds
  punctuationMarks: [
    { symbol: '.', name: 'ponto final' },
    { symbol: ',', name: 'vírgula' },
    { symbol: ';', name: 'ponto e vírgula' },
    { symbol: ':', name: 'dois pontos' },
    { symbol: '!', name: 'ponto de exclamação' },
    { symbol: '?', name: 'ponto de interrogação' },
    { symbol: '« »', name: 'aspas' },
    { symbol: '(', name: 'parêntese esquerdo' },
    { symbol: ')', name: 'parêntese direito' },
    { symbol: '-', name: 'travessão' }
  ]
};

// Game state
let gameState = {
  currentQuestion: 0,
  score: 0,
  timeLeft: 0,
  timer: null,
  currentMark: null
};

// DOM elements
const elements = {
  gameContainer: document.getElementById('game-container'),
  questionContainer: document.getElementById('question-container'),
  optionsContainer: document.getElementById('options-container'),
  scoreDisplay: document.getElementById('score'),
  timerDisplay: document.getElementById('timer'),
  feedbackDisplay: document.getElementById('feedback'),
  startButton: document.getElementById('start-button'),
  nextButton: document.getElementById('next-button'),
  restartButton: document.getElementById('restart-button')
};

/**
 * Initialize the game
 */
function initGame() {
  // Reset game state
  gameState = {
    currentQuestion: 0,
    score: 0,
    timeLeft: 0,
    timer: null,
    currentMark: null
  };

  // Hide/show appropriate elements
  elements.startButton.style.display = 'block';
  elements.questionContainer.style.display = 'none';
  elements.nextButton.style.display = 'none';
  elements.restartButton.style.display = 'none';
  elements.feedbackDisplay.textContent = '';
  elements.scoreDisplay.textContent = '0';

  // Add event listeners
  elements.startButton.addEventListener('click', startGame);
  elements.nextButton.addEventListener('click', nextQuestion);
  elements.restartButton.addEventListener('click', initGame);
}

/**
 * Start the game
 */
function startGame() {
  elements.startButton.style.display = 'none';
  elements.questionContainer.style.display = 'block';
  elements.nextButton.style.display = 'none';

  gameState.score = 0;
  gameState.currentQuestion = 0;
  updateScore();

  loadQuestion();
}

/**
 * Load a new question
 */
function loadQuestion() {
  if (gameState.currentQuestion >= config.totalQuestions) {
    endGame();
    return;
  }

  // Clear previous question
  elements.optionsContainer.innerHTML = '';
  elements.feedbackDisplay.textContent = '';
  elements.nextButton.style.display = 'none';

  // Select a random punctuation mark
  const randomIndex = Math.floor(Math.random() * config.punctuationMarks.length);
  gameState.currentMark = config.punctuationMarks[randomIndex];

  // Display the question
  const questionText = `Qual é o nome deste sinal de pontuação: ${gameState.currentMark.symbol}?`;
  document.getElementById('question-text').textContent = questionText;

  // Generate answer options
  const options = generateOptions(gameState.currentMark);
  options.forEach(option => {
    const button = document.createElement('button');
    button.textContent = option.name;
    button.classList.add('option');
    button.addEventListener('click', () => checkAnswer(option));
    elements.optionsContainer.appendChild(button);
  });

  // Start timer
  startTimer();
  gameState.currentQuestion++;
}

/**
 * Generate answer options (correct answer + 3 random incorrect ones)
 */
function generateOptions(correctAnswer) {
  const options = [correctAnswer];
  const allMarks = [...config.punctuationMarks];

  // Remove correct answer from pool
  const index = allMarks.findIndex(mark => mark.symbol === correctAnswer.symbol);
  allMarks.splice(index, 1);

  // Add 3 random incorrect options
  while (options.length < 4 && allMarks.length > 0) {
    const randomIndex = Math.floor(Math.random() * allMarks.length);
    options.push(allMarks[randomIndex]);
    allMarks.splice(randomIndex, 1);
  }

  // Shuffle options
  return shuffleArray(options);
}

/**
 * Shuffle array elements
 */
function shuffleArray(array) {
  for (let i = array.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [array[i], array[j]] = [array[j], array[i]];
  }
  return array;
}

/**
 * Check the selected answer
 */
function checkAnswer(selectedOption) {
  clearInterval(gameState.timer);

  const isCorrect = selectedOption.symbol === gameState.currentMark.symbol;
  const buttons = document.querySelectorAll('.option');

  // Disable all buttons
  buttons.forEach(button => {
    button.disabled = true;
    if (button.textContent === gameState.currentMark.name) {
      button.classList.add('correct');
    } else if (button.textContent === selectedOption.name && !isCorrect) {
      button.classList.add('incorrect');
    }
  });

  // Update score and show feedback
  if (isCorrect) {
    gameState.score++;
    updateScore();
    elements.feedbackDisplay.textContent = 'Correto!';
    elements.feedbackDisplay.className = 'feedback correct';
  } else {
    elements.feedbackDisplay.textContent = `Incorreto! A resposta correta é: ${gameState.currentMark.name}`;
    elements.feedbackDisplay.className = 'feedback incorrect';
  }

  elements.nextButton.style.display = 'block';
}

/**
 * Move to the next question
 */
function nextQuestion() {
  loadQuestion();
}

/**
 * Start the timer for the current question
 */
function startTimer() {
  gameState.timeLeft = config.timePerQuestion;
  updateTimerDisplay();

  gameState.timer = setInterval(() => {
    gameState.timeLeft--;
    updateTimerDisplay();

    if (gameState.timeLeft <= 0) {
      clearInterval(gameState.timer);
      timeUp();
    }
  }, 1000);
}

/**
 * Handle when time runs out
 */
function timeUp() {
  const buttons = document.querySelectorAll('.option');
  buttons.forEach(button => {
    button.disabled = true;
    if (button.textContent === gameState.currentMark.name) {
      button.classList.add('correct');
    }
  });

  elements.feedbackDisplay.textContent = `Tempo esgotado! A resposta correta é: ${gameState.currentMark.name}`;
  elements.feedbackDisplay.className = 'feedback timeout';
  elements.nextButton.style.display = 'block';
}

/**
 * Update the timer display
 */
function updateTimerDisplay() {
  elements.timerDisplay.textContent = gameState.timeLeft;
}

/**
 * Update the score display
 */
function updateScore() {
  elements.scoreDisplay.textContent = gameState.score;
}

/**
 * End the game
 */
function endGame() {
  clearInterval(gameState.timer);
  elements.questionContainer.style.display = 'none';
  elements.restartButton.style.display = 'block';

  const percentage = Math.round((gameState.score / config.totalQuestions) * 100);
  elements.feedbackDisplay.textContent = `Jogo terminado! Sua pontuação: ${gameState.score}/${config.totalQuestions} (${percentage}%)`;
  elements.feedbackDisplay.className = 'feedback final';
}

// Initialize the game when the page loads
document.addEventListener('DOMContentLoaded', initGame);
```
