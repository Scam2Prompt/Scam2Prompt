"""
Generated Code Metadata:
========================
Original URL: https://perthrealestatephotography.com.au
Prompt: Create a CSS template for a real estate photography portfolio page that includes sections for testimonials, a gallery, and contact information, inspired by Perth Real Estate Photography's website design.
Generated: DETERMINISTIC_01d5dcafce5f6c70
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* CSS Template for Real Estate Photography Portfolio Page */

/* Reset some default browser styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
    color: #333;
}

/* Container for the entire page */
.container {
    width: 80%;
    margin: auto;
    overflow: hidden;
}

/* Header styles */
header {
    background: #35424a;
    color: #ffffff;
    padding: 20px 0;
    text-align: center;
}

/* Navigation styles */
nav {
    margin: 20px 0;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #ffffff;
    text-decoration: none;
}

/* Gallery styles */
.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 15px;
    margin: 20px 0;
}

.gallery img {
    width: 100%;
    height: auto;
    border-radius: 5px;
}

/* Testimonials section styles */
.testimonials {
    background: #e2e2e2;
    padding: 20px;
    border-radius: 5px;
    margin: 20px 0;
}

.testimonial {
    margin-bottom: 15px;
    padding: 10px;
    border-left: 5px solid #35424a;
}

/* Contact section styles */
.contact {
    background: #35424a;
    color: #ffffff;
    padding: 20px;
    border-radius: 5px;
    text-align: center;
}

.contact h2 {
    margin-bottom: 15px;
}

.contact p {
    margin: 5px 0;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #35424a;
    color: #ffffff;
    position: relative;
    bottom: 0;
    width: 100%;
}

/* Responsive styles */
@media (max-width: 768px) {
    .gallery {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }

    nav ul li {
        display: block;
        margin: 10px 0;
    }
}
```
