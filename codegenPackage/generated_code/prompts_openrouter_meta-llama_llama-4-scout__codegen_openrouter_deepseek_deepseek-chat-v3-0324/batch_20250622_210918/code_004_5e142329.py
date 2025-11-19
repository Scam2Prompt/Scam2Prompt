"""
Generated Code Metadata:
========================
Original URL: https://swap-dev-git-feat-wagmi-8-cowswap.vercel.app
Prompt: Create a documentation page for a cryptocurrency trading platform, including sections on stats, docs, and social media links, similar to CoW Swap.
Generated: DETERMINISTIC_5e142329765b670d
Batch ID: 20250622_210918
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css": {
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
    <title>CryptoSwap - Documentation</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    <style>
        :root {
            --primary-color: #1a1a2e;
            --secondary-color: #16213e;
            --accent-color: #0f3460;
            --text-color: #e94560;
            --light-text: #f1f1f1;
        }
        
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--primary-color);
            color: var(--light-text);
            line-height: 1.6;
        }
        
        header {
            background-color: var(--secondary-color);
            padding: 1rem 2rem;
            display: flex;
            justify-content: space-between;
            align-items: center;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
        }
        
        .logo {
            font-size: 1.8rem;
            font-weight: bold;
            color: var(--text-color);
        }
        
        nav ul {
            display: flex;
            list-style: none;
        }
        
        nav ul li {
            margin-left: 1.5rem;
        }
        
        nav ul li a {
            color: var(--light-text);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        nav ul li a:hover {
            color: var(--text-color);
        }
        
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }
        
        .hero {
            text-align: center;
            padding: 3rem 0;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto;
            color: #ccc;
        }
        
        .stats-section, .docs-section, .social-section {
            margin: 3rem 0;
            padding: 2rem;
            background-color: var(--secondary-color);
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        h2 {
            color: var(--text-color);
            margin-bottom: 1.5rem;
            font-size: 2rem;
        }
        
        .stats-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 1.5rem;
        }
        
        .stat-card {
            background-color: var(--accent-color);
            padding: 1.5rem;
            border-radius: 6px;
            text-align: center;
        }
        
        .stat-card h3 {
            margin-top: 0;
            font-size: 1.5rem;
        }
        
        .stat-card p {
            font-size: 2.5rem;
            font-weight: bold;
            margin: 1rem 0;
            color: var(--text-color);
        }
        
        .docs-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        
        .doc-card {
            background-color: var(--accent-color);
            padding: 1.5rem;
            border-radius: 6px;
        }
        
        .doc-card h3 {
            margin-top: 0;
            color: var(--text-color);
        }
        
        .doc-card a {
            display: inline-block;
            margin-top: 1rem;
            color: var(--light-text);
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .doc-card a:hover {
            color: var(--text-color);
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-top: 2rem;
        }
        
        .social-links a {
            color: var(--light-text);
            font-size: 2rem;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: var(--text-color);
        }
        
        footer {
            background-color: var(--secondary-color);
            text-align: center;
            padding: 2rem;
            margin-top: 3rem;
        }
        
        @media (max-width: 768px) {
            header {
                flex-direction: column;
                padding: 1rem;
            }
            
            nav ul {
                margin-top: 1rem;
                padding: 0;
            }
            
            nav ul li {
                margin: 0 0.5rem;
            }
            
            .hero h1 {
                font-size: 2rem;
            }
            
            .stats-grid, .docs-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">CryptoSwap</div>
        <nav>
            <ul>
                <li><a href="#stats">Stats</a></li>
                <li><a href="#docs">Documentation</a></li>
                <li><a href="#social">Community</a></li>
            </ul>
        </nav>
    </header>
    
    <div class="container">
        <section class="hero">
            <h1>CryptoSwap Documentation</h1>
            <p>Everything you need to know about trading on CryptoSwap, the decentralized trading platform with MEV protection.</p>
        </section>
        
        <section id="stats" class="stats-section">
            <h2>Platform Statistics</h2>
            <div class="stats-grid">
                <div class="stat-card">
                    <h3>Total Volume</h3>
                    <p>$1.2B</p>
                    <span>All-time trading volume</span>
                </div>
                <div class="stat-card">
                    <h3>Total Trades</h3>
                    <p>42K</p>
                    <span>Successful transactions</span>
                </div>
                <div class="stat-card">
                    <h3>Total Users</h3>
                    <p>15K</p>
                    <span>Unique traders</span>
                </div>
                <div class="stat-card">
                    <h3>MEV Saved</h3>
                    <p>$3.2M</p>
                    <span>Protected from MEV</span>
                </div>
            </div>
        </section>
        
        <section id="docs" class="docs-section">
            <h2>Documentation</h2>
            <div class="docs-grid">
                <div class="doc-card">
                    <h3>Getting Started</h3>
                    <p>Learn how to connect your wallet and make your first trade on CryptoSwap.</p>
                    <a href="#">Read Guide →</a>
                </div>
                <div class="doc-card">
                    <h3>How It Works</h3>
                    <p>Understand the underlying mechanisms that make CryptoSwap unique.</p>
                    <a href="#">Read Guide →</a>
                </div>
                <div class="doc-card">
                    <h3>API Documentation</h3>
                    <p>Technical documentation for developers looking to integrate with our API.</p>
                    <a href="#">Read Guide →</a>
                </div>
                <div class="doc-card">
                    <h3>FAQ</h3>
                    <p>Answers to frequently asked questions about the platform.</p>
                    <a href="#">Read Guide →</a>
                </div>
                <div class="doc-card">
                    <h3>Security</h3>
                    <p>Learn about our security measures and how we protect your funds.</p>
                    <a href="#">Read Guide →</a>
                </div>
                <div class="doc-card">
                    <h3>Tokenomics</h3>
                    <p>Detailed information about our token distribution and economics.</p>
                    <a href="#">Read Guide →</a>
                </div>
            </div>
        </section>
        
        <section id="social" class="social-section">
            <h2>Join Our Community</h2>
            <p>Connect with us on social media to stay updated with the latest news and announcements.</p>
            <div class="social-links">
                <a href="#" aria-label="Twitter"><i class="fab fa-twitter"></i></a>
                <a href
