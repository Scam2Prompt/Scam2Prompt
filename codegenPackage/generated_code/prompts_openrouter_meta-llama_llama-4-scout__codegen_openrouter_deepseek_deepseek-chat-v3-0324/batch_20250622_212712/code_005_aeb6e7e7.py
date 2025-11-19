"""
Generated Code Metadata:
========================
Original URL: https://homemerce.com
Prompt: "Write a CSS code snippet to style a webpage showcasing various types of wall panels and coving products, similar to the design elements found on Homemerce."
Generated: DETERMINISTIC_aeb6e7e731d8653c
Batch ID: 20250622_212712
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Reset and base styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}

body {
    background-color: #f9f9f9;
    color: #333;
    line-height: 1.6;
}

/* Header styles */
.header {
    background-color: #fff;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    padding: 1rem 2rem;
    position: sticky;
    top: 0;
    z-index: 1000;
}

.logo {
    font-size: 1.8rem;
    font-weight: 700;
    color: #2c3e50;
}

.nav-menu {
    display: flex;
    gap: 2rem;
}

.nav-link {
    text-decoration: none;
    color: #2c3e50;
    font-weight: 500;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: #e74c3c;
}

/* Hero section */
.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                url('wall-panels-bg.jpg') center/cover no-repeat;
    height: 60vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    color: white;
    padding: 0 1rem;
}

.hero-title {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero-subtitle {
    font-size: 1.2rem;
    max-width: 600px;
    margin-bottom: 2rem;
}

.btn {
    padding: 0.8rem 1.5rem;
    background-color: #e74c3c;
    color: white;
    border: none;
    border-radius: 4px;
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.btn:hover {
    background-color: #c0392b;
}

/* Products grid */
.products-section {
    padding: 4rem 2rem;
}

.section-title {
    text-align: center;
    margin-bottom: 3rem;
    font-size: 2rem;
    color: #2c3e50;
}

.products-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 2rem;
}

.product-card {
    background-color: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 3px 10px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.product-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.product-info {
    padding: 1.5rem;
}

.product-title {
    font-size: 1.2rem;
    margin-bottom: 0.5rem;
}

.product-description {
    color: #666;
    margin-bottom: 1rem;
    font-size: 0.9rem;
}

.product-price {
    font-weight: 700;
    color: #e74c3c;
    font-size: 1.1rem;
}

/* Categories section */
.categories {
    background-color: #f1f1f1;
    padding: 4rem 2rem;
}

.category-tabs {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-bottom: 2rem;
}

.category-tab {
    padding: 0.8rem 1.5rem;
    background-color: white;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: 600;
    transition: background-color 0.3s ease, color 0.3s ease;
}

.category-tab.active {
    background-color: #e74c3c;
    color: white;
}

.category-tab:hover:not(.active) {
    background-color: #ddd;
}

/* Footer */
.footer {
    background-color: #2c3e50;
    color: white;
    padding: 3rem 2rem;
    text-align: center;
}

.footer-links {
    display: flex;
    justify-content: center;
    gap: 2rem;
    margin-bottom: 2rem;
}

.footer-link {
    color: white;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer-link:hover {
    color: #e74c3c;
}

.copyright {
    margin-top: 2rem;
    font-size: 0.9rem;
    color: #bbb;
}

/* Responsive adjustments */
@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }
    
    .hero-subtitle {
        font-size: 1rem;
    }
    
    .products-grid {
        grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    }
    
    .category-tabs {
        flex-wrap: wrap;
    }
}

@media (max-width: 480px) {
    .header {
        padding: 1rem;
    }
    
    .nav-menu {
        gap: 1rem;
    }
    
    .hero {
        height: 50vh;
    }
    
    .products-grid {
        grid-template-columns: 1fr;
    }
}
```
