"""
Generated Code Metadata:
========================
Original URL: https://egatur.edu.pe
Prompt: "Create a web page using HTML and CSS that showcases different culinary programs, including Cocina Nacional e Internacional, Pastelería y Panificación, and Barismo."
Generated: DETERMINISTIC_0b676b643e12c7cb
Batch ID: 20250622_212015
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
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Culinary Programs</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Culinary Programs</h1>
    </header>
    <main>
        <section id="programas">
            <h2>Our Culinary Programs</h2>
            <div class="program">
                <h3>Cocina Nacional e Internacional</h3>
                <p>Learn the art of cooking national and international dishes, from traditional recipes to modern fusion cuisine.</p>
                <img src="cocina.jpg" alt="Cocina Nacional e Internacional">
            </div>
            <div class="program">
                <h3>Pastelería y Panificación</h3>
                <p>Discover the world of pastry-making and bread-baking, from sweet treats to artisanal breads.</p>
                <img src="pasteleria.jpg" alt="Pastelería y Panificación">
            </div>
            <div class="program">
                <h3>Barismo</h3>
                <p>Master the art of coffee-making and become a skilled barista, from espresso to latte art.</p>
                <img src="barismo.jpg" alt="Barismo">
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Culinary Programs</p>
    </footer>
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

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

#programas {
    background-color: #f7f7f7;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.program {
    background-color: #fff;
    padding: 1em;
    border: 1px solid #ddd;
    margin-bottom: 1em;
}

.program h3 {
    margin-top: 0;
}

.program img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

footer p {
    margin-bottom: 0;
}
```
