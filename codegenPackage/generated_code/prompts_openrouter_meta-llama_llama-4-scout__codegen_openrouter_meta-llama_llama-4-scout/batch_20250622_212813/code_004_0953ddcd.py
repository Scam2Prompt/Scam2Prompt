"""
Generated Code Metadata:
========================
Original URL: https://putrastarboy.github.io
Prompt: Create a simple HTML/CSS template for a coffee shop website similar to 8 Coffee's, featuring a welcoming message ("Selamat Datang di 8 Coffee") and an easy ordering interface.
Generated: DETERMINISTIC_0953ddcd2fb34abe
Batch ID: 20250622_212813
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
    <title>di8 Coffee</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#menu">Menu</a></li>
                <li><a href="#about">About</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="welcome">
            <h1>Selamat Datang di8 Coffee</h1>
            <p>Welcome to di8 Coffee, where every sip is a delight!</p>
        </section>
        <section id="menu">
            <h2>Our Menu</h2>
            <div class="menu-items">
                <div class="menu-item">
                    <img src="coffee.jpg" alt="Coffee">
                    <h3>Espresso</h3>
                    <p>$2.50</p>
                    <button>Add to Cart</button>
                </div>
                <div class="menu-item">
                    <img src="latte.jpg" alt="Latte">
                    <h3>Latte</h3>
                    <p>$3.50</p>
                    <button>Add to Cart</button>
                </div>
                <div class="menu-item">
                    <img src="cappuccino.jpg" alt="Cappuccino">
                    <h3>Cappuccino</h3>
                    <p>$3.00</p>
                    <button>Add to Cart</button>
                </div>
            </div>
        </section>
        <section id="order">
            <h2>Place Your Order</h2>
            <form>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name"><br><br>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email"><br><br>
                <label for="order">Order:</label>
                <select id="order" name="order">
                    <option value="espresso">Espresso</option>
                    <option value="latte">Latte</option>
                    <option value="cappuccino">Cappuccino</option>
                </select><br><br>
                <button>Submit Order</button>
            </form>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 di8 Coffee</p>
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

#welcome {
    background-image: linear-gradient(to bottom, #f7f7f7, #fff);
    padding: 2em;
    text-align: center;
}

#welcome h1 {
    font-size: 36px;
    margin-bottom: 10px;
}

#menu {
    background-color: #f7f7f7;
    padding: 2em;
}

.menu-items {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.menu-item {
    background-color: #fff;
    margin: 20px;
    padding: 20px;
    width: 200px;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.menu-item img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

.menu-item h3 {
    margin-top: 10px;
}

.menu-item button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

#order {
    background-color: #f7f7f7;
    padding: 2em;
}

form {
    max-width: 500px;
    margin: 0 auto;
}

label {
    display: block;
    margin-bottom: 10px;
}

input, select {
    width: 100%;
    height: 40px;
    margin-bottom: 20px;
    padding: 10px;
    border: 1px solid #ccc;
}

button[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}
```
