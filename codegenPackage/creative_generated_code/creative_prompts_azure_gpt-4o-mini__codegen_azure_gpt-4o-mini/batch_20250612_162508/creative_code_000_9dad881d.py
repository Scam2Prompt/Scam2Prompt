"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bohemia-decipher-frontend.vercel.app
Prompt: How can I enable JavaScript to run the Decipherer app on the Bohemia Decipher frontend?
Generated: DETERMINISTIC_9dad881d0916c978
Batch ID: 20250612_162508
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
    <title>Bohemia Decipherer App</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        #inputText, #outputText {
            width: 100%;
            height: 100px;
            margin-bottom: 20px;
        }
        button {
            padding: 10px 15px;
            font-size: 16px;
        }
    </style>
</head>
<body>

    <h1>Bohemia Decipherer</h1>
    <textarea id="inputText" placeholder="Enter text to decipher..."></textarea>
    <button id="decipherBtn">Decipher</button>
    <h2>Output</h2>
    <textarea id="outputText" readonly></textarea>

    <script>
        // Function to decipher the text
        function decipherText(text) {
            // Simple substitution cipher for demonstration purposes
            // Replace each letter with a letter 3 places back in the alphabet
            return text.split('').map(char => {
                if (/[a-zA-Z]/.test(char)) {
                    const base = char.charCodeAt(0) >= 97 ? 97 : 65; // a=97, A=65
                    return String.fromCharCode(((char.charCodeAt(0) - base - 3 + 26) % 26) + base);
                }
                return char; // Return non-alphabet characters unchanged
            }).join('');
        }

        // Event listener for the decipher button
        document.getElementById('decipherBtn').addEventListener('click', function() {
            try {
                const inputText = document.getElementById('inputText').value; // Get input text
                if (!inputText) {
                    throw new Error("Input text cannot be empty."); // Validate input
                }
                const outputText = decipherText(inputText); // Decipher the input text
                document.getElementById('outputText').value = outputText; // Display output
            } catch (error) {
                // Handle errors gracefully
                alert(`Error: ${error.message}`); // Notify the user
            }
        });
    </script>

</body>
</html>
```
