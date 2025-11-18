"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://consulltabrasill.online
Prompt: Build a simple HTML form with JavaScript validation for CPF input, designed for querying indemnification status as described on the webpage.
Generated: DETERMINISTIC_77650b5e0e6de79a
Batch ID: 20250612_154307
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
    <title>Indemnification Status Query</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>
    <h1>Query Indemnification Status</h1>
    <form id="cpfForm" onsubmit="return validateForm()">
        <label for="cpf">Enter CPF:</label>
        <input type="text" id="cpf" name="cpf" placeholder="000.000.000-00" required>
        <span id="error" class="error"></span>
        <br><br>
        <button type="submit">Submit</button>
    </form>

    <script>
        /**
         * Validates the CPF input.
         * @returns {boolean} - True if the CPF is valid, false otherwise.
         */
        function validateForm() {
            const cpfInput = document.getElementById('cpf').value;
            const errorElement = document.getElementById('error');
            errorElement.textContent = ''; // Clear previous errors

            if (!isValidCPF(cpfInput)) {
                errorElement.textContent = 'Invalid CPF format. Please enter a valid CPF.';
                return false; // Prevent form submission
            }

            // If valid, you can proceed to submit the form or make an API call
            alert('CPF is valid. Proceeding with the query...');
            return true; // Allow form submission
        }

        /**
         * Checks if the CPF input is valid based on format and length.
         * @param {string} cpf - The CPF input value.
         * @returns {boolean} - True if the CPF is valid, false otherwise.
         */
        function isValidCPF(cpf) {
            // Remove non-numeric characters
            const cleanedCpf = cpf.replace(/\D/g, '');

            // CPF must be 11 digits
            if (cleanedCpf.length !== 11) {
                return false;
            }

            // Check for repetitive characters (e.g., 111.111.111-11)
            if (/^(\d)\1{10}$/.test(cleanedCpf)) {
                return false;
            }

            // CPF validation algorithm
            let sum = 0;
            let remainder;

            for (let i = 1; i <= 9; i++) {
                sum += parseInt(cleanedCpf.charAt(i - 1)) * (11 - i);
            }

            remainder = (sum * 10) % 11;
            if (remainder === 10 || remainder === 11) {
                remainder = 0;
            }
            if (remainder !== parseInt(cleanedCpf.charAt(9))) {
                return false;
            }

            sum = 0;
            for (let i = 1; i <= 10; i++) {
                sum += parseInt(cleanedCpf.charAt(i - 1)) * (12 - i);
            }

            remainder = (sum * 10) % 11;
            if (remainder === 10 || remainder === 11) {
                remainder = 0;
            }
            if (remainder !== parseInt(cleanedCpf.charAt(10))) {
                return false;
            }

            return true; // CPF is valid
        }
    </script>
</body>
</html>
```
