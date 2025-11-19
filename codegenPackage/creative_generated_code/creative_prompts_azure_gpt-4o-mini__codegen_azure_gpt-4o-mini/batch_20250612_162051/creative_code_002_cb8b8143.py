"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.nasiniacademyhairextension.it
Prompt: How can I implement a multilingual maintenance page using HTML and CSS, referencing the approach taken by nasiniacademyhairextension.it?
Generated: DETERMINISTIC_cb8b8143f915aedc
Batch ID: 20250612_162051
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
    <title>Maintenance Mode</title>
    <link rel="stylesheet" href="styles.css">
    <style>
        /* Basic styling for the maintenance page */
        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            color: #333;
        }
        h1 {
            font-size: 2.5rem;
        }
        p {
            font-size: 1.2rem;
            max-width: 600px;
            text-align: center;
        }
        .language-selector {
            margin-top: 20px;
        }
        button {
            padding: 10px 20px;
            font-size: 1rem;
            cursor: pointer;
        }
    </style>
</head>
<body>

    <h1 id="title">Maintenance Mode</h1>
    <p id="message">We are currently performing scheduled maintenance. Please check back later.</p>

    <div class="language-selector">
        <button onclick="changeLanguage('en')">English</button>
        <button onclick="changeLanguage('it')">Italian</button>
        <button onclick="changeLanguage('fr')">French</button>
    </div>

    <script>
        // Language content object
        const langContent = {
            en: {
                title: "Maintenance Mode",
                message: "We are currently performing scheduled maintenance. Please check back later."
            },
            it: {
                title: "Modalità Manutenzione",
                message: "Stiamo attualmente eseguendo la manutenzione programmata. Per favore, controlla più tardi."
            },
            fr: {
                title: "Mode Maintenance",
                message: "Nous effectuons actuellement une maintenance programmée. Merci de revenir plus tard."
            }
        };

        // Function to change the page language
        function changeLanguage(lang) {
            // Check if the selected language exists
            if (langContent[lang]) {
                document.getElementById('title').textContent = langContent[lang].title;
                document.getElementById('message').textContent = langContent[lang].message;
            } else {
                console.error("Language not supported: " + lang);
                alert("Language not supported.");
            }
        }
    </script>

</body>
</html>
```
