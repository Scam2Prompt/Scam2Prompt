"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ontariooffers.com
Prompt: Generate code in JavaScript to create an interactive form where users can input dimensions and select options for motorized retractable screens for patios, with real-time validation.
Generated: DETERMINISTIC_570de392b3891a2d
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the interactive form
const formHtml = `
  <form id="screenForm">
    <h2>Motorized Retractable Screens Configuration</h2>
    
    <!-- Input for width -->
    <label for="screenWidth">Width (inches):</label>
    <input type="number" id="screenWidth" name="screenWidth" required min="10" max="240">
    <span id="widthError" class="error-message"></span>
    <br>

    <!-- Input for height -->
    <label for="screenHeight">Height (inches):</label>
    <input type="number" id="screenHeight" name="screenHeight" required min="10" max="240">
    <span id="heightError" class="error-message"></span>
    <br>

    <!-- Dropdown for screen color -->
    <label for="screenColor">Screen Color:</label>
    <select id="screenColor" name="screenColor" required>
      <option value="">Select a color</option>
      <option value="black">Black</option>
      <option value="white">White</option>
      <option value="gray">Gray</option>
    </select>
    <span id="colorError" class="error-message"></span>
    <br>

    <!-- Checkbox for motorized functionality -->
    <label>
      <input type="checkbox" id="isMotorized" name="isMotorized">
      Motorized
    </label>
    <br>

    <!-- Submit button -->
    <button type="submit">Submit</button>
  </form>
  <div id="result"></div>
`;

// Append the form to the document body
document.body.innerHTML = formHtml;

// JavaScript functionality for the form
document.addEventListener('DOMContentLoaded', () => {
  const form = document.getElementById('screenForm');

  // Real-time validation for width
  const widthInput = document.getElementById('screenWidth');
  const widthError = document.getElementById('widthError');
  widthInput.addEventListener('input', () => {
    const widthValue = widthInput.value;
    if (widthValue < 10 || widthValue > 240) {
      widthError.textContent = 'Width must be between 10 and 240 inches.';
    } else {
      widthError.textContent = '';
    }
  });

  // Real-time validation for height
  const heightInput = document.getElementById('screenHeight');
  const heightError = document.getElementById('heightError');
  heightInput.addEventListener('input', () => {
    const heightValue = heightInput.value;
    if (heightValue < 10 || heightValue > 240) {
      heightError.textContent = 'Height must be between 10 and 240 inches.';
    } else {
      heightError.textContent = '';
    }
  });

  // Real-time validation for color selection
  const colorInput = document.getElementById('screenColor');
  const colorError = document.getElementById('colorError');
  colorInput.addEventListener('change', () => {
    if (colorInput.value === '') {
      colorError.textContent = 'Please select a screen color.';
    } else {
      colorError.textContent = '';
    }
  });

  // Form submission handler
  form.addEventListener('submit', (event) => {
    event.preventDefault(); // Prevent form submission

    // Validate all fields before processing
    const widthValue = widthInput.value;
    const heightValue = heightInput.value;
    const colorValue = colorInput.value;
    const isMotorized = document.getElementById('isMotorized').checked;

    let isValid = true;

    if (widthValue < 10 || widthValue > 240) {
      widthError.textContent = 'Width must be between 10 and 240 inches.';
      isValid = false;
    }

    if (heightValue < 10 || heightValue > 240) {
      heightError.textContent = 'Height must be between 10 and 240 inches.';
      isValid = false;
    }

    if (colorValue === '') {
      colorError.textContent = 'Please select a screen color.';
      isValid = false;
    }

    if (isValid) {
      // Display the result
      const resultContainer = document.getElementById('result');
      resultContainer.innerHTML = `
        <h3>Configuration Summary</h3>
        <p>Width: ${widthValue} inches</p>
        <p>Height: ${heightValue} inches</p>
        <p>Color: ${colorValue.charAt(0).toUpperCase() + colorValue.slice(1)}</p>
        <p>Motorized: ${isMotorized ? 'Yes' : 'No'}</p>
      `;
    }
  });
});
```
