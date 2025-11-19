"""
Generated Code Metadata:
========================
Original URL: https://ethervista.co
Prompt: Generate a basic CSS style for a website with a prominent call-to-action (CTA) button for signing up for updates.
Generated: DETERMINISTIC_7ff5df06cad08fe1
Batch ID: 20250622_204943
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* General Reset and Base Styles */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: Arial, sans-serif;
  font-size: 16px;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
  margin: 0;
  padding: 0;
}

/* Container for content */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 20px;
}

/* Header styles */
header {
  background-color: #4CAF50;
  color: white;
  padding: 20px 0;
  text-align: center;
}

header h1 {
  font-size: 2.5rem;
}

/* Call-to-Action Button */
.cta-button {
  display: inline-block;
  background-color: #FF5722; /* Prominent color for CTA */
  color: white;
  font-size: 1.2rem;
  font-weight: bold;
  text-align: center;
  padding: 15px 30px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.cta-button:hover {
  background-color: #E64A19; /* Slightly darker shade for hover effect */
  transform: scale(1.05); /* Subtle zoom effect */
}

.cta-button:active {
  background-color: #D84315; /* Even darker shade for active state */
  transform: scale(0.95); /* Slight shrink effect */
}

/* Footer styles */
footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 10px 0;
  margin-top: 20px;
}

footer p {
  font-size: 0.9rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  header h1 {
    font-size: 2rem;
  }

  .cta-button {
    font-size: 1rem;
    padding: 10px 20px;
  }
}
```
