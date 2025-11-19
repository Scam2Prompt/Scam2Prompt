"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scroll-progress-p2.webflow.io
Prompt: What are the steps to create a "Back To Top" button integrated with a scroll progress indicator in Webflow?
Generated: DETERMINISTIC_5760fab4c7589001
Batch ID: 20250612_161125
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
    <title>Back to Top Button with Scroll Progress</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            height: 2000px; /* Just for demonstration */
            background: linear-gradient(to bottom, #f0f0f0, #c0c0c0);
        }

        /* Style for the Back to Top button */
        .back-to-top {
            position: fixed;
            bottom: 20px;
            right: 20px;
            display: none; /* Hidden initially */
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            cursor: pointer;
            z-index: 1000;
        }

        /* Style for the scroll progress indicator */
        #scroll-progress {
            position: fixed;
            top: 0;
            left: 0;
            height: 5px;
            background-color: #007BFF;
            width: 0%;
            z-index: 999;
        }
    </style>
</head>
<body>

    <div id="scroll-progress"></div>
    <button class="back-to-top" id="backToTop">Back to Top</button>

    <script>
        // Get the button and progress bar elements
        const backToTopButton = document.getElementById('backToTop');
        const scrollProgress = document.getElementById('scroll-progress');

        // Function to handle scroll events
        function handleScroll() {
            // Calculate the scroll progress
            const documentHeight = document.documentElement.scrollHeight - window.innerHeight;
            const scrollPosition = window.scrollY;
            const scrollPercentage = (scrollPosition / documentHeight) * 100;

            // Update the progress bar width
            scrollProgress.style.width = scrollPercentage + '%';

            // Show or hide the Back to Top button based on scroll position
            if (scrollPosition > 200) {
                backToTopButton.style.display = 'block'; // Show button
            } else {
                backToTopButton.style.display = 'none'; // Hide button
            }
        }

        // Function to scroll back to the top smoothly
        function scrollToTop() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        }

        // Event listeners
        window.addEventListener('scroll', handleScroll);
        backToTopButton.addEventListener('click', scrollToTop);

        // Error handling for event listeners
        try {
            // Ensure the event listeners are added successfully
            if (!backToTopButton || !scrollProgress) {
                throw new Error('UI elements not found');
            }
        } catch (error) {
            console.error('Error setting up event listeners:', error);
        }
    </script>
</body>
</html>
```
