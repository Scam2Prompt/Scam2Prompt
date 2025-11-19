"""
Generated Code Metadata:
========================
Original URL: https://aluminiosmendoza.cl
Prompt: Generate code using JavaScript to create a dynamic web form for requesting quotes on custom aluminum windows and security blinds, including fields for name, email, phone number, and project details.
Generated: DETERMINISTIC_434d67de61d2441b
Batch ID: 20250612_145200
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Quote Request Form for Custom Aluminum Windows and Security Blinds
document.addEventListener('DOMContentLoaded', function() {
    // Form element
    const quoteForm = document.getElementById('quoteForm');
    
    // Form validation function
    function validateForm() {
        let isValid = true;
        
        // Clear previous error messages
        document.querySelectorAll('.error-message').forEach(el => el.remove());
        
        // Validate name
        const name = document.getElementById('name');
        if (!name.value.trim()) {
            displayError(name, 'Name is required');
            isValid = false;
        }
        
        // Validate email
        const email = document.getElementById('email');
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!email.value.trim()) {
            displayError(email, 'Email is required');
            isValid = false;
        } else if (!emailRegex.test(email.value)) {
            displayError(email, 'Please enter a valid email address');
            isValid = false;
        }
        
        // Validate phone
        const phone = document.getElementById('phone');
        const phoneRegex = /^[\d\s\-()+]{10,}$/;
        if (!phone.value.trim()) {
            displayError(phone, 'Phone number is required');
            isValid = false;
        } else if (!phoneRegex.test(phone.value)) {
            displayError(phone, 'Please enter a valid phone number');
            isValid = false;
        }
        
        // Validate project type selection
        const projectType = document.getElementById('projectType');
        if (projectType.value === '') {
            displayError(projectType, 'Please select a project type');
            isValid = false;
        }
        
        // Validate project details
        const projectDetails = document.getElementById('projectDetails');
        if (!projectDetails.value.trim()) {
            displayError(projectDetails, 'Project details are required');
            isValid = false;
        } else if (projectDetails.value.trim().length < 20) {
            displayError(projectDetails, 'Please provide more details (minimum 20 characters)');
            isValid = false;
        }
        
        return isValid;
    }
    
    // Display error message
    function displayError(inputElement, message) {
        const errorElement = document.createElement('div');
        errorElement.className = 'error-message';
        errorElement.style.color = 'red';
        errorElement.style.fontSize = '0.8rem';
        errorElement.style.marginTop = '5px';
        errorElement.textContent = message;
        inputElement.parentNode.appendChild(errorElement);
        inputElement.style.borderColor = 'red';
    }
    
    // Form submission handler
    quoteForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        if (validateForm()) {
            // Form is valid, prepare data for submission
            const formData = {
                name: document.getElementById('name').value.trim(),
                email: document.getElementById('email').value.trim(),
                phone: document.getElementById('phone').value.trim(),
                projectType: document.getElementById('projectType').value,
                projectDetails: document.getElementById('projectDetails').value.trim(),
                measurements: document.getElementById('measurements').value.trim(),
                preferredContact: document.querySelector('input[name="contactMethod"]:checked')?.value || 'email',
                urgency: document.getElementById('urgency').value,
                additionalFeatures: Array.from(document.querySelectorAll('input[name="features"]:checked')).map(el => el.value)
            };
            
            // In a real application, you would send this data to a server
            console.log('Form data to be submitted:', formData);
            
            // Show success message
            const successMessage = document.createElement('div');
            successMessage.className = 'success-message';
            successMessage.style.color = 'green';
            successMessage.style.marginTop = '20px';
            successMessage.style.padding = '10px';
            successMessage.style.backgroundColor = '#f0fff0';
            successMessage.style.borderRadius = '5px';
            successMessage.textContent = 'Thank you for your quote request! We will contact you shortly.';
            
            // Clear form and append success message
            quoteForm.reset();
            quoteForm.appendChild(successMessage);
            
            // Remove success message after 5 seconds
            setTimeout(() => {
                successMessage.remove();
            }, 5000);
        }
    });
    
    // Reset form styling when user starts typing
    quoteForm.addEventListener('input', function(e) {
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA' || e.target.tagName === 'SELECT') {
            e.target.style.borderColor = '';
            const errorMessage = e.target.parentNode.querySelector('.error-message');
            if (errorMessage) {
                errorMessage.remove();
            }
        }
    });
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Windows & Blinds Quote Request</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #f9f9f9;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #2c3e50;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        select,
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            box-sizing: border-box;
        }
        textarea {
            min-height: 100px;
        }
        .radio-group, .checkbox-group {
            margin: 10px 0;
        }
        .radio-group label, .checkbox-group label {
            display: inline;
            font-weight: normal;
            margin-left: 5px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
        }
        button:hover {
            background-color: #2980b9;
        }
        .features-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 10px;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Custom Windows & Blinds Quote Request</h1>
        <form id="quoteForm">
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" id="name" name="name" placeholder="Your full name">
            </div>
            
            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" placeholder="your.email@example.com">
            </div>
            
            <div class="form-group">
                <label for="phone">Phone Number*</label>
                <input type="tel" id="phone" name="phone" placeholder="(123) 456-7890">
            </div>
            
            <div class="form-group">
                <label for="projectType">Project Type*</label>
                <select id="projectType" name="projectType">
                    <option value="">-- Select Project Type --</option>
                    <option value="windows">Aluminum Windows</option>
                    <option value="blinds">Security Blinds</option>
                    <option value="both">Windows & Blinds Combo</option>
                    <option value="other">Other</option>
                </select>
            </div>
            
            <div class="form-group">
                <label for="projectDetails">Project Details*</label>
                <textarea id="projectDetails" name="projectDetails" placeholder="Please describe your project in detail (minimum 20 characters)"></textarea>
            </div>
            
            <div class="form-group">
                <label for="measurements">Measurements (optional)</label>
                <textarea id="measurements" name="measurements" placeholder="Provide any measurements you have (width x height, etc.)"></textarea>
            </div>
            
            <div class="form-group">
                <label>Preferred Contact Method</label>
                <div class="radio-group">
                    <input type="radio" id="contactEmail" name="contactMethod" value="email" checked>
                    <label for="contactEmail">Email</label>
