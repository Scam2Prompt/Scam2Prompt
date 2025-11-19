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
    <title>Football Quote of the Day</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            padding: 20px;
        }

        .quote-container {
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            padding: 30px;
            max-width: 600px;
            width: 100%;
            text-align: center;
        }

        h1 {
            color: #333;
            margin-bottom: 20px;
            font-size: 24px;
        }

        .quote {
            font-size: 18px;
            line-height: 1.6;
            margin-bottom: 20px;
            color: #555;
        }

        .author {
            font-style: italic;
            font-weight: bold;
            color: #333;
        }

        .btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            margin-top: 20px;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #45a049;
        }

        .loading {
            color: #777;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="quote-container">
        <h1>Football Quote of the Day</h1>
        <div id="quote-text" class="quote loading">Loading quote...</div>
        <div id="quote-author" class="author"></div>
        <button id="new-quote-btn" class="btn">New Quote</button>
    </div>

    <script>
        // Array of football quotes with authors
        const footballQuotes = [
            {
                quote: "Some people think football is a matter of life and death. I assure you, it's much more serious than that.",
                author: "Bill Shankly"
            },
            {
                quote: "Football is a simple game. Twenty-two men chase a ball for 90 minutes and at the end, the Germans always win.",
                author: "Gary Lineker"
            },
            {
                quote: "The ball is round, the game lasts 90 minutes, everything else is pure theory.",
                author: "Sepp Herberger"
            },
            {
                quote: "You can change your wife, your politics, your religion, but never, never can you change your favorite football team.",
                author: "Eric Cantona"
            },
            {
                quote: "I'm a great believer in luck, and I find the harder I work, the more I have of it.",
                author: "Alessandro Del Piero"
            },
            {
                quote: "Success is no accident. It is hard work, perseverance, learning, studying, sacrifice and most of all, love of what you are doing.",
                author: "Pelé"
            }
        ];

        // DOM elements
        const quoteTextElement = document.getElementById('quote-text');
        const quoteAuthorElement = document.getElementById('quote-author');
        const newQuoteBtn = document.getElementById('new-quote-btn');

        /**
         * Displays a random quote from the footballQuotes array
         */
        function displayRandomQuote() {
            try {
                // Get a random quote
                const randomIndex = Math.floor(Math.random() * footballQuotes.length);
                const randomQuote = footballQuotes[randomIndex];

                // Update the DOM
                quoteTextElement.textContent = `"${randomQuote.quote}"`;
                quoteAuthorElement.textContent = `- ${randomQuote.author}`;
            } catch (error) {
                console.error('Error displaying quote:', error);
                quoteTextElement.textContent = "Failed to load quote. Please try again.";
                quoteAuthorElement.textContent = "";
            }
        }

        // Event listener for the new quote button
        newQuoteBtn.addEventListener('click', displayRandomQuote);

        // Display a quote when the page loads
        document.addEventListener('DOMContentLoaded', displayRandomQuote);
    </script>
</body>
</html>
```
