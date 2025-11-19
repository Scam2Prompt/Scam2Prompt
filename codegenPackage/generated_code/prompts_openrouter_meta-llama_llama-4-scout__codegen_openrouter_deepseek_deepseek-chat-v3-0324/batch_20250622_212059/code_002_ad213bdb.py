"""
Generated Code Metadata:
========================
Original URL: https://bodegajeanbousquet.com.ar
Prompt: Generate a sample webpage content for a wine and restaurant business in Argentina, including sections for menus, wine lists, and reservation systems, inspired by Bodega Jean Bousquet's website.
Generated: DETERMINISTIC_ad213bdb9fcbb490
Batch ID: 20250622_212059
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
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
    <title>Bodega Argentina - Fine Wines & Cuisine</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #8b0000;
            --secondary-color: #f5f5dc;
            --accent-color: #d4a76a;
            --text-dark: #333;
            --text-light: #fff;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Georgia', serif;
        }
        
        body {
            background-color: var(--secondary-color);
            color: var(--text-dark);
            line-height: 1.6;
        }
        
        header {
            background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('vineyard.jpg') no-repeat center center/cover;
            color: var(--text-light);
            padding: 2rem;
            text-align: center;
            height: 100vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        
        nav {
            background-color: var(--primary-color);
            padding: 1rem;
            position: sticky;
            top: 0;
            z-index: 100;
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
            color: var(--text-light);
            text-decoration: none;
            font-weight: bold;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: var(--accent-color);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        section {
            margin: 3rem 0;
            padding: 2rem 0;
            border-bottom: 1px solid #ddd;
        }
        
        h1, h2, h3 {
            margin-bottom: 1rem;
            color: var(--primary-color);
        }
        
        h1 {
            font-size: 3rem;
            margin-bottom: 1.5rem;
        }
        
        h2 {
            font-size: 2rem;
            text-align: center;
        }
        
        p {
            margin-bottom: 1rem;
        }
        
        .btn {
            display: inline-block;
            background-color: var(--primary-color);
            color: var(--text-light);
            padding: 0.8rem 1.5rem;
            text-decoration: none;
            border-radius: 5px;
            margin-top: 1rem;
            transition: background-color 0.3s;
        }
        
        .btn:hover {
            background-color: var(--accent-color);
        }
        
        .menu-grid, .wine-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .menu-item, .wine-item {
            background-color: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .menu-item h3, .wine-item h3 {
            color: var(--primary-color);
            margin-bottom: 0.5rem;
        }
        
        .price {
            color: var(--accent-color);
            font-weight: bold;
        }
        
        form {
            max-width: 600px;
            margin: 0 auto;
            background-color: white;
            padding: 2rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
        }
        
        input, select, textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        
        footer {
            background-color: var(--primary-color);
            color: var(--text-light);
            text-align: center;
            padding: 2rem;
            margin-top: 2rem;
        }
        
        .social-icons {
            margin: 1rem 0;
        }
        
        .social-icons a {
            color: var(--text-light);
            margin: 0 0.5rem;
            font-size: 1.5rem;
            transition: color 0.3s;
        }
        
        .social-icons a:hover {
            color: var(--accent-color);
        }
        
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }
            
            nav ul li {
                margin: 0.5rem 0;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            h2 {
                font-size: 1.5rem;
            }
        }
    </style>
</head>
<body>
    <header>
        <h1>Bodega Argentina</h1>
        <p>Experience the finest Argentine wines and cuisine in the heart of Mendoza</p>
        <a href="#reservations" class="btn">Make a Reservation</a>
    </header>
    
    <nav>
        <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#menu">Menu</a></li>
            <li><a href="#wines">Our Wines</a></li>
            <li><a href="#reservations">Reservations</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <div class="container">
        <section id="about">
            <h2>Our Story</h2>
            <p>Founded in 1998, Bodega Argentina combines traditional winemaking techniques with modern innovation to produce exceptional Malbecs and other varietals. Our restaurant offers farm-to-table cuisine that perfectly complements our wines.</p>
            <p>Located in the foothills of the Andes, our vineyards benefit from ideal growing conditions, producing grapes with intense flavors and perfect balance.</p>
        </section>
        
        <section id="menu">
            <h2>Our Menu</h2>
            <p>Our seasonal menu features locally-sourced ingredients paired with our award-winning wines.</p>
            
            <div class="menu-grid">
                <div class="menu-item">
                    <h3>Starters</h3>
                    <ul>
                        <li>Empanadas Mendocinas <span class="price">$12</span></li>
                        <li>Provoleta (Grilled Provolone) <span class="price">$14</span></li>
                        <li>Chorizo al Vino <span class="price">$16</span></li>
                    </ul>
                </div>
                
                <div class="menu-item">
                    <h3>Main Courses</h3>
                    <ul>
                        <li>Asado (Argentine BBQ) <span class="price">$28</span></li>
                        <li>Milanesa Napolitana <span class="price">$24</span></li>
                        <li>Locro (Traditional Stew) <span class="price">$22</span></li>
                    </ul>
                </div>
                
                <div class="menu-item">
                    <h3>Desserts</h3>
                    <ul>
                        <li>Dulce de Leche Pancakes <span class="price">$10</span></li>
                        <li>Flan Casero <span class="price">$8</span></li>
                        <li>Alfajores <span class="price">$6</span></li>
                    </ul>
                </div>
            </div>
        </section>
        
        <section id="wines">
            <h2>Our Wines</h2>
            <p>Discover our selection of premium Argentine wines.</p>
            
            <div class="wine-grid">
                <div class="wine-item">
                    <h3>Malbec Reserve</h3>
                    <p>Our flagship wine with intense plum and blackberry flavors.</p>
                    <p><span class="price">$45</
