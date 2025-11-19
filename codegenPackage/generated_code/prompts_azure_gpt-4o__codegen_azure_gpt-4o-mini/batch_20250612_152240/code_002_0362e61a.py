"""
Generated Code Metadata:
========================
Original URL: https://emfresh2o-digitalres-preprocessing1.netlify.app
Prompt: Generate a CSS stylesheet that aligns with the design principles mentioned in the EMFresh2o portfolio, focusing on modern aesthetics and responsive design.
Generated: DETERMINISTIC_0362e61a5a40c3aa
Batch ID: 20250612_152240
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* EMFresh2o Portfolio Stylesheet */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: 'Arial', sans-serif; /* Modern font choice */
    line-height: 1.6; /* Improved readability */
    color: #333; /* Dark gray text for better contrast */
    background-color: #f4f4f4; /* Light background for a clean look */
}

/* Container for main content */
.container {
    max-width: 1200px; /* Limit the width for larger screens */
    margin: 0 auto; /* Center the container */
    padding: 20px; /* Add some padding */
}

/* Header styles */
header {
    background: #007BFF; /* Primary color for header */
    color: #fff; /* White text for contrast */
    padding: 20px 0; /* Padding for header */
    text-align: center; /* Centered text */
}

/* Navigation styles */
nav {
    margin: 20px 0; /* Margin for spacing */
}

nav ul {
    list-style: none; /* Remove bullet points */
    display: flex; /* Flexbox for horizontal layout */
    justify-content: center; /* Center navigation items */
}

nav ul li {
    margin: 0 15px; /* Spacing between items */
}

nav ul li a {
    text-decoration: none; /* Remove underline */
    color: #fff; /* White text */
    transition: color 0.3s; /* Smooth color transition */
}

nav ul li a:hover {
    color: #FFD700; /* Gold color on hover */
}

/* Main content styles */
main {
    margin: 20px 0; /* Margin for spacing */
}

/* Section styles */
section {
    background: #fff; /* White background for sections */
    border-radius: 8px; /* Rounded corners */
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1); /* Subtle shadow */
    padding: 20px; /* Padding for sections */
    margin-bottom: 20px; /* Spacing between sections */
}

/* Footer styles */
footer {
    text-align: center; /* Centered text */
    padding: 20px 0; /* Padding for footer */
    background: #007BFF; /* Match header color */
    color: #fff; /* White text */
}

/* Responsive design */
@media (max-width: 768px) {
    nav ul {
        flex-direction: column; /* Stack items vertically on small screens */
    }

    nav ul li {
        margin: 10px 0; /* Adjust margin for vertical layout */
    }

    .container {
        padding: 10px; /* Reduce padding on smaller screens */
    }
}
```
