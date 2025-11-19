"""
Generated Code Metadata:
========================
Original URL: https://iedeoccidente.edu.co
Prompt: "Generate a school management system login page using HTML and CSS for an educational institution like Institución Educativa de Occidente in Colombia."
Generated: DETERMINISTIC_22868eb94c208809
Batch ID: 20250622_210216
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Institución Educativa de Occidente - Inicio de sesión</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="login-container">
        <h1>Institución Educativa de Occidente</h1>
        <h2>Inicio de sesión</h2>
        <form id="login-form">
            <label for="username">Nombre de usuario:</label>
            <input type="text" id="username" name="username" required>

            <label for="password">Contraseña:</label>
            <input type="password" id="password" name="password" required>

            <button type="submit">Iniciar sesión</button>
            <p id="error-message"></p>
        </form>
    </div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    background-color: #f0f0f0;
}

.login-container {
    width: 300px;
    margin: 50px auto;
    background-color: #fff;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.login-container h1 {
    text-align: center;
    color: #333;
}

.login-container h2 {
    text-align: center;
    margin-bottom: 20px;
}

label {
    display: block;
    margin-bottom: 10px;
}

input[type="text"], input[type="password"] {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    width: 100%;
    height: 40px;
    background-color: #4CAF50;
    color: #fff;
    padding: 10px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#error-message {
    color: red;
    font-size: 12px;
    margin-top: 10px;
}
```

**script.js**
```javascript
const loginForm = document.getElementById('login-form');
const errorMessage = document.getElementById('error-message');

loginForm.addEventListener('submit', async (e) => {
    e.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    try {
        const response = await fetch('/api/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        const data = await response.json();

        if (data.success) {
            // Redirect to dashboard or protected route
            window.location.href = '/dashboard';
        } else {
            errorMessage.textContent = data.message;
        }
    } catch (error) {
        console.error(error);
        errorMessage.textContent = 'Error inesperado. Por favor, inténtelo de nuevo.';
    }
});
```

**server.js (Example using Node.js and Express)**
```javascript
const express = require('express');
const app = express();
const port = 3000;

app.use(express.json());

// Mock user data (replace with actual database connection)
const users = [
    { id: 1, username: 'admin', password: 'password123' }
];

app.post('/api/login', (req, res) => {
    const { username, password } = req.body;

    const user = users.find((u) => u.username === username && u.password === password);

    if (user) {
        res.json({ success: true });
    } else {
        res.json({ success: false, message: 'Nombre de usuario o contraseña incorrecta' });
    }
});

app.listen(port, () => {
    console.log(`Server listening on port ${port}`);
});
```
