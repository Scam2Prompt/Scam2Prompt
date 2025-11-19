"""
Generated Code Metadata:
========================
Original URL: https://getin.co.il
Prompt: Write a Hebrew-language webpage content for a company called Getin that uses JavaScript for functionality.
Generated: DETERMINISTIC_7c7eface2a03b714
Batch ID: 20250622_211951
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a clean, production-ready Hebrew-language webpage for Getin with JavaScript functionality:

```html
<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Getin - פתרונות טכנולוגיים מתקדמים</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
            color: #333;
        }
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px;
            text-align: center;
        }
        nav {
            background-color: #34495e;
            padding: 10px;
        }
        nav ul {
            list-style-type: none;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
        }
        nav li {
            margin: 0 15px;
        }
        nav a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        main {
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }
        section {
            margin-bottom: 30px;
            background-color: white;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 15px;
            margin-top: 20px;
        }
        button {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
        }
        button:hover {
            background-color: #2980b9;
        }
        .contact-form input, .contact-form textarea {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
    </style>
</head>
<body>
    <header>
        <h1>ברוכים הבאים ל-Getin</h1>
        <p>פתרונות טכנולוגיים מתקדמים לעסקים</p>
    </header>

    <nav>
        <ul>
            <li><a href="#about">אודות</a></li>
            <li><a href="#services">שירותים</a></li>
            <li><a href="#contact">צור קשר</a></li>
        </ul>
    </nav>

    <main>
        <section id="about">
            <h2>אודות החברה</h2>
            <p>Getin היא חברה מובילה בפיתוח פתרונות תוכנה מותאמים אישית. אנו מתמחים בבניית מערכות מתקדמות המבוססות על טכנולוגיות העדכניות ביותר.</p>
            <p>הצוות שלנו מורכב ממפתחים מומחים עם ניסיון רב בתעשייה, המחויבים לספק איכות ומצוינות בכל פרויקט.</p>
        </section>

        <section id="services">
            <h2>השירותים שלנו</h2>
            <ul>
                <li>פיתוח אפליקציות ווב ומובייל</li>
                <li>ייעוץ טכנולוגי</li>
                <li>פתרונות ענן</li>
                <li>אינטגרציה בין מערכות</li>
                <li>אבטחת מידע</li>
            </ul>
            <button id="moreInfoBtn">למידע נוסף</button>
        </section>

        <section id="contact" class="contact-form">
            <h2>צור קשר</h2>
            <form id="contactForm">
                <input type="text" id="name" placeholder="שם מלא" required>
                <input type="email" id="email" placeholder="אימייל" required>
                <input type="tel" id="phone" placeholder="טלפון">
                <textarea id="message" rows="5" placeholder="הודעה" required></textarea>
                <button type="submit">שלח</button>
            </form>
        </section>
    </main>

    <footer>
        <p>© 2023 Getin. כל הזכויות שמורות.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            // Smooth scrolling for navigation links
            document.querySelectorAll('nav a').forEach(anchor => {
                anchor.addEventListener('click', function(e) {
                    e.preventDefault();
                    document.querySelector(this.getAttribute('href')).scrollIntoView({
                        behavior: 'smooth'
                    });
                });
            });

            // More info button functionality
            document.getElementById('moreInfoBtn').addEventListener('click', function() {
                alert('למידע נוסף, אנא צרו איתנו קשר דרך הטופס באתר או בטלפון 03-1234567');
            });

            // Form submission handling
            document.getElementById('contactForm').addEventListener('submit', function(e) {
                e.preventDefault();
                
                const name = document.getElementById('name').value;
                const email = document.getElementById('email').value;
                const message = document.getElementById('message').value;
                
                // Basic validation
                if (!name || !email || !message) {
                    alert('אנא מלא את כל השדות המסומנים');
                    return;
                }
                
                // Here you would typically send the data to a server
                console.log('Form submitted:', { name, email, message });
                
                // Show success message
                alert('תודה על פנייתך! ניצור איתך קשר בהקדם.');
                
                // Reset form
                this.reset();
            });

            // Additional feature: Change header color on scroll
            window.addEventListener('scroll', function() {
                const header = document.querySelector('header');
                if (window.scrollY > 50) {
                    header.style.backgroundColor = '#1a252f';
                } else {
                    header.style.backgroundColor = '#2c3e50';
                }
            });
        });
    </script>
</body>
</html>
```
