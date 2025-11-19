"""
Generated Code Metadata:
========================
Original URL: https://casapiticilor.ro
Prompt: Design a simple webpage using HTML, CSS, and JavaScript that displays a quote of the day from a famous football personality, like Allesandro DK, and provide the code for it.
Generated: DETERMINISTIC_dc12f44ba565f220
Batch ID: 20250622_211917
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
    <title>Quote of the Day</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Quote of the Day</h1>
        <blockquote id="quote" class="quote">
            "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do." 
            <footer>- Allesandro DK</footer>
        </blockquote>
        <button id="newQuoteBtn">Get New Quote</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styling */
body {
    font-family: Arial, sans-serif;
    background-color: #f4f4f4;
    color: #333;
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* Container styling */
.container {
    text-align: center;
    background: white;
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

/* Quote styling */
.quote {
    font-size: 1.5em;
    margin-bottom: 20px;
}

/* Button styling */
button {
    padding: 10px 20px;
    font-size: 1em;
    color: white;
    background-color: #007BFF;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js

// Array of quotes from famous football personalities
const quotes = [
    "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice, and most of all, love of what you are doing or learning to do. - Allesandro DK",
    "The ball is round, the game lasts ninety minutes, and everything else is just theory. - Sepp Herberger",
    "I learned all about life with a ball at my feet. - Ronaldinho",
    "In football, the worst things are excuses. - Jorge Luis Borges"
];

// Function to get a random quote
function getRandomQuote() {
    const randomIndex = Math.floor(Math.random() * quotes.length);
    return quotes[randomIndex];
}

// Function to display a new quote
function displayNewQuote() {
    const quoteElement = document.getElementById('quote');
    try {
        quoteElement.innerHTML = getRandomQuote();
    } catch (error) {
        console.error("Error displaying new quote:", error);
        quoteElement.innerHTML = "An error occurred while fetching a new quote.";
    }
}

// Event listener for button click
document.getElementById('newQuoteBtn').addEventListener('click', displayNewQuote);
```
