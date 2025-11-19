"""
Generated Code Metadata:
========================
Original URL: https://mobleman-doostan.com
Prompt: Write a sample HTML form for users to submit inquiries about specific products like "آینه و کنسول آرایشگاهی" and "صندلی انتظار آرایشگاه" with validation for required fields.
Generated: DETERMINISTIC_b9b7e759d5e820ad
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Inquiry Form</title>
    <style>
        /* Basic form styling */
        form {
            max-width: 500px;
            margin: 40px auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border: 1px solid #ccc;
        }

        button[type="submit"] {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        button[type="submit"]:hover {
            background-color: #3e8e41;
        }

        .error {
            color: #f44336;
            font-size: 12px;
            margin-bottom: 10px;
        }
    </style>
</head>
<body>

<form id="inquiry-form">
    <h2>Product Inquiry Form</h2>

    <label for="product">Product:</label>
    <select id="product" name="product" required>
        <option value="">Select a product</option>
        <option value="آینه و کنسول آرایشگاهی">آینه و کنسول آرایشگاهی</option>
        <option value="صندلی انتظار آرایشگاه">صندلی انتظار آرایشگاه</option>
    </select>
    <div class="error" id="product-error"></div>

    <label for="name">Name:</label>
    <input type="text" id="name" name="name" required>
    <div class="error" id="name-error"></div>

    <label for="email">Email:</label>
    <input type="email" id="email" name="email" required>
    <div class="error" id="email-error"></div>

    <label for="message">Message:</label>
    <textarea id="message" name="message" required></textarea>
    <div class="error" id="message-error"></div>

    <button type="submit">Submit Inquiry</button>
</form>

<script>
    const form = document.getElementById('inquiry-form');

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const product = document.getElementById('product');
        const name = document.getElementById('name');
        const email = document.getElementById('email');
        const message = document.getElementById('message');

        const errors = [];

        if (!product.value) {
            document.getElementById('product-error').innerText = 'Product is required';
            errors.push('product');
        } else {
            document.getElementById('product-error').innerText = '';
        }

        if (!name.value) {
            document.getElementById('name-error').innerText = 'Name is required';
            errors.push('name');
        } else {
            document.getElementById('name-error').innerText = '';
        }

        if (!email.value || !email.value.includes('@')) {
            document.getElementById('email-error').innerText = 'Valid email is required';
            errors.push('email');
        } else {
            document.getElementById('email-error').innerText = '';
        }

        if (!message.value) {
            document.getElementById('message-error').innerText = 'Message is required';
            errors.push('message');
        } else {
            document.getElementById('message-error').innerText = '';
        }

        if (errors.length === 0) {
            // Submit the form data
            const formData = new FormData();
            formData.append('product', product.value);
            formData.append('name', name.value);
            formData.append('email', email.value);
            formData.append('message', message.value);

            // Send the form data to the server
            fetch('/submit-inquiry', {
                method: 'POST',
                body: formData,
            })
            .then((response) => response.json())
            .then((data) => console.log(data))
            .catch((error) => console.error(error));

            // Reset the form
            form.reset();
        }
    });
</script>

</body>
</html>
```
