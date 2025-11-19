"""
Generated Code Metadata:
========================
Original URL: https://polkadots.work
Prompt: Write HTML code that is automatically formatted for readability using a tool similar to the "HTMLフォーマッタ" feature on コピーツールラボ.
Generated: DETERMINISTIC_6e4ed5a0c0834081
Batch ID: 20250612_151239
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
    <title>HTML Formatter Tool</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f4f4f4;
        }
        h1 {
            color: #333;
        }
        textarea {
            width: 100%;
            height: 200px;
            margin-bottom: 20px;
            padding: 10px;
            font-family: monospace;
            font-size: 14px;
        }
        button {
            padding: 10px 15px;
            background-color: #007BFF;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        pre {
            background-color: #fff;
            padding: 10px;
            border: 1px solid #ccc;
            overflow: auto;
        }
    </style>
</head>
<body>

    <h1>HTML Formatter Tool</h1>
    <p>Paste your HTML code below and click "Format" to beautify it.</p>

    <textarea id="htmlInput" placeholder="Paste your HTML code here..."></textarea>
    <button id="formatButton">Format</button>

    <h2>Formatted HTML Output:</h2>
    <pre id="formattedOutput"></pre>

    <script>
        // Function to format HTML code
        function formatHTML(html) {
            // Create a temporary DOM element to parse the HTML
            const tempDiv = document.createElement('div');
            tempDiv.innerHTML = html;

            // Use JSON.stringify to format the HTML with indentation
            return tempDiv.innerHTML
                .replace(/></g, '>\n<') // Add new lines between tags
                .replace(/</g, '\n<')   // Add new lines before opening tags
                .replace(/>\n/g, '>\n'); // Clean up new lines after closing tags
        }

        // Event listener for the format button
        document.getElementById('formatButton').addEventListener('click', function() {
            // Get the input HTML code
            const inputHTML = document.getElementById('htmlInput').value;

            // Check if input is empty
            if (!inputHTML.trim()) {
                alert('Please enter some HTML code to format.');
                return;
            }

            try {
                // Format the HTML and display it
                const formattedHTML = formatHTML(inputHTML);
                document.getElementById('formattedOutput').textContent = formattedHTML;
            } catch (error) {
                // Handle any errors that occur during formatting
                console.error('Error formatting HTML:', error);
                alert('An error occurred while formatting the HTML. Please check the console for details.');
            }
        });
    </script>

</body>
</html>
```
