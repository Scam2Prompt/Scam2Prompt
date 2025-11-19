"""
Generated Code Metadata:
========================
Original URL: https://hnu.co.id
Prompt: Write a sample HTML form for users to submit questions about herbal supplements, similar to the FAQ section on Habbasyi Niaga Utama's website, focusing on Habbatussauda and its uses.
Generated: DETERMINISTIC_10c817ca2bdca759
Batch ID: 20250612_164000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready HTML form for submitting questions about herbal supplements:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Herbal Supplements FAQ - Submit Your Question</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        .form-container {
            background-color: #f9f9f9;
            border-radius: 8px;
            padding: 25px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c5e1a;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: bold;
        }
        input[type="text"],
        input[type="email"],
        textarea,
        select {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        textarea {
            height: 150px;
            resize: vertical;
        }
        .required {
            color: #e74c3c;
        }
        .submit-btn {
            background-color: #2c5e1a;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        .submit-btn:hover {
            background-color: #1e3f12;
        }
        .error-message {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
            display: none;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>Herbal Supplements Question Form</h1>
        <form id="faqForm" action="/submit-question" method="POST">
            <div class="form-group">
                <label for="name">Full Name <span class="required">*</span></label>
                <input type="text" id="name" name="name" required>
                <div id="name-error" class="error-message">Please enter your name</div>
            </div>

            <div class="form-group">
                <label for="email">Email Address <span class="required">*</span></label>
                <input type="email" id="email" name="email" required>
                <div id="email-error" class="error-message">Please enter a valid email address</div>
            </div>

            <div class="form-group">
                <label for="product">Product Interest</label>
                <select id="product" name="product">
                    <option value="">Select a product (optional)</option>
                    <option value="habbatussauda">Habbatussauda (Black Seed)</option>
                    <option value="honey">Pure Honey</option>
                    <option value="zamzam">Zamzam Water</option>
                    <option value="other">Other Herbal Products</option>
                </select>
            </div>

            <div class="form-group">
                <label for="question">Your Question <span class="required">*</span></label>
                <textarea id="question" name="question" required placeholder="Please ask your question about herbal supplements, dosage, benefits, or any related topic..."></textarea>
                <div id="question-error" class="error-message">Please enter your question</div>
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" name="subscribe" checked> Subscribe to our newsletter for health tips and product updates
                </label>
            </div>

            <button type="submit" class="submit-btn">Submit Question</button>
        </form>
    </div>

    <script>
        document.getElementById('faqForm').addEventListener('submit', function(e) {
            let isValid = true;
            
            // Validate name
            const name = document.getElementById('name');
            if (!name.value.trim()) {
                document.getElementById('name-error').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('name-error').style.display = 'none';
            }
            
            // Validate email
            const email = document.getElementById('email');
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailRegex.test(email.value)) {
                document.getElementById('email-error').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('email-error').style.display = 'none';
            }
            
            // Validate question
            const question = document.getElementById('question');
            if (!question.value.trim()) {
                document.getElementById('question-error').style.display = 'block';
                isValid = false;
            } else {
                document.getElementById('question-error').style.display = 'none';
            }
            
            if (!isValid) {
                e.preventDefault();
            }
        });
    </script>
</body>
</html>
```
