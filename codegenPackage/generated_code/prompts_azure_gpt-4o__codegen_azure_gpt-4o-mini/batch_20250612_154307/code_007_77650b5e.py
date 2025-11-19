"""
Generated Code Metadata:
========================
Original URL: https://consulltabrasill.online
Prompt: Build a simple HTML form with JavaScript validation for CPF input, designed for querying indemnification status as described on the webpage.
Generated: DETERMINISTIC_77650b5e0e6de79a
Batch ID: 20250612_154307
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
    <title>Indemnification Status Query</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
        }
    </style>
</head>
<body>
    <h1>Query Indemnification Status</h1>
    <form id="cpfForm" onsubmit="return validateCPF()">
        <label for="cpf">Enter CPF:</label>
        <input type="text" id="cpf" name="cpf" placeholder="XXX.XXX.XXX-XX" required>
        <span id="error-message" class="error"></span>
        <br><br>
        <button type="submit">Check Status</button>
    </form>

    <script>
        /**
         * Validates the CPF input format and checks if it is a valid CPF number.
         * @returns {boolean} - Returns true if the CPF is valid, otherwise false.
         */
        function validateCPF() {
            const cpfInput = document.getElementById('cpf').value;
            const errorMessage = document.getElementById('error-message');
            errorMessage.textContent = ''; // Clear previous error messages

            // Regular expression to validate CPF format
            const cpfPattern = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
            if (!cpfPattern.test(cpfInput)) {
                errorMessage.textContent = 'Invalid CPF format. Please use XXX.XXX.XXX-XX.';
                return false;
            }

            // Remove formatting for further validation
            const cpfDigits = cpfInput.replace(/\D/g, '');

            // Validate CPF digits
            if (!isValidCPF(cpfDigits)) {
                errorMessage.textContent = 'Invalid CPF number.';
                return false;
            }

            // If validation passes, form can be submitted
            return true;
        }

        /**
         * Checks if the provided CPF number is valid.
         * @param {string} cpf - The CPF number without formatting.
         * @returns {boolean} - Returns true if the CPF is valid, otherwise false.
         */
        function isValidCPF(cpf) {
            if (cpf.length !== 11 || /^(\d)\1{10}$/.test(cpf)) {
                return false; // CPF must be 11 digits and not all the same
            }

            let sum = 0;
            let remainder;

            // Validate first digit
            for (let i = 1; i <= 9; i++) {
                sum += parseInt(cpf.charAt(i - 1)) * (11 - i);
            }
            remainder = (sum * 10) % 11;
            if (remainder === 10 || remainder === 11) {
                remainder = 0;
            }
            if (remainder !== parseInt(cpf.charAt(9))) {
                return false;
            }

            // Validate second digit
            sum = 0;
            for (let i = 1; i <= 10; i++) {
                sum += parseInt(cpf.charAt(i - 1)) * (12 - i);
            }
            remainder = (sum * 10) % 11;
            if (remainder === 10 || remainder === 11) {
                remainder = 0;
            }
            if (remainder !== parseInt(cpf.charAt(10))) {
                return false;
            }

            return true; // CPF is valid
        }
    </script>
</body>
</html>
```
