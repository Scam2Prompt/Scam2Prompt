"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.ire-coinbase.com
Prompt: Write code to display a localized login interface for a webmail system, using the language options provided on the cPanel Webmail page.
Generated: DETERMINISTIC_4c90dc5d28df19f7
Batch ID: 20250612_154651
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
    <title>Webmail Login</title>
    <link rel="stylesheet" href="styles.css">
    <script src="script.js" defer></script>
</head>
<body>
    <div class="login-container">
        <h1 id="login-title">Webmail Login</h1>
        <form id="login-form" action="/login" method="POST" onsubmit="return validateForm()">
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" required>

            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required>

            <label for="language">Language:</label>
            <select id="language" name="language" onchange="changeLanguage()">
                <!-- Language options populated dynamically -->
            </select>

            <button type="submit">Login</button>
        </form>
        <div id="error-message" class="error"></div>
    </div>

    <script>
        // Language options for localization
        const languageOptions = {
            en: 'English',
            es: 'Español',
            fr: 'Français',
            de: 'Deutsch',
            it: 'Italiano'
        };

        // Populate language selection dropdown
        function populateLanguageOptions() {
            const languageSelect = document.getElementById('language');
            for (const [code, name] of Object.entries(languageOptions)) {
                const option = document.createElement('option');
                option.value = code;
                option.textContent = name;
                languageSelect.appendChild(option);
            }
        }

        // Change displayed language based on selection
        function changeLanguage() {
            const selectedLanguage = document.getElementById('language').value;
            // Set localized texts based on the selected language
            switch (selectedLanguage) {
                case 'en':
                    document.getElementById('login-title').textContent = 'Webmail Login';
                    break;
                case 'es':
                    document.getElementById('login-title').textContent = 'Iniciar sesión en Webmail';
                    break;
                case 'fr':
                    document.getElementById('login-title').textContent = 'Connexion Webmail';
                    break;
                case 'de':
                    document.getElementById('login-title').textContent = 'Webmail-Anmeldung';
                    break;
                case 'it':
                    document.getElementById('login-title').textContent = 'Accesso a Webmail';
                    break;
                default:
                    document.getElementById('login-title').textContent = 'Webmail Login';
            }
        }

        // Form validation before submission
        function validateForm() {
            const email = document.getElementById('email').value;
            const password = document.getElementById('password').value;
            const errorMessageDiv = document.getElementById('error-message');
            errorMessageDiv.textContent = ''; // Clear previous error messages

            // Basic validation (this can be enhanced as necessary)
            if (!email || !password) {
                errorMessageDiv.textContent = 'Email and Password are required.';
                return false; // Prevent form submission
            }

            return true; // Allow form submission
        }

        // Initialize language options on page load
        window.onload = populateLanguageOptions;
    </script>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .login-container {
            background: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .error {
            color: red;
            margin-top: 10px;
        }
    </style>
</body>
</html>
```
