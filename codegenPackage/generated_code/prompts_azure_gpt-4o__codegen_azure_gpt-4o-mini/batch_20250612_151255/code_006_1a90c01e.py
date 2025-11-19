"""
Generated Code Metadata:
========================
Original URL: https://staketelegramapp.com
Prompt: Generate JavaScript code to implement collapsible groups for a portfolio section, ensuring functionality similar to the collapsible items described in the Avenger template.
Generated: DETERMINISTIC_1a90c01e30edad4d
Batch ID: 20250612_151255
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
    <title>Collapsible Portfolio Section</title>
    <style>
        /* Basic styles for the collapsible sections */
        .collapsible {
            background-color: #f1f1f1;
            color: #444;
            cursor: pointer;
            padding: 10px;
            width: 100%;
            border: none;
            text-align: left;
            outline: none;
            font-size: 15px;
            transition: background-color 0.3s ease;
        }

        .active, .collapsible:hover {
            background-color: #ccc;
        }

        .content {
            padding: 0 18px;
            display: none; /* Hidden by default */
            overflow: hidden;
            background-color: white;
        }
    </style>
</head>
<body>

<h2>My Portfolio</h2>

<!-- Collapsible button for each portfolio group -->
<button class="collapsible">Project Group 1</button>
<div class="content">
    <p>Details about Project Group 1.</p>
</div>

<button class="collapsible">Project Group 2</button>
<div class="content">
    <p>Details about Project Group 2.</p>
</div>

<button class="collapsible">Project Group 3</button>
<div class="content">
    <p>Details about Project Group 3.</p>
</div>

<script>
    // Function to initialize collapsible elements
    function initCollapsible() {
        // Select all collapsible buttons
        const collapsibles = document.getElementsByClassName("collapsible");

        // Loop through each collapsible button
        for (let i = 0; i < collapsibles.length; i++) {
            // Add click event listener to each button
            collapsibles[i].addEventListener("click", function() {
                // Toggle the active class to change the button style
                this.classList.toggle("active");

                // Get the associated content div
                const content = this.nextElementSibling;

                // Check if the content is currently displayed
                if (content.style.display === "block") {
                    // If displayed, hide it
                    content.style.display = "none";
                } else {
                    // If hidden, show it
                    content.style.display = "block";
                }
            });
        }
    }

    // Initialize collapsible functionality on page load
    document.addEventListener("DOMContentLoaded", initCollapsible);
</script>

</body>
</html>
```
