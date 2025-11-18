"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://kocaeli.com
Prompt: Generate HTML and CSS code for a "Kocaeli Rehberi" section that includes categories like "Konaklama," "Eğlence Yerleri," and "Alışveriş Merkezleri," with a visually appealing layout.
Generated: DETERMINISTIC_042c9a9e0c5c215e
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kocaeli Rehberi</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS -->
</head>
<body>
    <header>
        <h1>Kocaeli Rehberi</h1>
    </header>
    <main>
        <section class="categories">
            <div class="category">
                <h2>Konaklama</h2>
                <p>En iyi konaklama seçenekleri için rehberlik.</p>
            </div>
            <div class="category">
                <h2>Eğlence Yerleri</h2>
                <p>Kocaeli'de keşfedilecek eğlence mekanları.</p>
            </div>
            <div class="category">
                <h2>Alışveriş Merkezleri</h2>
                <p>Popüler alışveriş noktaları ve merkezleri.</p>
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

/* Basic reset for margins and padding */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif; /* Setting a clean font */
    line-height: 1.6; /* Improving readability */
    color: #333; /* Default text color */
    background-color: #f4f4f4; /* Light background color */
}

/* Header styles */
header {
    background: #007bff; /* Blue background for the header */
    color: #fff; /* White text color */
    text-align: center; /* Centered text */
    padding: 1rem 0; /* Padding for spacing */
}

/* Main section styles */
main {
    padding: 20px; /* Padding around main content */
}

/* Category styles */
.categories {
    display: flex; /* Flexbox for layout */
    justify-content: space-around; /* Evenly distribute categories */
    flex-wrap: wrap; /* Allow wrapping on smaller screens */
}

.category {
    background: white; /* White background for each category */
    border: 1px solid #ccc; /* Light border */
    border-radius: 8px; /* Rounded corners */
    padding: 20px; /* Padding inside categories */
    margin: 10px; /* Margin between categories */
    flex: 1 0 30%; /* Allow categories to grow and shrink */
    min-width: 250px; /* Minimum width for responsiveness */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow for depth */
}

/* Footer styles */
footer {
    text-align: center; /* Centered text */
    padding: 10px 0; /* Padding for spacing */
    background: #007bff; /* Matching footer background */
    color: white; /* White text color */
    position: relative; /* Relative positioning for layout */
    bottom: 0; /* Stick to the bottom */
    width: 100%; /* Full width */
}
```
