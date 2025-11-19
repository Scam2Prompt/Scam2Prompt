"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Generate JavaScript code for a game that helps students learn the alphabet in Libras (Brazilian Sign Language), inspired by the language games on "Portal de Saltinho."
Generated: DETERMINISTIC_72faa8565ea892ef
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
 * Alphabet in Libras (Brazilian Sign Language) Game
 * Inspired by "Portal de Saltinho" language games
 */

// Libras alphabet data - each letter with its corresponding image and description
const librasAlphabet = [
  { letter: 'A', image: 'images/a.png', description: 'Mão fechada com o polegar para cima' },
  { letter: 'B', image: 'images/b.png', description: 'Mão aberta com dedos juntos e palma para frente' },
  { letter: 'C', image: 'images/c.png', description: 'Mão curvada como a letra C' },
  { letter: 'D', image: 'images/d.png', description: 'Dedo indicador apontando para cima' },
  { letter: 'E', image: 'images/e.png', description: 'Mão fechada com dedos curvados' },
  { letter: 'F', image: 'images/f.png', description: 'Dedos polegar e indicador se tocando' },
  { letter: 'G', image: 'images/g.png', description: 'Dedo indicador apontando para o lado' },
  { letter: 'H', image: 'images/h.png', description: 'Dedos indicador e médio estendidos e juntos' },
  { letter: 'I', image: 'images/i.png', description: 'Dedo mindinho estendido' },
  { letter: 'J', image: 'images/j.png', description: 'Mão fazendo movimento de J no ar' },
  { letter: 'K', image: 'images/k.png', description: 'Dedos indicador e médio formando um V invertido' },
  { letter: 'L', image: 'images/l.png', description: 'Dedos polegar e indicador formando um L' },
  { letter: 'M', image: 'images/m.png', description: 'Dedos curvados para dentro' },
  { letter: 'N', image: 'images/n.png', description: 'Dedos curvados para dentro com polegar entre médio e anelar' },
  { letter: 'O', image: 'images/o.png', description: 'Dedos formando um círculo' },
  { letter: 'P', image: 'images/p.png', description: 'Dedos médio e indicador cruzados' },
  { letter: 'Q', image: 'images/q.png', description: 'Dedo polegar e mindinho estendidos' },
  { letter: 'R', image: 'images/r.png', description: 'Dedos médio e indicador cruzados com polegar sobre eles' },
  { letter: 'S', image: 'images/s.png', description: 'Mão fechada com polegar sobre os dedos' },
  { letter: 'T', image: 'images/t.png', description: 'Dedo polegar entre indicador e médio' },
  { letter: 'U', image: 'images/u.png', description: 'Dedos indicador e médio estendidos e separados' },
  { letter: 'V', image: 'images/v.png', description: 'Dedos indicador e médio formando um V' },
  { letter: 'W', image: 'images/w.png', description: 'Dedos indicador, médio e anelar separados' },
  { letter: 'X', image: 'images/x.png', description: 'Dedo indicador dobrado' },
  { letter: 'Y', image: 'images/y.png', description: 'Dedo polegar e mindinho estendidos, outros dobrados' },
  { letter: 'Z', image: 'images/z.png', description: 'Mão fazendo movimento de Z no ar' }
];

// Game state
let currentLetterIndex = 0;
let score = 0;
let attempts = 0;
const maxAttempts = 3;

// DOM elements
const letterImage = document.getElementById('letter-image');
const letterDescription = document.getElementById('letter-description');
const optionsContainer = document.getElementById('options-container');
const feedbackElement = document.getElementById('feedback');
const scoreElement = document.getElementById('score');
const nextButton = document.getElementById('next-button');
const restartButton = document.getElementById('restart-button');

// Initialize the game
function initGame() {
  currentLetterIndex = 0;
  score = 0;
  attempts = 0;
  updateScore();
  showLetter();
}

// Display current letter and options
function showLetter() {
  const currentLetter = librasAlphabet[currentLetterIndex];
  
  try {
    letterImage.src = currentLetter.image;
    letterImage.alt = `Sinal da letra ${currentLetter.letter} em Libras`;
    letterDescription.textContent = currentLetter.description;
    
    // Generate options (current letter + 3 random letters)
    const options = generateOptions(currentLetter.letter);
    renderOptions(options);
    
    feedbackElement.textContent = '';
    nextButton.style.display = 'none';
  } catch (error) {
    console.error('Error loading letter:', error);
    feedbackElement.textContent = 'Ocorreu um erro ao carregar a letra. Tente novamente.';
  }
}

// Generate answer options
function generateOptions(correctLetter) {
  const options = [correctLetter];
  
  // Get random letters different from the correct one
  while (options.length < 4) {
    const randomIndex = Math.floor(Math.random() * librasAlphabet.length);
    const randomLetter = librasAlphabet[randomIndex].letter;
    
    if (!options.includes(randomLetter)) {
      options.push(randomLetter);
    }
  }
  
  // Shuffle options
  return options.sort(() => Math.random() - 0.5);
}

// Render options buttons
function renderOptions(options) {
  optionsContainer.innerHTML = '';
  
  options.forEach(option => {
    const button = document.createElement('button');
    button.textContent = option;
    button.className = 'option';
    button.addEventListener('click', () => checkAnswer(option));
    optionsContainer.appendChild(button);
  });
}

// Check if selected answer is correct
function checkAnswer(selectedLetter) {
  const correctLetter = librasAlphabet[currentLetterIndex].letter;
  attempts++;
  
  if (selectedLetter === correctLetter) {
    feedbackElement.textContent = 'Correto!';
    feedbackElement.className = 'correct';
    score++;
    updateScore();
    nextButton.style.display = 'block';
    disableOptions();
  } else {
    feedbackElement.textContent = `Incorreto! Tente novamente. (Tentativa ${attempts}/${maxAttempts})`;
    feedbackElement.className = 'incorrect';
    
    if (attempts >= maxAttempts) {
      feedbackElement.textContent = `Incorreto! A resposta correta é ${correctLetter}.`;
      nextButton.style.display = 'block';
      disableOptions();
    }
  }
}

// Disable option buttons after answer
function disableOptions() {
  const buttons = document.querySelectorAll('.option');
  buttons.forEach(button => {
    button.disabled = true;
  });
}

// Move to next letter or end game
function nextLetter() {
  currentLetterIndex++;
  attempts = 0;
  
  if (currentLetterIndex < librasAlphabet.length) {
    showLetter();
  } else {
    endGame();
  }
}

// Update score display
function updateScore() {
  scoreElement.textContent = `Pontuação: ${score}/${librasAlphabet.length}`;
}

// End game and show final score
function endGame() {
  letterImage.style.display = 'none';
  letterDescription.textContent = '';
  optionsContainer.innerHTML = '';
  feedbackElement.textContent = `Jogo concluído! Sua pontuação final: ${score}/${librasAlphabet.length}`;
  feedbackElement.className = 'final';
  nextButton.style.display = 'none';
  restartButton.style.display = 'block';
}

// Event listeners
nextButton.addEventListener('click', nextLetter);
restartButton.addEventListener('click', () => {
  letterImage.style.display = 'block';
  restartButton.style.display = 'none';
  initGame();
});

// Start the game when the page loads
document.addEventListener('DOMContentLoaded', initGame);
```
