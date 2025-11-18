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
  <title>CPF Indemnification Query</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }
    .form-container {
      max-width: 400px;
      margin: auto;
    }
    label {
      display: block;
      margin: 10px 0 5px;
    }
    input {
      width: 100%;
      padding: 8px;
      margin-bottom: 10px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }
    .error-message {
      color: red;
      font-size: 0.9em;
    }
    button {
      padding: 10px 15px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }
    button:hover {
      background-color: #0056b3;
    }
  </style>
</head>
<body>

<div class="form-container">
  <h2>Query Indemnification Status</h2>
  <form id="cpfForm">
    <label for="cpf">Enter your CPF (Brazilian identification number):</label>
    <input type="text" id="cpf" name="cpf" placeholder="Format: XXX.XXX.XXX-XX" required>
    <p class="error-message" id="cpfError"></p>
    <button type="submit">Check Status</button>
  </form>
</div>

<script>
  /**
   * Function to validate CPF input format.
   * CPF format: XXX.XXX.XXX-XX (11 digits with dots and dash).
   * @param {string} cpf - The CPF string to validate.
   * @returns {boolean} - True if CPF format is valid, false otherwise.
   */
  function validateCPF(cpf) {
    // Regular expression to match CPF pattern
    const cpfRegex = /^\d{3}\.\d{3}\.\d{3}-\d{2}$/;
    return cpfRegex.test(cpf);
  }

  // Get references to form and input elements
  const cpfForm = document.getElementById('cpfForm');
  const cpfInput = document.getElementById('cpf');
  const cpfError = document.getElementById('cpfError');

  // Add event listener for form submission
  cpfForm.addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent default form submission behavior

    // Get CPF input value
    const cpfValue = cpfInput.value.trim();

    // Validate CPF format
    if (!validateCPF(cpfValue)) {
      cpfError.textContent = 'Invalid CPF format. Please enter in XXX.XXX.XXX-XX format.';
      return;
    }

    // Clear error message and simulate query
    cpfError.textContent = '';
    alert(`CPF ${cpfValue} is valid. Querying indemnification status...`);

    // Normally, here you would make an API call to query the indemnification status
  });

  // Add event listener for input change to clear error message
  cpfInput.addEventListener('input', function() {
    cpfError.textContent = '';
  });
</script>

</body>
</html>
```
