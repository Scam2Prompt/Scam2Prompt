"""
Generated Code Metadata:
========================
Original URL: https://marchigue.cl
Prompt: Write a CSS style sheet that implements high contrast and low saturation themes for a tourism website, enhancing readability for users with different visual needs, as outlined in the accessibility features of Marchigüe.
Generated: DETERMINISTIC_8ba9bb7b05628a5e
Batch ID: 20250612_155250
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* High Contrast and Low Saturation Theme for Tourism Website */
/* Accessibility-focused design for enhanced readability */

/* General Reset */
body, h1, h2, h3, h4, h5, h6, p, ul, ol, li, a, button {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif; /* Simple, readable font */
  font-size: 16px; /* Base font size */
  line-height: 1.6; /* Improved readability */
  background-color: #000; /* High contrast background */
  color: #FFF; /* High contrast text */
}

/* Header Styling */
header {
  background-color: #222; /* Dark background for header */
  color: #FFF; /* High contrast text */
  padding: 20px;
  text-align: center;
  border-bottom: 2px solid #444; /* Subtle border for separation */
}

/* Navigation Menu */
nav {
  display: flex;
  justify-content: center;
  gap: 15px;
}

nav a {
  color: #FFF; /* High contrast link text */
  text-decoration: none;
  font-weight: bold;
  padding: 10px 15px;
  border: 1px solid #444; /* Subtle border for focus */
  border-radius: 5px;
  background-color: #333; /* Low saturation background */
}

nav a:hover, nav a:focus {
  background-color: #555; /* Slightly lighter background on hover/focus */
  outline: 2px solid #FFF; /* High contrast focus outline */
}

/* Main Content */
main {
  padding: 20px;
  background-color: #111; /* Dark background for content */
  color: #EEE; /* Slightly less bright text for comfort */
}

main h1, main h2, main h3 {
  color: #FFF; /* High contrast headings */
}

main p {
  color: #DDD; /* Low saturation text for paragraphs */
}

/* Buttons */
button {
  background-color: #333; /* Low saturation background */
  color: #FFF; /* High contrast text */
  border: 1px solid #444; /* Subtle border */
  padding: 10px 20px;
  border-radius: 5px;
  cursor: pointer;
}

button:hover, button:focus {
  background-color: #555; /* Slightly lighter background on hover/focus */
  outline: 2px solid #FFF; /* High contrast focus outline */
}

/* Footer Styling */
footer {
  background-color: #222; /* Dark background for footer */
  color: #FFF; /* High contrast text */
  text-align: center;
  padding: 15px;
  border-top: 2px solid #444; /* Subtle border for separation */
}

/* Links */
a {
  color: #00FFFF; /* High contrast cyan for links */
  text-decoration: underline;
}

a:hover, a:focus {
  color: #FFD700; /* High contrast yellow on hover/focus */
  outline: 2px solid #FFF; /* High contrast focus outline */
}

/* Images */
img {
  max-width: 100%; /* Ensure images are responsive */
  height: auto;
  border: 2px solid #444; /* Subtle border for images */
}

/* Accessibility Features */
/* Focus Styles */
:focus {
  outline: 3px solid #FFD700; /* High contrast focus outline */
}

/* High Contrast Tables */
table {
  width: 100%;
  border-collapse: collapse;
  background-color: #111; /* Dark background for tables */
  color: #FFF; /* High contrast text */
}

table th, table td {
  border: 1px solid #444; /* Subtle border for cells */
  padding: 10px;
  text-align: left;
}

table th {
  background-color: #222; /* Slightly darker background for headers */
}

table tr:nth-child(even) {
  background-color: #333; /* Low saturation alternating row color */
}

table tr:nth-child(odd) {
  background-color: #111; /* Dark background for alternating rows */
}

/* Media Queries for Responsiveness */
@media (max-width: 768px) {
  nav {
    flex-direction: column;
    gap: 10px;
  }

  main {
    padding: 10px;
  }

  button {
    width: 100%; /* Full-width buttons for smaller screens */
  }
}
```
