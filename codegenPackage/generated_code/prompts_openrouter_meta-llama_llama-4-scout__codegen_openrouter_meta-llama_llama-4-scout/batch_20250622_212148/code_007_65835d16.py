"""
Generated Code Metadata:
========================
Original URL: https://officineimmagine.it
Prompt: Create a photography website template using HTML, CSS, and JavaScript, incorporating Officine dell'Immagine's style and services.
Generated: DETERMINISTIC_65835d16af6fbae4
Batch ID: 20250622_212148
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
<html lang="it">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Officine dell'Immagine</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#servizi">Servizi</a></li>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#contatti">Contatti</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section id="home">
            <h1>Benvenuti in Officine dell'Immagine</h1>
            <p>Studio di fotografia e servizi di imaging</p>
            <button>Scopri di più</button>
        </section>
        <section id="servizi">
            <h2>I nostri servizi</h2>
            <ul>
                <li>
                    <h3>Fotografia pubblicitaria</h3>
                    <p>Fotografia per campagne pubblicitarie e marketing</p>
                </li>
                <li>
                    <h3>Fotografia di prodotto</h3>
                    <p>Fotografia per cataloghi e siti web</p>
                </li>
                <li>
                    <h3>Fotografia di eventi</h3>
                    <p>Fotografia per eventi e manifestazioni</p>
                </li>
            </ul>
        </section>
        <section id="portfolio">
            <h2>Il nostro portfolio</h2>
            <div class="gallery">
                <img src="image1.jpg" alt="Foto 1">
                <img src="image2.jpg" alt="Foto 2">
                <img src="image3.jpg" alt="Foto 3">
            </div>
        </section>
        <section id="contatti">
            <h2>Contattaci</h2>
            <p>Telefono: 0123456789</p>
            <p>Email: <a href="mailto:info@officineimmagine.it">info@officineimmagine.it</a></p>
            <form>
                <input type="text" placeholder="Nome">
                <input type="email" placeholder="Email">
                <textarea placeholder="Messaggio"></textarea>
                <button>Invia</button>
            </form>
        </section>
    </main>
    <script src="script.js"></script>
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

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 10px;
}

p {
    margin-bottom: 20px;
}

button {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

.gallery {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.gallery img {
    width: 200px;
    height: 150px;
    margin: 10px;
    border-radius: 10px;
}

form {
    display: flex;
    flex-direction: column;
    align-items: center;
}

input, textarea {
    padding: 10px;
    margin-bottom: 20px;
    border: 1px solid #ccc;
}

input[type="submit"] {
    background-color: #333;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

input[type="submit"]:hover {
    background-color: #444;
}
```

**script.js**
```javascript
// Smooth scrolling
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Form validation
const form = document.querySelector('form');
form.addEventListener('submit', function (e) {
    e.preventDefault();
    const name = document.querySelector('input[type="text"]').value;
    const email = document.querySelector('input[type="email"]').value;
    const message = document.querySelector('textarea').value;
    if (name && email && message) {
        // Send form data to server
        console.log('Form submitted:', { name, email, message });
    } else {
        alert('Please fill in all fields');
    }
});
```
