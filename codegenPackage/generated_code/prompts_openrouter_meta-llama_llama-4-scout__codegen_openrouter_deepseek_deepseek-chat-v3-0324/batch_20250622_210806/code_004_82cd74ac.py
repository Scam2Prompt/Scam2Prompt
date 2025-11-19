"""
Generated Code Metadata:
========================
Original URL: https://fusionjiujitsu.com.br
Prompt: "Create a basic HTML template for a Jiu-Jitsu school website that includes sections for programs, schedules, and contact information."
Generated: DETERMINISTIC_82cd74acf6d05793
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
    <title>Jiu-Jitsu Academy | Home</title>
    <style>
        /* Basic reset and styling */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            line-height: 1.6;
            color: #333;
        }
        
        header {
            background-color: #1a1a1a;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        nav {
            background-color: #333;
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
        
        nav ul li a:hover {
            color: #f0c14b;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        
        section {
            margin: 2rem 0;
            padding: 1rem;
            border-bottom: 1px solid #eee;
        }
        
        h2 {
            color: #1a1a1a;
            margin-bottom: 1rem;
        }
        
        footer {
            background-color: #1a1a1a;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
        
        .program-card {
            border: 1px solid #ddd;
            padding: 1rem;
            margin: 1rem 0;
            border-radius: 5px;
        }
        
        .schedule-table {
            width: 100%;
            border-collapse: collapse;
            margin: 1rem 0;
        }
        
        .schedule-table th, .schedule-table td {
            border: 1px solid #ddd;
            padding: 0.5rem;
            text-align: left;
        }
        
        .schedule-table th {
            background-color: #f4f4f4;
        }
        
        .contact-form input, 
        .contact-form textarea {
            width: 100%;
            padding: 0.5rem;
            margin: 0.5rem 0;
            border: 1px solid #ddd;
        }
        
        .contact-form button {
            background-color: #1a1a1a;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            cursor: pointer;
        }
        
        .contact-form button:hover {
            background-color: #333;
        }
    </style>
</head>
<body>
    <header>
        <h1>Jiu-Jitsu Academy</h1>
        <p>Master the art of Brazilian Jiu-Jitsu</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#programs">Programs</a></li>
            <li><a href="#schedule">Schedule</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <div class="container">
        <section id="home">
            <h2>Welcome to Our Academy</h2>
            <p>We offer world-class Jiu-Jitsu training for all ages and skill levels. Our experienced instructors will guide you on your journey to mastery.</p>
        </section>
        
        <section id="programs">
            <h2>Our Programs</h2>
            
            <div class="program-card">
                <h3>Kids Jiu-Jitsu</h3>
                <p>Ages 5-12. Focus on fundamentals, discipline, and fun in a safe environment.</p>
            </div>
            
            <div class="program-card">
                <h3>Adult Fundamentals</h3>
                <p>Perfect for beginners. Learn the core techniques and principles of Jiu-Jitsu.</p>
            </div>
            
            <div class="program-card">
                <h3>Advanced Training</h3>
                <p>For experienced practitioners looking to refine their skills and compete.</p>
            </div>
            
            <div class="program-card">
                <h3>Private Lessons</h3>
                <p>One-on-one instruction tailored to your specific needs and goals.</p>
            </div>
        </section>
        
        <section id="schedule">
            <h2>Class Schedule</h2>
            
            <table class="schedule-table">
                <thead>
                    <tr>
                        <th>Class</th>
                        <th>Days</th>
                        <th>Time</th>
                        <th>Instructor</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Kids Jiu-Jitsu</td>
                        <td>Mon, Wed, Fri</td>
                        <td>4:00 PM - 5:00 PM</td>
                        <td>Prof. Silva</td>
                    </tr>
                    <tr>
                        <td>Adult Fundamentals</td>
                        <td>Tue, Thu</td>
                        <td>6:00 PM - 7:30 PM</td>
                        <td>Prof. Santos</td>
                    </tr>
                    <tr>
                        <td>Advanced Training</td>
                        <td>Mon, Wed, Fri</td>
                        <td>7:00 PM - 8:30 PM</td>
                        <td>Prof. Oliveira</td>
                    </tr>
                </tbody>
            </table>
        </section>
        
        <section id="contact">
            <h2>Contact Us</h2>
            
            <div>
                <p><strong>Address:</strong> 123 Martial Arts Way, Cityville, ST 12345</p>
                <p><strong>Phone:</strong> (555) 123-4567</p>
                <p><strong>Email:</strong> info@jiujitsuacademy.com</p>
            </div>
            
            <h3>Send us a message</h3>
            <form class="contact-form">
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Subject">
                <textarea rows="5" placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>
    </div>
    
    <footer>
        <p>&copy; 2023 Jiu-Jitsu Academy. All rights reserved.</p>
    </footer>
</body>
</html>
```
