"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://alshehhi.net
Prompt: Write code to integrate a service request form into a website, ensuring compatibility with Arabic-language input, as seen in the "طلب خدمة" feature on Alshehhi.Net.
Generated: DETERMINISTIC_bedd36db3f6645cf
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>طلب خدمة</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
            direction: rtl; /* Ensures proper alignment for Arabic language */
            text-align: right; /* Aligns text to the right */
            margin: 0;
            padding: 0;
            background-color: #f4f4f9;
        }
        .form-container {
            max-width: 600px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
        }
        .form-container h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea, button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            border: 1px solid #cccccc;
            border-radius: 5px;
        }
        textarea {
            resize: none; /* Prevent resizing for better UX */
        }
        button {
            background-color: #007bff;
            color: #ffffff;
            font-weight: bold;
            cursor: pointer;
            border: none;
        }
        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h1>طلب خدمة</h1>
        <form id="serviceForm" action="/submit-request" method="POST">
            <!-- Service Name -->
            <div class="form-group">
                <label for="serviceName">اسم الخدمة</label>
                <input type="text" id="serviceName" name="serviceName" required placeholder="أدخل اسم الخدمة">
            </div>

            <!-- Full Name -->
            <div class="form-group">
                <label for="fullName">الاسم الكامل</label>
                <input type="text" id="fullName" name="fullName" required placeholder="أدخل اسمك الكامل">
            </div>

            <!-- Email -->
            <div class="form-group">
                <label for="email">البريد الإلكتروني</label>
                <input type="email" id="email" name="email" required placeholder="أدخل بريدك الإلكتروني">
            </div>

            <!-- Phone Number -->
            <div class="form-group">
                <label for="phone">رقم الهاتف</label>
                <input type="tel" id="phone" name="phone" required placeholder="أدخل رقم هاتفك">
            </div>

            <!-- Service Description -->
            <div class="form-group">
                <label for="description">وصف الخدمة</label>
                <textarea id="description" name="description" rows="4" required placeholder="أدخل وصف الخدمة المطلوبة"></textarea>
            </div>

            <!-- Submit Button -->
            <button type="submit">إرسال الطلب</button>
        </form>
    </div>

    <script>
        // Client-side form validation
        document.getElementById('serviceForm').addEventListener('submit', function(event) {
            try {
                // Fetch form inputs
                const serviceName = document.getElementById('serviceName').value.trim();
                const fullName = document.getElementById('fullName').value.trim();
                const email = document.getElementById('email').value.trim();
                const phone = document.getElementById('phone').value.trim();
                const description = document.getElementById('description').value.trim();

                // Basic validation checks
                if (!serviceName || !fullName || !email || !phone || !description) {
                    alert('يرجى ملء جميع الحقول المطلوبة.');
                    event.preventDefault(); // Prevent form submission
                    return;
                }

                // Valid email regex
                const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                if (!emailRegex.test(email)) {
                    alert('يرجى إدخال بريد إلكتروني صالح.');
                    event.preventDefault();
                    return;
                }

                // Valid phone number regex (basic check)
                const phoneRegex = /^[0-9\-\+]{9,15}$/;
                if (!phoneRegex.test(phone)) {
                    alert('يرجى إدخال رقم هاتف صالح.');
                    event.preventDefault();
                    return;
                }

                // If validation passes, allow form submission
                alert('تم إرسال الطلب بنجاح!');
            } catch (error) {
                // Catch and log any errors
                console.error('Error during form submission:', error);
                alert('حدث خطأ أثناء إرسال الطلب. يرجى المحاولة مرة أخرى.');
                event.preventDefault();
            }
        });
    </script>
</body>
</html>
```
