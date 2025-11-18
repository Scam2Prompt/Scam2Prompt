"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freenft07.vercel.app
Prompt: Write JavaScript code to detect if JavaScript is disabled in a browser and display a message prompting the user to enable it, similar to the functionality required by the Fritzy v1 app.
Generated: DETERMINISTIC_2da32558b212d3ca
Batch ID: 20250612_154913
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
    <title>JavaScript Detection</title>
    <style>
        /* Style for the message when JavaScript is disabled */
        #noscript-message {
            display: none; /* Hidden by default */
            background-color: #f8d7da; /* Light red background */
            color: #721c24; /* Dark red text */
            padding: 20px; /* Padding for spacing */
            border: 1px solid #f5c6cb; /* Border same color as background */
            margin: 20px; /* Margin for outer spacing */
            border-radius: 5px; /* Rounded corners */
        }
    </style>
</head>
<body>

    <noscript>
        <div id="noscript-message">
            <strong>JavaScript is disabled in your browser.</strong>
            <p>Please enable JavaScript to use this application.</p>
        </div>
    </noscript>

    <script>
        // Function to show a message if JavaScript is enabled
        function showPageContent() {
            // Ensure this function is called once the script is executed
            document.body.innerHTML += "<p>JavaScript is enabled! Welcome to our application.</p>";
        }

        // Call the function to show content indicating JS is on
        showPageContent();
    </script>
</body>
</html>
```
