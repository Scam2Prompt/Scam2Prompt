"""
Generated Code Metadata:
========================
Original URL: https://poocoiniswaptokens.blogspot.com
Prompt: Develop a simple HTML form for users to submit requests for tools like "furadeira" and "parafusadeira" from the "Railane Ferramentas e Aco" inventory.
Generated: DETERMINISTIC_5978b83ea65488b3
Batch ID: 20250612_164145
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
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Railane Ferramentas e Aco - Solicitação de Ferramentas</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1>Railane Ferramentas e Aco</h1>
    <h2>Solicitação de Ferramentas</h2>
    <form id="tool-request-form">
        <label for="tool">Ferramenta:</label>
        <select id="tool" name="tool">
            <option value="">Selecione uma ferramenta</option>
            <option value="furadeira">Furadeira</option>
            <option value="parafusadeira">Parafusadeira</option>
            <!-- Add more tools here -->
        </select>
        <br><br>
        <label for="quantity">Quantidade:</label>
        <input type="number" id="quantity" name="quantity" required>
        <br><br>
        <label for="user-name">Nome do Usuário:</label>
        <input type="text" id="user-name" name="user-name" required>
        <br><br>
        <button type="submit">Solicitar Ferramenta</button>
    </form>

    <div id="response"></div>

    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
}

form {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #4CAF50;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button[type="submit"]:hover {
    background-color: #3e8e41;
}

#response {
    width: 50%;
    margin: 40px auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}
```

**script.js**
```javascript
// Get the form and response elements
const form = document.getElementById('tool-request-form');
const responseDiv = document.getElementById('response');

// Add event listener to form submission
form.addEventListener('submit', (e) => {
    e.preventDefault();

    // Get the form data
    const tool = document.getElementById('tool').value;
    const quantity = document.getElementById('quantity').value;
    const userName = document.getElementById('user-name').value;

    // Validate form data
    if (!tool || !quantity || !userName) {
        responseDiv.innerHTML = '<p>Por favor, preencha todos os campos.</p>';
        return;
    }

    // Send the request to the server
    fetch('/request-tool', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            tool,
            quantity,
            userName
        })
    })
    .then((response) => response.json())
    .then((data) => {
        if (data.success) {
            responseDiv.innerHTML = `<p>Ferramenta solicitada com sucesso! <br> ${data.message}</p>`;
        } else {
            responseDiv.innerHTML = `<p>Erro ao solicitar ferramenta: ${data.message}</p>`;
        }
    })
    .catch((error) => {
        console.error(error);
        responseDiv.innerHTML = '<p>Erro ao solicitar ferramenta.</p>';
    });
});
```

**server.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON bodies
app.use(express.json());

// Inventory of tools
const inventory = {
    "furadeira": 10,
    "parafusadeira": 5
};

// Handle tool requests
app.post('/request-tool', (req, res) => {
    const { tool, quantity, userName } = req.body;

    // Validate request data
    if (!tool || !quantity || !userName) {
        res.status(400).json({
            success: false,
            message: 'Por favor, preencha todos os campos.'
        });
        return;
    }

    // Check if tool is available
    if (!inventory[tool] || inventory[tool] < quantity) {
        res.status(400).json({
            success: false,
            message: `Não há ${quantity} ${tool}(s) disponíveis.`
        });
        return;
    }

    // Update inventory
    inventory[tool] -= quantity;

    // Send response
    res.json({
        success: true,
        message: `Você solicitou ${quantity} ${tool}(s).`
    });
});

// Start server
app.listen(port, () => {
    console.log(`Server started on port ${port}`);
});
```
