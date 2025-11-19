"""
Generated Code Metadata:
========================
Original URL: https://www.sundancespasadvantage.com
Prompt: Generate a CSS stylesheet to design a professional showroom display layout for a Sundance Spas retailer website, focusing on branding and product presentation.
Generated: DETERMINISTIC_d7022f82b431fefb
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Sundance Spas Showroom Display Stylesheet */
/* Version: 1.0 */
/* Author: Professional Developer */
/* Date: [Current Date] */

:root {
    /* Brand Colors */
    --primary-color: #0056b3;
    --secondary-color: #e8f4ff;
    --accent-color: #ff6b00;
    --text-color: #333;
    --light-text: #fff;
    --background-color: #f9f9f9;
    --border-color: #ddd;
    
    /* Spacing */
    --spacing-small: 8px;
    --spacing-medium: 16px;
    --spacing-large: 32px;
    --spacing-xlarge: 64px;
    
    /* Typography */
    --font-main: 'Open Sans', sans-serif;
    --font-heading: 'Montserrat', sans-serif;
    --font-size-base: 16px;
    --font-size-large: 24px;
    --font-size-xlarge: 36px;
    --font-size-xxlarge: 48px;
}

/* Base Styles */
body {
    font-family: var(--font-main);
    font-size: var(--font-size-base);
    color: var(--text-color);
    background-color: var(--background-color);
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Header Styles */
.header {
    background-color: var(--primary-color);
    color: var(--light-text);
    padding: var(--spacing-medium) 0;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.header-container {
    max-width: 1200px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 var(--spacing-medium);
}

.logo {
    font-family: var(--font-heading);
    font-size: var(--font-size-xlarge);
    font-weight: 700;
    color: var(--light-text);
    text-decoration: none;
}

.nav-menu {
    display: flex;
    gap: var(--spacing-large);
}

.nav-link {
    color: var(--light-text);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: var(--accent-color);
}

/* Hero Section */
.hero {
    background: linear-gradient(rgba(0, 86, 179, 0.8), rgba(0, 86, 179, 0.8)), 
                url('spa-showroom-hero.jpg') center/cover no-repeat;
    height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: var(--light-text);
    padding: 0 var(--spacing-medium);
}

.hero-content {
    max-width: 800px;
}

.hero-title {
    font-family: var(--font-heading);
    font-size: var(--font-size-xxlarge);
    margin-bottom: var(--spacing-medium);
}

.hero-subtitle {
    font-size: var(--font-size-large);
    margin-bottom: var(--spacing-large);
}

/* Product Showcase */
.showroom-section {
    padding: var(--spacing-xlarge) var(--spacing-medium);
    max-width: 1200px;
    margin: 0 auto;
}

.section-title {
    font-family: var(--font-heading);
    font-size: var(--font-size-xlarge);
    text-align: center;
    margin-bottom: var(--spacing-xlarge);
    color: var(--primary-color);
}

.product-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: var(--spacing-large);
    margin-top: var(--spacing-large);
}

.product-card {
    background: var(--light-text);
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.15);
}

.product-image {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.product-info {
    padding: var(--spacing-medium);
}

.product-name {
    font-family: var(--font-heading);
    font-size: var(--font-size-large);
    margin-bottom: var(--spacing-small);
    color: var(--primary-color);
}

.product-features {
    margin-bottom: var(--spacing-medium);
    color: var(--text-color);
}

.product-price {
    font-weight: 700;
    color: var(--accent-color);
    font-size: var(--font-size-large);
}

/* Call to Action */
.cta-section {
    background-color: var(--secondary-color);
    padding: var(--spacing-xlarge) var(--spacing-medium);
    text-align: center;
}

.cta-title {
    font-family: var(--font-heading);
    font-size: var(--font-size-xlarge);
    margin-bottom: var(--spacing-medium);
    color: var(--primary-color);
}

.cta-button {
    display: inline-block;
    background-color: var(--accent-color);
    color: var(--light-text);
    padding: var(--spacing-medium) var(--spacing-large);
    border-radius: 4px;
    text-decoration: none;
    font-weight: 600;
    transition: background-color 0.3s ease;
}

.cta-button:hover {
    background-color: darken(var(--accent-color), 10%);
}

/* Footer */
.footer {
    background-color: var(--primary-color);
    color: var(--light-text);
    padding: var(--spacing-large) var(--spacing-medium);
    text-align: center;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: var(--spacing-large);
}

.footer-section h3 {
    font-family: var(--font-heading);
    margin-bottom: var(--spacing-medium);
}

.footer-links {
    list-style: none;
    padding: 0;
}

.footer-links li {
    margin-bottom: var(--spacing-small);
}

.footer-links a {
    color: var(--light-text);
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-links a:hover {
    color: var(--accent-color);
}

.copyright {
    margin-top: var(--spacing-large);
    padding-top: var(--spacing-medium);
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .header-container {
        flex-direction: column;
        gap: var(--spacing-medium);
    }
    
    .nav-menu {
        flex-direction: column;
        gap: var(--spacing-small);
        align-items: center;
    }
    
    .hero-title {
        font-size: var(--font-size-xlarge);
    }
    
    .hero-subtitle {
        font-size: var(--font-size-base);
    }
    
    .product-grid {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 480px) {
    .hero-title {
        font-size: var(--font-size-large);
    }
    
    .section-title {
        font-size: var(--font-size-large);
    }
    
    .footer-content {
        grid-template-columns: 1fr;
    }
}
```
