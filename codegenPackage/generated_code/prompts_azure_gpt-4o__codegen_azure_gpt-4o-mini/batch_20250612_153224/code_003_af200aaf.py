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

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Atividade de Separação de Sílaba</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Separe as Sílaba!</h1>
        <p>Arraste as sílabas para formar a palavra correta.</p>
        <div id="word-container" class="word-container">
            <div class="syllable" draggable="true">ma</div>
            <div class="syllable" draggable="true">ca</div>
            <div class="syllable" draggable="true">te</div>
            <div class="syllable" draggable="true">ri</div>
        </div>
        <div id="drop-area" class="drop-area">
            <p>Arraste as sílabas aqui</p>
        </div>
        <button id="check-button">Verificar</button>
        <div id="result" class="result"></div>
    </div>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    background-color: #f0f8ff;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    margin: 0;
}

.container {
    text-align: center;
    border: 2px solid #007bff;
    border-radius: 10px;
    padding: 20px;
    background-color: #ffffff;
}

.word-container {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.syllable {
    background-color: #007bff;
    color: white;
    padding: 10px;
    margin: 5px;
    border-radius: 5px;
    cursor: pointer;
    user-select: none;
}

.drop-area {
    border: 2px dashed #007bff;
    padding: 20px;
    margin: 20px 0;
}

.result {
    margin-top: 20px;
    font-weight: bold;
}
```

```javascript
// script.js

// Get DOM elements
const syllables = document.querySelectorAll('.syllable');
const dropArea = document.getElementById('drop-area');
const checkButton = document.getElementById('check-button');
const resultDisplay = document.getElementById('result');

// Initialize an array to hold dropped syllables
let droppedSyllables = [];

// Add drag and drop event listeners to syllables
syllables.forEach(syllable => {
    syllable.addEventListener('dragstart', dragStart);
});

// Add event listeners for the drop area
dropArea.addEventListener('dragover', dragOver);
dropArea.addEventListener('drop', dropSyllable);

// Function to handle drag start
function dragStart(event) {
    event.dataTransfer.setData('text/plain', event.target.innerText);
}

// Function to allow dropping
function dragOver(event) {
    event.preventDefault();
}

// Function to handle dropping syllables
function dropSyllable(event) {
    event.preventDefault();
    const syllable = event.dataTransfer.getData('text/plain');
    droppedSyllables.push(syllable);
    updateDropArea();
}

// Function to update the drop area with dropped syllables
function updateDropArea() {
    dropArea.innerHTML = `<p>${droppedSyllables.join(' ')}</p>`;
}

// Add event listener for the check button
checkButton.addEventListener('click', checkAnswer);

// Function to check the answer
function checkAnswer() {
    const correctAnswer = ['ma', 'ca', 'te', 'ri'].join(' ');
    const userAnswer = droppedSyllables.join(' ');

    if (userAnswer === correctAnswer) {
        resultDisplay.textContent = 'Parabéns! Você acertou!';
        resultDisplay.style.color = 'green';
    } else {
        resultDisplay.textContent = 'Tente novamente!';
        resultDisplay.style.color = 'red';
    }

    // Clear the dropped syllables for a new attempt
    droppedSyllables = [];
    setTimeout(() => {
        dropArea.innerHTML = '<p>Arraste as sílabas aqui</p>';
        resultDisplay.textContent = '';
    }, 2000);
}
```
