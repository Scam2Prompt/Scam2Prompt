"""
Generated Code Metadata:
========================
Original URL: https://kktravelsolutions.co.tz
Prompt: Generate a code snippet for a travel consultancy website that showcases services like DMCC, MICE & Tourism Safaris, and Study Abroad facilitations.
Generated: DETERMINISTIC_76a0ee0e37ee45c1
Batch ID: 20250622_211427
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
    <title>Global Travel Consultancy</title>
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

        .container {
            width: 90%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px 0;
        }

        /* Header styles */
        header {
            background-color: #003366;
            color: white;
            padding: 20px 0;
            text-align: center;
        }

        header h1 {
            margin-bottom: 10px;
        }

        /* Navigation */
        nav {
            background-color: #004080;
            padding: 10px 0;
        }

        nav ul {
            display: flex;
            justify-content: center;
            list-style: none;
        }

        nav ul li {
            margin: 0 15px;
        }

        nav ul li a {
            color: white;
            text-decoration: none;
            font-weight: bold;
            padding: 5px 10px;
            border-radius: 4px;
            transition: background-color 0.3s;
        }

        nav ul li a:hover {
            background-color: #0055a5;
        }

        /* Service cards */
        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }

        .service-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            padding: 20px;
            transition: transform 0.3s;
        }

        .service-card:hover {
            transform: translateY(-5px);
        }

        .service-card h3 {
            color: #003366;
            margin-bottom: 15px;
            border-bottom: 2px solid #004080;
            padding-bottom: 10px;
        }

        .service-card p {
            margin-bottom: 15px;
        }

        .btn {
            display: inline-block;
            background-color: #004080;
            color: white;
            padding: 8px 16px;
            border-radius: 4px;
            text-decoration: none;
            transition: background-color 0.3s;
        }

        .btn:hover {
            background-color: #0055a5;
        }

        /* Footer */
        footer {
            background-color: #003366;
            color: white;
            text-align: center;
            padding: 20px 0;
            margin-top: 30px;
        }

        /* Responsive adjustments */
        @media (max-width: 768px) {
            nav ul {
                flex-direction: column;
                align-items: center;
            }

            nav ul li {
                margin: 5px 0;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <h1>Global Travel Consultancy</h1>
            <p>Your trusted partner for global travel solutions</p>
        </div>
    </header>

    <nav>
        <div class="container">
            <ul>
                <li><a href="#home">Home</a></li>
                <li><a href="#services">Services</a></li>
                <li><a href="#about">About Us</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </div>
    </nav>

    <main class="container">
        <section id="services">
            <h2>Our Services</h2>
            <div class="services">
                <!-- DMCC Service -->
                <div class="service-card">
                    <h3>DMCC Business Setup</h3>
                    <p>Comprehensive services for setting up your business in Dubai Multi Commodities Centre (DMCC), including licensing, visa processing, and office setup.</p>
                    <a href="#contact" class="btn">Enquire Now</a>
                </div>

                <!-- MICE & Tourism Safaris -->
                <div class="service-card">
                    <h3>MICE & Tourism Safaris</h3>
                    <p>Tailored solutions for Meetings, Incentives, Conferences, and Exhibitions (MICE) along with bespoke safari experiences across Africa.</p>
                    <a href="#contact" class="btn">Plan Your Trip</a>
                </div>

                <!-- Study Abroad -->
                <div class="service-card">
                    <h3>Study Abroad Facilitations</h3>
                    <p>Expert guidance for students seeking international education opportunities, including university applications, visa assistance, and accommodation.</p>
                    <a href="#contact" class="btn">Start Your Journey</a>
                </div>
            </div>
        </section>

        <section id="about" style="margin-top: 50px;">
            <h2>About Us</h2>
            <p>Global Travel Consultancy is a premier travel and business solutions provider with over 15 years of experience in helping clients navigate international opportunities. Our team of experts ensures seamless experiences for all your travel and business needs.</p>
        </section>

        <section id="contact" style="margin-top: 50px;">
            <h2>Contact Us</h2>
            <form id="contactForm" style="max-width: 600px; margin-top: 20px;">
                <div style="margin-bottom: 15px;">
                    <label for="name" style="display: block; margin-bottom: 5px;">Name:</label>
                    <input type="text" id="name" name="name" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 15px;">
                    <label for="email" style="display: block; margin-bottom: 5px;">Email:</label>
                    <input type="email" id="email" name="email" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
                </div>
                <div style="margin-bottom: 15px;">
                    <label for="service" style="display: block; margin-bottom: 5px;">Service Interested In:</label>
                    <select id="service" name="service" style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;">
                        <option value="dmcc">DMCC Business Setup</option>
                        <option value="mice">MICE & Tourism Safaris</option>
                        <option value="study">Study Abroad Facilitations</option>
                        <option value="other">Other</option>
                    </select>
                </div>
                <div style="margin-bottom: 15px;">
                    <label for="message" style="display: block; margin-bottom: 5px;">Message:</label>
                    <textarea id="message" name="message" rows="4" required style="width: 100%; padding: 8px; border: 1px solid #ddd; border-radius: 4px;"></textarea>
                </div>
                <button type="submit" class="btn">Submit</button>
            </form>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2023 Global Travel Consultancy. All rights reserved.</p>
        </div>
    </footer>

    <script>
        // Form submission handling
        document.getElementById('contactForm').addEventListener('submit', function(e) {
            e.preventDefault();
            
            // Get form values
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const service = document.getElementById('service').value;
            const message = document.getElementById('message').value;
            
            // Basic validation
            if (!name || !email || !message) {
                alert('Please fill in all required fields.');
                return;
            }
            
            // In a real application, you would send this data to a server
            // For demo purposes, we'll just show a success message
            alert(`Thank you, ${name}! Your enquiry about ${service} has been received. We'll contact you at ${email} shortly.`);
            
            // Reset the form
            this.reset();
        });
    </script>
</body>
</html>
```
