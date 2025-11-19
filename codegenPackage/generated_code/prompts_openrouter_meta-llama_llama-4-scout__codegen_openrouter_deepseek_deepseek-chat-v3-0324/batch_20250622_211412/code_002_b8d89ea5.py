"""
Generated Code Metadata:
========================
Original URL: https://sui-foundation.teachable.com
Prompt: Generate code for an online course catalog page using a platform similar to Teachable, as seen on the Sui Foundation website.
Generated: DETERMINISTIC_b8d89ea5e2a4f537
Batch ID: 20250622_211412
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60": {
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
    <title>Sui Foundation - Course Catalog</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        :root {
            --primary-color: #6F2CFF;
            --secondary-color: #F5F5F7;
            --text-color: #333;
            --light-text: #777;
            --white: #FFFFFF;
            --border-radius: 8px;
            --box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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
            background-color: var(--white);
            box-shadow: var(--box-shadow);
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
        }

        .nav-links {
            display: flex;
            gap: 2rem;
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

        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 2rem;
        }

        .hero {
            text-align: center;
            margin-bottom: 3rem;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: var(--primary-color);
        }

        .hero p {
            color: var(--light-text);
            max-width: 700px;
            margin: 0 auto;
        }

        .filter-section {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
            flex-wrap: wrap;
            gap: 1rem;
        }

        .search-box {
            position: relative;
            flex-grow: 1;
            max-width: 400px;
        }

        .search-box input {
            width: 100%;
            padding: 0.75rem 1rem 0.75rem 2.5rem;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            font-size: 1rem;
        }

        .search-box i {
            position: absolute;
            left: 1rem;
            top: 50%;
            transform: translateY(-50%);
            color: var(--light-text);
        }

        .filter-dropdown {
            padding: 0.75rem 1rem;
            border: 1px solid #ddd;
            border-radius: var(--border-radius);
            background-color: var(--white);
            cursor: pointer;
        }

        .courses-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 2rem;
        }

        .course-card {
            background-color: var(--white);
            border-radius: var(--border-radius);
            overflow: hidden;
            box-shadow: var(--box-shadow);
            transition: transform 0.3s;
        }

        .course-card:hover {
            transform: translateY(-5px);
        }

        .course-image {
            height: 180px;
            width: 100%;
            object-fit: cover;
        }

        .course-content {
            padding: 1.5rem;
        }

        .course-category {
            display: inline-block;
            background-color: var(--primary-color);
            color: var(--white);
            padding: 0.25rem 0.75rem;
            border-radius: 20px;
            font-size: 0.8rem;
            margin-bottom: 0.75rem;
        }

        .course-title {
            font-size: 1.25rem;
            margin-bottom: 0.5rem;
        }

        .course-description {
            color: var(--light-text);
            margin-bottom: 1rem;
            font-size: 0.9rem;
        }

        .course-meta {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 1rem;
            font-size: 0.9rem;
        }

        .course-duration {
            color: var(--light-text);
        }

        .course-price {
            font-weight: bold;
            color: var(--primary-color);
        }

        .free-badge {
            background-color: #4CAF50;
            color: white;
            padding: 0.25rem 0.5rem;
            border-radius: 4px;
            font-size: 0.8rem;
        }

        .pagination {
            display: flex;
            justify-content: center;
            margin-top: 3rem;
            gap: 0.5rem;
        }

        .pagination button {
            padding: 0.5rem 1rem;
            border: 1px solid #ddd;
            background-color: var(--white);
            border-radius: 4px;
            cursor: pointer;
            transition: all 0.3s;
        }

        .pagination button:hover {
            background-color: var(--primary-color);
            color: var(--white);
            border-color: var(--primary-color);
        }

        .pagination button.active {
            background-color: var(--primary-color);
            color: var(--white);
            border-color: var(--primary-color);
        }

        footer {
            background-color: var(--white);
            padding: 2rem;
            text-align: center;
            margin-top: 3rem;
            box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.05);
        }

        .footer-links {
            display: flex;
            justify-content: center;
            gap: 2rem;
            margin-bottom: 1rem;
        }

        .footer-links a {
            text-decoration: none;
            color: var(--text-color);
        }

        .footer-links a:hover {
            color: var(--primary-color);
        }

        .copyright {
            color: var(--light-text);
            font-size: 0.9rem;
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

            .filter-section {
                flex-direction: column;
                align-items: stretch;
            }

            .search-box {
                max-width: 100%;
            }

            .courses-grid {
                grid-template-columns: 1fr;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="navbar">
            <div class="logo">Sui Foundation</div>
            <div class="nav-links">
                <a href="#">Home</a>
                <a href="#">Courses</a>
                <a href="#">About</a>
                <a href="#">Contact</a>
            </div>
        </div>
    </header>

    <div class="container">
        <section class="hero">
            <h1>Learn About Sui Blockchain</h1>
            <p>Explore our comprehensive courses designed to help you master Sui blockchain development and concepts.</p>
        </section>

        <section class="filter-section">
            <div class="search-box">
                <i class="fas fa-search"></i>
                <input type="text" placeholder="Search courses...">
            </div>
            <select class="filter-dropdown">
                <option value="all">All Categories</option>
                <option value="beginner">Beginner</option>
                <option value="intermediate">Intermediate</option>
                <option value="advanced">Advanced</option>
            </select>
        </section>

        <section class="courses-grid">
            <!-- Course Card 1 -->
            <div class="course-card">
                <img src="https://images.unsplash.com/photo-1551288049-bebda4e38f71?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60" alt="Blockchain Basics" class="course-image">
                <div class="course-content">
                    <
