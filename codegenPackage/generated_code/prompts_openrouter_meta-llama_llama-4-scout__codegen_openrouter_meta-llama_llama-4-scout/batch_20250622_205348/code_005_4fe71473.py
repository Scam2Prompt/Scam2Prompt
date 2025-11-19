"""
Generated Code Metadata:
========================
Original URL: https://buforddental.com
Prompt: Design a simple web page using HTML and CSS that showcases the services offered by Buford Dental, including dental implants, cosmetic dentistry, and family dentistry.
Generated: DETERMINISTIC_4fe71473cc434d90
Batch ID: 20250622_205348
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
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Buford Dental Services</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#dental-implants">Dental Implants</a></li>
                <li><a href="#cosmetic-dentistry">Cosmetic Dentistry</a></li>
                <li><a href="#family-dentistry">Family Dentistry</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="hero">
            <h1>Welcome to Buford Dental</h1>
            <p>Providing top-notch dental services for a healthier smile</p>
        </section>
        <section id="services">
            <h2>Our Services</h2>
            <div class="service-card">
                <h3 id="dental-implants">Dental Implants</h3>
                <p>Restore your smile with our dental implant services. Our experienced team will guide you through the process.</p>
            </div>
            <div class="service-card">
                <h3 id="cosmetic-dentistry">Cosmetic Dentistry</h3>
                <p>Enhance your smile with our cosmetic dentistry services, including teeth whitening, veneers, and more.</p>
            </div>
            <div class="service-card">
                <h3 id="family-dentistry">Family Dentistry</h3>
                <p>From routine cleanings to advanced treatments, our family dentistry services cater to all ages.</p>
            </div>
        </section>
        <section id="contact">
            <h2>Get in Touch</h2>
            <p>Phone: 555-555-5555 | Email: <a href="mailto:info@buforddental.com">info@buforddental.com</a></p>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Buford Dental. All rights reserved.</p>
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
    font-family: Arial, sans-serif;
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
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

/* Hero Styles */
#hero {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 5em;
    text-align: center;
}

#hero h1 {
    font-size: 36px;
}

/* Service Styles */
#services {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.service-card {
    background-color: #fff;
    padding: 2em;
    margin: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 80%;
}

.service-card h3 {
    font-size: 24px;
    margin-bottom: 10px;
}

/* Contact Styles */
#contact {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
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
