"""
Generated Code Metadata:
========================
Original URL: https://mercedariasgye.edu.ec
Prompt: Create a simple web page using HTML and CSS that showcases a school's mission, vision, and values, similar to the "Misión y Visión" section of MercedariasGye's website.
Generated: DETERMINISTIC_c77542b3ebb3a7a8
Batch ID: 20250622_210655
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
    <title>School Mission, Vision, and Values</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Our Mission, Vision, and Values</h1>
    </header>
    <main>
        <section id="mission">
            <h2>Our Mission</h2>
            <p>To provide a high-quality education that fosters academic excellence, creativity, and critical thinking, preparing students to become responsible and compassionate leaders in their communities.</p>
        </section>
        <section id="vision">
            <h2>Our Vision</h2>
            <p>To be a leading educational institution, recognized for its innovative approaches, commitment to social responsibility, and dedication to the holistic development of its students.</p>
        </section>
        <section id="values">
            <h2>Our Values</h2>
            <ul>
                <li><strong>Respect</strong>: We value the dignity and worth of every individual, promoting a culture of empathy and understanding.</li>
                <li><strong>Integrity</strong>: We act with honesty, transparency, and accountability, upholding the highest standards of ethics and morality.</li>
                <li><strong>Excellence</strong>: We strive for academic excellence, encouraging creativity, innovation, and continuous improvement.</li>
                <li><strong>Compassion</strong>: We care for the well-being of our students, staff, and community, fostering a sense of belonging and social responsibility.</li>
            </ul>
        </section>
    </main>
</body>
</html>
```

**styles.css**
```css
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
}

header {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

header h1 {
    margin: 0;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 0.5em;
}

strong {
    font-weight: bold;
}

/* Responsive design */
@media only screen and (max-width: 768px) {
    main {
        padding: 1em;
    }
    section {
        margin-bottom: 0.5em;
    }
}
```
