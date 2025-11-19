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
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>طلب خدمة</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            direction: rtl; /* Right-to-left for Arabic */
            padding: 20px;
            background-color: #f4f4f4;
        }
        form {
            background: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #218838;
        }
    </style>
</head>
<body>

    <h1>طلب خدمة</h1>
    <form id="serviceRequestForm">
        <label for="name">الاسم:</label>
        <input type="text" id="name" name="name" required placeholder="أدخل اسمك">

        <label for="email">البريد الإلكتروني:</label>
        <input type="email" id="email" name="email" required placeholder="أدخل بريدك الإلكتروني">

        <label for="service">الخدمة المطلوبة:</label>
        <textarea id="service" name="service" required placeholder="أدخل تفاصيل الخدمة المطلوبة"></textarea>

        <button type="submit">إرسال الطلب</button>
    </form>

    <div id="responseMessage" style="margin-top: 20px;"></div>

    <script>
        // Function to handle form submission
        document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent default form submission

            // Gather form data
            const formData = new FormData(this);

            // Send data to the server
            fetch('/submit-service-request', {
                method: 'POST',
                body: formData
            })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Display success message
                document.getElementById('responseMessage').innerText = 'تم إرسال الطلب بنجاح!';
                this.reset(); // Reset the form
            })
            .catch(error => {
                // Display error message
                document.getElementById('responseMessage').innerText = 'حدث خطأ: ' + error.message;
            });
        });
    </script>

</body>
</html>
```
