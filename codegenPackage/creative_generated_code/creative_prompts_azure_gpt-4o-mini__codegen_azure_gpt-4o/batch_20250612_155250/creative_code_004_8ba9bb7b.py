"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marchigue.cl
Prompt: Write a CSS style sheet that implements high contrast and low saturation themes for a tourism website, enhancing readability for users with different visual needs, as outlined in the accessibility features of Marchigüe.
Generated: DETERMINISTIC_8ba9bb7b05628a5e
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```css
/* 
  High Contrast and Low Saturation Theme for Tourism Website
  Ensuring accessibility for users with varying visual needs.
  Author: [Your Name]
  Date: [Current Date]
*/

/* General Reset for Consistency Across Browsers */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body Styling */
body {
    font-family: Arial, sans-serif; /* Clean, sans-serif font for readability */
    background-color: #000; /* High contrast black background */
    color: #FFF; /* High contrast white text */
    line-height: 1.6; /* Improve readability with adequate line spacing */
}

/* Heading Styles */
h1, h2, h3, h4, h5, h6 {
    color: #FFD700; /* High contrast golden color for titles */
}

/* Link Styling */
a {
    color: #1E90FF; /* High contrast blue for links */
    text-decoration: underline; /* Clear indication that it is a link */
}

a:hover, a:focus {
    color: #FF4500; /* High contrast orange for hover and focus states */
}

/* Button Styling */
button {
    background-color: #444; /* Low saturation dark gray background */
    color: #FFF; /* High contrast white text */
    border: 2px solid #FFD700; /* High contrast golden border */
    padding: 10px 20px;
    font-size: 1rem;
    cursor: pointer;
}

button:hover, button:focus {
    background-color: #555; /* Slightly lighter gray for hover/focus state */
}

/* Input Field Styling */
input[type="text"], textarea {
    background-color: #222; /* Low saturation dark background */
    color: #FFF; /* High contrast white text */
    border: 2px solid #444; /* Low saturation border */
    padding: 10px;
    font-size: 1rem;
}

input[type="text"]:focus, textarea:focus {
    border-color: #FFD700; /* High visibility border on focus */
    outline: none; /* Remove default outline for better styling */
}

/* Accessible Navigation Bar */
nav {
    background-color: #111; /* Low saturation black for navigation bar */
    padding: 15px;
}

nav a {
    color: #FFF; /* High contrast white for navigation links */
    margin-right: 20px;
    font-size: 1.2rem;
}

nav a:hover, nav a:focus {
    color: #FFD700; /* High contrast golden color for hover/focus state */
}

/* Section Styling */
section {
    background-color: #222; /* Low saturation dark background for sections */
    padding: 20px;
    margin: 20px 0;
    border: 1px solid #444; /* Low saturation border */
}

section h2 {
    margin-bottom: 10px;
}

/* Footer Styling */
footer {
    background-color: #111; /* Low saturation black background */
    color: #FFF; /* High contrast white text */
    text-align: center;
    padding: 10px;
    border-top: 1px solid #444; /* Low saturation border */
}

/* Media Query for Responsive Font Sizes */
@media (max-width: 768px) {
    body {
        font-size: 0.9rem; /* Adjust font size for smaller screens */
    }

    nav a {
        font-size: 1rem; /* Adjust navbar link size for smaller screens */
    }
}
```
