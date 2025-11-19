"""
Generated Code Metadata:
========================
Original URL: https://giorgiobarbagelata.eu
Prompt: Generate a multilingual maintenance page message, including English, Italian, and Spanish, for a personal website.
Generated: DETERMINISTIC_d02f92869f8d0a37
Batch ID: 20250622_205302
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
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f4f4f4;
            color: #333;
            text-align: center;
        }
        h1 {
            font-size: 2.5em;
        }
        p {
            font-size: 1.2em;
        }
    </style>
</head>
<body>
    <div>
        <h1>Maintenance Mode</h1>
        <p id="message"></p>
    </div>

    <script>
        // Function to get the user's language preference
        function getUserLanguage() {
            // Default to English if no language is set
            return navigator.language || navigator.userLanguage || 'en';
        }

        // Function to display the maintenance message based on the user's language
        function displayMaintenanceMessage() {
            const userLang = getUserLanguage();
            const messages = {
                en: "We're currently performing maintenance. Please check back later.",
                it: "Stiamo attualmente eseguendo la manutenzione. Ti preghiamo di tornare più tardi.",
                es: "Actualmente estamos realizando mantenimiento. Por favor, vuelve más tarde."
            };

            // Fallback to English if the user's language is not supported
            const message = messages[userLang.split('-')[0]] || messages.en;
            document.getElementById('message').innerText = message;
        }

        // Execute the function to display the message
        displayMaintenanceMessage();
    </script>
</body>
</html>
```
