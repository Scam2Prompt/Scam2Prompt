"""
Generated Code Metadata:
========================
Original URL: https://pp4.swiebodzin.pl
Prompt: Create a basic HTML page for a preschool website, including sections for news, events, and contact information.
Generated: DETERMINISTIC_6f2b21260d2b1b44
Batch ID: 20250622_210703
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
    <title>Sunshine Preschool</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            background-color: #f9f9f9;
        }
        
        /* Header styles */
        header {
            background-color: #4CAF50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }
        
        .logo {
            font-size: 2rem;
            margin-bottom: 0.5rem;
        }
        
        /* Navigation styles */
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
            padding: 0.5rem 1rem;
            transition: background-color 0.3s;
        }
        
        nav ul li a:hover {
            background-color: #4CAF50;
            border-radius: 4px;
        }
        
        /* Main content styles */
        main {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }
        
        section {
            margin-bottom: 2rem;
            padding: 1rem;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }
        
        h2 {
            color: #4CAF50;
            margin-bottom: 1rem;
            border-bottom: 2px solid #4CAF50;
            padding-bottom: 0.5rem;
        }
        
        /* News section styles */
        .news-item {
            margin-bottom: 1rem;
            padding-bottom: 1rem;
            border-bottom: 1px solid #eee;
        }
        
        .news-item:last-child {
            border-bottom: none;
        }
        
        .news-item h3 {
            color: #333;
            margin-bottom: 0.5rem;
        }
        
        .news-date {
            color: #666;
            font-size: 0.9rem;
            margin-bottom: 0.5rem;
        }
        
        /* Events section styles */
        .event {
            margin-bottom: 1rem;
            padding: 1rem;
            background-color: #f5f5f5;
            border-radius: 4px;
        }
        
        .event h3 {
            color: #333;
            margin-bottom: 0.5rem;
        }
        
        .event-date {
            font-weight: bold;
            color: #4CAF50;
        }
        
        /* Contact section styles */
        .contact-info {
            margin-bottom: 1rem;
        }
        
        .contact-info p {
            margin-bottom: 0.5rem;
        }
        
        .contact-form input,
        .contact-form textarea {
            width: 100%;
            padding: 0.5rem;
            margin-bottom: 1rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        
        .contact-form button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .contact-form button:hover {
            background-color: #45a049;
        }
        
        /* Footer styles */
        footer {
            background-color: #333;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }
        
        /* Responsive styles */
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
        <div class="logo">Sunshine Preschool</div>
        <p>Where learning begins with fun!</p>
    </header>
    
    <nav>
        <ul>
            <li><a href="#home">Home</a></li>
            <li><a href="#news">News</a></li>
            <li><a href="#events">Events</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
    
    <main>
        <section id="news">
            <h2>Latest News</h2>
            
            <div class="news-item">
                <h3>New Playground Equipment Installed</h3>
                <p class="news-date">June 15, 2023</p>
                <p>We're excited to announce the installation of our new playground equipment, featuring a climbing structure and slide designed specifically for preschoolers.</p>
            </div>
            
            <div class="news-item">
                <h3>Preschool Receives Excellence Award</h3>
                <p class="news-date">May 28, 2023</p>
                <p>Sunshine Preschool has been recognized with the Early Childhood Excellence Award for our innovative curriculum and outstanding staff.</p>
            </div>
        </section>
        
        <section id="events">
            <h2>Upcoming Events</h2>
            
            <div class="event">
                <h3>Summer Picnic</h3>
                <p class="event-date">July 10, 2023 | 10:00 AM - 2:00 PM</p>
                <p>Join us for our annual summer picnic at Riverside Park. Bring your family for games, food, and fun!</p>
            </div>
            
            <div class="event">
                <h3>Parent-Teacher Conferences</h3>
                <p class="event-date">August 5-6, 2023</p>
                <p>Schedule a time to meet with your child's teacher and discuss their progress and development.</p>
            </div>
            
            <div class="event">
                <h3>First Day of Fall Semester</h3>
                <p class="event-date">September 1, 2023</p>
                <p>We look forward to welcoming all our students back for another exciting semester of learning and growth.</p>
            </div>
        </section>
        
        <section id="contact">
            <h2>Contact Us</h2>
            
            <div class="contact-info">
                <p><strong>Address:</strong> 123 Sunshine Lane, Happyville, HV 12345</p>
                <p><strong>Phone:</strong> (555) 123-4567</p>
                <p><strong>Email:</strong> info@sunshinepreschool.com</p>
                <p><strong>Hours:</strong> Monday-Friday, 7:30 AM - 5:30 PM</p>
            </div>
            
            <form class="contact-form">
                <h3>Send Us a Message</h3>
                <input type="text" placeholder="Your Name" required>
                <input type="email" placeholder="Your Email" required>
                <input type="text" placeholder="Subject">
                <textarea rows="5" placeholder="Your Message" required></textarea>
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>
    
    <footer>
        <p>&copy; 2023 Sunshine Preschool. All rights reserved.</p>
    </footer>
</body>
</html>
```
