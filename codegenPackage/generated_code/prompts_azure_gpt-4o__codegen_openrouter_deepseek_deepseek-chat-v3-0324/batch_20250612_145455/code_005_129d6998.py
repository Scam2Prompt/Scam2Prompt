"""
Generated Code Metadata:
========================
Original URL: https://cpanel.sophon.am
Prompt: Create a multilingual login interface with locale options similar to the ones listed on the cPanel login page, ensuring support for languages like Arabic, Japanese, and Russian.
Generated: DETERMINISTIC_129d69980d0f6f67
Batch ID: 20250612_145455
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
    <title>Multilingual Login Interface</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            direction: ltr;
        }
        
        .login-container {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            padding: 30px;
            width: 350px;
            text-align: center;
        }
        
        .login-container.rtl {
            direction: rtl;
        }
        
        h1 {
            margin-bottom: 20px;
            color: #333;
        }
        
        .form-group {
            margin-bottom: 15px;
            text-align: left;
        }
        
        .form-group.rtl {
            text-align: right;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        
        button {
            width: 100%;
            padding: 10px;
            background-color: #0078d7;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-weight: bold;
            margin-top: 10px;
        }
        
        button:hover {
            background-color: #005fa3;
        }
        
        .language-selector {
            margin-top: 20px;
            text-align: center;
        }
        
        select {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        
        .error {
            color: red;
            margin-top: 10px;
            font-size: 14px;
        }
    </style>
</head>
<body>
    <div class="login-container" id="loginContainer">
        <h1 id="loginTitle">Login</h1>
        <form id="loginForm">
            <div class="form-group" id="usernameGroup">
                <label id="usernameLabel">Username</label>
                <input type="text" id="username" required>
            </div>
            <div class="form-group" id="passwordGroup">
                <label id="passwordLabel">Password</label>
                <input type="password" id="password" required>
            </div>
            <button type="submit" id="loginButton">Login</button>
            <div class="error" id="errorMessage"></div>
        </form>
        
        <div class="language-selector">
            <select id="languageSelect">
                <option value="en">English</option>
                <option value="ar">العربية (Arabic)</option>
                <option value="ja">日本語 (Japanese)</option>
                <option value="ru">Русский (Russian)</option>
            </select>
        </div>
    </div>

    <script>
        // Language translations
        const translations = {
            en: {
                loginTitle: "Login",
                usernameLabel: "Username",
                passwordLabel: "Password",
                loginButton: "Login",
                errorMessage: "Invalid username or password"
            },
            ar: {
                loginTitle: "تسجيل الدخول",
                usernameLabel: "اسم المستخدم",
                passwordLabel: "كلمة المرور",
                loginButton: "تسجيل الدخول",
                errorMessage: "اسم المستخدم أو كلمة المرور غير صحيحة"
            },
            ja: {
                loginTitle: "ログイン",
                usernameLabel: "ユーザー名",
                passwordLabel: "パスワード",
                loginButton: "ログイン",
                errorMessage: "ユーザー名またはパスワードが無効です"
            },
            ru: {
                loginTitle: "Вход",
                usernameLabel: "Имя пользователя",
                passwordLabel: "Пароль",
                loginButton: "Войти",
                errorMessage: "Неверное имя пользователя или пароль"
            }
        };

        // RTL languages
        const rtlLanguages = ['ar'];

        // DOM elements
        const loginContainer = document.getElementById('loginContainer');
        const loginTitle = document.getElementById('loginTitle');
        const usernameLabel = document.getElementById('usernameLabel');
        const passwordLabel = document.getElementById('passwordLabel');
        const loginButton = document.getElementById('loginButton');
        const errorMessage = document.getElementById('errorMessage');
        const usernameGroup = document.getElementById('usernameGroup');
        const passwordGroup = document.getElementById('passwordGroup');
        const languageSelect = document.getElementById('languageSelect');
        const loginForm = document.getElementById('loginForm');

        // Set language and update UI
        function setLanguage(lang) {
            const translation = translations[lang] || translations['en'];
            
            loginTitle.textContent = translation.loginTitle;
            usernameLabel.textContent = translation.usernameLabel;
            passwordLabel.textContent = translation.passwordLabel;
            loginButton.textContent = translation.loginButton;
            errorMessage.textContent = '';
            
            // Handle RTL languages
            if (rtlLanguages.includes(lang)) {
                loginContainer.classList.add('rtl');
                usernameGroup.classList.add('rtl');
                passwordGroup.classList.add('rtl');
                loginContainer.style.direction = 'rtl';
            } else {
                loginContainer.classList.remove('rtl');
                usernameGroup.classList.remove('rtl');
                passwordGroup.classList.remove('rtl');
                loginContainer.style.direction = 'ltr';
            }
        }

        // Language selector change event
        languageSelect.addEventListener('change', (e) => {
            const selectedLanguage = e.target.value;
            setLanguage(selectedLanguage);
        });

        // Form submission
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;
            
            // Simple validation (replace with actual authentication)
            if (!username || !password) {
                const lang = languageSelect.value;
                errorMessage.textContent = translations[lang].errorMessage;
                return;
            }
            
            // Here you would typically make an API call to authenticate
            console.log('Login attempt:', { username, password });
            
            // For demo purposes, just show success
            alert('Login successful! (This is a demo)');
        });

        // Initialize with default language
        setLanguage('en');
    </script>
</body>
</html>
```
