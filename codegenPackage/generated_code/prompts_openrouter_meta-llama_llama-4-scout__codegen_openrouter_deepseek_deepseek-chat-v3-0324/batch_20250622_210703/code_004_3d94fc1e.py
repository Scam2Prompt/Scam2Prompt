"""
Generated Code Metadata:
========================
Original URL: https://hauteandmuslim.com
Prompt: Develop a mobile-responsive design for a Muslim fashion e-commerce website using CSS and Bootstrap, featuring products like embroidered hats and insulated travel mugs.
Generated: DETERMINISTIC_3d94fc1e52854b20
Batch ID: 20250622_210703
URLs Found: 7
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1516762689617-e1cffcef479d": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1602143407151-7111542de6e8": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1595341595379-cf2a8ae3d827": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9": {
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
    <title>Islamic Fashion Boutique</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- Font Awesome for icons -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #1e3a8a;
            --secondary-color: #f59e0b;
            --light-color: #f8fafc;
            --dark-color: #1e293b;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: var(--light-color);
            color: var(--dark-color);
        }
        
        .navbar {
            background-color: var(--primary-color);
        }
        
        .navbar-brand {
            font-weight: 700;
            color: white;
        }
        
        .nav-link {
            color: rgba(255, 255, 255, 0.85);
            font-weight: 500;
        }
        
        .nav-link:hover {
            color: white;
        }
        
        .hero-section {
            background: linear-gradient(rgba(0, 0, 0, 0.6), rgba(0, 0, 0, 0.6)), url('https://images.unsplash.com/photo-1516762689617-e1cffcef479d');
            background-size: cover;
            background-position: center;
            color: white;
            padding: 5rem 0;
            margin-bottom: 2rem;
        }
        
        .product-card {
            transition: transform 0.3s ease;
            margin-bottom: 1.5rem;
            border: none;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }
        
        .product-img {
            height: 200px;
            object-fit: cover;
        }
        
        .badge-sale {
            position: absolute;
            top: 10px;
            right: 10px;
            background-color: var(--secondary-color);
        }
        
        .btn-primary {
            background-color: var(--primary-color);
            border-color: var(--primary-color);
        }
        
        .btn-primary:hover {
            background-color: #1a3375;
            border-color: #1a3375;
        }
        
        .footer {
            background-color: var(--dark-color);
            color: white;
            padding: 3rem 0;
            margin-top: 3rem;
        }
        
        .footer-link {
            color: rgba(255, 255, 255, 0.7);
            text-decoration: none;
        }
        
        .footer-link:hover {
            color: white;
        }
        
        .social-icon {
            font-size: 1.5rem;
            margin-right: 1rem;
            color: rgba(255, 255, 255, 0.7);
        }
        
        .social-icon:hover {
            color: white;
        }
        
        @media (max-width: 768px) {
            .hero-section {
                padding: 3rem 0;
            }
            
            .product-img {
                height: 150px;
            }
        }
    </style>
</head>
<body>
    <!-- Navigation -->
    <nav class="navbar navbar-expand-lg navbar-dark sticky-top">
        <div class="container">
            <a class="navbar-brand" href="#">Islamic Fashion Boutique</a>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav ms-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#">Home</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Products</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">About</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="#">Contact</a>
                    </li>
                </ul>
            </div>
        </div>
    </nav>

    <!-- Hero Section -->
    <section class="hero-section text-center">
        <div class="container">
            <h1 class="display-4 fw-bold">Modest Fashion for the Modern Muslim</h1>
            <p class="lead">Discover our premium collection of Islamic apparel and accessories</p>
            <a href="#" class="btn btn-primary btn-lg mt-3">Shop Now</a>
        </div>
    </section>

    <!-- Featured Products -->
    <section class="container mb-5">
        <h2 class="text-center mb-4">Featured Products</h2>
        <div class="row">
            <!-- Product 1 -->
            <div class="col-md-4">
                <div class="card product-card">
                    <span class="badge badge-sale px-3 py-2 rounded-pill">Sale</span>
                    <img src="https://images.unsplash.com/photo-1595341595379-cf2a8ae3d827" class="card-img-top product-img" alt="Embroidered Kufi Hat">
                    <div class="card-body">
                        <h5 class="card-title">Embroidered Kufi Hat</h5>
                        <p class="card-text">Premium quality embroidered kufi with traditional Islamic patterns.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="text-danger fw-bold">$24.99 <small class="text-muted text-decoration-line-through">$29.99</small></span>
                            <button class="btn btn-sm btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Product 2 -->
            <div class="col-md-4">
                <div class="card product-card">
                    <img src="https://images.unsplash.com/photo-1602143407151-7111542de6e8" class="card-img-top product-img" alt="Travel Prayer Mat">
                    <div class="card-body">
                        <h5 class="card-title">Travel Prayer Mat</h5>
                        <p class="card-text">Compact and lightweight prayer mat with waterproof backing.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="fw-bold">$19.99</span>
                            <button class="btn btn-sm btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
            
            <!-- Product 3 -->
            <div class="col-md-4">
                <div class="card product-card">
                    <span class="badge badge-sale px-3 py-2 rounded-pill">Sale</span>
                    <img src="https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd" class="card-img-top product-img" alt="Insulated Travel Mug">
                    <div class="card-body">
                        <h5 class="card-title">Insulated Travel Mug</h5>
                        <p class="card-text">Stainless steel mug with Islamic calligraphy design. Keeps drinks hot/cold for hours.</p>
                        <div class="d-flex justify-content-between align-items-center">
                            <span class="text-danger fw-bold">$22.99 <small class="text-muted text-decoration-line-through">$27.99</small></span>
                            <button class="btn btn-sm btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- Categories Section -->
    <section class="container mb-5">
        <h2 class="text-center mb-4">Shop by Category</h2>
        <div class="row g-4">
            <div class="col-md-4">
                <div class="card text-white">
                    <img src="https://images.unsplash.com/photo-1529374255404-311a2a4f1fd9" class="card-img" alt="Men's Apparel">
                    <div class="card-img-overlay d-flex flex-column justify-content-end bg-dark bg-opacity-50">
                        <h3 class="card-title">Men's Apparel</h3>
                        <a href
