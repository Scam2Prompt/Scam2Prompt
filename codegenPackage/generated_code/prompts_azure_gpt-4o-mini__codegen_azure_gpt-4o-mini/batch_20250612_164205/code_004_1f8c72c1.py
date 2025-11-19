"""
Generated Code Metadata:
========================
Original URL: https://fin-flix.me
Prompt: Design a user interface mockup for a financial service website that offers loans without Schufa checks, highlighting features like cashback rewards and flexible membership options.
Generated: DETERMINISTIC_1f8c72c14b5f6aa1
Batch ID: 20250612_164205
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
    <title>Loan Service - No Schufa Check</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to Easy Loans</h1>
        <nav>
            <ul>
                <li><a href="#features">Features</a></li>
                <li><a href="#membership">Membership Options</a></li>
                <li><a href="#contact">Contact Us</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section id="hero">
            <h2>Your Financial Freedom Starts Here</h2>
            <p>Get loans without Schufa checks and enjoy cashback rewards!</p>
            <button onclick="applyNow()">Apply Now</button>
        </section>

        <section id="features">
            <h2>Our Features</h2>
            <ul>
                <li>
                    <h3>No Schufa Checks</h3>
                    <p>We provide loans without the hassle of Schufa checks.</p>
                </li>
                <li>
                    <h3>Cashback Rewards</h3>
                    <p>Earn cashback on every loan you take with us!</p>
                </li>
                <li>
                    <h3>Flexible Membership Options</h3>
                    <p>Choose a membership plan that suits your needs.</p>
                </li>
            </ul>
        </section>

        <section id="membership">
            <h2>Membership Options</h2>
            <div class="membership-plan">
                <h3>Basic Plan</h3>
                <p>Access to standard loan options.</p>
                <button onclick="selectPlan('Basic')">Select Plan</button>
            </div>
            <div class="membership-plan">
                <h3>Premium Plan</h3>
                <p>Access to exclusive loans and higher cashback rates.</p>
                <button onclick="selectPlan('Premium')">Select Plan</button>
            </div>
        </section>

        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contactForm" onsubmit="return handleSubmit(event)">
                <label for="name">Name:</label>
                <input type="text" id="name" name="name" required>
                
                <label for="email">Email:</label>
                <input type="email" id="email" name="email" required>
                
                <label for="message">Message:</label>
                <textarea id="message" name="message" required></textarea>
                
                <button type="submit">Send Message</button>
            </form>
        </section>
    </main>

    <footer>
        <p>&copy; 2023 Easy Loans. All rights reserved.</p>
    </footer>

    <script>
        // Function to handle loan application
        function applyNow() {
            alert("Redirecting to loan application form...");
            // Redirect to application form (placeholder)
            window.location.href = "loan-application.html";
        }

        // Function to handle membership plan selection
        function selectPlan(plan) {
            alert(`You have selected the ${plan} plan.`);
            // Logic to handle plan selection can be added here
        }

        // Function to handle form submission
        function handleSubmit(event) {
            event.preventDefault(); // Prevent default form submission
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            // Basic validation
            if (name && email && message) {
                alert("Thank you for your message!");
                // Logic to send the message can be added here
                document.getElementById('contactForm').reset(); // Reset form
            } else {
                alert("Please fill in all fields.");
            }
            return false; // Prevent form from submitting
        }
    </script>
</body>
</html>
```

```css
/* styles.css */

/* Basic reset for margins and paddings */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

/* Body styles */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    background-color: #f4f4f4;
}

/* Header styles */
header {
    background: #007bff;
    color: #fff;
    padding: 10px 0;
    text-align: center;
}

nav ul {
    list-style: none;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

/* Main section styles */
main {
    padding: 20px;
}

/* Hero section styles */
#hero {
    background: #e9ecef;
    padding: 20px;
    text-align: center;
}

/* Features section styles */
#features {
    margin: 20px 0;
}

/* Membership plan styles */
.membership-plan {
    background: #fff;
    border: 1px solid #ccc;
    padding: 15px;
    margin: 10px 0;
}

/* Contact form styles */
form {
    display: flex;
    flex-direction: column;
}

form label {
    margin: 10px 0 5px;
}

form input, form textarea {
    padding: 10px;
    margin-bottom: 10px;
}

/* Footer styles */
footer {
    text-align: center;
    padding: 10px 0;
    background: #007bff;
    color: #fff;
}
```
