"""
Generated Code Metadata:
========================
Original URL: https://azuharu.net
Prompt: Generate a simple webpage using HTML/CSS that showcases various types of packaging materials, including blister packaging mentioned in the article "Kenalan yuk dengan Kemasan Blister".
Generated: DETERMINISTIC_3f879e79854d2699
Batch ID: 20250622_205603
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!-- index.html -->

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Packaging Materials Showcase</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Packaging Materials Showcase</h1>
    </header>
    <main>
        <section id="blister-packaging">
            <h2>Blister Packaging</h2>
            <p>Blister packaging, also known as bubble packaging, is a type of packaging that uses a pre-formed plastic cavity to protect and display products.</p>
            <img src="blister-packaging.jpg" alt="Blister Packaging Example">
        </section>
        <section id="cardboard-packaging">
            <h2>Cardboard Packaging</h2>
            <p>Cardboard packaging, also known as paperboard packaging, is a sustainable and eco-friendly option for packaging products.</p>
            <img src="cardboard-packaging.jpg" alt="Cardboard Packaging Example">
        </section>
        <section id="bubble-wrap-packaging">
            <h2>Bubble Wrap Packaging</h2>
            <p>Bubble wrap packaging is a type of packaging material that uses air-filled bubbles to cushion and protect products during shipping.</p>
            <img src="bubble-wrap-packaging.jpg" alt="Bubble Wrap Packaging Example">
        </section>
        <section id="foam-packaging">
            <h2>Foam Packaging</h2>
            <p>Foam packaging, also known as expanded polystyrene (EPS) packaging, is a lightweight and shock-absorbing material used to protect fragile products.</p>
            <img src="foam-packaging.jpg" alt="Foam Packaging Example">
        </section>
    </main>
</body>
</html>
```

```css
/* styles.css */

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

section {
    background-color: #f7f7f7;
    padding: 1em;
    margin-bottom: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h2 {
    margin-top: 0;
}

img {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px 10px 0 0;
}

p {
    margin-bottom: 1em;
}

@media only screen and (max-width: 768px) {
    main {
        padding: 1em;
    }
    section {
        margin-bottom: 0.5em;
    }
}
```
