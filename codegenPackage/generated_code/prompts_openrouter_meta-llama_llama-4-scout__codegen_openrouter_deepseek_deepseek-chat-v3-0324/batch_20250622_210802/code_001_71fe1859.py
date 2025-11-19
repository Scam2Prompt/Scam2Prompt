"""
Generated Code Metadata:
========================
Original URL: https://cooperativacooprometa.com
Prompt: Generate a simple webpage layout for a cooperative organization that offers financial solutions, event management, and knowledge base resources.
Generated: DETERMINISTIC_71fe18596cc04083
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cooperative Solutions Hub</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
            padding: 0.5rem 0;
        }
        
        nav ul li {
            margin: 0 1rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: #3498db;
        }
        
        /* Main content styles */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        .hero {
            background-color: #3498db;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
            border-radius: 5px;
            margin-bottom: 2rem;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-bottom: 2rem;
        }
        
        .service-card {
            background-color: white;
            border-radius: 5px;
            padding: 1.5rem;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: transform 0.3s;
        }
        
        .service-card:hover {
            transform: translateY(-5px);
        }
        
        .service-card h3 {
            color: #2c3e50;
            margin-bottom: 1rem;
            font-size: 1.5rem;
        }
        
        .service-card p {
            margin-bottom: 1rem;
        }
        
        .btn {
            display: inline-block;
            background-color: #3498db;
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 3px;
            text-decoration: none;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #2980b9;
        }
        
        /* Footer styles */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1.5rem 0;
            margin-top: 2rem;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            margin-bottom: 1rem;
        }
        
        .footer-links a {
            color: white;
            margin: 0 1rem;
            text-decoration: none;
        }
        
        .footer-links a:hover {
            text-decoration: underline;
        }
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
            
            .services {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Cooperative Solutions Hub</div>
        <nav>
            <ul>
                <li><a href="#financial">Financial Solutions</a></li>
                <li><a href="#events">Event Management</a></li>
                <li><a href="#knowledge">Knowledge Base</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="container">
        <section class="hero">
            <h1>Empowering Communities Through Cooperation</h1>
            <p>Providing financial solutions, event management, and knowledge resources to help your organization thrive.</p>
            <a href="#contact" class="btn">Get Started</a>
        </section>
        
        <section id="services" class="services">
            <div class="service-card" id="financial">
                <h3>Financial Solutions</h3>
                <p>Access cooperative banking, loans, and investment opportunities tailored to your needs.</p>
                <a href="#financial" class="btn">Learn More</a>
            </div>
            
            <div class="service-card" id="events">
                <h3>Event Management</h3>
                <p>Professional planning and execution of cooperative meetings, conferences, and community events.</p>
                <a href="#events" class="btn">Learn More</a>
            </div>
            
            <div class="service-card" id="knowledge">
                <h3>Knowledge Base</h3>
                <p>Educational resources, training materials, and best practices for cooperative success.</p>
                <a href="#knowledge" class="btn">Learn More</a>
            </div>
        </section>
    </div>
    
    <footer>
        <div class="footer-links">
            <a href="#privacy">Privacy Policy</a>
            <a href="#terms">Terms of Service</a>
            <a href="#faq">FAQ</a>
        </div>
        <p>&copy; 2023 Cooperative Solutions Hub. All rights reserved.</p>
    </footer>
</body>
</html>
```
