"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rabbie-wall--extension-docs.teachable.com
Prompt: Generate JavaScript code for implementing a "Sort by" dropdown menu for an online course platform, as seen in the rabbie-wall--extension-docs interface.
Generated: DETERMINISTIC_61113d3f13992763
Batch ID: 20250612_153722
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
    <title>Sort By Dropdown</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }
        .dropdown {
            position: relative;
            display: inline-block;
        }
        .dropdown-content {
            display: none;
            position: absolute;
            background-color: #f9f9f9;
            min-width: 160px;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1;
        }
        .dropdown-content a {
            color: black;
            padding: 12px 16px;
            text-decoration: none;
            display: block;
        }
        .dropdown-content a:hover {
            background-color: #f1f1f1;
        }
        .show {
            display: block;
        }
    </style>
</head>
<body>

<div class="dropdown">
    <button onclick="toggleDropdown()" class="dropbtn">Sort by</button>
    <div id="myDropdown" class="dropdown-content">
        <a href="#" data-sort="date">Date</a>
        <a href="#" data-sort="popularity">Popularity</a>
        <a href="#" data-sort="rating">Rating</a>
        <a href="#" data-sort="price">Price</a>
    </div>
</div>

<script>
    // Function to toggle the visibility of the dropdown menu
    function toggleDropdown() {
        document.getElementById("myDropdown").classList.toggle("show");
    }

    // Event listener to close the dropdown if the user clicks outside of it
    window.onclick = function(event) {
        if (!event.target.matches('.dropbtn')) {
            let dropdowns = document.getElementsByClassName("dropdown-content");
            for (let i = 0; i < dropdowns.length; i++) {
                let openDropdown = dropdowns[i];
                if (openDropdown.classList.contains('show')) {
                    openDropdown.classList.remove('show');
                }
            }
        }
    }

    // Event listener for sort options
    document.getElementById("myDropdown").addEventListener("click", function(event) {
        // Check if a sort option was clicked
        if (event.target.tagName === 'A') {
            event.preventDefault(); // Prevent default link behavior

            // Get the sort type from the clicked link
            const sortType = event.target.getAttribute('data-sort');
            try {
                sortCourses(sortType); // Call the sort function
            } catch (error) {
                console.error("Error sorting courses:", error);
                alert("An error occurred while sorting. Please try again."); // User-friendly error message
            }
        }
    });

    // Placeholder function to sort courses based on the selected option
    function sortCourses(criteria) {
        // TODO: Implement sorting logic based on the criteria
        console.log("Sorting courses by:", criteria);
    }
</script>

</body>
</html>
```
