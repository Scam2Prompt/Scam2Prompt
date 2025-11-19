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
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>محصولات آرایشگاهی - فرم پرسش</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f9f9f9;
            border: 1px solid #ddd;
            border-radius: 5px;
        }
        label {
            margin-top: 10px;
            display: block;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin-top: 5px;
            border: 1px solid #ccc;
            border-radius: 3px;
        }
        button {
            margin-top: 20px;
            padding: 10px 15px;
            background-color: #5cb85c;
            color: white;
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        button:hover {
            background-color: #4cae4c;
        }
    </style>
</head>
<body>

    <h1>پرسش درباره محصولات آرایشگاهی</h1>
    <form id="inquiryForm" action="/submit-inquiry" method="POST">
        <label for="name">نام شما:</label>
        <input type="text" id="name" name="name" required placeholder="نام خود را وارد کنید">

        <label for="email">ایمیل شما:</label>
        <input type="email" id="email" name="email" required placeholder="ایمیل خود را وارد کنید">

        <label for="product">محصول مورد نظر:</label>
        <select id="product" name="product" required>
            <option value="">لطفا انتخاب کنید</option>
            <option value="آینه و کنسول آرایشگاهی">آینه و کنسول آرایشگاهی</option>
            <option value="صندلی انتظار آرایشگاه">صندلی انتظار آرایشگاه</option>
        </select>

        <label for="message">پیام شما:</label>
        <textarea id="message" name="message" required placeholder="پیام خود را وارد کنید"></textarea>

        <button type="submit">ارسال پرسش</button>
    </form>

    <script>
        // Form submission handler
        document.getElementById('inquiryForm').addEventListener('submit', function(event) {
            // Perform client-side validation before submission
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const product = document.getElementById('product').value;
            const message = document.getElementById('message').value;

            if (!name || !email || !product || !message) {
                alert('لطفا تمام فیلدهای الزامی را پر کنید.');
                event.preventDefault(); // Prevent form submission
            }
        });
    </script>

</body>
</html>
```
