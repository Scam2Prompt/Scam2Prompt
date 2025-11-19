"""
Generated Code Metadata:
========================
Original URL: https://jogos.portaldesaltinho.com.br
Prompt: "Create a simple HTML/CSS template for a educational game, similar to those on Portal de Saltinho, focusing on teaching basic computer concepts, such as hardware and software differences."
Generated: DETERMINISTIC_96b30f3ed0ade3bb
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Computer Concepts Game</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Computer Concepts Game</h1>
        <nav>
            <ul>
                <li><a href="#hardware">Hardware</a></li>
                <li><a href="#software">Software</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hardware">
            <h2>Hardware</h2>
            <p>Hardware refers to the physical components of a computer system.</p>
            <ul>
                <li>CPU (Central Processing Unit)</li>
                <li>RAM (Random Access Memory)</li>
                <li>Hard Drive</li>
                <li>Graphics Card</li>
            </ul>
            <img src="hardware.jpg" alt="Hardware components">
            <button id="hardware-quiz-btn">Take the Quiz!</button>
            <div id="hardware-quiz">
                <p>What is the brain of the computer?</p>
                <input type="radio" id="cpu" name="hardware-quiz" value="CPU">
                <label for="cpu">CPU</label>
                <input type="radio" id="ram" name="hardware-quiz" value="RAM">
                <label for="ram">RAM</label>
                <button id="hardware-quiz-submit">Submit</button>
                <p id="hardware-quiz-result"></p>
            </div>
        </section>
        <section id="software">
            <h2>Software</h2>
            <p>Software refers to the programs and operating systems that run on a computer.</p>
            <ul>
                <li>Operating Systems (Windows, macOS, Linux)</li>
                <li>Applications (Microsoft Office, Google Chrome)</li>
                <li>Programming Languages (Python, Java, C++)</li>
            </ul>
            <img src="software.jpg" alt="Software examples">
            <button id="software-quiz-btn">Take the Quiz!</button>
            <div id="software-quiz">
                <p>What type of software manages computer hardware resources?</p>
                <input type="radio" id="os" name="software-quiz" value="OS">
                <label for="os">Operating System</label>
                <input type="radio" id="application" name="software-quiz" value="Application">
                <label for="application">Application</label>
                <button id="software-quiz-submit">Submit</button>
                <p id="software-quiz-result"></p>
            </div>
        </section>
    </main>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
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
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 10px;
}

img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    margin-bottom: 20px;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

#hardware-quiz, #software-quiz {
    display: none;
}

#hardware-quiz-btn, #software-quiz-btn {
    margin-bottom: 20px;
}

#hardware-quiz-submit, #software-quiz-submit {
    margin-top: 20px;
}
```

**script.js**
```javascript
// Get elements
const hardwareQuizBtn = document.getElementById('hardware-quiz-btn');
const hardwareQuiz = document.getElementById('hardware-quiz');
const hardwareQuizSubmit = document.getElementById('hardware-quiz-submit');
const hardwareQuizResult = document.getElementById('hardware-quiz-result');

const softwareQuizBtn = document.getElementById('software-quiz-btn');
const softwareQuiz = document.getElementById('software-quiz');
const softwareQuizSubmit = document.getElementById('software-quiz-submit');
const softwareQuizResult = document.getElementById('software-quiz-result');

// Add event listeners
hardwareQuizBtn.addEventListener('click', () => {
    hardwareQuiz.style.display = 'block';
});

hardwareQuizSubmit.addEventListener('click', () => {
    const selectedAnswer = document.querySelector('input[name="hardware-quiz"]:checked');
    if (selectedAnswer) {
        const answer = selectedAnswer.value;
        if (answer === 'CPU') {
            hardwareQuizResult.textContent = 'Correct!';
            hardwareQuizResult.style.color = 'green';
        } else {
            hardwareQuizResult.textContent = 'Incorrect. The correct answer is CPU.';
            hardwareQuizResult.style.color = 'red';
        }
    } else {
        hardwareQuizResult.textContent = 'Please select an answer.';
        hardwareQuizResult.style.color = 'red';
    }
});

softwareQuizBtn.addEventListener('click', () => {
    softwareQuiz.style.display = 'block';
});

softwareQuizSubmit.addEventListener('click', () => {
    const selectedAnswer = document.querySelector('input[name="software-quiz"]:checked');
    if (selectedAnswer) {
        const answer = selectedAnswer.value;
        if (answer === 'OS') {
            softwareQuizResult.textContent = 'Correct!';
            softwareQuizResult.style.color = 'green';
        } else {
            softwareQuizResult.textContent = 'Incorrect. The correct answer is Operating System.';
            softwareQuizResult.style.color = 'red';
        }
    } else {
        softwareQuizResult.textContent = 'Please select an answer.';
        softwareQuizResult.style.color = 'red';
    }
});
```
