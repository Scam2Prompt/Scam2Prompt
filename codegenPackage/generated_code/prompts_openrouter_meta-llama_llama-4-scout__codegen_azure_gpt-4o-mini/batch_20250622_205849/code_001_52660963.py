"""
Generated Code Metadata:
========================
Original URL: https://ingoflex.de
Prompt: How can I create a webpage that displays a multilingual "page not available" message, like the one on ingoflex.de, using HTML and JavaScript?
Generated: DETERMINISTIC_52660963ad8f1896
Batch ID: 20250622_205849
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
    <title>Page Not Available</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f8f9fa;
            color: #343a40;
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
    <div id="message-container">
        <h1 id="message-title"></h1>
        <p id="message-description"></p>
    </div>

    <script>
        // Multilingual messages for "Page Not Available"
        const messages = {
            en: {
                title: "Page Not Available",
                description: "We're sorry, but the page you are looking for does not exist."
            },
            de: {
                title: "Seite Nicht Verfügbar",
                description: "Es tut uns leid, aber die von Ihnen gesuchte Seite existiert nicht."
            },
            fr: {
                title: "Page Non Disponible",
                description: "Nous sommes désolés, mais la page que vous recherchez n'existe pas."
            }
        };

        // Function to get the user's language preference
        function getUserLanguage() {
            // Default to English if no language is found
            const lang = navigator.language || navigator.userLanguage;
            return lang.split('-')[0]; // Get the language code (e.g., 'en', 'de', 'fr')
        }

        // Function to display the appropriate message based on user language
        function displayMessage() {
            const userLang = getUserLanguage();
            const message = messages[userLang] || messages.en; // Fallback to English

            // Set the title and description in the message container
            document.getElementById('message-title').innerText = message.title;
            document.getElementById('message-description').innerText = message.description;
        }

        // Execute the displayMessage function on page load
        window.onload = displayMessage;
    </script>
</body>
</html>
```
