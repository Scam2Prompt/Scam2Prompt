"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cpanel.arbitrium.adv.br
Prompt: Generate a script in JavaScript to dynamically change the language of a cPanel login page based on user selection.
Generated: DETERMINISTIC_036a6c7ba6123e6a
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// LanguageSwitcher.js

// Function to dynamically change the language of the cPanel login page
class LanguageSwitcher {
    constructor() {
        // Supported languages
        this.languages = {
            en: {
                welcome: "Welcome to cPanel",
                username: "Username",
                password: "Password",
                login: "Login"
            },
            es: {
                welcome: "Bienvenido a cPanel",
                username: "Nombre de usuario",
                password: "Contraseña",
                login: "Iniciar sesión"
            },
            fr: {
                welcome: "Bienvenue sur cPanel",
                username: "Nom d'utilisateur",
                password: "Mot de passe",
                login: "Connexion"
            }
        };

        // Initialize the default language
        this.currentLanguage = 'en';
        
        // Bind the changeLanguage method
        this.changeLanguage = this.changeLanguage.bind(this);
    }

    // Method to change the language based on user selection
    changeLanguage(lang) {
        if (this.languages[lang]) {
            this.currentLanguage = lang;
            this.updateUI();
        } else {
            console.error(`Language '${lang}' is not supported.`);
        }
    }

    // Method to update the UI text based on the current language
    updateUI() {
        try {
            document.getElementById('welcomeMessage').innerText = this.languages[this.currentLanguage].welcome;
            document.getElementById('usernameLabel').innerText = this.languages[this.currentLanguage].username;
            document.getElementById('passwordLabel').innerText = this.languages[this.currentLanguage].password;
            document.getElementById('loginButton').innerText = this.languages[this.currentLanguage].login;
        } catch (error) {
            console.error("Error updating UI:", error);
        }
    }
}

// Instantiate the LanguageSwitcher
const languageSwitcher = new LanguageSwitcher();

// Event listener for language selection
document.getElementById('languageSelect').addEventListener('change', (event) => {
    const selectedLanguage = event.target.value;
    languageSwitcher.changeLanguage(selectedLanguage);
});

// Initial UI setup
window.onload = () => {
    languageSwitcher.updateUI();
};
```

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cPanel Login</title>
    <script src="LanguageSwitcher.js" defer></script>
</head>
<body>
    <h1 id="welcomeMessage">Welcome to cPanel</h1>
    <label id="usernameLabel" for="usernameInput">Username</label>
    <input type="text" id="usernameInput">
    <label id="passwordLabel" for="passwordInput">Password</label>
    <input type="password" id="passwordInput">
    <button id="loginButton">Login</button>

    <select id="languageSelect">
        <option value="en">English</option>
        <option value="es">Español</option>
        <option value="fr">Français</option>
    </select>
</body>
</html>
```
