"""
Generated Code Metadata:
========================
Original URL: https://prohoster.biz
Prompt: Generate code to create a landing page using ProHoster's free website builder, referencing their video tutorial for templates and SEO tools.
Generated: DETERMINISTIC_7970ec57f5b34109
Batch ID: 20250612_151752
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.youtube.com/embed/EXAMPLE": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://via.placeholder.com/1920x1080": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional landing page created with ProHoster's free website builder">
    <meta name="keywords" content="ProHoster, website builder, landing page, templates, SEO tools">
    <title>My ProHoster Landing Page</title>
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
        
        /* Navigation */
        nav {
            background-color: #34495e;
            padding: 0.5rem 0;
        }
        
        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }
        
        nav ul li {
            margin: 0 1rem;
        }
        
        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
        }
        
        /* Hero section */
        .hero {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('https://via.placeholder.com/1920x1080');
            background-size: cover;
            background-position: center;
            height: 60vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            text-align: center;
            color: white;
            padding: 0 1rem;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin-bottom: 2rem;
        }
        
        .btn {
            display: inline-block;
            background-color: #e74c3c;
            color: white;
            padding: 0.8rem 1.5rem;
            border-radius: 5px;
            text-decoration: none;
            font-weight: bold;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: #c0392b;
        }
        
        /* Features section */
        .features {
            padding: 4rem 1rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .features h2 {
            text-align: center;
            margin-bottom: 2rem;
            font-size: 2rem;
        }
        
        .features-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .feature-card {
            background-color: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .feature-card i {
            font-size: 2.5rem;
            color: #3498db;
            margin-bottom: 1rem;
        }
        
        /* Testimonials */
        .testimonials {
            background-color: #ecf0f1;
            padding: 4rem 1rem;
            text-align: center;
        }
        
        .testimonials h2 {
            margin-bottom: 2rem;
            font-size: 2rem;
        }
        
        .testimonial-card {
            max-width: 800px;
            margin: 0 auto;
            background-color: white;
            padding: 2rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 2rem 1rem;
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
        
        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
        }
    </style>
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
</head>
<body>
    <header>
        <div class="logo">MyWebsite</div>
        <p>Built with ProHoster's Free Website Builder</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#features">Features</a></li>
            <li><a href="#tutorial">Tutorial</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <section id="home" class="hero">
        <h1>Welcome to My Professional Website</h1>
        <p>Created easily with ProHoster's drag-and-drop builder and powerful SEO tools</p>
        <a href="#tutorial" class="btn">Watch Tutorial Video</a>
    </section>
    
    <section id="features" class="features">
        <h2>Why Choose ProHoster</h2>
        <div class="features-grid">
            <div class="feature-card">
                <i class="fas fa-magic"></i>
                <h3>Easy Templates</h3>
                <p>Beautiful, responsive templates that work on any device with just a few clicks.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-search"></i>
                <h3>SEO Tools</h3>
                <p>Built-in SEO optimization to help your site rank higher in search results.</p>
            </div>
            <div class="feature-card">
                <i class="fas fa-rocket"></i>
                <h3>Fast Hosting</h3>
                <p>Lightning-fast hosting included with every website for optimal performance.</p>
            </div>
        </div>
    </section>
    
    <section id="tutorial" class="testimonials">
        <h2>Learn How to Build Your Site</h2>
        <div class="testimonial-card">
            <h3>ProHoster Website Builder Tutorial</h3>
            <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin: 2rem 0;">
                <iframe 
                    style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
                    src="https://www.youtube.com/embed/EXAMPLE" 
                    frameborder="0" 
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
                    allowfullscreen>
                </iframe>
            </div>
            <p>Watch our tutorial video to learn how to create your own professional website in minutes using ProHoster's free website builder.</p>
        </div>
    </section>
    
    <footer id="contact">
        <div class="footer-links">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Contact Us</a>
        </div>
        <p>&copy; 2023 MyWebsite. All rights reserved. Built with ProHoster.</p>
    </footer>
</body>
</html>
```
