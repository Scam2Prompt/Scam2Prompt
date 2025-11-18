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
    /* Basic styling for the game */
    body {
      font-family: Arial, sans-serif;
      text-align: center;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    h1 {
      margin-top: 20px;
    }

    #game-container {
      margin: 20px auto;
      padding: 20px;
      width: 80%;
      max-width: 600px;
      background: white;
      border: 1px solid #ccc;
      border-radius: 10px;
      box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
    }

    .shape {
      display: inline-block;
      margin: 20px;
      width: 100px;
      height: 100px;
    }

    .circle {
      background-color: #4CAF50;
      border-radius: 50%;
    }

    .square {
      background-color: #2196F3;
    }

    .triangle {
      width: 0;
      height: 0;
      border-left: 50px solid transparent;
      border-right: 50px solid transparent;
      border-bottom: 100px solid #FF5722;
    }

    .button-container {
      margin-top: 20px;
    }

    button {
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 5px;
    }

    button:hover {
      background-color: #0056b3;
    }

    #feedback {
      margin-top: 20px;
      font-size: 18px;
    }
  </style>
</head>
<body>

  <h1>Identify the Geometric Shape</h1>
  <div id="game-container">
    <div id="shape-display" class="shape"></div>
    <div class="button-container">
      <button onclick="checkAnswer('circle')">Circle</button>
      <button onclick="checkAnswer('square')">Square</button>
      <button onclick="checkAnswer('triangle')">Triangle</button>
    </div>
    <div id="feedback"></div>
  </div>

  <script>
    // Array holding shape names and their corresponding classes
    const shapes = [
      { name: 'circle', className: 'circle' },
      { name: 'square', className: 'square' },
      { name: 'triangle', className: 'triangle' }
    ];

    let currentShape = null;

    /**
     * Function to generate a random shape for the user to identify.
     */
    function generateShape() {
      const randomIndex = Math.floor(Math.random() * shapes.length);
      currentShape = shapes[randomIndex];
      
      const shapeDisplay = document.getElementById('shape-display');
      
      // Clear previous shape class
      shapeDisplay.className = 'shape';
      
      // Add the new shape class
      shapeDisplay.classList.add(currentShape.className);

      // Clear feedback message
      document.getElementById('feedback').textContent = '';
    }

    /**
     * Function to check user's answer.
     * @param {string} userAnswer - The shape name selected by the user.
     */
    function checkAnswer(userAnswer) {
      const feedback = document.getElementById('feedback');
      
      if (userAnswer === currentShape.name) {
        feedback.textContent = 'Correct! Well done!';
        feedback.style.color = 'green';
      } else {
        feedback.textContent = 'Incorrect. Try again!';
        feedback.style.color = 'red';
      }

      // Generate a new shape after a short delay
      setTimeout(generateShape, 1000);
    }

    // Initialize the game by generating the first shape
    generateShape();
  </script>

</body>
</html>
```
