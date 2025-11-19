"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://poocoinmod.blogspot.com
Prompt: Develop a simple HTML form that allows users to submit their favorite types of shoes like "sapato social" or "tenis de esporte" and stores the data for Eleiton Sapatos em Geral.
Generated: DETERMINISTIC_9eca79881f6bd7d1
Batch ID: 20250612_155235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro de Tipos de Sapatos</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to an external CSS file for styling -->
</head>
<body>

    <h1>Cadastro de Sapatos Favoritos</h1>
    <form id="shoeForm" action="submit.php" method="POST">
        <label for="shoeType">Tipo de Sapato:</label>
        <input type="text" id="shoeType" name="shoeType" required placeholder="Ex: sapato social, tenis de esporte">
        <br>
        <button type="submit">Enviar</button>
    </form>

    <div id="message" style="color: red;"></div> <!-- Message display area for errors or confirmations -->

    <script>
        // Add event listener to handle form submission
        document.getElementById('shoeForm').addEventListener('submit', function(event) {
            // Prevent default form submission
            event.preventDefault();

            const shoeType = document.getElementById('shoeType').value;

            // Basic validation
            if (shoeType.trim() === '') {
                document.getElementById('message').innerText = 'Por favor, insira um tipo de sapato.';
                return;
            }

            // Create a FormData object to send the form data
            const formData = new FormData();
            formData.append('shoeType', shoeType);

            // Send form data to the server using Fetch API
            fetch('submit.php', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Erro ao enviar os dados.');
                }
                return response.text();
            })
            .then(data => {
                document.getElementById('message').innerText = 'Dados enviados com sucesso!';
                document.getElementById('shoeForm').reset(); // Clear the form
            })
            .catch(error => {
                document.getElementById('message').innerText = error.message;
            });
        });
    </script>

</body>
</html>
```

```php
<?php
// submit.php - Handles the form submission and stores the shoe type

// Set content type to JSON
header('Content-Type: application/json');

// Function to respond with JSON
function jsonResponse($status, $message) {
    echo json_encode(['status' => $status, 'message' => $message]);
    exit;
}

// Check if the request method is POST
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    jsonResponse('error', 'Método inválido.');
}

// Check if the shoeType is set and not empty
if (isset($_POST['shoeType']) && !empty(trim($_POST['shoeType']))) {
    $shoeType = trim($_POST['shoeType']);

    // Here you would typically store the data in a database
    // For demonstration, we will just simulate a successful response.
    // In a real application, add database insertion logic here.

    jsonResponse('success', 'Tipo de sapato "' . $shoeType . '" armazenado com sucesso!');
} else {
    jsonResponse('error', 'Tipo de sapato inválido.');
}
?>
```
