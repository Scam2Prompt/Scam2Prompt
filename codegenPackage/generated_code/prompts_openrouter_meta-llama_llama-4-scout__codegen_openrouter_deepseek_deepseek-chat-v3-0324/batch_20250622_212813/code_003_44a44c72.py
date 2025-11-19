"""
Generated Code Metadata:
========================
Original URL: https://redstarksten.github.io
Prompt: Create a simple contact page template in HTML/CSS, inspired by the contact section of the StarkX-Kernel project website.
Generated: DETERMINISTIC_44a44c72d95ab8ab
Batch ID: 20250622_212813
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
    <title>Contact Us</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }

        body {
            background-color: #f8f9fa;
            color: #333;
            line-height: 1.6;
        }

        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }

        /* Header styles */
        header {
            text-align: center;
            margin-bottom: 3rem;
        }

        h1 {
            font-size: 2.5rem;
            margin-bottom: 1rem;
            color: #2c3e50;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #7f8c8d;
            max-width: 600px;
            margin: 0 auto;
        }

        /* Contact form styles */
        .contact-section {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            justify-content: center;
        }

        .contact-form {
            flex: 1;
            min-width: 300px;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .form-group {
            margin-bottom: 1.5rem;
        }

        label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 600;
            color: #2c3e50;
        }

        input, textarea {
            width: 100%;
            padding: 0.8rem;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 1rem;
            transition: border-color 0.3s;
        }

        input:focus, textarea:focus {
            outline: none;
            border-color: #3498db;
        }

        textarea {
            min-height: 150px;
            resize: vertical;
        }

        .submit-btn {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 0.8rem 1.5rem;
            font-size: 1rem;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .submit-btn:hover {
            background-color: #2980b9;
        }

        /* Contact info styles */
        .contact-info {
            flex: 1;
            min-width: 300px;
            background: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }

        .info-item {
            display: flex;
            align-items: flex-start;
            margin-bottom: 1.5rem;
        }

        .info-icon {
            margin-right: 1rem;
            color: #3498db;
            font-size: 1.5rem;
        }

        .info-content h3 {
            margin-bottom: 0.3rem;
            color: #2c3e50;
        }

        .info-content p {
            color: #7f8c8d;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            .contact-section {
                flex-direction: column;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Get In Touch</h1>
            <p class="subtitle">Have questions or want to discuss a project? Fill out the form below and we'll get back to you as soon as possible.</p>
        </header>

        <section class="contact-section">
            <form class="contact-form" id="contactForm">
                <div class="form-group">
                    <label for="name">Name</label>
                    <input type="text" id="name" name="name" required>
                </div>
                <div class="form-group">
                    <label for="email">Email</label>
                    <input type="email" id="email" name="email" required>
                </div>
                <div class="form-group">
                    <label for="subject">Subject</label>
                    <input type="text" id="subject" name="subject" required>
                </div>
                <div class="form-group">
                    <label for="message">Message</label>
                    <textarea id="message" name="message" required></textarea>
                </div>
                <button type="submit" class="submit-btn">Send Message</button>
            </form>

            <div class="contact-info">
                <div class="info-item">
                    <div class="info-icon">📍</div>
                    <div class="info-content">
                        <h3>Our Location</h3>
                        <p>123 Tech Street, Silicon Valley, CA 94025</p>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-icon">✉️</div>
                    <div class="info-content">
                        <h3>Email Us</h3>
                        <p>contact@starkx-kernel.com</p>
                    </div>
                </div>
                <div class="info-item">
                    <div class="info-icon">📞</div>
                    <div class="info-content">
                        <h3>Call Us</h3>
                        <p>+1 (555) 123-4567</p>
                    </div>
                </div>
            </div>
        </section>
    </div>

    <script>
        // Form submission handling
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Form validation
            const name = document.getElementById('name').value.trim();
            const email = document.getElementById('email').value.trim();
            const subject = document.getElementById('subject').value.trim();
            const message = document.getElementById('message').value.trim();
            
            if (!name || !email || !subject || !message) {
                alert('Please fill in all fields');
                return;
            }
            
            // Here you would typically send the form data to a server
            // For demo purposes, we'll just show a success message
            alert('Thank you for your message! We will get back to you soon.');
            this.reset();
        });
    </script>
</body>
</html>
```
