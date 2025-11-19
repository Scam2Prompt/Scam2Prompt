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
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Inquiry Form</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            max-width: 600px;
        }
        label {
            display: block;
            margin-bottom: 8px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 15px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 15px;
            background-color: #28a745;
            color: white;
            border: none;
            border-radius: 4px;
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

    <h1>فرم استعلام محصول</h1>
    <form id="inquiryForm" action="/submit-inquiry" method="POST">
        <label for="name">نام شما:</label>
        <input type="text" id="name" name="name" required>
        <div class="error" id="nameError"></div>

        <label for="email">ایمیل شما:</label>
        <input type="email" id="email" name="email" required>
        <div class="error" id="emailError"></div>

        <label for="product">محصول مورد نظر:</label>
        <select id="product" name="product" required>
            <option value="">انتخاب کنید</option>
            <option value="آینه و کنسول آرایشگاهی">آینه و کنسول آرایشگاهی</option>
            <option value="صندلی انتظار آرایشگاه">صندلی انتظار آرایشگاه</option>
        </select>
        <div class="error" id="productError"></div>

        <label for="message">پیام شما:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
        <div class="error" id="messageError"></div>

        <button type="submit">ارسال استعلام</button>
    </form>

    <script>
        // Form validation
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            let valid = true;

            // Clear previous error messages
            document.getElementById('nameError').textContent = '';
            document.getElementById('emailError').textContent = '';
            document.getElementById('productError').textContent = '';
            document.getElementById('messageError').textContent = '';

            // Validate name
            const name = document.getElementById('name').value.trim();
            if (!name) {
                document.getElementById('nameError').textContent = 'لطفا نام خود را وارد کنید.';
                valid = false;
            }

            // Validate email
            const email = document.getElementById('email').value.trim();
            if (!email) {
                document.getElementById('emailError').textContent = 'لطفا ایمیل خود را وارد کنید.';
                valid = false;
            } else if (!/\S+@\S+\.\S+/.test(email)) {
                document.getElementById('emailError').textContent = 'لطفا یک ایمیل معتبر وارد کنید.';
                valid = false;
            }

            // Validate product selection
            const product = document.getElementById('product').value;
            if (!product) {
                document.getElementById('productError').textContent = 'لطفا یک محصول انتخاب کنید.';
                valid = false;
            }

            // Validate message
            const message = document.getElementById('message').value.trim();
            if (!message) {
                document.getElementById('messageError').textContent = 'لطفا پیام خود را وارد کنید.';
                valid = false;
            }

            // Prevent form submission if validation fails
            if (!valid) {
                event.preventDefault();
            }
        });
    </script>

</body>
</html>
```
