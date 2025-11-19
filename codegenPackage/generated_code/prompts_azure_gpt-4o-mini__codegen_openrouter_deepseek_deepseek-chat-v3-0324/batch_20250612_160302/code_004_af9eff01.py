"""
Generated Code Metadata:
========================
Original URL: https://idex.xyz
Prompt: What features should I include in a domain sale webpage to enhance user experience, inspired by Idex.xyz?
Generated: DETERMINISTIC_af9eff01b8ed94d4
Batch ID: 20250612_160302
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

Here's a clean, production-ready implementation of a domain sale webpage inspired by Idex.xyz:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Premium Domains Marketplace</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #4f46e5;
            --secondary-color: #f9fafb;
            --accent-color: #10b981;
            --text-color: #1f2937;
            --light-text: #6b7280;
            --border-color: #e5e7eb;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: var(--secondary-color);
            color: var(--text-color);
            line-height: 1.6;
        }
        
        header {
            background-color: white;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            padding: 1rem 2rem;
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        .navbar {
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary-color);
            text-decoration: none;
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--text-color);
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--primary-color);
        }
        
        .connect-wallet {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 0.375rem;
            font-weight: 500;
            cursor: pointer;
            transition: opacity 0.3s;
        }
        
        .connect-wallet:hover {
            opacity: 0.9;
        }
        
        .hero {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            color: var(--light-text);
            max-width: 700px;
            margin: 0 auto 2rem;
        }
        
        .search-container {
            display: flex;
            max-width: 600px;
            margin: 0 auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            border-radius: 0.5rem;
            overflow: hidden;
        }
        
        .search-input {
            flex: 1;
            padding: 0.75rem 1rem;
            border: 1px solid var(--border-color);
            border-right: none;
            border-radius: 0.5rem 0 0 0.5rem;
            font-size: 1rem;
        }
        
        .search-button {
            background-color: var(--primary-color);
            color: white;
            border: none;
            padding: 0 1.5rem;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .search-button:hover {
            background-color: #4338ca;
        }
        
        .filters {
            display: flex;
            justify-content: center;
            gap: 1rem;
            margin: 2rem 0;
            flex-wrap: wrap;
        }
        
        .filter-button {
            background-color: white;
            border: 1px solid var(--border-color);
            padding: 0.5rem 1rem;
            border-radius: 2rem;
            cursor: pointer;
            transition: all 0.3s;
        }
        
        .filter-button:hover, .filter-button.active {
            background-color: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }
        
        .domains-grid {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 1.5rem;
        }
        
        .domain-card {
            background-color: white;
            border-radius: 0.5rem;
            overflow: hidden;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
            transition: transform 0.3s, box-shadow 0.3s;
        }
        
        .domain-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 10px 15px rgba(0, 0, 0, 0.1);
        }
        
        .domain-name {
            padding: 1.5rem;
            border-bottom: 1px solid var(--border-color);
            font-size: 1.25rem;
            font-weight: 600;
        }
        
        .domain-details {
            padding: 1rem 1.5rem;
        }
        
        .domain-price {
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 0.5rem;
        }
        
        .domain-meta {
            display: flex;
            justify-content: space-between;
            color: var(--light-text);
            font-size: 0.875rem;
        }
        
        .buy-button {
            display: block;
            width: 100%;
            background-color: var(--accent-color);
            color: white;
            border: none;
            padding: 0.75rem;
            border-radius: 0.375rem;
            font-weight: 600;
            cursor: pointer;
            margin-top: 1rem;
            transition: background-color 0.3s;
        }
        
        .buy-button:hover {
            background-color: #0d9e6e;
        }
        
        .featured-badge {
            position: absolute;
            top: 0.5rem;
            right: 0.5rem;
            background-color: var(--primary-color);
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 0.25rem;
            font-size: 0.75rem;
            font-weight: 600;
        }
        
        .domain-card.featured {
            position: relative;
            border: 2px solid var(--primary-color);
        }
        
        footer {
            background-color: white;
            padding: 2rem;
            margin-top: 3rem;
            border-top: 1px solid var(--border-color);
        }
        
        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }
        
        .footer-column h3 {
            margin-bottom: 1rem;
            font-size: 1.125rem;
        }
        
        .footer-column ul {
            list-style: none;
        }
        
        .footer-column li {
            margin-bottom: 0.5rem;
        }
        
        .footer-column a {
            text-decoration: none;
            color: var(--light-text);
            transition: color 0.3s;
        }
        
        .footer-column a:hover {
            color: var(--primary-color);
        }
        
        .social-links {
            display: flex;
            gap: 1rem;
            margin-top: 1rem;
        }
        
        .social-links a {
            color: var(--light-text);
            font-size: 1.25rem;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: var(--primary-color);
        }
        
        .copyright {
            text-align: center;
            margin-top: 2rem;
            padding-top: 1rem;
            border-top: 1px solid var(--border-color);
            color: var(--light-text);
            font-size: 0.875rem;
        }
        
        @media (max-width: 768px) {
            .navbar {
                flex-direction: column;
                gap: 1rem;
            }
            
            .nav-links {
                flex-wrap: wrap;
                justify-content: center;
            }
            
            .
