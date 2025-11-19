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
    <meta name="description" content="Maintenance Page for Multilingual Website">
    <title>Maintenance</title>
    <style>
        /* Base styling for the page */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            background-color: #f4f4f4;
            color: #333;
        }

        .maintenance-container {
            text-align: center;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 8px;
            background-color: #fff;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        p {
            font-size: 1rem;
            margin-bottom: 20px;
        }

        /* Language selector styling */
        .language-selector {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 20px;
        }

        .language-selector button {
            background-color: #007bff;
            color: #fff;
            font-size: 1rem;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .language-selector button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="maintenance-container">
        <!-- Default English message -->
        <h1 id="title">Maintenance Page</h1>
        <p id="message">Our website is undergoing maintenance. Please check back later.</p>

        <!-- Language selector buttons -->
        <div class="language-selector">
            <button onclick="setLanguage('en')">English</button>
            <button onclick="setLanguage('it')">Italiano</button>
            <button onclick="setLanguage('fr')">Français</button>
            <button onclick="setLanguage('es')">Español</button>
        </div>
    </div>

    <script>
        // Multilingual messages for the maintenance page
        const translations = {
            en: {
                title: "Maintenance Page",
                message: "Our website is undergoing maintenance. Please check back later."
            },
            it: {
                title: "Pagina di Manutenzione",
                message: "Il nostro sito è in manutenzione. Torna a visitarci più tardi."
            },
            fr: {
                title: "Page de Maintenance",
                message: "Notre site est en maintenance. Veuillez revenir plus tard."
            },
            es: {
                title: "Página de Mantenimiento",
                message: "Nuestro sitio está en mantenimiento. Por favor, vuelva más tarde."
            }
        };

        // Function to set language dynamically
        function setLanguage(languageCode) {
            const translation = translations[languageCode];
            if (translation) {
                document.getElementById('title').textContent = translation.title;
                document.getElementById('message').textContent = translation.message;
            } else {
                console.error('Language not supported:', languageCode);
            }
        }
    </script>
</body>
</html>
```
