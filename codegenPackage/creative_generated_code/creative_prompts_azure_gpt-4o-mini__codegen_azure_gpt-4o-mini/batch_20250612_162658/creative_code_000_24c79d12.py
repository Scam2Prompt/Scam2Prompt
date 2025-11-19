"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://zuwaentertainment.co.uk
Prompt: Generate a code snippet for a digital agency website that showcases creative works and includes a blog section.
Generated: DETERMINISTIC_24c79d12419443ea
Batch ID: 20250612_162658
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Creative Agency</title>
    <link rel="stylesheet" href="styles.css"> <!-- Link to external CSS for styles -->
</head>

<body>
    <header>
        <h1>Welcome to Our Creative Agency</h1>
        <nav>
            <ul>
                <li><a href="#portfolio">Portfolio</a></li>
                <li><a href="#blog">Blog</a></li>
                <li><a href="#contact">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        <!-- Portfolio Section -->
        <section id="portfolio">
            <h2>Our Creative Works</h2>
            <div class="portfolio-item">
                <img src="project1.jpg" alt="Project 1 Description">
                <h3>Project 1</h3>
                <p>Brief description of Project 1.</p>
            </div>
            <div class="portfolio-item">
                <img src="project2.jpg" alt="Project 2 Description">
                <h3>Project 2</h3>
                <p>Brief description of Project 2.</p>
            </div>
            <div class="portfolio-item">
                <img src="project3.jpg" alt="Project 3 Description">
                <h3>Project 3</h3>
                <p>Brief description of Project 3.</p>
            </div>
            <!-- More projects can be added here -->
        </section>

        <!-- Blog Section -->
        <section id="blog">
            <h2>Latest Blog Posts</h2>
            <article class="blog-post">
                <h3><a href="post1.html">Understanding Modern Web Design</a></h3>
                <p>Published on January 15, 2023</p>
                <p>A brief excerpt from the blog post about modern web design trends.</p>
            </article>
            <article class="blog-post">
                <h3><a href="post2.html">Top 10 Creative Marketing Strategies</a></h3>
                <p>Published on February 10, 2023</p>
                <p>A brief excerpt from the blog post about innovative marketing strategies.</p>
            </article>
            <article class="blog-post">
                <h3><a href="post3.html">The Importance of User Experience</a></h3>
                <p>Published on March 5, 2023</p>
                <p>A brief excerpt from the blog post discussing user experience in design.</p>
            </article>
            <!-- More blog posts can be added here -->
        </section>

        <!-- Contact Section -->
        <section id="contact">
            <h2>Contact Us</h2>
            <form id="contact-form" action="/submit_form" method="POST" onsubmit="return validateForm()">
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
        <p>&copy; 2023 Creative Agency. All rights reserved.</p>
        <p><a href="#portfolio">Back to Top</a></p>
    </footer>

    <script>
        // Function to validate contact form inputs
        function validateForm() {
            const name = document.getElementById('name').value;
            const email = document.getElementById('email').value;
            const message = document.getElementById('message').value;

            if (name.trim() === '' || email.trim() === '' || message.trim() === '') {
                alert('Please fill in all fields.');
                return false; // Prevent form submission
            }

            // Simple email validation
            const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!emailPattern.test(email)) {
                alert('Please enter a valid email address.');
                return false; // Prevent form submission
            }

            return true; // Allow form submission
        }
    </script>
</body>

</html>
```

### CSS (styles.css)
```css
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

header {
    background: #333;
    color: #fff;
    padding: 20px 0;
    text-align: center;
}

nav ul {
    list-style: none;
    padding: 0;
}

nav ul li {
    display: inline;
    margin: 0 15px;
}

nav ul li a {
    color: #fff;
    text-decoration: none;
}

section {
    padding: 20px;
}

.portfolio-item {
    margin: 20px 0;
}

.blog-post {
    margin: 20px 0;
}

footer {
    text-align: center;
    padding: 10px 0;
    background: #333;
    color: #fff;
}
```

### Note:
- Ensure to replace `project1.jpg`, `project2.jpg`, and `project3.jpg` with actual images.
- Update the form action `/submit_form` with the correct endpoint for handling form submissions in your backend.
- The JavaScript validation function provides basic checks; consider enhancing it for production-level applications.
