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
    <title>Customizable Product Options</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
</head>
<body>
    <h1>انتخاب گزینه‌های سفارشی محصول</h1>
    
    <!-- Product selection form -->
    <form id="productForm" action="/submit" method="POST">
        <label for="product">محصول را انتخاب کنید:</label>
        <select id="product" name="product" required>
            <option value="" disabled selected>-- انتخاب کنید --</option>
            <option value="آرم رست تاتو">آرم رست تاتو</option>
            <option value="آینه و کنسول آرایشگاهی">آینه و کنسول آرایشگاهی</option>
        </select>
        
        <label for="color">رنگ را انتخاب کنید:</label>
        <select id="color" name="color" required>
            <option value="" disabled selected>-- انتخاب کنید --</option>
            <option value="قرمز">قرمز</option>
            <option value="آبی">آبی</option>
            <option value="سبز">سبز</option>
            <option value="زرد">زرد</option>
        </select>
        
        <label for="material">جنس را انتخاب کنید:</label>
        <select id="material" name="material" required>
            <option value="" disabled selected>-- انتخاب کنید --</option>
            <option value="چوب">چوب</option>
            <option value="فلز">فلز</option>
            <option value="پلاستیک">پلاستیک</option>
            <option value="شیشه">شیشه</option>
        </select>
        
        <button type="submit">ارسال</button>
    </form>

    <!-- JavaScript for form validation -->
    <script>
        document.getElementById('productForm').addEventListener('submit', function(event) {
            // Prevent form submission if validation fails
            if (!this.checkValidity()) {
                event.preventDefault(); // Prevent form submission
                alert('لطفاً همه گزینه‌ها را پر کنید.'); // Alert user to fill all fields
            }
        });
    </script>
</body>
</html>
```
