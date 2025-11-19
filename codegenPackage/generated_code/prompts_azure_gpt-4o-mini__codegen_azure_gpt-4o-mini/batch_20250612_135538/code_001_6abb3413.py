"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: How can I implement a multilingual maintenance page in HTML/CSS that includes messages in Italian, English, and Spanish, as seen on the Giorgiobarbagelata site?
Generated: DETERMINISTIC_6abb34137f6c801f
Batch ID: 20250612_135538
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
    <title>Maintenance Page</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic reset for margins and paddings */
        body, h1, p {
            margin: 0;
            padding: 0;
        }

        /* Full viewport height and center content */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }

        /* Styling for the maintenance message */
        .maintenance-message {
            background: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 20px;
            max-width: 400px;
            width: 100%;
        }

        /* Language selection buttons */
        .language-selector {
            margin-top: 20px;
        }

        .language-button {
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            margin: 0 5px;
        }

        .language-button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="maintenance-message" id="message">
        <h1>Maintenance Mode</h1>
        <p id="message-text">We are currently performing maintenance. Please check back later.</p>
        <div class="language-selector">
            <button class="language-button" onclick="setLanguage('en')">English</button>
            <button class="language-button" onclick="setLanguage('it')">Italiano</button>
            <button class="language-button" onclick="setLanguage('es')">Español</button>
        </div>
    </div>

    <script>
        // Function to set the language of the maintenance message
        function setLanguage(lang) {
            const messageText = document.getElementById('message-text');

            // Language messages
            const messages = {
                en: "We are currently performing maintenance. Please check back later.",
                it: "Stiamo attualmente eseguendo la manutenzione. Ti preghiamo di tornare più tardi.",
                es: "Actualmente estamos realizando mantenimiento. Por favor, vuelve más tarde."
            };

            // Update the message text based on the selected language
            if (messages[lang]) {
                messageText.textContent = messages[lang];
            } else {
                console.error('Language not supported:', lang);
                messageText.textContent = messages['en']; // Fallback to English
            }
        }
    </script>
</body>
</html>
```
