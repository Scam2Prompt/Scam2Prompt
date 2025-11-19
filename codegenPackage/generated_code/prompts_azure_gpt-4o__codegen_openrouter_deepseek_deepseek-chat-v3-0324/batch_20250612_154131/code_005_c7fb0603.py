"""
Generated Code Metadata:
========================
Original URL: https://symbiotic-services.com
Prompt: Write code for a contact form for a Squarespace-based website, similar to the one on Symbiotic Services, including fields for name, email, and message submission.
Generated: DETERMINISTIC_c7fb0603c3a748aa
Batch ID: 20250612_154131
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
        /* Basic styling for the form */
        body {
            font-family: 'Arial', sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        
        .contact-form {
            background-color: #f9f9f9;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .form-group {
            margin-bottom: 20px;
        }
        
        label {
            display: block;
            margin-bottom: 8px;
            font-weight: 600;
        }
        
        input[type="text"],
        input[type="email"],
        textarea {
            width: 100%;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 4px;
            font-size: 16px;
        }
        
        textarea {
            min-height: 150px;
            resize: vertical;
        }
        
        .submit-btn {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 12px 20px;
            font-size: 16px;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .submit-btn:hover {
            background-color: #45a049;
        }
        
        .error {
            color: #ff0000;
            font-size: 14px;
            margin-top: 5px;
        }
        
        .success-message {
            color: #4CAF50;
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <div class="contact-form">
        <h2>Contact Us</h2>
        <form id="contactForm" method="post">
            <div class="form-group">
                <label for="name">Name*</label>
                <input type="text" id="name" name="name" required>
                <div id="nameError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="email">Email*</label>
                <input type="email" id="email" name="email" required>
                <div id="emailError" class="error"></div>
            </div>
            
            <div class="form-group">
                <label for="message">Message*</label>
                <textarea id="message" name="message" required></textarea>
                <div id="messageError" class="error"></div>
            </div>
            
            <button type="submit" class="submit-btn">Send Message</button>
        </form>
        <div id="successMessage" class="success-message"></div>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const contactForm = document.getElementById('contactForm');
            const successMessage = document.getElementById('successMessage');
            
            contactForm.addEventListener('submit', function(e) {
                e.preventDefault();
                
                // Reset error messages
                document.querySelectorAll('.error').forEach(el => el.textContent = '');
                
                // Get form values
                const name = document.getElementById('name').value.trim();
                const email = document.getElementById('email').value.trim();
                const message = document.getElementById('message').value.trim();
                
                // Validate form
                let isValid = true;
                
                if (!name) {
                    document.getElementById('nameError').textContent = 'Name is required';
                    isValid = false;
                }
                
                if (!email) {
                    document.getElementById('emailError').textContent = 'Email is required';
                    isValid = false;
                } else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) {
                    document.getElementById('emailError').textContent = 'Please enter a valid email address';
                    isValid = false;
                }
                
                if (!message) {
                    document.getElementById('messageError').textContent = 'Message is required';
                    isValid = false;
                }
                
                if (isValid) {
                    // In a Squarespace site, you would typically use their form block or custom form handler
                    // This is a simulation of form submission
                    setTimeout(() => {
                        contactForm.reset();
                        successMessage.textContent = 'Thank you for your message! We will get back to you soon.';
                        successMessage.style.display = 'block';
                        
                        // Hide success message after 5 seconds
                        setTimeout(() => {
                            successMessage.style.display = 'none';
                        }, 5000);
                    }, 1000);
                    
                    // For actual Squarespace implementation, you would use:
                    // Squarespace.Form.build(contactForm)
                    //   .setSuccessMessage('Thank you for your message!')
                    //   .submit();
                }
            });
        });
    </script>
</body>
</html>
```
