"""
Generated Code Metadata:
========================
Original URL: https://mercatura.co.id
Prompt: Design a basic company profile page using JavaScript, HTML, and CSS that can be easily updated to reflect sections like "About Us," "Our Mission," "What Makes Us Special," and "Our Services."
Generated: DETERMINISTIC_c1f6919a773b34e0
Batch ID: 20250622_204824
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's the complete code for a basic company profile page:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Company Profile</title>
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
            background-color: #2c3e50;
            color: white;
            padding: 1rem 0;
            text-align: center;
        }

        .logo {
            font-size: 2rem;
            font-weight: bold;
            margin-bottom: 0.5rem;
        }

        /* Navigation */
        nav {
            background-color: #34495e;
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
            padding: 0.5rem;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #3498db;
        }

        /* Main content */
        .container {
            max-width: 1200px;
            margin: 2rem auto;
            padding: 0 1rem;
        }

        section {
            margin-bottom: 2rem;
            padding: 1.5rem;
            background-color: white;
            border-radius: 5px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }

        section h2 {
            color: #2c3e50;
            margin-bottom: 1rem;
            padding-bottom: 0.5rem;
            border-bottom: 2px solid #3498db;
        }

        /* Footer */
        footer {
            background-color: #2c3e50;
            color: white;
            text-align: center;
            padding: 1rem 0;
            margin-top: 2rem;
        }

        /* Responsive design */
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
        <div class="logo" id="companyName">Company Name</div>
        <div id="companyTagline">Your trusted partner</div>
    </header>

    <nav>
        <ul>
            <li><a href="#about">About Us</a></li>
            <li><a href="#mission">Our Mission</a></li>
            <li><a href="#special">What Makes Us Special</a></li>
            <li><a href="#services">Our Services</a></li>
        </ul>
    </nav>

    <div class="container">
        <section id="about">
            <h2>About Us</h2>
            <div id="aboutContent">
                <!-- Content will be loaded dynamically -->
            </div>
        </section>

        <section id="mission">
            <h2>Our Mission</h2>
            <div id="missionContent">
                <!-- Content will be loaded dynamically -->
            </div>
        </section>

        <section id="special">
            <h2>What Makes Us Special</h2>
            <div id="specialContent">
                <!-- Content will be loaded dynamically -->
            </div>
        </section>

        <section id="services">
            <h2>Our Services</h2>
            <div id="servicesContent">
                <!-- Content will be loaded dynamically -->
            </div>
        </section>
    </div>

    <footer>
        <p id="footerContent">© 2023 Company Name. All rights reserved.</p>
    </footer>

    <script>
        // Company data - can be easily updated
        const companyData = {
            name: "Acme Corporation",
            tagline: "Innovative solutions for your business",
            about: "Founded in 2010, Acme Corporation has been providing top-quality services to clients worldwide. Our team of experts is dedicated to delivering excellence in every project we undertake.",
            mission: "Our mission is to empower businesses through innovative technology solutions while maintaining the highest standards of integrity and customer service.",
            special: [
                "20+ years of combined industry experience",
                "Customer-first approach",
                "Cutting-edge technology solutions",
                "Proven track record of success"
            ],
            services: [
                "Web Development",
                "Mobile App Development",
                "Cloud Solutions",
                "IT Consulting",
                "Digital Marketing"
            ],
            footer: "© 2023 Acme Corporation. All rights reserved."
        };

        // Function to update page content
        function updatePageContent() {
            try {
                // Update header
                document.getElementById('companyName').textContent = companyData.name;
                document.getElementById('companyTagline').textContent = companyData.tagline;

                // Update sections
                document.getElementById('aboutContent').innerHTML = `<p>${companyData.about}</p>`;
                document.getElementById('missionContent').innerHTML = `<p>${companyData.mission}</p>`;
                
                // Update special section with list
                const specialList = companyData.special.map(item => `<li>${item}</li>`).join('');
                document.getElementById('specialContent').innerHTML = `<ul>${specialList}</ul>`;
                
                // Update services section with list
                const servicesList = companyData.services.map(item => `<li>${item}</li>`).join('');
                document.getElementById('servicesContent').innerHTML = `<ul>${servicesList}</ul>`;
                
                // Update footer
                document.getElementById('footerContent').textContent = companyData.footer;
            } catch (error) {
                console.error("Error updating page content:", error);
                // Fallback content if there's an error
                document.getElementById('aboutContent').innerHTML = "<p>Error loading content. Please try again later.</p>";
            }
        }

        // Initialize the page when DOM is loaded
        document.addEventListener('DOMContentLoaded', updatePageContent);
    </script>
</body>
</html>
```
