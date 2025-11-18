"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://polkadots.work
Prompt: Create JavaScript code to reverse text strings using a browser-based tool, as described in the "テキスト反転ツール" section of コピーツールラボ.
Generated: DETERMINISTIC_d3654ebc918110cc
Batch ID: 20250612_151239
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
    <title>Text Reversal Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #inputText {
            width: 100%;
            height: 100px;
            margin-bottom: 10px;
        }
        #outputText {
            width: 100%;
            height: 100px;
            margin-top: 10px;
            background-color: #f0f0f0;
            border: 1px solid #ccc;
            resize: none;
        }
        button {
            padding: 10px 15px;
            font-size: 16px;
            cursor: pointer;
        }
    </style>
</head>
<body>
    <h1>テキスト反転ツール (Text Reversal Tool)</h1>
    <textarea id="inputText" placeholder="Enter text to reverse..."></textarea>
    <br>
    <button id="reverseButton">Reverse Text</button>
    <h2>Reversed Text:</h2>
    <textarea id="outputText" readonly></textarea>

    <script>
        // Function to reverse the input text
        function reverseText(text) {
            // Check if the input is a string
            if (typeof text !== 'string') {
                throw new Error('Input must be a string');
            }
            // Return the reversed string
            return text.split('').reverse().join('');
        }

        // Event listener for the button click
        document.getElementById('reverseButton').addEventListener('click', function() {
            try {
                // Get the input text from the textarea
                const inputText = document.getElementById('inputText').value;

                // Reverse the input text
                const reversedText = reverseText(inputText);

                // Display the reversed text in the output textarea
                document.getElementById('outputText').value = reversedText;
            } catch (error) {
                // Log any errors to the console
                console.error('Error reversing text:', error);
                alert('An error occurred while reversing the text. Please try again.');
            }
        });
    </script>
</body>
</html>
```
