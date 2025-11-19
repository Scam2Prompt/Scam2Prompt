"""
Generated Code Metadata:
========================
Original URL: https://ristorantelafenice.ch
Prompt: Generate a simple web page in HTML and CSS that showcases a restaurant's menu, including sections for Italian and Mediterranean dishes like those offered at Ristorante La Fenice.
Generated: DETERMINISTIC_23975c2a78a99584
Batch ID: 20250622_210703
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
    <title>Ristorante La Fenice Menu</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Ristorante La Fenice</h1>
        <h2>Menu</h2>
    </header>
    <main>
        <section id="italian-dishes">
            <h3>Italian Dishes</h3>
            <ul>
                <li>
                    <strong>Spaghetti Carbonara</strong>
                    <p>Tender spaghetti tossed with bacon, eggs, and parmesan cheese</p>
                    <span>$18.95</span>
                </li>
                <li>
                    <strong>Fettuccine Alfredo</strong>
                    <p>Rich and creamy fettuccine pasta with parmesan sauce</p>
                    <span>$19.95</span>
                </li>
                <li>
                    <strong>Pizza Margherita</strong>
                    <p>Classic Neapolitan-style pizza with tomato sauce, mozzarella, and basil</p>
                    <span>$14.95</span>
                </li>
            </ul>
        </section>
        <section id="mediterranean-dishes">
            <h3>Mediterranean Dishes</h3>
            <ul>
                <li>
                    <strong>Grilled Halloumi</strong>
                    <p>Cypriot-style cheese served with a side of honey and figs</p>
                    <span>$12.95</span>
                </li>
                <li>
                    <strong>Shawarma Wrap</strong>
                    <p>Juicy lamb and beef wrap with tzatziki sauce and pickled turnips</p>
                    <span>$10.95</span>
                </li>
                <li>
                    <strong>Greek Salad</strong>
                    <p>Tomatoes, cucumbers, red onion, feta cheese, and olives with a drizzle of Greek vinaigrette</p>
                    <span>$14.95</span>
                </li>
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
    background-color: #f0f0f0;
    padding: 20px;
    text-align: center;
}

header h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

header h2 {
    font-size: 24px;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 20px;
}

section {
    background-color: #f7f7f7;
    padding: 20px;
    margin-bottom: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

section h3 {
    font-size: 24px;
    margin-bottom: 10px;
}

ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 20px;
}

strong {
    font-weight: bold;
    font-size: 18px;
}

p {
    font-size: 16px;
    margin-bottom: 5px;
}

span {
    font-size: 18px;
    font-weight: bold;
    color: #666;
}
```
