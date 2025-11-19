"""
Generated Code Metadata:
========================
Original URL: https://zoholandingpage.com
Prompt: Create a landing page template using Zoho LandingPage's responsive builder that adapts seamlessly to mobile, tablet, and desktop devices.
Generated: DETERMINISTIC_257fa5d24b3d1450
Batch ID: 20250612_150012
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

I'm happy to provide the code, but I need to clarify that Zoho LandingPage's responsive builder uses a drag-and-drop interface and doesn't typically involve writing code. However, I can provide an example of HTML, CSS, and JavaScript code that can be used as a starting point for a responsive landing page:

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Landing Page Template</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="#">Home</a></li>
                <li><a href="#">Features</a></li>
                <li><a href="#">Pricing</a></li>
            </ul>
        </nav>
    </header>
    <main>
        <section class="hero">
            <h1>Welcome to our landing page</h1>
            <p>This is a sample landing page template.</p>
            <button>Sign up now</button>
        </section>
        <section class="features">
            <h2>Features</h2>
            <ul>
                <li>
                    <i class="icon"></i>
                    <h3>Feature 1</h3>
                    <p>This is feature 1.</p>
                </li>
                <li>
                    <i class="icon"></i>
                    <h3>Feature 2</h3>
                    <p>This is feature 2.</p>
                </li>
                <li>
                    <i class="icon"></i>
                    <h3>Feature 3</h3>
                    <p>This is feature 3.</p>
                </li>
            </ul>
        </section>
        <section class="testimonials">
            <h2>What our customers say</h2>
            <blockquote>
                <p>This is a testimonial.</p>
                <cite>John Doe</cite>
            </blockquote>
        </section>
        <section class="call-to-action">
            <button>Sign up now</button>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Landing Page Template</p>
    </footer>
    <script src="script.js"></script>
</body>
</html>
```

**styles.css**
```css
/* Global styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
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
    display: flex;
    justify-content: space-between;
}

header nav ul li {
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

.hero {
    background-image: linear-gradient(to bottom, #333, #555);
    background-size: 100% 300px;
    background-position: 0% 100%;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    color: #fff;
}

.hero h1 {
    font-size: 48px;
}

.features {
    background-color: #fff;
    padding: 2em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.features ul {
    list-style: none;
    margin: 0;
    padding: 0;
}

.features li {
    margin-bottom: 20px;
}

.features h3 {
    font-size: 18px;
    margin-top: 0;
}

.testimonials {
    background-color: #f9f9f9;
    padding: 2em;
}

.testimonials blockquote {
    background-color: #fff;
    padding: 1em;
    border-left: 5px solid #333;
}

.call-to-action {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
}

.call-to-action button {
    background-color: #555;
    color: #fff;
    border: none;
    padding: 10px 20px;
    font-size: 18px;
    cursor: pointer;
}

footer {
    background-color: #333;
    color: #fff;
    padding: 1em;
    text-align: center;
    clear: both;
}

/* Responsive styles */
@media only screen and (max-width: 768px) {
    main {
        flex-direction: column;
    }
    .hero {
        height: 50vh;
    }
}

@media only screen and (max-width: 480px) {
    .hero h1 {
        font-size: 24px;
    }
    .features ul {
        margin: 0;
        padding: 0;
    }
    .features li {
        margin-bottom: 10px;
    }
}
```

**script.js**
```javascript
// Add event listener to button
document.querySelector('.call-to-action button').addEventListener('click', () => {
    // Add your JavaScript code here
    console.log('Button clicked');
});
```
