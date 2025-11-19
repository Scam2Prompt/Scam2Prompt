"""
Generated Code Metadata:
========================
Original URL: https://alshehhi.net
Prompt: Write code to integrate a service request form into a website, ensuring compatibility with Arabic-language input, as seen in the "طلب خدمة" feature on Alshehhi.Net.
Generated: DETERMINISTIC_bedd36db3f6645cf
Batch ID: 20250612_151553
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>طلب خدمة</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f5f5f5;
            margin: 0;
            padding: 20px;
            color: #333;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0,0,0,0.1);
        }
        h1 {
            color: #2c3e50;
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
        input, textarea, select {
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
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            display: block;
            width: 100%;
            transition: background-color 0.3s;
        }
        button:hover {
            background-color: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            background-color: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            text-align: center;
            display: none;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>طلب خدمة</h1>
        
        <div id="successMessage" class="success-message">
            تم إرسال طلب الخدمة بنجاح. سنتواصل معك قريبًا.
        </div>
        
        <form id="serviceRequestForm">
            <div class="form-group">
                <label for="name">الاسم الكامل</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">البريد الإلكتروني</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="phone">رقم الهاتف</label>
                <input type="tel" id="phone" name="phone" required>
                <div id="phoneError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="service">نوع الخدمة</label>
                <select id="service" name="service" required>
                    <option value="">اختر الخدمة</option>
                    <option value="web-development">تطوير مواقع الويب</option>
                    <option value="mobile-app">تطبيقات الجوال</option>
                    <option value="graphic-design">تصميم جرافيك</option>
                    <option value="consulting">استشارات تقنية</option>
                    <option value="other">خدمة أخرى</option>
                </select>
                <div id="serviceError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="details">تفاصيل الطلب</label>
                <textarea id="details" name="details" required></textarea>
                <div id="detailsError" class="error"></div>
            </div>
            
            <button type="submit">إرسال الطلب</button>
        </form>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const form = document.getElementById('serviceRequestForm');
            const successMessage = document.getElementById('successMessage');
            
            form.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                document.querySelectorAll('.error').forEach(el => el.textContent = '');
                
                // Validate form
                let isValid = true;
                
                const name = document.getElementById('name').value.trim();
                if (name === '') {
                    document.getElementById('nameError').textContent = 'الرجاء إدخال الاسم الكامل';
                    isValid = false;
                }
                
                const email = document.getElementById('email').value.trim();
                if (email === '') {
                    document.getElementById('emailError').textContent = 'الرجاء إدخال البريد الإلكتروني';
                    isValid = false;
                } else if (!isValidEmail(email)) {
                    document.getElementById('emailError').textContent = 'البريد الإلكتروني غير صالح';
                    isValid = false;
                }
                
                const phone = document.getElementById('phone').value.trim();
                if (phone === '') {
                    document.getElementById('phoneError').textContent = 'الرجاء إدخال رقم الهاتف';
                    isValid = false;
                }
                
                const service = document.getElementById('service').value;
                if (service === '') {
                    document.getElementById('serviceError').textContent = 'الرجاء اختيار نوع الخدمة';
                    isValid = false;
                }
                
                const details = document.getElementById('details').value.trim();
                if (details === '') {
                    document.getElementById('detailsError').textContent = 'الرجاء إدخال تفاصيل الطلب';
                    isValid = false;
                }
                
                if (isValid) {
                    // Simulate form submission (replace with actual AJAX call)
                    setTimeout(() => {
                        form.reset();
                        successMessage.style.display = 'block';
                        setTimeout(() => {
                            successMessage.style.display = 'none';
                        }, 5000);
                    }, 1000);
                }
            });
            
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
        });
    </script>
</body>
</html>
```
