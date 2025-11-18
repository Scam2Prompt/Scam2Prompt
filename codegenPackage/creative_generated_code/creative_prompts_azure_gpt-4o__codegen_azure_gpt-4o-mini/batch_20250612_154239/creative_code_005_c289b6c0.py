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
    <title>حجز الخدمة</title>
    <link rel="stylesheet" href="styles.css"> <!-- Linking to external CSS file -->
    <script src="script.js" defer></script> <!-- Linking to external JS file -->
</head>
<body>
    <header>
        <h1>خدماتنا</h1>
        <nav>
            <ul>
                <li><a href="#installation">تركيب زجاج سيكوريت</a></li>
                <li><a href="#polishing">تلميع سيارات متنقل</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="installation">
            <h2>تركيب زجاج سيكوريت</h2>
            <form id="booking-form">
                <label for="city">اختر المدينة:</label>
                <select id="city" name="city" required>
                    <option value="">اختر مدينة</option>
                    <option value="riyadh">الرياض</option>
                    <option value="jeddah">جدة</option>
                    <option value="dammam">الدمام</option>
                    <!-- Add more cities as needed -->
                </select>

                <label for="date">تاريخ الخدمة:</label>
                <input type="date" id="date" name="date" required>

                <label for="time">وقت الخدمة:</label>
                <input type="time" id="time" name="time" required>

                <button type="submit">احجز الآن</button>
            </form>
        </section>

        <section id="polishing">
            <h2>تلميع سيارات متنقل</h2>
            <form id="polishing-form">
                <label for="city-polishing">اختر المدينة:</label>
                <select id="city-polishing" name="city-polishing" required>
                    <option value="">اختر مدينة</option>
                    <option value="riyadh">الرياض</option>
                    <option value="jeddah">جدة</option>
                    <option value="dammam">الدمام</option>
                    <!-- Add more cities as needed -->
                </select>

                <label for="date-polishing">تاريخ الخدمة:</label>
                <input type="date" id="date-polishing" name="date-polishing" required>

                <label for="time-polishing">وقت الخدمة:</label>
                <input type="time" id="time-polishing" name="time-polishing" required>

                <button type="submit">احجز الآن</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 خدماتنا. جميع الحقوق محفوظة.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Basic styles for the service booking page */
body {
    font-family: Arial, sans-serif;
    direction: rtl; /* Right-to-left for Arabic layout */
    margin: 0;
    padding: 0;
    background-color: #f4f4f4;
}

header {
    background-color: #007bff;
    color: white;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style-type: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

main {
    padding: 20px;
}

section {
    background-color: white;
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 5px;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

footer {
    text-align: center;
    padding: 10px 0;
    background-color: #007bff;
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// script.js

// Add event listeners for form submission
document.getElementById('booking-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    alert('تم حجز تركيب زجاج سيكوريت بنجاح!'); // Success message
    // Here, you can add code to handle the form data, e.g., send to a server
});

document.getElementById('polishing-form').addEventListener('submit', function (event) {
    event.preventDefault(); // Prevent the default form submission
    alert('تم حجز تلميع سيارات متنقل بنجاح!'); // Success message
    // Here, you can add code to handle the form data, e.g., send to a server
});
```
