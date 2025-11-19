"""
Generated Code Metadata:
========================
Original URL: https://coworkingcomercio.com.br
Prompt: "Create a web page using HTML, CSS, and JavaScript that displays the 'Horário de Funcionamento' of a coworking space and allows users to send a message via email or WhatsApp."
Generated: DETERMINISTIC_cd0ec9dcc17fe71a
Batch ID: 20250622_205842
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
    <title>Horário de Funcionamento - Coworking Space</title>
    <style>
        /* Reset and Base Styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
            padding: 20px;
        }

        header {
            text-align: center;
            margin-bottom: 30px;
            padding: 20px 0;
            background-color: #2c3e50;
            color: white;
            border-radius: 8px;
        }

        h1 {
            font-size: 2.2rem;
            margin-bottom: 10px;
        }

        h2 {
            font-size: 1.8rem;
            margin-bottom: 20px;
            color: #2c3e50;
        }

        /* Opening Hours Section */
        .hours-section {
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }

        .hours-grid {
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 15px;
        }

        .day-hours {
            display: flex;
            justify-content: space-between;
            padding: 10px;
            border-bottom: 1px solid #eee;
        }

        .day {
            font-weight: bold;
        }

        /* Contact Form Section */
        .contact-section {
            background-color: white;
            padding: 25px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 20px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }

        input, textarea, select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }

        textarea {
            height: 120px;
            resize: vertical;
        }

        button {
            background-color: #2c3e50;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #1a252f;
        }

        .button-group {
            display: flex;
            gap: 15px;
            margin-top: 20px;
        }

        .whatsapp-btn {
            background-color: #25D366;
        }

        .whatsapp-btn:hover {
            background-color: #128C7E;
        }

        .email-btn {
            background-color: #3498db;
        }

        .email-btn:hover {
            background-color: #2980b9;
        }

        .success-message {
            color: #27ae60;
            margin-top: 15px;
            font-weight: bold;
            display: none;
        }

        .error-message {
            color: #e74c3c;
            margin-top: 15px;
            font-weight: bold;
            display: none;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .hours-grid {
                grid-template-columns: 1fr;
            }

            .button-group {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Coworking Space</h1>
            <p>Seu espaço de trabalho colaborativo</p>
        </header>

        <section class="hours-section">
            <h2>Horário de Funcionamento</h2>
            <div class="hours-grid">
                <div class="day-hours">
                    <span class="day">Segunda-feira</span>
                    <span class="hours">08:00 - 20:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Terça-feira</span>
                    <span class="hours">08:00 - 20:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Quarta-feira</span>
                    <span class="hours">08:00 - 20:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Quinta-feira</span>
                    <span class="hours">08:00 - 20:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Sexta-feira</span>
                    <span class="hours">08:00 - 20:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Sábado</span>
                    <span class="hours">09:00 - 14:00</span>
                </div>
                <div class="day-hours">
                    <span class="day">Domingo</span>
                    <span class="hours">Fechado</span>
                </div>
            </div>
        </section>

        <section class="contact-section">
            <h2>Entre em Contato</h2>
            <form id="contactForm">
                <div class="form-group">
                    <label for="name">Nome:</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email:</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="phone">Telefone:</label>
                    <input type="tel" id="phone" name="phone">
                </div>
                <div class="form-group">
                    <label for="subject">Assunto:</label>
                    <select id="subject" name="subject" required>
                        <option value="">Selecione um assunto</option>
                        <option value="membership">Membros</option>
                        <option value="event">Eventos</option>
                        <option value="question">Dúvidas</option>
                        <option value="other">Outros</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Mensagem:</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <div class="button-group">
                    <button type="button" id="whatsappBtn" class="whatsapp-btn">Enviar via WhatsApp</button>
                    <button type="button" id="emailBtn" class="email-btn">Enviar via Email</button>
                </div>
                <div id="successMessage" class="success-message">Mensagem enviada com sucesso!</div>
                <div id="errorMessage" class="error-message">Ocorreu um erro ao enviar a mensagem.</div>
            </form>
        </section>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const contactForm = document.getElementById('contactForm');
            const whatsappBtn = document.getElementById('whatsappBtn');
            const emailBtn = document.getElementById('emailBtn');
            const successMessage = document.getElementById('successMessage');
            const errorMessage = document.getElementById('errorMessage');

            // Function to validate form
            function validateForm() {
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const subject = document.getElementById('subject').value;
                const message = document.getElementById('message').value.trim();

                if (!name || !email || !subject || !message) {
                    showError('Por favor, preencha todos os campos obrigatórios.');
                    return false;
                }

                if (!validateEmail(email)) {
                    showError('Por favor, insira um email válido.');
                    return false;
                }

                return true;
            }

            // Email validation helper
            function validateEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }

            // Show success message
            function showSuccess() {
                successMessage.style.display = 'block';
                errorMessage.style
