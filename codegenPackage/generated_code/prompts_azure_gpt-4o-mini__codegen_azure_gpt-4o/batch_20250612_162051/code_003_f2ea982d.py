"""
Generated Code Metadata:
========================
Original URL: https://okulistatrzebnica.pl
Prompt: Develop a simple HTML/CSS layout for a website homepage for an eye clinic, incorporating sections for services, contact information, and a booking form.
Generated: DETERMINISTIC_f2ea982d761c3fe5
Batch ID: 20250612_162051
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
    <meta name="description" content="Eye Clinic Homepage - Services, Contact Information, and Booking Form">
    <title>Eye Clinic Homepage</title>
    <style>
        /* General Styles */
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f9f9f9;
            color: #333;
        }

        header {
            background-color: #0077b6;
            color: #fff;
            padding: 20px;
            text-align: center;
        }

        header h1 {
            margin: 0;
        }

        nav {
            margin-top: 10px;
        }

        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }

        nav a:hover {
            text-decoration: underline;
        }

        main {
            padding: 20px;
        }

        section {
            margin-bottom: 40px;
        }

        h2 {
            color: #0077b6;
        }

        /* Services Section */
        .services {
            display: flex;
            gap: 20px;
        }

        .service {
            flex: 1;
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        /* Contact Section */
        .contact {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .contact p {
            margin: 10px 0;
        }

        /* Booking Form Section */
        .booking-form {
            background-color: #e3f2fd;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }

        .booking-form label {
            display: block;
            margin: 10px 0 5px;
        }

        .booking-form input,
        .booking-form textarea,
        .booking-form button {
            width: 100%;
            padding: 10px;
            margin-bottom: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        .booking-form button {
            background-color: #0077b6;
            color: #fff;
            border: none;
            cursor: pointer;
        }

        .booking-form button:hover {
            background-color: #005f8a;
        }

        footer {
            text-align: center;
            padding: 10px;
            background-color: #0077b6;
            color: #fff;
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header>
        <h1>Welcome to Our Eye Clinic</h1>
        <nav>
            <a href="#services">Services</a>
            <a href="#contact">Contact</a>
            <a href="#booking">Book Appointment</a>
        </nav>
    </header>

    <!-- Main Content -->
    <main>
        <!-- Services Section -->
        <section id="services">
            <h2>Our Services</h2>
            <div class="services">
                <div class="service">
                    <h3>Eye Exams</h3>
                    <p>Comprehensive eye exams to ensure your vision is healthy.</p>
                </div>
                <div class="service">
                    <h3>Contact Lenses</h3>
                    <p>Fitting and consultation for contact lenses.</p>
                </div>
                <div class="service">
                    <h3>Surgical Procedures</h3>
                    <p>Advanced surgical procedures for various eye conditions.</p>
                </div>
            </div>
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <h2>Contact Us</h2>
            <div class="contact">
                <p><strong>Address:</strong> 123 Vision Lane, Eye City, EC 45678</p>
                <p><strong>Phone:</strong> (123) 456-7890</p>
                <p><strong>Email:</strong> contact@eyeclinic.com</p>
            </div>
        </section>

        <!-- Booking Form Section -->
        <section id="booking">
            <h2>Book an Appointment</h2>
            <div class="booking-form">
                <form action="/submit-booking" method="POST">
                    <label for="name">Full Name:</label>
                    <input type="text" id="name" name="name" required>

                    <label for="email">Email Address:</label>
                    <input type="email" id="email" name="email" required>

                    <label for="phone">Phone Number:</label>
                    <input type="tel" id="phone" name="phone" required>

                    <label for="message">Additional Information:</label>
                    <textarea id="message" name="message" rows="4"></textarea>

                    <button type="submit">Submit</button>
                </form>
            </div>
        </section>
    </main>

    <!-- Footer Section -->
    <footer>
        <p>&copy; 2023 Eye Clinic. All rights reserved.</p>
    </footer>
</body>
</html>
```
