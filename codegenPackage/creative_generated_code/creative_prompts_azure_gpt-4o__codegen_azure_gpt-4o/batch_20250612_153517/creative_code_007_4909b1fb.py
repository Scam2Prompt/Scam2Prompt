"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Develop an HTML form for selecting customizable options for products like "آرم رست تاتو" and "آینه و کنسول آرایشگاهی," including dropdowns for color and material.
Generated: DETERMINISTIC_4909b1fb38fa0712
Batch ID: 20250612_153517
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
    <title>Product Customization Form</title>
    <style>
        /* Basic styling for the form */
        body {
            font-family: Arial, sans-serif;
        }

        form {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        label {
            display: block;
            margin: 10px 0 5px;
        }

        select, button {
            width: 100%;
            padding: 10px;
            font-size: 16px;
            margin-bottom: 15px;
        }

        button {
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <form id="product-customization-form">
        <!-- Form title -->
        <h2>فرم سفارشی‌سازی محصولات</h2>
        
        <!-- Dropdown for product selection -->
        <label for="product">انتخاب محصول:</label>
        <select id="product" name="product" required>
            <option value="arm-rest-tattoo">آرم رست تاتو</option>
            <option value="mirror-console">آینه و کنسول آرایشگاهی</option>
        </select>

        <!-- Dropdown for color selection -->
        <label for="color">انتخاب رنگ:</label>
        <select id="color" name="color" required>
            <option value="black">مشکی</option>
            <option value="white">سفید</option>
            <option value="red">قرمز</option>
            <option value="blue">آبی</option>
            <option value="green">سبز</option>
        </select>

        <!-- Dropdown for material selection -->
        <label for="material">انتخاب جنس:</label>
        <select id="material" name="material" required>
            <option value="wood">چوب</option>
            <option value="metal">فلز</option>
            <option value="plastic">پلاستیک</option>
            <option value="leather">چرم</option>
            <option value="glass">شیشه</option>
        </select>

        <!-- Submit button -->
        <button type="submit">ثبت سفارش</button>
    </form>

    <script>
        // Adding functionality to the form
        document.getElementById('product-customization-form').addEventListener('submit', function(event) {
            event.preventDefault(); // Prevent page reload

            // Retrieve form values
            const product = document.getElementById('product').value;
            const color = document.getElementById('color').value;
            const material = document.getElementById('material').value;

            try {
                // Simulate form submission or handle data
                alert(`سفارش شما ثبت شد:\nمحصول: ${product}\nرنگ: ${color}\nجنس: ${material}`);
            } catch (error) {
                // Handle errors gracefully
                console.error('مشکلی در ثبت سفارش وجود دارد:', error);
                alert('خطایی رخ داد. لطفاً مجدداً تلاش کنید.');
            }
        });
    </script>
</body>
</html>
```
