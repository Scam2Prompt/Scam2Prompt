"""
Generated Code Metadata:
========================
Original URL: https://ihsh.edu.bd
Prompt: Write a code to create a simple website for a school like Ideal High School, including sections for academics, administration, and activities.
Generated: DETERMINISTIC_bc8030bcc0b1ec72
Batch ID: 20250622_210806
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
    <title>Ideal High School</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
            background-color: #f5f5f5;
        }
        
        header {
            background-color: #1a5276;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        nav {
            background-color: #2874a6;
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
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        
        nav ul li a:hover {
            background-color: #3498db;
        }
        
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        section {
            margin-bottom: 2rem;
            background: white;
            padding: 1.5rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        h1, h2, h3 {
            margin-bottom: 1rem;
            color: #1a5276;
        }
        
        footer {
            background-color: #1a5276;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
        
        .hero {
            background-image: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url('school-building.jpg');
            background-size: cover;
            background-position: center;
            height: 300px;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            text-align: center;
            margin-bottom: 2rem;
        }
        
        .hero h1 {
            color: white;
            font-size: 2.5rem;
        }
        
        .card-container {
            display: flex;
            flex-wrap: wrap;
            gap: 1rem;
            justify-content: space-between;
        }
        
        .card {
            flex: 1 1 300px;
            background: white;
            padding: 1rem;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
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
        <h1>Ideal High School</h1>
        <p>Excellence in Education Since 1990</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#academics">Academics</a></li>
            <li><a href="#administration">Administration</a></li>
            <li><a href="#activities">Activities</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <div class="hero" id="home">
        <h1>Welcome to Ideal High School</h1>
    </div>
    
    <div class="container">
        <section id="academics">
            <h2>Academics</h2>
            <p>At Ideal High School, we offer a comprehensive academic program designed to prepare students for college and beyond.</p>
            
            <div class="card-container">
                <div class="card">
                    <h3>Core Curriculum</h3>
                    <p>Our core curriculum includes Mathematics, Science, English, and Social Studies, meeting all state requirements.</p>
                </div>
                <div class="card">
                    <h3>Advanced Placement</h3>
                    <p>We offer 15 AP courses across various subjects for students seeking college-level coursework.</p>
                </div>
                <div class="card">
                    <h3>Electives</h3>
                    <p>Students can choose from a wide range of electives including foreign languages, arts, and technology courses.</p>
                </div>
            </div>
        </section>
        
        <section id="administration">
            <h2>Administration</h2>
            <p>Our dedicated administrative staff works tirelessly to ensure a safe and productive learning environment.</p>
            
            <div class="card-container">
                <div class="card">
                    <h3>Principal</h3>
                    <p>Dr. Jane Smith<br>Email: principal@idealhigh.edu</p>
                </div>
                <div class="card">
                    <h3>Vice Principal</h3>
                    <p>Mr. John Doe<br>Email: viceprincipal@idealhigh.edu</p>
                </div>
                <div class="card">
                    <h3>Guidance</h3>
                    <p>Counseling services available Monday-Friday<br>Email: guidance@idealhigh.edu</p>
                </div>
            </div>
        </section>
        
        <section id="activities">
            <h2>Activities</h2>
            <p>We believe in holistic development and offer numerous extracurricular activities for our students.</p>
            
            <div class="card-container">
                <div class="card">
                    <h3>Sports</h3>
                    <p>Football, Basketball, Soccer, Track & Field, Swimming, and more.</p>
                </div>
                <div class="card">
                    <h3>Clubs</h3>
                    <p>Debate, Robotics, Drama, Music, Art, and many other student-led organizations.</p>
                </div>
                <div class="card">
                    <h3>Events</h3>
                    <p>Annual Science Fair, Cultural Festival, Sports Day, and various community service initiatives.</p>
                </div>
            </div>
        </section>
        
        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm">
                <div style="margin-bottom: 1rem;">
                    <label for="name" style="display: block; margin-bottom: 0.5rem;">Name:</label>
                    <input type="text" id="name" name="name" required style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="email" style="display: block; margin-bottom: 0.5rem;">Email:</label>
                    <input type="email" id="email" name="email" required style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 1rem;">
                    <label for="message" style="display: block; margin-bottom: 0.5rem;">Message:</label>
                    <textarea id="message" name="message" required style="width: 100%; padding: 0.5rem; border: 1px solid #ddd; border-radius: 4px; min-height: 100px;"></textarea>
                </div>
                <button type="submit" style="background-color: #1a5276; color: white; padding: 0.5rem 1rem; border: none; border-radius: 4px; cursor: pointer;">Submit</button>
            </form>
        </section>
    </div>
    
    <footer>
        <p>&copy; 2023 Ideal High School. All Rights Reserved.</p>
        <p>123 Education Lane, Learning City, LC 12345 | Phone: (555) 123-4567</p>
    </footer>
    
    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;
            
            // Basic validation
            if (!name || !email || !message) {
