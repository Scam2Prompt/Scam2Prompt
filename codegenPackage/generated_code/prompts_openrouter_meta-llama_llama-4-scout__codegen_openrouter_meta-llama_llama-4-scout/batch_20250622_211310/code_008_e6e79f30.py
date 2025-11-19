"""
Generated Code Metadata:
========================
Original URL: https://immediate-peak.nl
Prompt: Create a simple e-learning module or tutorial on "Introduction to Investment" using a framework like HTML5 or Articulate Storyline, inspired by Immediate Peak's educational resources.
Generated: DETERMINISTIC_e6e79f30976dc6cf
Batch ID: 20250622_211310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Introduction to Investment</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Introduction to Investment</h1>
    </header>
    <main>
        <section id="welcome">
            <h2>Welcome to Introduction to Investment</h2>
            <p>Investing can seem intimidating, but it doesn't have to be. In this tutorial, we'll cover the basics of investing and help you get started on your investment journey.</p>
        </section>
        <section id="what-is-investing">
            <h2>What is Investing?</h2>
            <p>Investing is the act of putting your money into assets that have a potential for growth, income, or both. This can include stocks, bonds, real estate, and more.</p>
        </section>
        <section id="types-of-investments">
            <h2>Types of Investments</h2>
            <ul>
                <li><b>Stocks:</b> Represent ownership in companies.</li>
                <li><b>Bonds:</b> Represent debt obligations.</li>
                <li><b>Real Estate:</b> Includes property and REITs.</li>
                <li><b>Mutual Funds:</b> Diversified portfolios of stocks, bonds, or other securities.</li>
            </ul>
        </section>
        <section id="risk-and-return">
            <h2>Risk and Return</h2>
            <p>All investments carry some level of risk. Understanding the relationship between risk and return is crucial to making informed investment decisions.</p>
        </section>
        <section id="getting-started">
            <h2>Getting Started</h2>
            <p>Now that you've learned the basics, it's time to start investing! Consider consulting with a financial advisor or using online resources to find the right investment strategy for you.</p>
            <button id="quiz-button">Take the Quiz</button>
            <div id="quiz-container" style="display: none;">
                <h2>Quiz: Introduction to Investment</h2>
                <form id="quiz-form">
                    <label for="question-1">What is investing?</label>
                    <input type="radio" id="question-1-a" name="question-1" value="a"> 
                    <label for="question-1-a">A type of savings account</label><br>
                    <input type="radio" id="question-1-b" name="question-1" value="b"> 
                    <label for="question-1-b">Putting money into assets with potential for growth or income</label><br>
                    <input type="radio" id="question-1-c" name="question-1" value="c"> 
                    <label for="question-1-c">A type of loan</label><br>

                    <label for="question-2">What type of investment represents ownership in companies?</label>
                    <input type="radio" id="question-2-a" name="question-2" value="a"> 
                    <label for="question-2-a">Bonds</label><br>
                    <input type="radio" id="question-2-b" name="question-2" value="b"> 
                    <label for="question-2-b">Stocks</label><br>
                    <input type="radio" id="question-2-c" name="question-2" value="c"> 
                    <label for="question-2-c">Real Estate</label><br>

                    <button id="submit-quiz">Submit</button>
                </form>
                <div id="quiz-results"></div>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 0.5em;
}

b {
    font-weight: bold;
}

#quiz-button {
    background-color: #4CAF50;
    color: #fff;
    padding: 1em 2em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#quiz-button:hover {
    background-color: #3e8e41;
}

#quiz-container {
    padding: 1em;
}

#quiz-form {
    display: flex;
    flex-direction: column;
}

label {
    margin-bottom: 0.5em;
}

input[type="radio"] {
    margin-right: 0.5em;
}

#submit-quiz {
    background-color: #4CAF50;
    color: #fff;
    padding: 1em 2em;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#submit-quiz:hover {
    background-color: #3e8e41;
}

#quiz-results {
    margin-top: 1em;
}
```

```javascript
// script.js

document.getElementById('quiz-button').addEventListener('click', () => {
    document.getElementById('quiz-container').style.display = 'block';
});

document.getElementById('submit-quiz').addEventListener('click', (e) => {
    e.preventDefault();
    const formData = new FormData(document.getElementById('quiz-form'));
    const answers = {
        'question-1': document.querySelector('input[name="question-1"]:checked').value,
        'question-2': document.querySelector('input[name="question-2"]:checked').value,
    };

    const correctAnswers = {
        'question-1': 'b',
        'question-2': 'b',
    };

    let score = 0;
    Object.keys(answers).forEach((question) => {
        if (answers[question] === correctAnswers[question]) {
            score++;
        }
    });

    document.getElementById('quiz-results').innerHTML = `You scored ${score} out of 2`;
});
```
