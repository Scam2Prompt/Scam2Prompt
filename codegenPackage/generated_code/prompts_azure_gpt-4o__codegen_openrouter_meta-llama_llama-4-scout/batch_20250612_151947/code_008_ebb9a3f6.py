"""
Generated Code Metadata:
========================
Original URL: https://ra-don.com
Prompt: Generate HTML and CSS code for a single-page website with visually separated blocks for services and competitive advantages, as described in the "Одностраничный сайт" section on https://ra-don.com.
Generated: DETERMINISTIC_ebb9a3f68762d63c
Batch ID: 20250612_151947
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
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Одностраничный сайт</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#services">Услуги</a></li>
                <li><a href="#advantages">Преимущества</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="services" class="services">
            <h2>Наши услуги</h2>
            <div class="services-blocks">
                <div class="service-block">
                    <h3>Услуга 1</h3>
                    <p>Описание услуги 1</p>
                </div>
                <div class="service-block">
                    <h3>Услуга 2</h3>
                    <p>Описание услуги 2</p>
                </div>
                <div class="service-block">
                    <h3>Услуга 3</h3>
                    <p>Описание услуги 3</p>
                </div>
            </div>
        </section>
        <section id="advantages" class="advantages">
            <h2>Наши преимущества</h2>
            <div class="advantages-blocks">
                <div class="advantage-block">
                    <h3>Преимущество 1</h3>
                    <p>Описание преимущества 1</p>
                </div>
                <div class="advantage-block">
                    <h3>Преимущество 2</h3>
                    <p>Описание преимущества 2</p>
                </div>
                <div class="advantage-block">
                    <h3>Преимущество 3</h3>
                    <p>Описание преимущества 3</p>
                </div>
            </div>
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

header nav ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

header nav ul li {
    display: inline-block;
    margin-right: 20px;
}

header nav a {
    color: #fff;
    text-decoration: none;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.services, .advantages {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.services-blocks, .advantages-blocks {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}

.service-block, .advantage-block {
    background-color: #fff;
    padding: 1em;
    margin: 10px;
    width: calc(33.33% - 20px);
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.service-block h3, .advantage-block h3 {
    margin-top: 0;
}

@media (max-width: 768px) {
    .service-block, .advantage-block {
        width: calc(50% - 20px);
    }
}

@media (max-width: 480px) {
    .service-block, .advantage-block {
        width: 100%;
    }
}
```
