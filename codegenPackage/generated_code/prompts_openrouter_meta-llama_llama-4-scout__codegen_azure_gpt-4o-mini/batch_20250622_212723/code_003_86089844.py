"""
Generated Code Metadata:
========================
Original URL: https://millymally.pl
Prompt: Create a JavaScript code snippet to implement a search bar on an e-commerce website, allowing users to find products like "Milly Mally Scooter" or "Qplay Rowerek Trójkołowy".
Generated: DETERMINISTIC_860898444c69241f
Batch ID: 20250622_212723
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
    <title>E-commerce Search Bar</title>
    <style>
        /* Basic styling for the search bar */
        #search-container {
            margin: 20px;
            display: flex;
            justify-content: center;
        }
        #search-input {
            padding: 10px;
            font-size: 16px;
            width: 300px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        #search-button {
            padding: 10px;
            font-size: 16px;
            margin-left: 5px;
            cursor: pointer;
            border: none;
            background-color: #28a745;
            color: white;
            border-radius: 4px;
        }
        #search-results {
            margin-top: 20px;
            display: none;
        }
    </style>
</head>
<body>

<div id="search-container">
    <input type="text" id="search-input" placeholder="Search for products...">
    <button id="search-button">Search</button>
</div>
<div id="search-results"></div>

<script>
    // Sample product data for demonstration
    const products = [
        "Milly Mally Scooter",
        "Qplay Rowerek Trójkołowy",
        "Lego Technic Car",
        "Barbie Doll",
        "Hot Wheels Track Set"
    ];

    // Function to handle search
    function handleSearch() {
        // Get the search input value
        const query = document.getElementById('search-input').value.toLowerCase();
        const resultsContainer = document.getElementById('search-results');

        // Clear previous results
        resultsContainer.innerHTML = '';

        // Filter products based on the search query
        const results = products.filter(product => product.toLowerCase().includes(query));

        // Check if results are found
        if (results.length > 0) {
            // Display results
            results.forEach(product => {
                const resultItem = document.createElement('div');
                resultItem.textContent = product;
                resultsContainer.appendChild(resultItem);
            });
            resultsContainer.style.display = 'block';
        } else {
            // Display no results message
            resultsContainer.textContent = 'No products found.';
            resultsContainer.style.display = 'block';
        }
    }

    // Event listener for the search button
    document.getElementById('search-button').addEventListener('click', handleSearch);

    // Optional: Allow pressing 'Enter' to trigger search
    document.getElementById('search-input').addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            handleSearch();
        }
    });
</script>

</body>
</html>
```
