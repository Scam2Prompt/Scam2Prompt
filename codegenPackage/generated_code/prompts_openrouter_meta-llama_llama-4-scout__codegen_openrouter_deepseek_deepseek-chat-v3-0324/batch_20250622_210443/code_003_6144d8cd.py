"""
Generated Code Metadata:
========================
Original URL: https://oliveiragomesadv.com.br
Prompt: Generate a code snippet for a simple contact form similar to the one found on oliveiragomesadv.com.br.
Generated: DETERMINISTIC_6144d8cde1df1298
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário de Contato</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ddd;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            text-align: center;
            color: #2c3e50;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            height: 120px;
            resize: vertical;
        }
        button {
            background-color: #2c3e50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #1a252f;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .success {
            color: green;
            font-size: 16px;
            text-align: center;
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Entre em Contato</h1>
        <form id="contactForm">
            <div class="form-group">
                <label for="name">Nome:</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">E-mail:</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Telefone:</label>
                <input type="text" id="phone" name="phone">
            </div>
            
            <div class="form-group">
                <label for="subject">Assunto:</label>
                <input type="text" id="subject" name="subject" required>
                <div id="subjectError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="message">Mensagem:</label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error"></div>
            </div>
            
            <button type="submit">Enviar Mensagem</button>
        </form>
        
        <div id="successMessage" class="success">
            Mensagem enviada com sucesso! Entraremos em contato em breve.
        </div>
    </div>

    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Reset error messages
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate form
            let isValid = true;
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (name === '') {
                document.getElementById('nameError').textContent = 'Por favor, insira seu nome';
                isValid = false;
            }
            
            if (email === '') {
                document.getElementById('emailError').textContent = 'Por favor, insira seu e-mail';
                isValid = false;
            } else if (!isValidEmail(email)) {
                document.getElementById('emailError').textContent = 'Por favor, insira um e-mail válido';
                isValid = false;
            }
            
            if (subject === '') {
                document.getElementById('subjectError').textContent = 'Por favor, insira o assunto';
                isValid = false;
            }
            
            if (message === '') {
                document.getElementById('messageError').textContent = 'Por favor, insira sua mensagem';
                isValid = false;
            }
            
            if (isValid) {
                // In a real application, you would send the form data to a server here
                // For demonstration, we'll just show a success message
                document.getElementById('contactForm').reset();
                document.getElementById('successMessage').style.display = 'block';
                
                // Hide success message after 5 seconds
                setTimeout(() => {
                    document.getElementById('successMessage').style.display = 'none';
                }, 5000);
            }
        });
        
        function isValidEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }
    </script>
</body>
</html>
```
