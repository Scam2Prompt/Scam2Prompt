"""
Generated Code Metadata:
========================
Original URL: https://craftintra.com
Prompt: Generate HTML and CSS code for a webpage showcasing instructions for making a pop-up snowman card, inspired by the content on Craft Intra.
Generated: DETERMINISTIC_a55d27d4276e9f8e
Batch ID: 20250612_152109
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
    <title>Pop-up Snowman Card Tutorial</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Pop-up Snowman Card Tutorial</h1>
    </header>
    <main>
        <section class="intro">
            <h2>Welcome to our Pop-up Snowman Card Tutorial!</h2>
            <p>Inspired by Craft Intra, we'll guide you through creating a beautiful pop-up snowman card.</p>
        </section>
        <section class="materials">
            <h2>Materials Needed:</h2>
            <ul>
                <li>White cardstock (for the card base)</li>
                <li>Colored paper (for the snowman and hat)</li>
                <li>Glue</li>
                <li>Scissors</li>
                <li> ruler or straightedge</li>
                <li>Pencil or marker</li>
            </ul>
        </section>
        <section class="instructions">
            <h2>Step-by-Step Instructions:</h2>
            <ol>
                <li>
                    <strong>Step 1: Create the Card Base</strong>
                    <p>Cut a piece of white cardstock to the desired size for your card.</p>
                </li>
                <li>
                    <strong>Step 2: Cut Out the Snowman</strong>
                    <p>Cut out three snowman body parts from colored paper: two small circles for the head and body, and one large circle for the base.</p>
                </li>
                <li>
                    <strong>Step 3: Assemble the Snowman</strong>
                    <p>Glue the snowman body parts together, starting with the base, then the body, and finally the head.</p>
                </li>
                <li>
                    <strong>Step 4: Add the Hat and Details</strong>
                    <p>Cut out a small hat from colored paper and glue it onto the snowman's head. Add details like eyes, a nose, and a mouth using a pencil or marker.</p>
                </li>
                <li>
                    <strong>Step 5: Create the Pop-up Mechanism</strong>
                    <p>Cut a small slit on either side of the snowman's base, then fold the card in half. Glue the snowman's base to the inside of the card, making sure it's centered.</p>
                </li>
                <li>
                    <strong>Step 6: Add the Final Touches</strong>
                    <p>Add any final details, such as a greeting or a signature.</p>
                </li>
            </ol>
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
    background-color: #fff;
    padding: 1em;
    margin-bottom: 1em;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1, h2 {
    color: #333;
    margin-bottom: 0.5em;
}

ul, ol {
    list-style: none;
    padding: 0;
    margin: 0;
}

li {
    margin-bottom: 0.5em;
}

strong {
    font-weight: bold;
}

ol {
    counter-reset: step;
}

li::before {
    counter-increment: step;
    content: "Step " counter(step) ": ";
    font-weight: bold;
}
```
