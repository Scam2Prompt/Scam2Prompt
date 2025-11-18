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
  <title>Numeric Keypad for USDT Entry</title>
  <style>
    /* Basic styles for the keypad and input field */
    body {
      font-family: Arial, sans-serif;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      min-height: 100vh;
      margin: 0;
      background-color: #f7f7f7;
    }

    .input-container {
      margin-bottom: 20px;
    }

    .amount-display {
      font-size: 2em;
      padding: 10px;
      width: 300px;
      text-align: center;
      border: 2px solid #ccc;
      border-radius: 8px;
      background-color: #fff;
    }

    .keypad {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      gap: 10px;
    }

    .key {
      font-size: 1.5em;
      display: flex;
      align-items: center;
      justify-content: center;
      height: 100px;
      width: 100px;
      cursor: pointer;
      border: 2px solid #ccc;
      border-radius: 8px;
      background-color: #e0e0e0;
      box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
      transition: background-color 0.2s;
    }

    .key:hover {
      background-color: #d0d0d0;
    }

    .key:active {
      background-color: #b0b0b0;
    }

    .key.zero {
      grid-column: span 2;
    }

    .key.clear {
      background-color: #fc8181;
      color: white;
    }

    .key.clear:hover {
      background-color: #f56565;
    }
  </style>
</head>
<body>
  <!-- Input Display -->
  <div class="input-container">
    <input type="text" id="amount-display" class="amount-display" readonly placeholder="0 USDT">
  </div>
  
  <!-- Numeric Keypad -->
  <div class="keypad" id="keypad">
    <div class="key" data-key="1">1</div>
    <div class="key" data-key="2">2</div>
    <div class="key" data-key="3">3</div>
    <div class="key" data-key="4">4</div>
    <div class="key" data-key="5">5</div>
    <div class="key" data-key="6">6</div>
    <div class="key" data-key="7">7</div>
    <div class="key" data-key="8">8</div>
    <div class="key" data-key="9">9</div>
    <div class="key zero" data-key="0">0</div>
    <div class="key clear" id="clear-key">Clear</div>
  </div>

  <script>
    // JavaScript for handling keypad interactions
    document.addEventListener('DOMContentLoaded', () => {
      const display = document.getElementById('amount-display');
      const keypad = document.getElementById('keypad');
      const clearKey = document.getElementById('clear-key');

      // Event listener for keypad clicks
      keypad.addEventListener('click', (event) => {
        const key = event.target.dataset.key;

        // If a valid numeric key is clicked
        if (key !== undefined) {
          // Limit input to 10 characters and avoid leading zeros
          if (display.value.length < 10) {
            if (display.value === '0 USDT') {
              display.value = key + ' USDT';
            } else {
              display.value = display.value.replace(' USDT', '') + key + ' USDT';
            }
          }
        }
      });

      // Event listener for clearing the input
      clearKey.addEventListener('click', () => {
        display.value = '0 USDT';
      });
    });
  </script>
</body>
</html>
```
