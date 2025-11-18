"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://webmail.dexodoor.com
Prompt: Generate code to implement a multilingual locale selector for a webmail login page, supporting languages like Arabic, Japanese, and Russian, as described on the Dexodoor Webmail site.
Generated: DETERMINISTIC_e7b12223c0139fc6
Batch ID: 20250612_152441
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
    <title>Dexodoor Webmail Login</title>
    <style>
        /* Basic styling for the locale selector */
        .locale-selector {
            margin-bottom: 10px;
        }

        .locale-selector select {
            font-size: 1rem;
            padding: 5px;
        }

        .login-form {
            max-width: 300px;
            margin: auto;
            text-align: left;
        }

        .form-group {
            margin-bottom: 15px;
        }

        .form-group label {
            display: block;
            margin-bottom: 5px;
        }

        .form-group input {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }

        .form-group button {
            width: 100%;
            padding: 10px;
            background-color: #007BFF;
            color: #FFF;
            border: none;
            cursor: pointer;
        }

        .form-group button:hover {
            background-color: #0056b3;
        }
    </style>
    <script>
        // Language translations for the login page
        const translations = {
            en: {
                username: "Username",
                password: "Password",
                loginButton: "Login"
            },
            ar: {
                username: "اسم المستخدم",
                password: "كلمة المرور",
                loginButton: "تسجيل الدخول"
            },
            ja: {
                username: "ユーザー名",
                password: "パスワード",
                loginButton: "ログイン"
            },
            ru: {
                username: "Имя пользователя",
                password: "Пароль",
                loginButton: "Войти"
            }
        };

        /**
         * Updates the login form labels and button text based on the selected locale.
         */
        function updateLocale() {
            const selectedLocale = document.getElementById("locale").value;
            const translation = translations[selectedLocale];

            if (translation) {
                document.getElementById("username-label").textContent = translation.username;
                document.getElementById("password-label").textContent = translation.password;
                document.getElementById("login-button").textContent = translation.loginButton;
            } else {
                console.error("Translation not found for selected locale:", selectedLocale);
            }
        }

        // Ensure the locale updates on page load
        window.onload = updateLocale;
    </script>
</head>

<body>
    <div class="login-form">
        <!-- Locale selector dropdown -->
        <div class="locale-selector">
            <label for="locale">Select Language:</label>
            <select id="locale" onchange="updateLocale()">
                <option value="en">English</option>
                <option value="ar">العربية (Arabic)</option>
                <option value="ja">日本語 (Japanese)</option>
                <option value="ru">Русский (Russian)</option>
            </select>
        </div>

        <!-- Login form -->
        <form action="/login" method="POST">
            <div class="form-group">
                <label id="username-label" for="username">Username</label>
                <input type="text" id="username" name="username" required />
            </div>
            <div class="form-group">
                <label id="password-label" for="password">Password</label>
                <input type="password" id="password" name="password" required />
            </div>
            <div class="form-group">
                <button id="login-button" type="submit">Login</button>
            </div>
        </form>
    </div>
</body>

</html>
```
