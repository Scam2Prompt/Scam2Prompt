"""
Generated Code Metadata:
========================
Original URL: https://kocaeli.com
Prompt: Generate HTML and CSS code for a "Kocaeli Rehberi" section that includes categories like "Konaklama," "Eğlence Yerleri," and "Alışveriş Merkezleri," with a visually appealing layout.
Generated: DETERMINISTIC_042c9a9e0c5c215e
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kocaeli Rehberi</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Kocaeli Rehberi</h1>
    </header>
    <main>
        <section class="categories">
            <div class="category">
                <h2>Konaklama</h2>
                <p>Şehirdeki oteller, pansiyonlar ve diğer konaklama seçenekleri hakkında bilgi.</p>
            </div>
            <div class="category">
                <h2>Eğlence Yerleri</h2>
                <p>Sinema, tiyatro, konser ve diğer eğlence mekanları hakkında bilgi.</p>
            </div>
            <div class="category">
                <h2>Alışveriş Merkezleri</h2>
                <p>Şehirdeki alışveriş merkezleri ve mağazalar hakkında bilgi.</p>
            </div>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Kocaeli Rehberi. Tüm hakları saklıdır.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Header styles */
header {
    background: #007BFF;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Categories section styles */
.categories {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
}

/* Individual category styles */
.category {
    background: #fff;
    border: 1px solid #ddd;
    border-radius: 5px;
    padding: 15px;
    margin: 10px;
    width: 30%;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
    transition: transform 0.2s;
}

/* Hover effect for categories */
.category:hover {
    transform: scale(1.05);
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007BFF;
    color: #fff;
    position: relative;
    bottom: 0;
    width: 100%;
}
```
