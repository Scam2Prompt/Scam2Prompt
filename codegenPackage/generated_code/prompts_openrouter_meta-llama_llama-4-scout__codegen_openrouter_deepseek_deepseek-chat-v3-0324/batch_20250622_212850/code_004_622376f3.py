"""
Generated Code Metadata:
========================
Original URL: https://www.prointegrationfuture.asia
Prompt: Design a simple web page using HTML, CSS, and JavaScript to promote the Pro Integration Future Asia event, including sections for event details, registration, and exhibitor information.
Generated: DETERMINISTIC_622376f3c7a7d828
Batch ID: 20250622_212850
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
    <title>Pro Integration Future Asia</title>
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
            background: linear-gradient(135deg, #1a237e, #283593);
            color: white;
            padding: 2rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 1rem;
        }

        .tagline {
            font-size: 1.2rem;
            opacity: 0.9;
        }

        /* Navigation */
        nav {
            background-color: #3949ab;
            padding: 1rem 0;
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
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav ul li a:hover {
            background-color: #5c6bc0;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        section {
            margin-bottom: 3rem;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }

        h2 {
            color: #1a237e;
            margin-bottom: 1.5rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #e8eaf6;
        }

        /* Event details */
        .event-details {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }

        .detail-card {
            padding: 1.5rem;
            background: #e8eaf6;
            border-radius: 6px;
        }

        .detail-card h3 {
            color: #283593;
            margin-bottom: 1rem;
        }

        /* Registration form */
        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: bold;
            color: #1a237e;
        }

        input, select, textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
        }

        button {
            background-color: #3949ab;
            color: white;
            border: none;
            padding: 1rem 2rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        button:hover {
            background-color: #5c6bc0;
        }

        /* Exhibitors */
        .exhibitors-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 1.5rem;
        }

        .exhibitor-card {
            border: 1px solid #ddd;
            border-radius: 6px;
            overflow: hidden;
            transition: transform 0.3s, box-shadow 0.3s;
        }

        .exhibitor-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
        }

        .exhibitor-img {
            height: 150px;
            background-color: #e8eaf6;
            display: flex;
            align-items: center;
            justify-content: center;
            color: #5c6bc0;
        }

        .exhibitor-info {
            padding: 1.5rem;
        }

        .exhibitor-info h3 {
            margin-bottom: 0.5rem;
            color: #1a237e;
        }

        /* Footer */
        footer {
            background-color: #1a237e;
            color: white;
            text-align: center;
            padding: 2rem 0;
            margin-top: 2rem;
        }

        .social-links {
            margin: 1rem 0;
        }

        .social-links a {
            color: white;
            margin: 0 0.5rem;
            font-size: 1.5rem;
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
        }
    </style>
</head>
<body>
    <header>
        <div class="logo">Pro Integration Future Asia</div>
        <div class="tagline">Connecting Businesses Across Asia</div>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About</a></li>
            <li><a href="#details">Event Details</a></li>
            <li><a href="#register">Register</a></li>
            <li><a href="#exhibitors">Exhibitors</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="about">
            <h2>About the Event</h2>
            <p>Pro Integration Future Asia is the premier networking and business integration event in the region, bringing together industry leaders, innovators, and entrepreneurs to shape the future of Asian business collaboration.</p>
            <p>Join us for three days of insightful discussions, networking opportunities, and exhibitions showcasing the latest in business technology and integration solutions.</p>
        </section>

        <section id="details">
            <h2>Event Details</h2>
            <div class="event-details">
                <div class="detail-card">
                    <h3>Date & Time</h3>
                    <p>November 15-17, 2023</p>
                    <p>9:00 AM - 6:00 PM Daily</p>
                </div>
                <div class="detail-card">
                    <h3>Location</h3>
                    <p>Asia World Expo</p>
                    <p>Hong Kong</p>
                </div>
                <div class="detail-card">
                    <h3>Highlights</h3>
                    <ul>
                        <li>Keynote speeches</li>
                        <li>Panel discussions</li>
                        <li>Networking sessions</li>
                        <li>Product exhibitions</li>
                    </ul>
                </div>
            </div>
        </section>

        <section id="register">
            <h2>Registration</h2>
            <form id="registrationForm">
                <div class="form-group">
                    <label for="name">Full Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="company">Company</label>
                    <input type="text" id="company" name="company" required>
                </div>
                <div class="form-group">
                    <label for="position">Position</label>
                    <input type="text" id="position" name="position" required>
                </div>
                <div class="form-group">
                    <label for="ticket">Ticket Type</label>
                    <select id="ticket" name="ticket" required>
                        <option value="">Select ticket type</option>
                        <option value="standard">Standard Pass (Free)</option>
                        <option value="premium">Premium Pass ($199)</option>
                        <option value="vip">VIP Pass ($499)</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="message">Special Requirements</label>
                    <textarea id="message
