"""
Generated Code Metadata:
========================
Original URL: https://bitcoinpepe-en.xyz
Prompt: Design a simple webpage for displaying the Bitcoin Pepe roadmap, including PHASE1 to PHASE6 milestones, using HTML, CSS, and JavaScript.
Generated: DETERMINISTIC_036e59a59e296134
Batch ID: 20250622_212238
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
    <title>Bitcoin Pepe Roadmap</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Bitcoin Pepe Roadmap</h1>
    </header>
    <main>
        <section class="roadmap">
            <h2>Milestones</h2>
            <div class="phases">
                <div class="phase">
                    <h3>PHASE 1</h3>
                    <p>Q1 2023 - Project initiation and community building</p>
                </div>
                <div class="phase">
                    <h3>PHASE 2</h3>
                    <p>Q2 2023 - Development of core features and Pepe token creation</p>
                </div>
                <div class="phase">
                    <h3>PHASE 3</h3>
                    <p>Q3 2023 - Private sale and IDO preparation</p>
                </div>
                <div class="phase">
                    <h3>PHASE 4</h3>
                    <p>Q4 2023 - IDO and listing on major exchanges</p>
                </div>
                <div class="phase">
                    <h3>PHASE 5</h3>
                    <p>Q1 2024 - Marketing and community growth initiatives</p>
                </div>
                <div class="phase">
                    <h3>PHASE 6</h3>
                    <p>Q2 2024 - Continued development and expansion of ecosystem</p>
                </div>
            </div>
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
    background-color: #f0f0f0;
    padding: 1em;
    text-align: center;
}

main {
    display: flex;
    flex-direction: column;
    align-items: center;
    padding: 2em;
}

.roadmap {
    background-color: #f9f9f9;
    padding: 1em;
    border: 1px solid #ddd;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.phases {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
}

.phase {
    background-color: #f0f0f0;
    padding: 1em;
    margin: 1em;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    width: 200px;
}

.phase h3 {
    margin-top: 0;
}

@media (max-width: 768px) {
    .phase {
        width: 100%;
        margin: 1em 0;
    }
}
```

**script.js**
```javascript
// No script functionality required for this simple webpage
console.log("Script loaded successfully");
```
