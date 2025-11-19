"""
Generated Code Metadata:
========================
Original URL: https://safarait.com
Prompt: How can I utilize animation in web design to enhance user experience on a site developed by Safara IT?
Generated: DETERMINISTIC_8c0f99b821c9096e
Batch ID: 20250612_155200
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
    <title>Safara IT - Enhanced UX with Animations</title>
    <style>
        /* Base styles */
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            color: #333;
            background-color: #f9f9f9;
        }

        /* Smooth scrolling */
        html {
            scroll-behavior: smooth;
        }

        /* Header animation */
        header {
            background: linear-gradient(135deg, #6e48aa, #9d50bb);
            color: white;
            padding: 2rem 0;
            text-align: center;
            position: relative;
            overflow: hidden;
        }

        .header-content {
            position: relative;
            z-index: 2;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out forwards;
        }

        @keyframes fadeInUp {
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        /* Navigation */
        nav {
            background-color: #fff;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .nav-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .logo {
            font-weight: bold;
            font-size: 1.5rem;
            color: #6e48aa;
            transition: transform 0.3s ease;
        }

        .logo:hover {
            transform: scale(1.05);
        }

        .nav-links {
            display: flex;
            gap: 2rem;
        }

        .nav-links a {
            text-decoration: none;
            color: #333;
            font-weight: 500;
            position: relative;
            padding: 0.5rem 0;
            transition: color 0.3s ease;
        }

        .nav-links a::after {
            content: '';
            position: absolute;
            bottom: 0;
            left: 0;
            width: 0;
            height: 2px;
            background-color: #6e48aa;
            transition: width 0.3s ease;
        }

        .nav-links a:hover {
            color: #6e48aa;
        }

        .nav-links a:hover::after {
            width: 100%;
        }

        /* Hero section */
        .hero {
            padding: 4rem 2rem;
            text-align: center;
            background-color: white;
        }

        .hero h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out 0.3s forwards;
        }

        .hero p {
            font-size: 1.2rem;
            max-width: 800px;
            margin: 0 auto 2rem;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out 0.6s forwards;
        }

        .cta-button {
            display: inline-block;
            background-color: #6e48aa;
            color: white;
            padding: 0.8rem 2rem;
            border-radius: 50px;
            text-decoration: none;
            font-weight: bold;
            transition: all 0.3s ease;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out 0.9s forwards;
        }

        .cta-button:hover {
            background-color: #9d50bb;
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        }

        /* Features section */
        .features {
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .features h2 {
            text-align: center;
            margin-bottom: 3rem;
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out forwards;
        }

        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .feature-card {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
            opacity: 0;
            transform: translateY(20px);
        }

        .feature-card:nth-child(1) {
            animation: fadeInUp 1s ease-out 0.3s forwards;
        }

        .feature-card:nth-child(2) {
            animation: fadeInUp 1s ease-out 0.6s forwards;
        }

        .feature-card:nth-child(3) {
            animation: fadeInUp 1s ease-out 0.9s forwards;
        }

        .feature-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 15px 30px rgba(0,0,0,0.1);
        }

        .feature-icon {
            font-size: 2.5rem;
            color: #6e48aa;
            margin-bottom: 1rem;
        }

        /* Stats section */
        .stats {
            background: linear-gradient(135deg, #6e48aa, #9d50bb);
            color: white;
            padding: 4rem 2rem;
            text-align: center;
        }

        .stats-container {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }

        .stat-item {
            opacity: 0;
            transform: translateY(20px);
        }

        .stat-item:nth-child(1) {
            animation: fadeInUp 1s ease-out 0.3s forwards;
        }

        .stat-item:nth-child(2) {
            animation: fadeInUp 1s ease-out 0.6s forwards;
        }

        .stat-item:nth-child(3) {
            animation: fadeInUp 1s ease-out 0.9s forwards;
        }

        .stat-number {
            font-size: 3rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        /* Testimonials */
        .testimonials {
            padding: 4rem 2rem;
            max-width: 1200px;
            margin: 0 auto;
        }

        .testimonials h2 {
            text-align: center;
            margin-bottom: 3rem;
        }

        .testimonial-slider {
            position: relative;
            overflow: hidden;
        }

        .testimonial-slide {
            background-color: white;
            border-radius: 8px;
            padding: 2rem;
            box-shadow: 0 5px 15px rgba(0,0,0,0.05);
            margin: 0 1rem;
            transition: transform 0.5s ease, opacity 0.5s ease;
        }

        .testimonial-slide.active {
            opacity: 1;
            transform: translateX(0);
        }

        .testimonial-slide.next {
            opacity: 0;
            transform: translateX(100%);
        }

        .testimonial-slide.prev {
            opacity: 0;
            transform: translateX(-100%);
        }

        /* Footer */
        footer {
            background-color: #333;
            color: white;
            padding: 3rem 2rem;
            text-align: center;
        }

        .footer-content {
            max-width: 1200px;
            margin: 0 auto;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }

        .footer-section {
            opacity: 0;
            transform: translateY(20px);
            animation: fadeInUp 1s ease-out forwards;
        }

        .footer-section:nth-child(1) {
            animation-delay: 0.3s;
        }

        .footer-section:nth-child(2) {
            animation-delay: 0.6s;
        }

        .footer-section:nth-child
