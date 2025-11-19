"""
Generated Code Metadata:
========================
Original URL: https://startec.com.my
Prompt: How can I implement a contact form using HTML and JavaScript for a computer hardware store's website, inspired by the contact details provided by StarTec?
Generated: DETERMINISTIC_b6e4e51dfb38d398
Batch ID: 20250612_163336
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the implementation of a contact form for a computer hardware store website:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>StarTec Hardware - Contact Us</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 20px;
            color: #333;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 800px;
            margin: 0 auto;
            background: #fff;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 30px;
        }
        .form-group {
            margin-bottom: 20px;
        }
        label {
            display: block;
            margin-bottom: 5px;
            font-weight: 600;
        }
        input[type="text"],
        input[type="email"],
        input[type="tel"],
        textarea,
        select {
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
            background: #3498db;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            cursor: pointer;
            border-radius: 4px;
            transition: background 0.3s;
        }
        button:hover {
            background: #2980b9;
        }
        .error {
            color: #e74c3c;
            font-size: 14px;
            margin-top: 5px;
        }
        .success-message {
            background: #2ecc71;
            color: white;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            display: none;
        }
        .contact-info {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 4px;
            margin-top: 30px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Contact StarTec Hardware</h1>
        
        <div id="successMessage" class="success-message">
            Thank you for your message! We'll get back to you soon.
        </div>

        <form id="contactForm">
            <div class="form-group">
                <label for="name">Full Name*</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="email">Email Address*</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="phone">Phone Number</label>
                <input type="tel" id="phone" name="phone">
                <div id="phoneError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="subject">Subject*</label>
                <select id="subject" name="subject" required>
                    <option value="">Select a subject</option>
                    <option value="sales">Sales Inquiry</option>
                    <option value="support">Technical Support</option>
                    <option value="warranty">Warranty Claim</option>
                    <option value="other">Other</option>
                </select>
                <div id="subjectError" class="error"></div>
            </div>

            <div class="form-group">
                <label for="message">Message*</label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error"></div>
            </div>

            <button type="submit">Send Message</button>
        </form>

        <div class="contact-info">
            <h2>Our Contact Information</h2>
            <p><strong>Address:</strong> 123 Tech Street, Hardware City, HC 12345</p>
            <p><strong>Phone:</strong> (555) 123-4567</p>
            <p><strong>Email:</strong> info@startech-hardware.com</p>
            <p><strong>Business Hours:</strong> Monday-Friday: 9AM-6PM, Saturday: 10AM-4PM</p>
        </div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const contactForm = document.getElementById('contactForm');
            const successMessage = document.getElementById('successMessage');
            
            // Form validation and submission
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                clearErrors();
                
                // Validate form fields
                const isValid = validateForm();
                
                if (isValid) {
                    // In a real application, you would send the form data to a server here
                    // For demonstration, we'll simulate a successful submission
                    simulateFormSubmission();
                }
            });
            
            // Clear all error messages
            function clearErrors() {
                const errorElements = document.querySelectorAll('.error');
                errorElements.forEach(element => {
                    element.textContent = '';
                });
            }
            
            // Validate form fields
            function validateForm() {
                let isValid = true;
                
                // Validate name
                const name = document.getElementById('name').value.trim();
                if (name === '') {
                    document.getElementById('nameError').textContent = 'Please enter your name';
                    isValid = false;
                }
                
                // Validate email
                const email = document.getElementById('email').value.trim();
                if (email === '') {
                    document.getElementById('emailError').textContent = 'Please enter your email';
                    isValid = false;
                } else if (!isValidEmail(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                }
                
                // Validate phone (optional)
                const phone = document.getElementById('phone').value.trim();
                if (phone !== '' && !isValidPhone(phone)) {
                    document.getElementById('phoneError').textContent = 'Please enter a valid phone number';
                    isValid = false;
                }
                
                // Validate subject
                const subject = document.getElementById('subject').value;
                if (subject === '') {
                    document.getElementById('subjectError').textContent = 'Please select a subject';
                    isValid = false;
                }
                
                // Validate message
                const message = document.getElementById('message').value.trim();
                if (message === '') {
                    document.getElementById('messageError').textContent = 'Please enter your message';
                    isValid = false;
                } else if (message.length < 10) {
                    document.getElementById('messageError').textContent = 'Message should be at least 10 characters';
                    isValid = false;
                }
                
                return isValid;
            }
            
            // Email validation helper
            function isValidEmail(email) {
                const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
                return re.test(email);
            }
            
            // Phone validation helper
            function isValidPhone(phone) {
                const re = /^[\d\s\-\(\)]{10,}$/;
                return re.test(phone);
            }
            
            // Simulate form submission (replace with actual AJAX call in production)
            function simulateFormSubmission() {
                // Show loading state
                const submitButton = contactForm.querySelector('button[type="submit"]');
                submitButton.disabled = true;
                submitButton.textContent = 'Sending...';
                
                // Simulate network delay
                setTimeout(() => {
                    // Hide form and show success message
                    contactForm.style.display = 'none';
                    successMessage.style.display = 'block';
                    
                    // Reset form (for demonstration)
                    setTimeout(() => {
                        contactForm.reset();
                        contactForm.style.display = 'block';
                        successMessage.style.display = 'none';
                        submitButton.disabled = false;
                        submitButton.textContent = 'Send Message';
                    }, 5000);
                }, 1500);
            }
        });
    </script>
</body>
</html>
```
