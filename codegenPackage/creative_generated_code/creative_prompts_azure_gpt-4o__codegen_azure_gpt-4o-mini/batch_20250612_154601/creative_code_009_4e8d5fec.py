"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://okx-web3-tron-usdt-trc20-000000325.pages.dev
Prompt: Write code to integrate a numeric keypad for entering USDT (TRC-20) amounts in a web application, similar to the design described on the OKX platform.
Generated: DETERMINISTIC_4e8d5fec8c591225
Batch ID: 20250612_154601
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
    <title>USDT Amount Entry</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="container">
        <h1>Enter USDT Amount</h1>
        <div class="input-container">
            <input type="text" id="usdtAmount" placeholder="0.00" readonly />
        </div>
        
        <div class="keypad">
            <button class="key" onclick="appendNumber('1')">1</button>
            <button class="key" onclick="appendNumber('2')">2</button>
            <button class="key" onclick="appendNumber('3')">3</button>
            <button class="key" onclick="appendNumber('4')">4</button>
            <button class="key" onclick="appendNumber('5')">5</button>
            <button class="key" onclick="appendNumber('6')">6</button>
            <button class="key" onclick="appendNumber('7')">7</button>
            <button class="key" onclick="appendNumber('8')">8</button>
            <button class="key" onclick="appendNumber('9')">9</button>
            <button class="key" onclick="clearInput()">C</button>
            <button class="key" onclick="appendNumber('0')">0</button>
            <button class="key" onclick="appendDecimal()">.</button>
        </div>
        
        <button id="submitBtn" onclick="submitAmount()">Submit</button>
        <div id="errorMessage" class="error-message"></div>
    </div>

    <script>
        // Append a number to the input field
        function appendNumber(number) {
            const inputField = document.getElementById("usdtAmount");
            // If the input field is read-only, change it to editable temporarily.
            inputField.readOnly = false;
            // Append the number to the current value
            inputField.value += number;
            inputField.readOnly = true; // Set it back to read-only
        }

        // Append a decimal point to the input field
        function appendDecimal() {
            const inputField = document.getElementById("usdtAmount");
            if (!inputField.value.includes('.')) {
                inputField.readOnly = false;
                inputField.value += '.';
                inputField.readOnly = true;
            }
        }

        // Clear the input field
        function clearInput() {
            const inputField = document.getElementById("usdtAmount");
            inputField.readOnly = false;
            inputField.value = '';
            inputField.readOnly = true;
        }

        // Validate and submit the amount
        function submitAmount() {
            const inputField = document.getElementById("usdtAmount");
            const errorMessage = document.getElementById("errorMessage");
            const amount = parseFloat(inputField.value);

            // Clear previous error messages
            errorMessage.textContent = '';

            // Validate the amount
            if (isNaN(amount) || amount <= 0) {
                errorMessage.textContent = 'Please enter a valid USDT amount.';
                return;
            }

            // Here you would proceed with the amount submission logic, e.g., API call
            console.log(`Submitting amount: ${amount} USDT`);
            // Insert API call or other logic for processing the amount here
        }
    </script>

    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f9f9f9;
        }
        .container {
            text-align: center;
        }
        .input-container {
            margin-bottom: 20px;
        }
        #usdtAmount {
            width: 200px;
            height: 40px;
            font-size: 24px;
            text-align: right;
            margin-bottom: 20px;
        }
        .keypad {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 10px;
            margin-bottom: 20px;
        }
        .key {
            padding: 15px;
            font-size: 18px;
            cursor: pointer;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            transition: background-color 0.3s;
        }
        .key:hover {
            background-color: #0056b3;
        }
        #submitBtn {
            padding: 10px 20px;
            font-size: 18px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        #submitBtn:hover {
            background-color: #218838;
        }
        .error-message {
            color: red;
            margin-top: 10px;
        }
    </style>
</body>
</html>
```
