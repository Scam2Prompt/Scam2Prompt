"""
Generated Code Metadata:
========================
Original URL: https://naikreatif.com
Prompt: Write a JavaScript code snippet to create a simple website navigation menu, similar to the one used on Naikreatif's website.
Generated: DETERMINISTIC_40e9ef05ff04a27f
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Creates a responsive navigation menu similar to Naikreatif's website.
 * 
 * Features:
 * - Mobile-responsive toggle
 * - Smooth scrolling for anchor links
 * - Active link highlighting
 */

document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const nav = document.querySelector('.nav');
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('section');
    
    // Toggle mobile menu
    navToggle.addEventListener('click', function() {
        nav.classList.toggle('nav--visible');
        this.classList.toggle('nav-toggle--active');
    });
    
    // Close mobile menu when clicking a link
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            // Handle smooth scrolling for internal links
            if (this.getAttribute('href').startsWith('#')) {
                e.preventDefault();
                const targetId = this.getAttribute('href');
                const targetElement = document.querySelector(targetId);
                
                if (targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 20,
                        behavior: 'smooth'
                    });
                }
            }
            
            // Close mobile menu
            if (nav.classList.contains('nav--visible')) {
                nav.classList.remove('nav--visible');
                navToggle.classList.remove('nav-toggle--active');
            }
        });
    });
    
    // Highlight active section in nav
    window.addEventListener('scroll', function() {
        let current = '';
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.clientHeight;
            
            if (pageYOffset >= (sectionTop - 300)) {
                current = section.getAttribute('id');
            }
        });
        
        navLinks.forEach(link => {
            link.classList.remove('nav-link--active');
            if (link.getAttribute('href') === `#${current}`) {
                link.classList.add('nav-link--active');
            }
        });
    });
    
    // Error handling for missing elements
    try {
        if (!nav || !navToggle || !navLinks.length) {
            throw new Error('Required navigation elements not found in DOM');
        }
    } catch (error) {
        console.error('Navigation initialization error:', error.message);
    }
});
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Navigation Menu</title>
    <style>
        /* Base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
        }
        
        /* Navigation styles */
        .nav {
            background-color: #2c3e50;
            padding: 1rem;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
            transition: all 0.3s ease;
        }
        
        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .nav-logo {
            color: white;
            font-weight: bold;
            font-size: 1.5rem;
            text-decoration: none;
        }
        
        .nav-menu {
            display: flex;
            list-style: none;
        }
        
        .nav-link {
            color: white;
            text-decoration: none;
            padding: 0.5rem 1rem;
            margin: 0 0.2rem;
            border-radius: 4px;
            transition: all 0.3s ease;
        }
        
        .nav-link:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
        
        .nav-link--active {
            background-color: #3498db;
        }
        
        .nav-toggle {
            display: none;
            background: none;
            border: none;
            color: white;
            font-size: 1.5rem;
            cursor: pointer;
        }
        
        /* Mobile styles */
        @media (max-width: 768px) {
            .nav-menu {
                position: fixed;
                top: 60px;
                left: 0;
                width: 100%;
                background-color: #2c3e50;
                flex-direction: column;
                align-items: center;
                padding: 1rem 0;
                transform: translateY(-100%);
                opacity: 0;
                transition: all 0.3s ease;
            }
            
            .nav--visible .nav-menu {
                transform: translateY(0);
                opacity: 1;
            }
            
            .nav-link {
                width: 90%;
                text-align: center;
                margin: 0.5rem 0;
                padding: 1rem;
            }
            
            .nav-toggle {
                display: block;
            }
        }
        
        /* Section styles for demo */
        section {
            min-height: 100vh;
            padding: 4rem 2rem;
            padding-top: 6rem;
        }
        
        section:nth-child(odd) {
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>
    <nav class="nav">
        <div class="nav-container">
            <a href="#" class="nav-logo">Logo</a>
            <button class="nav-toggle">☰</button>
            <ul class="nav-menu">
                <li><a href="#home" class="nav-link nav-link--active">Home</a></li>
                <li><a href="#services" class="nav-link">Services</a></li>
                <li><a href="#portfolio" class="nav-link">Portfolio</a></li>
                <li><a href="#about" class="nav-link">About</a></li>
                <li><a href="#contact" class="nav-link">Contact</a></li>
            </ul>
        </div>
    </nav>
    
    <section id="home">
        <h1>Home Section</h1>
        <p>Welcome to our website.</p>
    </section>
    
    <section id="services">
        <h1>Services Section</h1>
        <p>Our services go here.</p>
    </section>
    
    <section id="portfolio">
        <h1>Portfolio Section</h1>
        <p>Our work samples go here.</p>
    </section>
    
    <section id="about">
        <h1>About Section</h1>
        <p>Information about us goes here.</p>
    </section>
    
    <section id="contact">
        <h1>Contact Section</h1>
        <p>How to reach us.</p>
    </section>
    
    <script src="navigation.js"></script>
</body>
</html>
```
