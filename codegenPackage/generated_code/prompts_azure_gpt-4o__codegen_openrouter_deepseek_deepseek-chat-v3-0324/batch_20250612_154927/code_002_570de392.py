"""
Generated Code Metadata:
========================
Original URL: https://ontariooffers.com
Prompt: Generate code in JavaScript to create an interactive form where users can input dimensions and select options for motorized retractable screens for patios, with real-time validation.
Generated: DETERMINISTIC_570de392b3891a2d
Batch ID: 20250612_154927
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Interactive form for motorized retractable screens with real-time validation
 */

document.addEventListener('DOMContentLoaded', function() {
    // Form elements
    const form = document.getElementById('screenForm');
    const widthInput = document.getElementById('width');
    const heightInput = document.getElementById('height');
    const screenTypeSelect = document.getElementById('screenType');
    const colorSelect = document.getElementById('color');
    const motorTypeSelect = document.getElementById('motorType');
    const remoteOption = document.getElementById('remoteOption');
    const warrantySelect = document.getElementById('warranty');
    const submitBtn = document.getElementById('submitBtn');
    const priceDisplay = document.getElementById('priceDisplay');
    const errorContainer = document.getElementById('errorContainer');

    // Price calculation variables
    const basePrice = 500;
    const pricePerSqFt = 15;
    const screenTypePrices = {
        standard: 0,
        premium: 200,
        solar: 350
    };
    const motorTypePrices = {
        basic: 0,
        quiet: 150,
        premium: 300
    };
    const remotePrice = 75;
    const warrantyPrices = {
        '1-year': 0,
        '3-year': 100,
        '5-year': 200
    };

    // Initialize form validation
    initFormValidation();

    // Event listeners for real-time validation and price calculation
    [widthInput, heightInput, screenTypeSelect, colorSelect, motorTypeSelect, remoteOption, warrantySelect].forEach(element => {
        element.addEventListener('input', validateForm);
        element.addEventListener('change', calculatePrice);
    });

    // Form submission handler
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        if (validateForm()) {
            // In a real application, you would submit the form data here
            alert('Form submitted successfully!');
        }
    });

    /**
     * Initialize form validation
     */
    function initFormValidation() {
        // Set initial validation states
        validateForm();
        calculatePrice();
    }

    /**
     * Validate form inputs in real-time
     * @returns {boolean} True if form is valid, false otherwise
     */
    function validateForm() {
        let isValid = true;
        clearErrors();

        // Validate width
        const width = parseFloat(widthInput.value);
        if (isNaN(width) || width <= 0 || width > 20) {
            showError('width', 'Please enter a valid width between 1 and 20 feet');
            isValid = false;
        }

        // Validate height
        const height = parseFloat(heightInput.value);
        if (isNaN(height) || height <= 0 || height > 12) {
            showError('height', 'Please enter a valid height between 1 and 12 feet');
            isValid = false;
        }

        // Validate screen type
        if (!screenTypeSelect.value) {
            showError('screenType', 'Please select a screen type');
            isValid = false;
        }

        // Validate color
        if (!colorSelect.value) {
            showError('color', 'Please select a color');
            isValid = false;
        }

        // Validate motor type
        if (!motorTypeSelect.value) {
            showError('motorType', 'Please select a motor type');
            isValid = false;
        }

        // Update submit button state
        submitBtn.disabled = !isValid;
        return isValid;
    }

    /**
     * Display an error message for a specific field
     * @param {string} fieldId - The ID of the field with the error
     * @param {string} message - The error message to display
     */
    function showError(fieldId, message) {
        const field = document.getElementById(fieldId);
        const errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.textContent = message;
        errorElement.id = `${fieldId}Error`;
        
        // Insert error message after the field
        field.parentNode.insertBefore(errorElement, field.nextSibling);
        
        // Highlight the field
        field.classList.add('error');
    }

    /**
     * Clear all error messages and styling
     */
    function clearErrors() {
        // Remove all error messages
        const errorMessages = document.querySelectorAll('.error-message');
        errorMessages.forEach(msg => msg.remove());
        
        // Remove error styling from all fields
        const errorFields = document.querySelectorAll('.error');
        errorFields.forEach(field => field.classList.remove('error'));
    }

    /**
     * Calculate and display the total price based on form inputs
     */
    function calculatePrice() {
        if (!validateForm()) return;

        const width = parseFloat(widthInput.value);
        const height = parseFloat(heightInput.value);
        const area = width * height;
        
        // Calculate base price
        let totalPrice = basePrice + (area * pricePerSqFt);
        
        // Add screen type price
        totalPrice += screenTypePrices[screenTypeSelect.value] || 0;
        
        // Add motor type price
        totalPrice += motorTypePrices[motorTypeSelect.value] || 0;
        
        // Add remote option price
        if (remoteOption.checked) {
            totalPrice += remotePrice;
        }
        
        // Add warranty price
        totalPrice += warrantyPrices[warrantySelect.value] || 0;
        
        // Display formatted price
        priceDisplay.textContent = `$${totalPrice.toFixed(2)}`;
    }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Motorized Retractable Screens</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input, select {
            width: 100%;
            padding: 8px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        input[type="checkbox"] {
            width: auto;
        }
        .error {
            border-color: #ff0000;
        }
        .error-message {
            color: #ff0000;
            font-size: 0.8em;
            margin-top: 5px;
        }
        #priceDisplay {
            font-size: 1.5em;
            font-weight: bold;
            margin: 20px 0;
            color: #0066cc;
        }
        button {
            background-color: #0066cc;
            color: white;
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:disabled {
            background-color: #cccccc;
            cursor: not-allowed;
        }
    </style>
</head>
<body>
    <h1>Motorized Retractable Screen Configuration</h1>
    <form id="screenForm">
        <div class="form-group">
            <label for="width">Width (feet)</label>
            <input type="number" id="width" name="width" min="1" max="20" step="0.1" required>
        </div>
        
        <div class="form-group">
            <label for="height">Height (feet)</label>
            <input type="number" id="height" name="height" min="1" max="12" step="0.1" required>
        </div>
        
        <div class="form-group">
            <label for="screenType">Screen Type</label>
            <select id="screenType" name="screenType" required>
                <option value="">Select a screen type</option>
                <option value="standard">Standard Mesh</option>
                <option value="premium">Premium Fine Mesh</option>
                <option value="solar">Solar Screen</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="color">Color</label>
            <select id="color" name="color" required>
                <option value="">Select a color</option>
                <option value="black">Black</option>
                <option value="charcoal">Charcoal</option>
                <option value="bronze">Bronze</option>
                <option value="gray">Gray</option>
            </select>
        </div>
        
        <div class="form-group">
            <label for="motorType">Motor Type</label>
            <select id="motorType" name="motorType" required>
                <option value="">Select a motor type</option>
                <option value="basic">Basic Motor</option>
                <option value="quiet">Quiet Motor</option>
                <option value="premium">Premium Quiet Motor</option>
            </select>
        </div>
        
        <div class="form-group">
            <label>
                <input type="checkbox" id="remoteOption" name="remoteOption">
                Include Remote Control (+$75)
            </label>
        </div
