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
            background-color: #f5f5f5;
            color: #333;
        }
        .container {
            text-align: center;
            max-width: 600px;
            padding: 20px;
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #d32f2f;
            margin-bottom: 20px;
        }
        .language-selector {
            margin-top: 30px;
        }
        select {
            padding: 8px 12px;
            border-radius: 4px;
            border: 1px solid #ddd;
            font-size: 16px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1 id="title">Page Not Available</h1>
        <p id="message">We're sorry, but this page is currently not available in your language.</p>
        <div class="language-selector">
            <select id="language-selector">
                <option value="en">English</option>
                <option value="de">Deutsch</option>
                <option value="fr">Français</option>
                <option value="es">Español</option>
                <option value="it">Italiano</option>
                <option value="pt">Português</option>
                <option value="ru">Русский</option>
                <option value="zh">中文</option>
                <option value="ja">日本語</option>
            </select>
        </div>
    </div>

    <script>
        // Language translations
        const translations = {
            en: {
                title: "Page Not Available",
                message: "We're sorry, but this page is currently not available in your language."
            },
            de: {
                title: "Seite nicht verfügbar",
                message: "Entschuldigung, diese Seite ist in Ihrer Sprache derzeit nicht verfügbar."
            },
            fr: {
                title: "Page non disponible",
                message: "Désolé, cette page n'est actuellement pas disponible dans votre langue."
            },
            es: {
                title: "Página no disponible",
                message: "Lo sentimos, esta página no está disponible actualmente en su idioma."
            },
            it: {
                title: "Pagina non disponibile",
                message: "Siamo spiacenti, questa pagina non è attualmente disponibile nella tua lingua."
            },
            pt: {
                title: "Página não disponível",
                message: "Desculpe, esta página não está disponível no seu idioma no momento."
            },
            ru: {
                title: "Страница недоступна",
                message: "Извините, эта страница в настоящее время недоступна на вашем языке."
            },
            zh: {
                title: "页面不可用",
                message: "抱歉，此页面目前无法使用您的语言。"
            },
            ja: {
                title: "ページが利用できません",
                message: "申し訳ありませんが、このページは現在あなたの言語では利用できません。"
            }
        };

        // Get DOM elements
        const titleElement = document.getElementById('title');
        const messageElement = document.getElementById('message');
        const languageSelector = document.getElementById('language-selector');

        // Function to update page content based on selected language
        function updateLanguage() {
            const selectedLanguage = languageSelector.value;
            const translation = translations[selectedLanguage] || translations['en'];
            
            titleElement.textContent = translation.title;
            messageElement.textContent = translation.message;
        }

        // Set initial language based on browser preference or default to English
        function setInitialLanguage() {
            const browserLanguage = navigator.language.split('-')[0];
            if (translations[browserLanguage]) {
                languageSelector.value = browserLanguage;
            } else {
                languageSelector.value = 'en';
            }
            updateLanguage();
        }

        // Event listener for language selection change
        languageSelector.addEventListener('change', updateLanguage);

        // Initialize the page
        document.addEventListener('DOMContentLoaded', setInitialLanguage);
    </script>
</body>
</html>
```
