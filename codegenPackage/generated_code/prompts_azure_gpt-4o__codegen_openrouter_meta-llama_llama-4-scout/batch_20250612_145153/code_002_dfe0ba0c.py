"""
Generated Code Metadata:
========================
Original URL: https://idex.marketing
Prompt: Generate HTML/CSS code for designing a modern, user-friendly website tailored to Jordanian market preferences, as emphasized by IDEX Marketing.
Generated: DETERMINISTIC_dfe0ba0cd6786edf
Batch ID: 20250612_145153
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**index.html**
```html
<!DOCTYPE html>
<html lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Modern Jordanian Website</title>
    <link rel="stylesheet" href="styles.css">
    <link rel="icon" href="favicon.ico" type="image/x-icon">
</head>
<body>
    <!-- Header Section -->
    <header>
        <nav>
            <ul>
                <li><a href="#home">الرئيسية</a></li>
                <li><a href="#services">الخدمات</a></li>
                <li><a href="#about">عن الموقع</a></li>
                <li><a href="#contact">اتصل بنا</a></li>
            </ul>
        </nav>
    </header>

    <!-- Hero Section -->
    <section id="home">
        <h1>مرحبًا بك في موقعنا</h1>
        <p>موقع إلكتروني عصري و سهل الاستخدام</p>
        <button>تعرف على المزيد</button>
    </section>

    <!-- Services Section -->
    <section id="services">
        <h2>الخدمات</h2>
        <div class="service-cards">
            <div class="card">
                <h3>خدمة 1</h3>
                <p>وصف الخدمة الأولى</p>
            </div>
            <div class="card">
                <h3>خدمة 2</h3>
                <p>وصف الخدمة الثانية</p>
            </div>
            <div class="card">
                <h3>خدمة 3</h3>
                <p>وصف الخدمة الثالثة</p>
            </div>
        </div>
    </section>

    <!-- About Section -->
    <section id="about">
        <h2>عن الموقع</h2>
        <p>موقعنا الإلكتروني يهدف إلى توفير معلومات قيمة وخدمات متميزة للزوار</p>
    </section>

    <!-- Contact Section -->
    <section id="contact">
        <h2>اتصل بنا</h2>
        <form>
            <input type="text" placeholder="الاسم">
            <input type="email" placeholder="البريد الإلكتروني">
            <textarea placeholder="الرسالة"></textarea>
            <button>إرسال</button>
        </form>
    </section>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 موقعنا الإلكتروني</p>
    </footer>
</body>
</html>
```

**styles.css**
```css
/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Cairo', sans-serif;
    direction: rtl;
    text-align: right;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Header Styles */
header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: space-between;
}

header nav ul li {
    margin-left: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
#home {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: cover;
    background-position: center;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

#home h1 {
    font-size: 48px;
}

/* Services Styles */
#services {
    padding: 2em;
}

.service-cards {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.card {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    margin: 20px;
    width: calc(33.33% - 20px);
}

/* About Styles */
#about {
    padding: 2em;
}

/* Contact Styles */
#contact {
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

input, textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

button {
    background-color: #333;
    color: #fff;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

/* Footer Styles */
footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
