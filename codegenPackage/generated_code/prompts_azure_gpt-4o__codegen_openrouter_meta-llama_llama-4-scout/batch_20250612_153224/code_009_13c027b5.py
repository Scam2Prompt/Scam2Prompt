"""
Generated Code Metadata:
========================
Original URL: https://alwan.om
Prompt: Write code to create a "Terms & Conditions" page that dynamically updates based on user interactions, similar to the structure seen on Alwan's website.
Generated: DETERMINISTIC_13c027b504d7a511
Batch ID: 20250612_153224
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
    <title>Terms & Conditions</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="terms-container">
        <h1>Terms & Conditions</h1>
        <div class="terms-sections">
            <button class="section-button active">Introduction</button>
            <button class="section-button">Definitions</button>
            <button class="section-button">Terms of Use</button>
            <button class="section-button">Disclaimer</button>
            <button class="section-button">Limitation of Liability</button>
        </div>
        <div class="terms-content">
            <div class="term-content introduction active">
                <h2>Introduction</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </div>
            <div class="term-content definitions">
                <h2>Definitions</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <ul>
                    <li><strong>Term 1:</strong> Lorem ipsum dolor sit amet.</li>
                    <li><strong>Term 2:</strong> Lorem ipsum dolor sit amet.</li>
                </ul>
            </div>
            <div class="term-content terms-of-use">
                <h2>Terms of Use</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
                <ol>
                    <li>Lorem ipsum dolor sit amet.</li>
                    <li>Lorem ipsum dolor sit amet.</li>
                </ol>
            </div>
            <div class="term-content disclaimer">
                <h2>Disclaimer</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </div>
            <div class="term-content limitation-of-liability">
                <h2 Limitation of Liability</h2>
                <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
            </div>
        </div>
    </div>

    <script src="script.js"></script>
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

.terms-container {
    max-width: 800px;
    margin: 40px auto;
    padding: 20px;
    background-color: #f9f9f9;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.terms-sections {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 20px;
}

.section-button {
    background-color: #4CAF50;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 16px;
    cursor: pointer;
}

.section-button.active {
    background-color: #3e8e41;
}

.terms-content {
    display: flex;
    flex-direction: column;
}

.term-content {
    display: none;
}

.term-content.active {
    display: block;
}

.term-content h2 {
    margin-top: 0;
}

.term-content ul, .term-content ol {
    padding-left: 20px;
}

.term-content li {
    margin-bottom: 10px;
}

.term-content strong {
    font-weight: bold;
}
```

```javascript
// script.js

const sectionButtons = document.querySelectorAll('.section-button');
const termContents = document.querySelectorAll('.term-content');

sectionButtons.forEach(button => {
    button.addEventListener('click', () => {
        // Remove active class from all buttons
        sectionButtons.forEach(btn => btn.classList.remove('active'));
        // Add active class to clicked button
        button.classList.add('active');

        // Get the index of the clicked button
        const index = Array.prototype.indexOf.call(sectionButtons, button);

        // Remove active class from all term contents
        termContents.forEach(content => content.classList.remove('active'));
        // Add active class to corresponding term content
        termContents[index].classList.add('active');
    });
});

// Set the first button and term content as active by default
sectionButtons[0].classList.add('active');
termContents[0].classList.add('active');
```
