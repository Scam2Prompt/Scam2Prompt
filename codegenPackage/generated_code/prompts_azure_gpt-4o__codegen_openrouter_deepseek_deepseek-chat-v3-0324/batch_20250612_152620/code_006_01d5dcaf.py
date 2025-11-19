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
/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Open Sans', sans-serif;
}

body {
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

.container {
    width: 90%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

/* Header Styles */
.header {
    background-color: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    position: fixed;
    width: 100%;
    z-index: 1000;
}

.navbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
}

.logo {
    font-size: 24px;
    font-weight: 700;
    color: #2c3e50;
    text-decoration: none;
}

.nav-links {
    display: flex;
    list-style: none;
}

.nav-links li {
    margin-left: 30px;
}

.nav-links a {
    text-decoration: none;
    color: #2c3e50;
    font-weight: 600;
    transition: color 0.3s;
}

.nav-links a:hover {
    color: #e74c3c;
}

/* Hero Section */
.hero {
    height: 100vh;
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('hero-bg.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    text-align: center;
    color: #fff;
    padding-top: 80px;
}

.hero-content h1 {
    font-size: 48px;
    margin-bottom: 20px;
}

.hero-content p {
    font-size: 20px;
    margin-bottom: 30px;
}

.btn {
    display: inline-block;
    background-color: #e74c3c;
    color: #fff;
    padding: 12px 30px;
    border-radius: 4px;
    text-decoration: none;
    font-weight: 600;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: #c0392b;
}

/* Gallery Section */
.section {
    padding: 80px 0;
}

.section-title {
    text-align: center;
    margin-bottom: 50px;
}

.section-title h2 {
    font-size: 36px;
    color: #2c3e50;
    margin-bottom: 15px;
}

.section-title p {
    color: #7f8c8d;
    font-size: 18px;
}

.gallery {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 20px;
}

.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s;
}

.gallery-item:hover {
    transform: translateY(-10px);
}

.gallery-item img {
    width: 100%;
    height: 250px;
    object-fit: cover;
    display: block;
    transition: transform 0.5s;
}

.gallery-item:hover img {
    transform: scale(1.05);
}

/* Testimonials Section */
.testimonials {
    background-color: #f1f1f1;
}

.testimonial-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 30px;
}

.testimonial-card {
    background-color: #fff;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.testimonial-content {
    margin-bottom: 20px;
    font-style: italic;
    color: #555;
}

.testimonial-author {
    display: flex;
    align-items: center;
}

.testimonial-author img {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    margin-right: 15px;
    object-fit: cover;
}

.author-info h4 {
    color: #2c3e50;
    margin-bottom: 5px;
}

.author-info p {
    color: #7f8c8d;
    font-size: 14px;
}

/* Contact Section */
.contact-form {
    max-width: 600px;
    margin: 0 auto;
    background-color: #fff;
    padding: 40px;
    border-radius: 8px;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
}

.form-group {
    margin-bottom: 20px;
}

.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #2c3e50;
    font-weight: 600;
}

.form-control {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 16px;
}

textarea.form-control {
    min-height: 150px;
    resize: vertical;
}

.submit-btn {
    background-color: #e74c3c;
    color: #fff;
    border: none;
    padding: 12px 30px;
    border-radius: 4px;
    cursor: pointer;
    font-size: 16px;
    font-weight: 600;
    transition: background-color 0.3s;
}

.submit-btn:hover {
    background-color: #c0392b;
}

/* Footer */
.footer {
    background-color: #2c3e50;
    color: #fff;
    padding: 50px 0 20px;
}

.footer-content {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-bottom: 40px;
}

.footer-column h3 {
    font-size: 20px;
    margin-bottom: 20px;
}

.footer-column p {
    margin-bottom: 15px;
    color: #bdc3c7;
}

.social-links {
    display: flex;
    gap: 15px;
}

.social-links a {
    color: #fff;
    font-size: 20px;
    transition: color 0.3s;
}

.social-links a:hover {
    color: #e74c3c;
}

.copyright {
    text-align: center;
    padding-top: 20px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    color: #bdc3c7;
    font-size: 14px;
}

/* Responsive Design */
@media (max-width: 768px) {
    .navbar {
        flex-direction: column;
        padding: 15px 0;
    }

    .nav-links {
        margin-top: 15px;
    }

    .nav-links li {
        margin-left: 15px;
    }

    .hero-content h1 {
        font-size: 36px;
    }

    .hero-content p {
        font-size: 18px;
    }

    .section-title h2 {
        font-size: 30px;
    }

    .testimonial-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .nav-links {
        flex-direction: column;
        align-items: center;
    }

    .nav-links li {
        margin: 5px 0;
    }

    .hero-content h1 {
        font-size: 28px;
    }

    .gallery {
        grid-template-columns: 1fr;
    }
}
```
