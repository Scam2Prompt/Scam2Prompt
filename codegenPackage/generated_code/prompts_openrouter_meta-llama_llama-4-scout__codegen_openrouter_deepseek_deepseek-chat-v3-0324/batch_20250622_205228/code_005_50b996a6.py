"""
Generated Code Metadata:
========================
Original URL: https://arbitrum-token-bridge-hq126qa8s-offchain-labs.vercel.app
Prompt: "Design a careers page for Offchain Labs, the team behind Arbitrum, highlighting opportunities in blockchain development."
Generated: DETERMINISTIC_50b996a6a3898104
Batch ID: 20250622_205228
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
    <title>Careers at Offchain Labs | Build the Future of Blockchain</title>
    <meta name="description" content="Join Offchain Labs, the team behind Arbitrum, and help shape the future of blockchain technology. Explore exciting career opportunities in blockchain development.">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary: #2b6cb0;
            --secondary: #4299e1;
            --dark: #1a202c;
            --light: #f7fafc;
            --accent: #38b2ac;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: var(--light);
            color: var(--dark);
            line-height: 1.6;
        }
        
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px 0;
        }
        
        .logo {
            font-size: 24px;
            font-weight: 700;
            color: var(--primary);
            text-decoration: none;
        }
        
        .nav-links {
            display: flex;
            gap: 30px;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--primary);
        }
        
        .hero {
            background: linear-gradient(135deg, var(--primary), var(--secondary));
            color: white;
            padding: 80px 0;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 48px;
            margin-bottom: 20px;
        }
        
        .hero p {
            font-size: 20px;
            max-width: 800px;
            margin: 0 auto 30px;
        }
        
        .btn {
            display: inline-block;
            background-color: white;
            color: var(--primary);
            padding: 12px 30px;
            border-radius: 30px;
            text-decoration: none;
            font-weight: 600;
            transition: all 0.3s;
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
        }
        
        .btn-primary {
            background-color: var(--accent);
            color: white;
        }
        
        .section {
            padding: 80px 0;
        }
        
        .section-title {
            text-align: center;
            margin-bottom: 50px;
            font-size: 36px;
            color: var(--dark);
        }
        
        .benefits {
            background-color: white;
        }
        
        .benefits-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 30px;
        }
        
        .benefit-card {
            background-color: var(--light);
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            transition: transform 0.3s;
        }
        
        .benefit-card:hover {
            transform: translateY(-10px);
        }
        
        .benefit-card i {
            font-size: 40px;
            color: var(--accent);
            margin-bottom: 20px;
        }
        
        .benefit-card h3 {
            margin-bottom: 15px;
            font-size: 22px;
        }
        
        .jobs {
            background-color: var(--light);
        }
        
        .job-list {
            max-width: 800px;
            margin: 0 auto;
        }
        
        .job-card {
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
            margin-bottom: 20px;
            transition: all 0.3s;
        }
        
        .job-card:hover {
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
        }
        
        .job-card h3 {
            font-size: 22px;
            margin-bottom: 10px;
            color: var(--primary);
        }
        
        .job-meta {
            display: flex;
            gap: 20px;
            margin-bottom: 15px;
            color: #718096;
        }
        
        .job-meta span {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        .job-description {
            margin-bottom: 20px;
        }
        
        .apply-btn {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-weight: 600;
            transition: background-color 0.3s;
        }
        
        .apply-btn:hover {
            background-color: var(--secondary);
        }
        
        footer {
            background-color: var(--dark);
            color: white;
            padding: 50px 0 20px;
            text-align: center;
        }
        
        .footer-links {
            display: flex;
            justify-content: center;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .footer-links a {
            color: white;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: var(--accent);
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-bottom: 30px;
        }
        
        .social-links a {
            color: white;
            font-size: 20px;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: var(--accent);
        }
        
        .copyright {
            color: #a0aec0;
            font-size: 14px;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 36px;
            }
            
            .hero p {
                font-size: 18px;
            }
            
            .nav-links {
                gap: 15px;
            }
            
            .section-title {
                font-size: 30px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <a href="/" class="logo">Offchain Labs</a>
                <div class="nav-links">
                    <a href="/">Home</a>
                    <a href="/about">About</a>
                    <a href="/technology">Technology</a>
                    <a href="/careers" class="active">Careers</a>
                    <a href="/blog">Blog</a>
                    <a href="/contact">Contact</a>
                </div>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Build the Future of Blockchain</h1>
            <p>Join Offchain Labs, the team behind Arbitrum, and help scale Ethereum to its full potential. We're looking for passionate individuals to shape the next generation of blockchain technology.</p>
            <a href="#open-positions" class="btn btn-primary">View Open Positions</a>
        </div>
    </section>

    <section class="section benefits">
        <div class="container">
            <h2 class="section-title">Why Join Offchain Labs?</h2>
            <div class="benefits-grid">
                <div class="benefit-card">
                    <i class="fas fa-rocket"></i>
                    <h3>Work on Cutting-Edge Tech</h3>
                    <p>Contribute to Arbitrum, the leading Ethereum scaling solution, and solve complex challenges in blockchain scalability.</p>
                </div
