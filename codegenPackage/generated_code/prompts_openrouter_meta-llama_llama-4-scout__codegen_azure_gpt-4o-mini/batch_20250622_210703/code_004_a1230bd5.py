"""
Generated Code Metadata:
========================
Original URL: https://learnenglishsimply.com
Prompt: Develop a simple game in JavaScript that teaches English vocabulary using the Topic Based Vocab section from Learn English Simply, focusing on Metal and Mineral vocabulary.
Generated: DETERMINISTIC_a1230bd5a5ae8efb
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Metal and Mineral Vocabulary Game</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            text-align: center;
            padding: 20px;
        }
        #game-container {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            display: inline-block;
        }
        button {
            padding: 10px 20px;
            margin: 10px;
            border: none;
            border-radius: 5px;
            background-color: #007BFF;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>

<div id="game-container">
    <h1>Metal and Mineral Vocabulary Game</h1>
    <p id="question"></p>
    <input type="text" id="answer" placeholder="Type your answer here" />
    <button id="submit">Submit</button>
    <p id="result"></p>
    <button id="next" style="display:none;">Next</button>
</div>

<script>
    // Vocabulary list for the game
    const vocabulary = [
        { word: "Gold", definition: "A yellow precious metal used for jewelry and currency." },
        { word: "Silver", definition: "A shiny gray-white metal used in jewelry and tableware." },
        { word: "Copper", definition: "A reddish-brown metal used in electrical wiring." },
        { word: "Iron", definition: "A strong metal used in construction and manufacturing." },
        { word: "Aluminum", definition: "A lightweight metal used in cans and aircraft." },
        { word: "Lead", definition: "A heavy metal used in batteries and radiation shielding." },
        { word: "Zinc", definition: "A bluish-white metal used for galvanizing iron." },
        { word: "Nickel", definition: "A silvery-white metal used in coins and alloys." }
    ];

    let currentIndex = 0;

    // Function to display the current question
    function displayQuestion() {
        if (currentIndex < vocabulary.length) {
            document.getElementById("question").innerText = `What is the definition of ${vocabulary[currentIndex].word}?`;
            document.getElementById("result").innerText = '';
            document.getElementById("answer").value = '';
            document.getElementById("next").style.display = 'none';
        } else {
            document.getElementById("game-container").innerHTML = "<h2>Congratulations! You've completed the game!</h2>";
        }
    }

    // Function to check the answer
    function checkAnswer() {
        const userAnswer = document.getElementById("answer").value.trim().toLowerCase();
        const correctAnswer = vocabulary[currentIndex].definition.toLowerCase();

        if (userAnswer === correctAnswer) {
            document.getElementById("result").innerText = "Correct! Well done.";
        } else {
            document.getElementById("result").innerText = `Incorrect. The correct answer is: ${vocabulary[currentIndex].definition}`;
        }

        document.getElementById("next").style.display = 'inline';
    }

    // Event listeners for button clicks
    document.getElementById("submit").addEventListener("click", checkAnswer);
    document.getElementById("next").addEventListener("click", () => {
        currentIndex++;
        displayQuestion();
    });

    // Initialize the game
    displayQuestion();
</script>

</body>
</html>
```
