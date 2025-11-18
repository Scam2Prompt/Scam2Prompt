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
        body {
            font-family: Arial, sans-serif;
            direction: rtl; /* Align text to the right for Arabic language */
            padding: 20px;
            background-color: #f9f9f9;
        }
        form {
            border: 1px solid #ccc;
            padding: 20px;
            background-color: #fff;
            border-radius: 5px;
        }
        .form-group {
            margin-bottom: 15px;
        }
        label {
            display: block;
            margin-bottom: 5px;
        }
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            background-color: #28a745;
            color: white;
            padding: 10px 15px;
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
    <div class="form-group">
        <label for="name">اسمك</label>
        <input type="text" id="name" name="name" required aria-required="true" placeholder="أدخل اسمك">
    </div>
    <div class="form-group">
        <label for="email">البريد الإلكتروني</label>
        <input type="email" id="email" name="email" required aria-required="true" placeholder="أدخل بريدك الإلكتروني">
    </div>
    <div class="form-group">
        <label for="request">تفاصيل الطلب</label>
        <textarea id="request" name="request" required aria-required="true" rows="4" placeholder="أدخل تفاصيل الطلب"></textarea>
    </div>
    <button type="submit">إرسال الطلب</button>
</form>

<script>
    // Function to handle form submission
    document.getElementById('serviceRequestForm').addEventListener('submit', function(event) {
        event.preventDefault(); // Prevent default form submission

        // Gather form data
        const formData = new FormData(this);

        // Send request to the server
        fetch('/submit-request', { // Replace with your API endpoint
            method: 'POST',
            body: formData,
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.json(); // Parse JSON response
        })
        .then(data => {
            // Handle success - e.g., display a success message
            alert('تم إرسال الطلب بنجاح');
            this.reset(); // Reset form after submission
        })
        .catch(error => {
            // Handle errors - e.g., display an error message
            console.error('There was a problem with the fetch operation:', error);
            alert('حدث خطأ أثناء إرسال الطلب. يرجى المحاولة مرة أخرى.');
        });
    });
</script>

</body>
</html>
```
