"""
Generated Code Metadata:
========================
Original URL: https://amarparasanar.com.mx
Prompt: Develop a basic survey or assessment tool using HTML, CSS, and JavaScript to help individuals identify their emotional needs and recommend suitable therapy services or courses from Amar para Sanar.
Generated: DETERMINISTIC_54e36337a81c5fb1
Batch ID: 20250622_211453
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
    <title>Emotional Needs Survey</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Emotional Needs Survey</h1>
        <form id="surveyForm">
            <div class="question">
                <label for="question1">1. How often do you feel overwhelmed by your emotions?</label>
                <select id="question1" required>
                    <option value="">Select an option</option>
                    <option value="never">Never</option>
                    <option value="sometimes">Sometimes</option>
                    <option value="often">Often</option>
                    <option value="always">Always</option>
                </select>
            </div>
            <div class="question">
                <label for="question2">2. Do you find it difficult to connect with others?</label>
                <select id="question2" required>
                    <option value="">Select an option</option>
                    <option value="never">Never</option>
                    <option value="sometimes">Sometimes</option>
                    <option value="often">Often</option>
                    <option value="always">Always</option>
                </select>
            </div>
            <div class="question">
                <label for="question3">3. How often do you feel anxious or stressed?</label>
                <select id="question3" required>
                    <option value="">Select an option</option>
                    <option value="never">Never</option>
                    <option value="sometimes">Sometimes</option>
                    <option value="often">Often</option>
                    <option value="always">Always</option>
                </select>
            </div>
            <button type="submit">Submit</button>
        </form>
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
    background-color: #f4f4f4;
    margin: 0;
    padding: 20px;
}

.container {
    max-width: 600px;
    margin: auto;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
    text-align: center;
}

.question {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
}

select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}

button {
    width: 100%;
    padding: 10px;
    background-color: #28a745;
    color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

button:hover {
    background-color: #218838;
}

.result {
    margin-top: 20px;
    font-weight: bold;
    text-align: center;
}
```

```javascript
// script.js

// Function to handle form submission
document.getElementById('surveyForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    // Collect responses
    const responses = {
        question1: document.getElementById('question1').value,
        question2: document.getElementById('question2').value,
        question3: document.getElementById('question3').value
    };

    // Validate responses
    if (validateResponses(responses)) {
        // Process responses and display results
        const result = processResponses(responses);
        displayResult(result);
    } else {
        alert('Please answer all questions before submitting.');
    }
});

// Function to validate responses
function validateResponses(responses) {
    return Object.values(responses).every(response => response !== "");
}

// Function to process responses and recommend services
function processResponses(responses) {
    let score = 0;

    // Simple scoring based on responses
    score += getScore(responses.question1);
    score += getScore(responses.question2);
    score += getScore(responses.question3);

    // Recommend services based on score
    if (score <= 3) {
        return "You may benefit from individual therapy. Consider reaching out to Amar para Sanar for personalized support.";
    } else if (score <= 6) {
        return "Group therapy or workshops could be beneficial. Check out Amar para Sanar for available courses.";
    } else {
        return "You might want to explore intensive therapy options. Amar para Sanar offers various programs to help.";
    }
}

// Function to convert response to score
function getScore(response) {
    switch (response) {
        case 'never':
            return 1;
        case 'sometimes':
            return 2;
        case 'often':
            return 3;
        case 'always':
            return 4;
        default:
            return 0;
    }
}

// Function to display the result
function displayResult(result) {
    const resultDiv = document.getElementById('result');
    resultDiv.textContent = result;
}
```
