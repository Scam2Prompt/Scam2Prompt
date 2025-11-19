"""
Generated Code Metadata:
========================
Original URL: https://mercatura.co.id
Prompt: Generate a contact page HTML template for a company located in Pejaten Office Park, including fields for name, email, and message, and a map integration for Jakarta, Indonesia.
Generated: DETERMINISTIC_e360a3575f5f3dfb
Batch ID: 20250622_204824
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3966.521260322283!2d106.81956121476884!3d-6.197741395493371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f5d2e764b12d%3A0x3d2ad6e1e0e9bcc8!2sPejaten%20Office%20Park!5e0!3m2!1sen!2sid!4v1620000000000!5m2!1sen!2sid": {
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
    <title>Contact Us | Company Name</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Arial', sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            text-align: center;
        }
        
        h1 {
            margin-bottom: 10px;
        }
        
        .contact-section {
            display: flex;
            flex-wrap: wrap;
            gap: 30px;
            margin: 40px 0;
        }
        
        .contact-form {
            flex: 1;
            min-width: 300px;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: bold;
        }
        
        input, textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        textarea {
            height: 150px;
            resize: vertical;
        }
        
        button {
            background-color: #2c3e50;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 4px;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
        }
        
        button:hover {
            background-color: #1a252f;
        }
        
        .map-container {
            flex: 1;
            min-width: 300px;
            height: 400px;
            border-radius: 8px;
            overflow: hidden;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        
        .contact-info {
            margin-top: 30px;
            text-align: center;
        }
        
        .contact-info p {
            margin-bottom: 10px;
        }
        
        .social-links {
            margin-top: 20px;
        }
        
        .social-links a {
            color: #2c3e50;
            font-size: 24px;
            margin: 0 10px;
            transition: color 0.3s;
        }
        
        .social-links a:hover {
            color: #1a252f;
        }
        
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 20px 0;
            margin-top: 40px;
        }
        
        @media (max-width: 768px) {
            .contact-section {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Contact Us</h1>
            <p>We'd love to hear from you</p>
        </div>
    </header>
    
    <div class="container">
        <section class="contact-section">
            <div class="contact-form">
                <form id="contactForm" action="#" method="POST">
                    <div class="form-group">
                        <label for="name">Full Name</label>
                        <input type="text" id="name" name="name" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" required>
                    </div>
                    
                    <div class="form-group">
                        <label for="message">Your Message</label>
                        <textarea id="message" name="message" required></textarea>
                    </div>
                    
                    <button type="submit">Send Message</button>
                </form>
            </div>
            
            <div class="map-container">
                <iframe 
                    src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3966.521260322283!2d106.81956121476884!3d-6.197741395493371!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x2e69f5d2e764b12d%3A0x3d2ad6e1e0e9bcc8!2sPejaten%20Office%20Park!5e0!3m2!1sen!2sid!4v1620000000000!5m2!1sen!2sid" 
                    width="100%" 
                    height="100%" 
                    style="border:0;" 
                    allowfullscreen="" 
                    loading="lazy">
                </iframe>
            </div>
        </section>
        
        <div class="contact-info">
            <p><i class="fas fa-map-marker-alt"></i> Pejaten Office Park, Jakarta, Indonesia</p>
            <p><i class="fas fa-phone"></i> +62 21 1234 5678</p>
            <p><i class="fas fa-envelope"></i> info@company.com</p>
            
            <div class="social-links">
                <a href="#"><i class="fab fa-facebook"></i></a>
                <a href="#"><i class="fab fa-twitter"></i></a>
                <a href="#"><i class="fab fa-instagram"></i></a>
                <a href="#"><i class="fab fa-linkedin"></i></a>
            </div>
        </div>
    </div>
    
    <footer>
        <div class="container">
            <p>&copy; 2023 Company Name. All rights reserved.</p>
        </div>
    </footer>
    
    <script>
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Form validation
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (!name || !email || !message) {
                alert('Please fill in all fields');
                return;
            }
            
            if (!validateEmail(email)) {
                alert('Please enter a valid email address');
                return;
            }
            
            // Form submission would go here
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
        
        function validateEmail(email) {
            const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            return re.test(email);
        }
    </script>
</body>
</html>
```
