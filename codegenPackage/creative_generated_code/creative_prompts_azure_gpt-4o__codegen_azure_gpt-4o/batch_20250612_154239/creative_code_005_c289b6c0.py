"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.khadamy.com
Prompt: Create an HTML template for a service booking page that includes options for "تركيب زجاج سيكوريت" and "تلميع سيارات متنقل," with city-specific filters inspired by the layout of https://www.khadamy.com.
Generated: DETERMINISTIC_c289b6c07c716633
Batch ID: 20250612_154239
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
    <meta name="description" content="صفحة حجز خدمات تركيب زجاج سيكوريت وتلميع سيارات متنقل">
    <title>صفحة حجز الخدمات</title>
    <link rel="stylesheet" href="styles.css">
    <!-- Add external styles or libraries if needed -->
</head>
<body>
    <header>
        <!-- Navigation bar -->
        <nav>
            <ul>
                <li><a href="#">الرئيسية</a></li>
                <li><a href="#">الخدمات</a></li>
                <li><a href="#">اتصل بنا</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Hero section -->
        <section class="hero">
            <h1>احجز خدماتك بكل سهولة</h1>
            <p>اختر الخدمة والموقع واحجز فورًا</p>
        </section>

        <!-- Service booking section -->
        <section class="service-booking">
            <h2>الخدمات المتوفرة</h2>
            <form id="booking-form" action="/submit-booking" method="POST">
                <!-- Service selection -->
                <div class="form-group">
                    <label for="service">الخدمة المطلوبة:</label>
                    <select id="service" name="service" required>
                        <option value="تركيب زجاج سيكوريت">تركيب زجاج سيكوريت</option>
                        <option value="تلميع سيارات متنقل">تلميع سيارات متنقل</option>
                    </select>
                </div>

                <!-- City filter -->
                <div class="form-group">
                    <label for="city">اختر المدينة:</label>
                    <select id="city" name="city" required>
                        <option value="الرياض">الرياض</option>
                        <option value="جدة">جدة</option>
                        <option value="مكة">مكة</option>
                        <option value="الدمام">الدمام</option>
                        <option value="المدينة المنورة">المدينة المنورة</option>
                    </select>
                </div>

                <!-- Submit button -->
                <div class="form-group">
                    <button type="submit">احجز الآن</button>
                </div>
            </form>
        </section>
    </main>

    <footer>
        <!-- Footer content -->
        <p>حقوق الطبع والنشر &copy; 2023 - جميع الحقوق محفوظة.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
body, h1, h2, p, ul, li, select, button {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: 'Arial', sans-serif;
    direction: rtl; /* Ensures proper text alignment for Arabic */
    text-align: right; /* Aligns text to the right */
    background-color: #f9f9f9;
    color: #333;
}

/* Header styles */
header {
    background-color: #007bff;
    padding: 10px;
    color: #fff;
}

nav ul {
    display: flex;
    list-style: none;
    justify-content: flex-start;
}

nav ul li {
    margin-right: 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
    font-size: 1.2em;
}

/* Hero section */
.hero {
    text-align: center;
    padding: 20px;
    background-color: #e9ecef;
}

.hero h1 {
    font-size: 2.5em;
    color: #007bff;
}

.hero p {
    font-size: 1.2em;
    margin-top: 10px;
}

/* Service booking section */
.service-booking {
    padding: 20px;
    background-color: #fff;
    margin: 20px auto;
    max-width: 600px;
    border: 1px solid #ddd;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.service-booking h2 {
    font-size: 1.8em;
    margin-bottom: 20px;
}

.form-group {
    margin-bottom: 15px;
}

label {
    display: block;
    margin-bottom: 5px;
    font-weight: bold;
}

select, button {
    width: 100%;
    padding: 10px;
    border: 1px solid #ddd;
    border-radius: 5px;
    font-size: 1em;
}

button {
    background-color: #007bff;
    color: #fff;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px;
    background-color: #007bff;
    color: #fff;
    margin-top: 20px;
}
```
