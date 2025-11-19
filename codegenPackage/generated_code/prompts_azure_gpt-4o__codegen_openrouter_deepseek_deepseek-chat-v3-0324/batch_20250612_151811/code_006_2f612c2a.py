"""
Generated Code Metadata:
========================
Original URL: https://balancer-app.pages.dev
Prompt: Create a CSS stylesheet for a restaurant website that highlights Italian cuisine, with design elements inspired by the RAVIOLI HOUSE branding.
Generated: DETERMINISTIC_2f612c2a5a1137d4
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* RAVIOLI HOUSE - Italian Restaurant Website Stylesheet */
/* Color Palette */
:root {
    --primary-color: #e63946; /* Vibrant red for passion and energy */
    --secondary-color: #f1faee; /* Creamy white for elegance */
    --accent-color: #a8dadc; /* Soft teal for contrast */
    --dark-color: #1d3557; /* Deep blue for sophistication */
    --light-color: #f8f9fa; /* Off-white for backgrounds */
    --gold-color: #ffd700; /* Gold for accents */
}

/* Base Styles */
body {
    font-family: 'Playfair Display', serif;
    background-color: var(--light-color);
    color: var(--dark-color);
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Montserrat', sans-serif;
    font-weight: 700;
    color: var(--dark-color);
}

h1 {
    font-size: 3rem;
    color: var(--primary-color);
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
}

/* Navigation */
.navbar {
    background-color: var(--secondary-color);
    border-bottom: 3px solid var(--gold-color);
    padding: 1rem 2rem;
}

.navbar-brand {
    font-family: 'Dancing Script', cursive;
    font-size: 2.5rem;
    color: var(--primary-color) !important;
}

.nav-link {
    color: var(--dark-color) !important;
    font-weight: 600;
    margin: 0 0.5rem;
    transition: color 0.3s ease;
}

.nav-link:hover {
    color: var(--primary-color) !important;
}

/* Hero Section */
.hero {
    background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), 
                url('../images/pasta-hero.jpg') no-repeat center center;
    background-size: cover;
    height: 80vh;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    color: var(--secondary-color);
}

.hero-content h1 {
    color: var(--secondary-color);
    text-shadow: 2px 2px 8px rgba(0, 0, 0, 0.8);
}

/* Menu Section */
.menu-section {
    padding: 4rem 0;
    background-color: var(--secondary-color);
}

.menu-item {
    background-color: white;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    margin-bottom: 2rem;
    overflow: hidden;
    transition: transform 0.3s ease;
}

.menu-item:hover {
    transform: translateY(-5px);
}

.menu-item img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.menu-item h3 {
    color: var(--primary-color);
    padding: 1rem;
    margin: 0;
}

.menu-item p {
    padding: 0 1rem 1rem;
    color: var(--dark-color);
}

.price {
    display: block;
    font-weight: bold;
    color: var(--gold-color);
    font-size: 1.2rem;
    padding: 0 1rem 1rem;
}

/* About Section */
.about-section {
    background-color: var(--light-color);
    padding: 4rem 0;
}

.about-content {
    max-width: 800px;
    margin: 0 auto;
    text-align: center;
}

/* Footer */
footer {
    background-color: var(--dark-color);
    color: var(--secondary-color);
    padding: 2rem 0;
    text-align: center;
}

.social-icons a {
    color: var(--secondary-color);
    font-size: 1.5rem;
    margin: 0 0.5rem;
    transition: color 0.3s ease;
}

.social-icons a:hover {
    color: var(--gold-color);
}

/* Buttons */
.btn-primary {
    background-color: var(--primary-color);
    border-color: var(--primary-color);
    color: white;
    padding: 0.5rem 1.5rem;
    font-weight: 600;
    transition: all 0.3s ease;
}

.btn-primary:hover {
    background-color: #c1121f;
    border-color: #c1121f;
    transform: translateY(-2px);
}

/* Specials Banner */
.specials-banner {
    background-color: var(--primary-color);
    color: white;
    padding: 1rem;
    text-align: center;
    font-weight: bold;
    margin-bottom: 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    h1 {
        font-size: 2rem;
    }
    
    .navbar-brand {
        font-size: 1.8rem;
    }
    
    .hero {
        height: 60vh;
    }
}

/* Animation for Menu Items */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

.menu-item {
    animation: fadeIn 0.5s ease forwards;
}

/* Delay animations for staggered effect */
.menu-item:nth-child(1) { animation-delay: 0.1s; }
.menu-item:nth-child(2) { animation-delay: 0.2s; }
.menu-item:nth-child(3) { animation-delay: 0.3s; }
.menu-item:nth-child(4) { animation-delay: 0.4s; }
```
