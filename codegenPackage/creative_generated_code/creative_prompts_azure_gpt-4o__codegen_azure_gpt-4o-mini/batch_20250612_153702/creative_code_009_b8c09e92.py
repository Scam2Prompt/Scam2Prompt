"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dustbox.netlify.app
Prompt: Generate code to implement a searchable table of contents feature inspired by Dustbox.netlify.app.
Generated: DETERMINISTIC_b8c09e920aa8d664
Batch ID: 20250612_153702
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
    <title>Searchable Table of Contents</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        #toc {
            margin-top: 20px;
        }
        .toc-item {
            padding: 5px;
            cursor: pointer;
        }
        .toc-item:hover {
            background-color: #f0f0f0;
        }
        #search {
            margin-bottom: 10px;
            padding: 8px;
            width: 100%;
            box-sizing: border-box;
        }
    </style>
</head>
<body>

<h1>Document Title</h1>
<p>This is the content of the document. It is filled with various sections that the table of contents will link to.</p>

<!-- Search Input -->
<input type="text" id="search" placeholder="Search...">

<!-- Table of Contents -->
<div id="toc">
    <div class="toc-item" data-target="section1">Section 1</div>
    <div class="toc-item" data-target="section2">Section 2</div>
    <div class="toc-item" data-target="section3">Section 3</div>
    <div class="toc-item" data-target="section4">Section 4</div>
</div>

<!-- Sections -->
<h2 id="section1">Section 1</h2>
<p>Content for section 1...</p>
<h2 id="section2">Section 2</h2>
<p>Content for section 2...</p>
<h2 id="section3">Section 3</h2>
<p>Content for section 3...</p>
<h2 id="section4">Section 4</h2>
<p>Content for section 4...</p>

<script>
    // Wait for the DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', function () {
        const searchInput = document.getElementById('search');
        const tocItems = document.querySelectorAll('.toc-item');

        // Event listener for search input
        searchInput.addEventListener('input', function () {
            const searchTerm = searchInput.value.toLowerCase();

            // Filter TOC items based on search term
            tocItems.forEach(item => {
                const text = item.textContent.toLowerCase();
                if (text.includes(searchTerm)) {
                    item.style.display = 'block'; // Show item if it matches
                } else {
                    item.style.display = 'none'; // Hide item if it doesn't match
                }
            });
        });

        // Event listener for clicking TOC items
        tocItems.forEach(item => {
            item.addEventListener('click', function () {
                const targetId = item.getAttribute('data-target');
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    targetElement.scrollIntoView({ behavior: 'smooth' }); // Smooth scroll to the section
                } else {
                    console.error(`Target element with id ${targetId} not found.`); // Error handling
                }
            });
        });
    });
</script>
</body>
</html>
```
