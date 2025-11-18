"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://flagship.luc.edu
Prompt: Write code to implement a non-discriminatory policy notice on a university library website, similar to the one outlined on the Loyola University Chicago Libraries portal.
Generated: DETERMINISTIC_03f4b57748617a5d
Batch ID: 20250612_150615
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
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>University Library Non-Discriminatory Policy</title>
    <link rel="stylesheet" href="styles.css">
</head>

<body>
    <header>
        <h1>University Library</h1>
    </header>

    <main>
        <section class="policy-notice">
            <h2>Non-Discriminatory Policy Notice</h2>
            <p>
                The University Library is committed to providing an inclusive and welcoming environment for all members of
                our community. We do not discriminate on the basis of race, color, ethnicity, national origin, sex, gender
                identity, sexual orientation, disability, age, or religion.
            </p>
            <p>
                Our services, resources, and facilities are available to everyone without regard to these characteristics.
                We encourage all users to engage with our library services and to report any instances of discrimination
                or harassment to our staff.
            </p>
            <p>
                For more information about our commitment to equity and inclusion, please visit our <a href="inclusion-policy.html">Inclusion Policy</a>.
            </p>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 University Library. All rights reserved.</p>
    </footer>

    <script src="scripts.js"></script>
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

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #004b87; /* University color */
    color: white;
    padding: 10px 20px;
    text-align: center;
}

main {
    padding: 20px;
}

.policy-notice {
    background-color: #f9f9f9;
    border: 1px solid #ccc;
    border-radius: 5px;
    padding: 15px;
}

footer {
    text-align: center;
    padding: 10px 0;
    background-color: #004b87; /* University color */
    color: white;
    position: relative;
    bottom: 0;
    width: 100%;
}
```

```javascript
// scripts.js

// Function to display an alert for user feedback
function displayFeedback() {
    try {
        alert("Thank you for visiting the University Library. Your feedback is important to us.");
    } catch (error) {
        console.error("Error displaying feedback alert:", error);
    }
}

// Event listener for page load to display feedback
document.addEventListener("DOMContentLoaded", () => {
    displayFeedback();
});
```

This code provides a simple, clean, and functional implementation of a non-discriminatory policy notice for a university library website, adhering to best practices for HTML, CSS, and JavaScript.
