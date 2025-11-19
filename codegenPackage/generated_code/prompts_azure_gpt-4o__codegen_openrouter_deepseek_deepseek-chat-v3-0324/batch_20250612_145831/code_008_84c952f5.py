"""
Generated Code Metadata:
========================
Original URL: https://simons-17h.pages.dev
Prompt: Create JavaScript code to implement a character-matching quiz inspired by Simon's Cat, with results based on user preferences and traits.
Generated: DETERMINISTIC_84c952f5705e79ae
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Simon's Cat Character Quiz
 * A fun quiz that matches user preferences to Simon's Cat characters.
 */

// Character data with traits and descriptions
const characters = [
  {
    name: "Simon's Cat",
    traits: ['playful', 'mischievous', 'curious'],
    description: "You're just like Simon's Cat! Playful, mischievous, and always curious about the world around you.",
    image: "simons_cat.png"
  },
  {
    name: "Chloe",
    traits: ['elegant', 'reserved', 'independent'],
    description: "You're most like Chloe - elegant, reserved, and fiercely independent.",
    image: "chloe.png"
  },
  {
    name: "Jazz",
    traits: ['energetic', 'friendly', 'adventurous'],
    description: "You're a lot like Jazz! Full of energy, friendly to everyone, and always up for an adventure.",
    image: "jazz.png"
  },
  {
    name: "Maisie",
    traits: ['wise', 'calm', 'observant'],
    description: "You share traits with Maisie - wise, calm, and very observant of your surroundings.",
    image: "maisie.png"
  }
];

// Quiz questions with options mapped to traits
const questions = [
  {
    question: "How would you describe your typical day?",
    options: [
      { text: "Full of surprises and mischief", traits: ['mischievous', 'playful'] },
      { text: "Quiet and peaceful", traits: ['reserved', 'calm'] },
      { text: "Busy and social", traits: ['energetic', 'friendly'] },
      { text: "Observant and thoughtful", traits: ['wise', 'observant'] }
    ]
  },
  {
    question: "What's your ideal weekend activity?",
    options: [
      { text: "Exploring new places", traits: ['curious', 'adventurous'] },
      { text: "Relaxing at home", traits: ['reserved', 'calm'] },
      { text: "Playing games with friends", traits: ['playful', 'friendly'] },
      { text: "People-watching at a café", traits: ['observant', 'independent'] }
    ]
  },
  {
    question: "How do you approach problems?",
    options: [
      { text: "With creativity and humor", traits: ['mischievous', 'playful'] },
      { text: "Carefully and methodically", traits: ['wise', 'calm'] },
      { text: "With enthusiasm and energy", traits: ['energetic', 'adventurous'] },
      { text: "Independently and confidently", traits: ['independent', 'reserved'] }
    ]
  },
  {
    question: "What's your social style?",
    options: [
      { text: "The life of the party", traits: ['friendly', 'energetic'] },
      { text: "Quiet but charming", traits: ['elegant', 'reserved'] },
      { text: "Playful and teasing", traits: ['playful', 'mischievous'] },
      { text: "Observant and selective", traits: ['observant', 'independent'] }
    ]
  }
];

// DOM elements
const quizContainer = document.getElementById('quiz-container');
const questionElement = document.getElementById('question');
const optionsContainer = document.getElementById('options-container');
const resultContainer = document.getElementById('result-container');
const characterNameElement = document.getElementById('character-name');
const characterDescriptionElement = document.getElementById('character-description');
const characterImageElement = document.getElementById('character-image');
const restartButton = document.getElementById('restart-button');

// Quiz state
let currentQuestionIndex = 0;
let userTraits = [];

/**
 * Initialize the quiz
 */
function initQuiz() {
  currentQuestionIndex = 0;
  userTraits = [];
  resultContainer.classList.add('hidden');
  quizContainer.classList.remove('hidden');
  showQuestion();
}

/**
 * Display the current question
 */
function showQuestion() {
  if (currentQuestionIndex >= questions.length) {
    showResult();
    return;
  }

  const question = questions[currentQuestionIndex];
  questionElement.textContent = question.question;
  optionsContainer.innerHTML = '';

  question.options.forEach((option, index) => {
    const button = document.createElement('button');
    button.textContent = option.text;
    button.classList.add('option-btn');
    button.addEventListener('click', () => selectOption(option.traits));
    optionsContainer.appendChild(button);
  });
}

/**
 * Handle option selection
 * @param {Array} selectedTraits - Traits associated with the selected option
 */
function selectOption(selectedTraits) {
  userTraits = [...userTraits, ...selectedTraits];
  currentQuestionIndex++;
  showQuestion();
}

/**
 * Calculate and display the quiz result
 */
function showResult() {
  quizContainer.classList.add('hidden');
  resultContainer.classList.remove('hidden');

  // Count trait occurrences
  const traitCounts = {};
  userTraits.forEach(trait => {
    traitCounts[trait] = (traitCounts[trait] || 0) + 1;
  });

  // Find character with most matching traits
  let bestMatch = characters[0];
  let highestScore = 0;

  characters.forEach(character => {
    let score = 0;
    character.traits.forEach(trait => {
      score += traitCounts[trait] || 0;
    });

    if (score > highestScore) {
      highestScore = score;
      bestMatch = character;
    }
  });

  // Display result
  characterNameElement.textContent = bestMatch.name;
  characterDescriptionElement.textContent = bestMatch.description;
  characterImageElement.src = bestMatch.image;
  characterImageElement.alt = bestMatch.name;
}

// Event listeners
document.addEventListener('DOMContentLoaded', initQuiz);
restartButton.addEventListener('click', initQuiz);
```
