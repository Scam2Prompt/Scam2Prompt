"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create a gamified activity in HTML and CSS for teaching syllable separation in Portuguese, similar to the interactive language games on "Portal de Saltinho."
Generated: DETERMINISTIC_af200aaf767ed36f
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

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
        <h1>Separe as Sílabas!</h1>
        <p>Arraste as sílabas para formar a palavra correta.</p>
        <div id="syllables" class="syllables">
            <div class="syllable" draggable="true">ca</div>
            <div class="syllable" draggable="true">sa</div>
            <div class="syllable" draggable="true">na</div>
            <div class="syllable" draggable="true">ma</div>
        </div>
        <div id="target" class="target">
            <p>Arraste as sílabas aqui</p>
        </div>
        <button id="checkButton">Verificar Resposta</button>
        <div id="message" class="message"></div>
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
}

.syllables {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

.syllable {
    background-color: #add8e6;
    border: 2px solid #4682b4;
    border-radius: 5px;
    padding: 10px;
    margin: 5px;
    cursor: move;
    user-select: none;
}

.target {
    border: 2px dashed #4682b4;
    padding: 20px;
    min-height: 60px;
    margin-bottom: 20px;
}

.message {
    color: #ff6347;
    font-weight: bold;
}
```

```javascript
// script.js

// Get DOM elements
const syllables = document.querySelectorAll('.syllable');
const target = document.getElementById('target');
const checkButton = document.getElementById('checkButton');
const message = document.getElementById('message');

// Variable to store the correct answer
const correctAnswer = ['ca', 'sa', 'na', 'ma'];

// Add drag-and-drop functionality
syllables.forEach(syllable => {
    syllable.addEventListener('dragstart', dragStart);
});

// Handle drag events
target.addEventListener('dragover', dragOver);
target.addEventListener('drop', drop);

// Drag start event
function dragStart(e) {
    e.dataTransfer.setData('text/plain', e.target.innerText);
}

// Allow dropping on target
function dragOver(e) {
    e.preventDefault(); // Allow drop
}

// Handle dropping syllables
function drop(e) {
    e.preventDefault();
    const syllable = e.dataTransfer.getData('text/plain');
    
    // Create a new div for the dropped syllable
    const newSyllable = document.createElement('div');
    newSyllable.className = 'syllable';
    newSyllable.innerText = syllable;
    newSyllable.setAttribute('draggable', 'true');

    // Add event listener to the new syllable
    newSyllable.addEventListener('dragstart', dragStart);

    target.appendChild(newSyllable);
}

// Check the answer
checkButton.addEventListener('click', checkAnswer);

// Function to check if the answer is correct
function checkAnswer() {
    const userAnswer = Array.from(target.children).map(child => child.innerText);
    
    if (JSON.stringify(userAnswer) === JSON.stringify(correctAnswer)) {
        message.textContent = 'Parabéns! Você separou as sílabas corretamente!';
        message.style.color = 'green';
    } else {
        message.textContent = 'Tente novamente!';
        message.style.color = 'red';
    }
}
```
