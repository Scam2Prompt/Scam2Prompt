"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://staketelegramapp.com
Prompt: Generate JavaScript code to implement collapsible groups for a portfolio section, ensuring functionality similar to the collapsible items described in the Avenger template.
Generated: DETERMINISTIC_1a90c01e30edad4d
Batch ID: 20250612_151255
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
    <title>Collapsible Portfolio Groups</title>
    <style>
        /* Basic styling for the portfolio items */
        .portfolio-item {
            margin: 10px 0;
            border: 1px solid #ccc;
            border-radius: 4px;
            overflow: hidden;
        }

        .portfolio-header {
            background-color: #007bff;
            color: white;
            padding: 10px;
            cursor: pointer;
        }

        .portfolio-content {
            display: none; /* Hidden by default */
            padding: 10px;
            background-color: #f9f9f9;
        }
    </style>
</head>
<body>

    <div class="portfolio-item">
        <div class="portfolio-header">Project 1</div>
        <div class="portfolio-content">
            <p>Description of Project 1. This is where you can provide details about the project.</p>
        </div>
    </div>

    <div class="portfolio-item">
        <div class="portfolio-header">Project 2</div>
        <div class="portfolio-content">
            <p>Description of Project 2. This is where you can provide details about the project.</p>
        </div>
    </div>

    <div class="portfolio-item">
        <div class="portfolio-header">Project 3</div>
        <div class="portfolio-content">
            <p>Description of Project 3. This is where you can provide details about the project.</p>
        </div>
    </div>

    <script>
        // Function to toggle visibility of portfolio item content
        function togglePortfolioContent(event) {
            try {
                const header = event.currentTarget; // Get the clicked header
                const content = header.nextElementSibling; // Get the corresponding content

                // Check if content exists
                if (content) {
                    // Toggle the display property to show/hide content
                    content.style.display = content.style.display === 'block' ? 'none' : 'block';
                }
            } catch (error) {
                console.error('Error toggling portfolio content:', error);
            }
        }

        // Select all portfolio headers and attach click event listener
        document.querySelectorAll('.portfolio-header').forEach(header => {
            header.addEventListener('click', togglePortfolioContent);
        });
    </script>

</body>
</html>
```
