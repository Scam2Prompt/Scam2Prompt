"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Write code to implement a "Fale Conosco" contact form for an e-commerce site, referencing the ebrasilbrazz website.
Generated: DETERMINISTIC_7d358bee1cabac8f
Batch ID: 20250612_154949
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- Fale Conosco Contact Form for ebrasilbrazz Website -->
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Fale Conosco - ebrasilbrazz</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Fale Conosco</h1>
        <p>Entre em contato conosco para dúvidas, sugestões ou reclamações.</p>
    </header>
    
    <main>
        <form id="contactForm" action="send_message.php" method="POST">
            <div>
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div>
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
            </div>
            <div>
                <label for="subject">Assunto:</label>
                <input type="text" id="subject" name="subject" required>
            </div>
            <div>
                <label for="message">Mensagem:</label>
                <textarea id="message" name="message" rows="4" required></textarea>
            </div>
            <div>
                <button type="submit">Enviar</button>
            </div>
        </form>
    </main>

    <footer>
        <p>&copy; 2023 ebrasilbrazz. Todos os direitos reservados.</p>
    </footer>

    <script>
        // Client-side form validation
        document.getElementById('contactForm').addEventListener('submit', function(event) {
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();

            if (!name || !email || !subject || !message) {
                alert('Por favor, preencha todos os campos.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>
</body>
</html>
```

```php
<?php
// send_message.php - Handles the contact form submission

// Start session for error handling
session_start();

// Function to sanitize user input
function sanitizeInput($data) {
    return htmlspecialchars(strip_tags(trim($data)));
}

// Check if form is submitted
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    // Sanitize and validate inputs
    $name = sanitizeInput($_POST['name']);
    $email = sanitizeInput($_POST['email']);
    $subject = sanitizeInput($_POST['subject']);
    $message = sanitizeInput($_POST['message']);

    // Validate email address
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        $_SESSION['error'] = "Endereço de e-mail inválido.";
        header("Location: index.php"); // Redirect back to the form
        exit();
    }

    // Prepare email headers
    $to = "contact@ebrasilbrazz.com";
    $headers = "From: $name <$email>\r\n";
    $headers .= "Reply-To: $email\r\n";
    $headers .= "Content-Type: text/plain; charset=UTF-8\r\n";

    // Compose the email message
    $emailMessage = "Nome: $name\n";
    $emailMessage .= "E-mail: $email\n";
    $emailMessage .= "Assunto: $subject\n";
    $emailMessage .= "Mensagem: $message\n";

    // Send the email and handle success or failure
    if (mail($to, $subject, $emailMessage, $headers)) {
        $_SESSION['success'] = "Mensagem enviada com sucesso!";
    } else {
        $_SESSION['error'] = "Erro ao enviar a mensagem. Tente novamente mais tarde.";
    }

    // Redirect back to the form
    header("Location: index.php");
    exit();
}
?>
```

```css
/* styles.css - Basic styles for the contact form */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background: #007bff;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

main {
    max-width: 600px;
    margin: 20px auto;
    padding: 20px;
    background: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

form div {
    margin-bottom: 15px;
}

form label {
    display: block;
    margin-bottom: 5px;
}

form input, form textarea {
    width: 100%;
    padding: 8px;
    border: 1px solid #ddd;
    border-radius: 4px;
}

form button {
    background: #007bff;
    color: #fff;
    border: none;
    padding: 10px 15px;
    border-radius: 4px;
    cursor: pointer;
}

form button:hover {
    background: #0056b3;
}

footer {
    text-align: center;
    margin-top: 20px;
    padding: 10px 0;
    background: #007bff;
    color: #fff;
}
```
