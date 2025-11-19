"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Write a sample HTML form for users to submit inquiries about specific products like "آینه و کنسول آرایشگاهی" and "صندلی انتظار آرایشگاه" with validation for required fields.
Generated: DETERMINISTIC_b9b7e759d5e820ad
Batch ID: 20250612_162325
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
    <title>Product Inquiry Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
        }
        form {
            max-width: 600px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input, textarea, select, button {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
        .error {
            color: red;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

<form id="productInquiryForm">
    <h2>Product Inquiry Form</h2>
    
    <!-- Name Field -->
    <label for="name">Full Name <span class="error" id="nameError"></span></label>
    <input type="text" id="name" name="name" placeholder="Enter your name" required>
    
    <!-- Email Field -->
    <label for="email">Email Address <span class="error" id="emailError"></span></label>
    <input type="email" id="email" name="email" placeholder="Enter your email" required>
    
    <!-- Phone Field -->
    <label for="phone">Phone Number <span class="error" id="phoneError"></span></label>
    <input type="tel" id="phone" name="phone" placeholder="Enter your phone number" required>
    
    <!-- Product Selection -->
    <label for="product">Product <span class="error" id="productError"></span></label>
    <select id="product" name="product" required>
        <option value="">Select a product</option>
        <option value="آینه و کنسول آرایشگاهی">آینه و کنسول آرایشگاهی</option>
        <option value="صندلی انتظار آرایشگاه">صندلی انتظار آرایشگاه</option>
    </select>
    
    <!-- Inquiry Message -->
    <label for="message">Inquiry Message <span class="error" id="messageError"></span></label>
    <textarea id="message" name="message" placeholder="Enter your inquiry details" required></textarea>
    
    <!-- Submit Button -->
    <button type="submit">Submit Inquiry</button>
</form>

<script>
    // Add simple client-side validation
    document.getElementById('productInquiryForm').addEventListener('submit', function(event) {
        // Prevent the form from submitting
        event.preventDefault();
        
        // Clear any existing error messages
        const errors = document.querySelectorAll('.error');
        errors.forEach(error => error.textContent = '');
        
        // Validate fields
        let isValid = true;
        
        const name = document.getElementById('name');
        if (name.value.trim() === '') {
            isValid = false;
            document.getElementById('nameError').textContent = 'Name is required.';
        }
        
        const email = document.getElementById('email');
        if (email.value.trim() === '') {
            isValid = false;
            document.getElementById('emailError').textContent = 'Email is required.';
        } else if (!/\S+@\S+\.\S+/.test(email.value)) {
            isValid = false;
            document.getElementById('emailError').textContent = 'Invalid email format.';
        }
        
        const phone = document.getElementById('phone');
        if (phone.value.trim() === '') {
            isValid = false;
            document.getElementById('phoneError').textContent = 'Phone number is required.';
        }
        
        const product = document.getElementById('product');
        if (product.value === '') {
            isValid = false;
            document.getElementById('productError').textContent = 'Please select a product.';
        }
        
        const message = document.getElementById('message');
        if (message.value.trim() === '') {
            isValid = false;
            document.getElementById('messageError').textContent = 'Message is required.';
        }
        
        // Submit form if valid
        if (isValid) {
            alert('Inquiry submitted successfully!');
            // You can add code here to send the form data to the server
            event.target.submit();
        }
    });
</script>

</body>
</html>
```
