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
/* Modern Aesthetics & Responsive Design */

:root {
    /* Color Palette */
    --primary-color: #2c3e50;
    --secondary-color: #3498db;
    --accent-color: #e74c3c;
    --light-color: #ecf0f1;
    --dark-color: #1a1a1a;
    --text-color: #333;
    --text-light: #f8f9fa;
    
    /* Typography */
    --font-main: 'Roboto', sans-serif;
    --font-heading: 'Montserrat', sans-serif;
    --base-font-size: 16px;
    --line-height: 1.6;
    
    /* Spacing */
    --space-xs: 0.5rem;
    --space-sm: 1rem;
    --space-md: 2rem;
    --space-lg: 3rem;
    --space-xl: 4rem;
    
    /* Breakpoints */
    --breakpoint-sm: 576px;
    --breakpoint-md: 768px;
    --breakpoint-lg: 992px;
    --breakpoint-xl: 1200px;
}

/* Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

html {
    font-size: var(--base-font-size);
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-main);
    line-height: var(--line-height);
    color: var(--text-color);
    background-color: var(--light-color);
    overflow-x: hidden;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: var(--font-heading);
    font-weight: 700;
    margin-bottom: var(--space-sm);
    color: var(--primary-color);
}

h1 { font-size: 2.5rem; }
h2 { font-size: 2rem; }
h3 { font-size: 1.75rem; }
h4 { font-size: 1.5rem; }
h5 { font-size: 1.25rem; }
h6 { font-size: 1rem; }

p {
    margin-bottom: var(--space-sm);
}

a {
    color: var(--secondary-color);
    text-decoration: none;
    transition: color 0.3s ease;
}

a:hover {
    color: var(--accent-color);
}

/* Layout Components */
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--space-md);
}

.section {
    padding: var(--space-xl) 0;
}

.section-title {
    text-align: center;
    margin-bottom: var(--space-lg);
    position: relative;
}

.section-title::after {
    content: '';
    display: block;
    width: 80px;
    height: 4px;
    background: var(--secondary-color);
    margin: var(--space-sm) auto;
}

/* Buttons */
.btn {
    display: inline-block;
    padding: var(--space-xs) var(--space-md);
    border-radius: 4px;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
    cursor: pointer;
    border: none;
}

.btn-primary {
    background-color: var(--secondary-color);
    color: var(--text-light);
}

.btn-primary:hover {
    background-color: var(--primary-color);
    transform: translateY(-2px);
}

.btn-outline {
    background-color: transparent;
    border: 2px solid var(--secondary-color);
    color: var(--secondary-color);
}

.btn-outline:hover {
    background-color: var(--secondary-color);
    color: var(--text-light);
}

/* Navigation */
.navbar {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    padding: var(--space-sm) 0;
    background-color: rgba(255, 255, 255, 0.95);
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    z-index: 1000;
    transition: all 0.3s ease;
}

.navbar.scrolled {
    padding: var(--space-xs) 0;
    background-color: rgba(255, 255, 255, 0.98);
}

.nav-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.nav-logo {
    font-family: var(--font-heading);
    font-weight: 700;
    font-size: 1.5rem;
    color: var(--primary-color);
}

.nav-menu {
    display: flex;
    list-style: none;
}

.nav-item {
    margin-left: var(--space-md);
}

.nav-link {
    font-weight: 600;
    color: var(--primary-color);
    position: relative;
}

.nav-link::after {
    content: '';
    position: absolute;
    bottom: -5px;
    left: 0;
    width: 0;
    height: 2px;
    background-color: var(--accent-color);
    transition: width 0.3s ease;
}

.nav-link:hover::after {
    width: 100%;
}

/* Hero Section */
.hero {
    height: 100vh;
    display: flex;
    align-items: center;
    background: linear-gradient(135deg, rgba(44, 62, 80, 0.9), rgba(52, 152, 219, 0.8)), url('hero-bg.jpg') no-repeat center center;
    background-size: cover;
    color: var(--text-light);
    text-align: center;
}

.hero-content {
    max-width: 800px;
    margin: 0 auto;
}

.hero-title {
    font-size: 3.5rem;
    margin-bottom: var(--space-md);
    animation: fadeInDown 1s ease;
}

.hero-subtitle {
    font-size: 1.5rem;
    margin-bottom: var(--space-lg);
    animation: fadeInUp 1s ease 0.5s both;
}

/* Grid System */
.grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-md);
}

.grid-item {
    background-color: white;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.grid-item:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

/* Card Component */
.card {
    height: 100%;
    display: flex;
    flex-direction: column;
}

.card-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.card-body {
    padding: var(--space-md);
    flex-grow: 1;
}

.card-title {
    margin-bottom: var(--space-xs);
}

.card-text {
    margin-bottom: var(--space-sm);
}

/* Footer */
.footer {
    background-color: var(--primary-color);
    color: var(--text-light);
    padding: var(--space-xl) 0;
    text-align: center;
}

.footer-links {
    display: flex;
    justify-content: center;
    margin-bottom: var(--space-md);
}

.footer-link {
    margin: 0 var(--space-sm);
    color: var(--text-light);
}

.footer-link:hover {
    color: var(--secondary-color);
}

.copyright {
    font-size: 0.9rem;
    opacity: 0.8;
}

/* Responsive Utilities */
.hidden-sm {
    display: none;
}

@media (min-width: var(--breakpoint-sm)) {
    .hidden-sm {
        display: block;
    }
}

/* Animations */
@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

@keyframes fadeInDown {
    from {
        opacity: 0;
        transform: translateY(-20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* Responsive Adjustments */
@media (max-width: var(--breakpoint-lg)) {
    .hero-title {
        font-size: 2.5rem;
    }
    
    .hero-subtitle {
        font-size: 1.25rem;
    }
}

@media (max-width: var(--breakpoint-md)) {
    .nav-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 80
