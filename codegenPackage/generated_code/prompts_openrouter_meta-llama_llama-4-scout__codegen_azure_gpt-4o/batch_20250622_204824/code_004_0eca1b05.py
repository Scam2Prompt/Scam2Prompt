"""
Generated Code Metadata:
========================
Original URL: https://metamaks.xyz
Prompt: Create a CSS style sheet for a website that offers interior and exterior design services, incorporating colors and layouts similar to those on the AYOFT website.
Generated: DETERMINISTIC_0eca1b0518debfc3
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
  Stylesheet for Interior and Exterior Design Services Website
  Author: [Your Name]
  Created: [Date]
  Description: This CSS file defines the layout, colors, and typography for a professional design services website.
*/

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Root Variables for Colors and Fonts */
:root {
  --primary-color: #2A2A2A; /* Dark gray for text and accents */
  --secondary-color: #F5F5F5; /* Light gray for backgrounds */
  --accent-color: #E63946; /* Red for highlights and buttons */
  --neutral-color: #A8DADC; /* Soft teal for secondary accents */
  --font-family: 'Roboto', sans-serif; /* Clean and modern font */
}

/* Body Styling */
body {
  font-family: var(--font-family);
  background-color: var(--secondary-color);
  color: var(--primary-color);
  line-height: 1.6;
}

/* Header Styling */
header {
  background-color: var(--primary-color);
  color: var(--secondary-color);
  padding: 20px;
  text-align: center;
}

header h1 {
  font-size: 2.5rem;
  margin-bottom: 10px;
}

header nav {
  margin-top: 10px;
}

header nav a {
  color: var(--neutral-color);
  text-decoration: none;
  margin: 0 15px;
  font-size: 1.1rem;
}

header nav a:hover {
  color: var(--accent-color);
}

/* Main Content Styling */
main {
  padding: 20px;
}

main h2 {
  font-size: 2rem;
  margin-bottom: 15px;
  color: var(--accent-color);
}

main p {
  margin-bottom: 20px;
}

/* Section Styling */
section {
  margin-bottom: 40px;
}

section h3 {
  font-size: 1.8rem;
  margin-bottom: 10px;
  color: var(--primary-color);
}

section .content {
  display: flex;
  gap: 20px;
}

section .content div {
  flex: 1;
  background-color: var(--neutral-color);
  padding: 15px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

section .content div:hover {
  background-color: var(--accent-color);
  color: var(--secondary-color);
}

/* Footer Styling */
footer {
  background-color: var(--primary-color);
  color: var(--secondary-color);
  text-align: center;
  padding: 15px;
}

footer p {
  font-size: 0.9rem;
}

/* Button Styling */
button {
  background-color: var(--accent-color);
  color: var(--secondary-color);
  border: none;
  padding: 10px 20px;
  font-size: 1rem;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: var(--neutral-color);
  color: var(--primary-color);
}

/* Responsive Design */
@media (max-width: 768px) {
  header h1 {
    font-size: 2rem;
  }

  header nav a {
    font-size: 1rem;
  }

  main h2 {
    font-size: 1.8rem;
  }

  section .content {
    flex-direction: column;
  }
}
```
