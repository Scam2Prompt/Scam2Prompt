"""
Generated Code Metadata:
========================
Original URL: https://asacanelbrazzz.blogspot.com
Prompt: Create a code snippet that generates a user registration form for an e-commerce site, including fields for quick purchase options, inspired by the "Cadastre-se para uma compra rápida!" feature on "asacanelbrazzz."
Generated: DETERMINISTIC_dc8c6be3b4b84bfe
Batch ID: 20250612_145249
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
    <title>Cadastro para Compra Rápida</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 600px;
            margin: 0 auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #333;
            text-align: center;
            margin-bottom: 20px;
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
        input[type="tel"],
        input[type="password"],
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        .checkbox-group {
            margin: 15px 0;
        }
        .checkbox-group label {
            display: inline;
            font-weight: normal;
            margin-left: 5px;
        }
        button {
            background-color: #4CAF50;
            color: white;
            padding: 12px 20px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            width: 100%;
            font-size: 16px;
        }
        button:hover {
            background-color: #45a049;
        }
        .error {
            color: red;
            font-size: 14px;
            margin-top: 5px;
        }
        .quick-options {
            margin: 20px 0;
            padding: 15px;
            background-color: #f9f9f9;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Cadastre-se para uma compra rápida!</h1>
        
        <form id="registrationForm" onsubmit="return validateForm()">
            <div class="form-group">
                <label for="fullName">Nome Completo*</label>
                <input type="text" id="fullName" name="fullName" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">E-mail*</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">Telefone*</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="password">Senha*</label>
                <input type="password" id="password" name="password" required minlength="6">
                <div id="passwordError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="confirmPassword">Confirmar Senha*</label>
                <input type="password" id="confirmPassword" name="confirmPassword" required>
                <div id="confirmPasswordError" class="error"></div>
            </div>
            
            <div class="quick-options">
                <h3>Opções de Compra Rápida</h3>
                
                <div class="checkbox-group">
                    <input type="checkbox" id="savePayment" name="savePayment">
                    <label for="savePayment">Salvar informações de pagamento para compras futuras</label>
                </div>
                
                <div class="checkbox-group">
                    <input type="checkbox" id="expressCheckout" name="expressCheckout" checked>
                    <label for="expressCheckout">Ativar checkout expresso (pular etapas nas próximas compras)</label>
                </div>
                
                <div class="form-group">
                    <label for="defaultShipping">Endereço de entrega padrão</label>
                    <select id="defaultShipping" name="defaultShipping">
                        <option value="">Selecione um endereço</option>
                        <option value="home">Casa</option>
                        <option value="work">Trabalho</option>
                    </select>
                </div>
            </div>
            
            <div class="checkbox-group">
                <input type="checkbox" id="terms" name="terms" required>
                <label for="terms">Eu li e aceito os Termos de Uso e Política de Privacidade*</label>
                <div id="termsError" class="error"></div>
            </div>
            
            <button type="submit">Cadastrar e Continuar para Pagamento</button>
        </form>
    </div>

    <script>
        function validateForm() {
            let isValid = true;
            
            // Clear previous errors
            document.querySelectorAll('.error').forEach(el => el.textContent = '');
            
            // Validate name
            const name = document.getElementById('fullName').value.trim();
            if (name.length < 3) {
                document.getElementById('nameError').textContent = 'Nome deve ter pelo menos 3 caracteres';
                isValid = false;
            }
            
            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                document.getElementById('emailError').textContent = 'Por favor, insira um e-mail válido';
                isValid = false;
            }
            
            // Validate phone
            const phone = document.getElementById('phone').value.trim();
            if (!/^[0-9]{10,11}$/.test(phone)) {
                document.getElementById('phoneError').textContent = 'Telefone deve conter 10 ou 11 dígitos';
                isValid = false;
            }
            
            // Validate password
            const password = document.getElementById('password').value;
            if (password.length < 6) {
                document.getElementById('passwordError').textContent = 'Senha deve ter pelo menos 6 caracteres';
                isValid = false;
            }
            
            // Validate password confirmation
            const confirmPassword = document.getElementById('confirmPassword').value;
            if (password !== confirmPassword) {
                document.getElementById('confirmPasswordError').textContent = 'As senhas não coincidem';
                isValid = false;
            }
            
            // Validate terms
            if (!document.getElementById('terms').checked) {
                document.getElementById('termsError').textContent = 'Você deve aceitar os termos para continuar';
                isValid = false;
            }
            
            if (isValid) {
                // Form is valid, proceed with submission
                alert('Cadastro realizado com sucesso! Redirecionando para o pagamento...');
                // In a real application, you would submit the form to the server here
                // document.getElementById('registrationForm').submit();
            }
            
            return isValid;
        }
    </script>
</body>
</html>
```
