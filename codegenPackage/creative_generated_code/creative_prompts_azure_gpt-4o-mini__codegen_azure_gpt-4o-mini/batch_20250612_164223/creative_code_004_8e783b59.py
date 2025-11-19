"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.spinecomfy.com
Prompt: Design a simple HTML form that allows users to select their preferred Spinetress mattress type and thickness, ensuring it includes options for organic and latex materials as discussed on the website.
Generated: DETERMINISTIC_8e783b593518e19c
Batch ID: 20250612_164223
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Spinetress Mattress Selection</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styling -->
    <script src="script.js" defer></script> <!-- Link to external JS for interactivity -->
</head>
<body>
    <header>
        <h1>Select Your Preferred Spinetress Mattress</h1>
    </header>
    <main>
        <form id="mattressForm">
            <fieldset>
                <legend>Choose Mattress Type</legend>

                <label for="mattressType">Mattress Type:</label>
                <select id="mattressType" name="mattressType" required>
                    <option value="" disabled selected>Select a type</option>
                    <option value="organic">Organic</option>
                    <option value="latex">Latex</option>
                </select>
            </fieldset>

            <fieldset>
                <legend>Choose Thickness</legend>

                <label for="mattressThickness">Thickness:</label>
                <select id="mattressThickness" name="mattressThickness" required>
                    <option value="" disabled selected>Select thickness</option>
                    <option value="8">8 inches</option>
                    <option value="10">10 inches</option>
                    <option value="12">12 inches</option>
                </select>
            </fieldset>

            <button type="submit">Submit</button>
        </form>
        <div id="feedback" aria-live="polite"></div> <!-- Feedback area for user submission -->
    </main>
    <footer>
        <p>&copy; 2023 Spinetress. All rights reserved.</p>
    </footer>
</body>
</html>
```

```css
/* styles.css */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 1rem;
    background-color: #f9f9f9;
}

header, footer {
    text-align: center;
}

fieldset {
    margin-bottom: 1rem;
    padding: 1rem;
    border: 1px solid #ccc;
}

button {
    padding: 0.5rem 1rem;
    background-color: #007BFF;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #0056b3;
}
```

```javascript
// script.js
document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById("mattressForm");
    const feedback = document.getElementById("feedback");

    // Handle form submission
    form.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission
        
        // Retrieve selected values
        const mattressType = form.mattressType.value;
        const mattressThickness = form.mattressThickness.value;

        // Basic validation
        if (!mattressType || !mattressThickness) {
            feedback.textContent = "Please select both mattress type and thickness.";
            return;
        }

        // Success message
        feedback.textContent = `You have selected a ${mattressThickness}-inch ${mattressType} mattress.`;
    });
});
```
