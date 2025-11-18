"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: Create HTML and JavaScript code for a game that teaches students to identify geometric shapes, inspired by the interactive math games on "Portal de Saltinho."
Generated: DETERMINISTIC_e63b15436e4123b7
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Geometric Shapes Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
        }
        #game-container {
            margin: 20px auto;
            padding: 20px;
            border: 2px solid #333;
            background: #fff;
            border-radius: 8px;
            width: 300px;
        }
        .shape {
            width: 100px;
            height: 100px;
            margin: 20px auto;
            cursor: pointer;
            border: 2px solid #333;
        }
        #score {
            font-size: 20px;
            margin-top: 20px;
        }
    </style>
</head>
<body>

<div id="game-container">
    <h1>Identify the Shape!</h1>
    <div id="shape" class="shape"></div>
    <div id="options"></div>
    <div id="score">Score: 0</div>
</div>

<script>
    // Shape data with corresponding color and names
    const shapes = [
        { name: 'Circle', color: 'red', type: 'circle' },
        { name: 'Square', color: 'blue', type: 'square' },
        { name: 'Triangle', color: 'green', type: 'triangle' },
        { name: 'Rectangle', color: 'orange', type: 'rectangle' },
    ];

    let score = 0; // Initialize score

    // Generates a random shape
    function getRandomShape() {
        return shapes[Math.floor(Math.random() * shapes.length)];
    }

    // Draws the shape on the screen
    function drawShape(shape) {
        const shapeDiv = document.getElementById('shape');
        shapeDiv.style.backgroundColor = shape.color;
        shapeDiv.style.borderRadius = shape.type === 'circle' ? '50%' : '0';
        shapeDiv.style.transform = shape.type === 'triangle' 
            ? 'rotate(180deg) translateY(-50%)' : 'none';
        shapeDiv.dataset.shape = shape.name; // Store shape name in data attribute
    }

    // Creates options for user to select
    function createOptions() {
        const optionsDiv = document.getElementById('options');
        optionsDiv.innerHTML = ''; // Clear previous options
        shapes.forEach(shape => {
            const button = document.createElement('button');
            button.textContent = shape.name;
            button.onclick = () => checkAnswer(shape.name);
            optionsDiv.appendChild(button);
        });
    }

    // Check user's answer
    function checkAnswer(userShape) {
        const correctShape = document.getElementById('shape').dataset.shape;
        if (userShape === correctShape) {
            alert('Correct!'); // Notify user of correct answer
            score++; // Increment score
        } else {
            alert(`Wrong! The correct shape was ${correctShape}.`); // Notify of wrong answer
            if (score > 0) score--; // Decrement score if not already at 0
        }
        updateScore(); // Update displayed score
        startGame(); // Restart the game with a new shape
    }

    // Update score display
    function updateScore() {
        document.getElementById('score').textContent = `Score: ${score}`;
    }

    // Start or restart the game
    function startGame() {
        const randomShape = getRandomShape(); // Get a random shape
        drawShape(randomShape); // Draw the shape
        createOptions(); // Create answer options
    }

    // Initialize the game on page load
    window.onload = startGame;

</script>

</body>
</html>
```
