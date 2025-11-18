"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinekiosk.gr
Prompt: Create JavaScript code to dynamically display product categories like "CBG," "CBD," and "Cocktails" on Marine Kiosk's homepage, ensuring the categories are expandable to show detailed product listings.
Generated: DETERMINISTIC_9a77a473811b599b
Batch ID: 20250612_153246
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
    <title>Marine Kiosk - Product Categories</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 0;
        }
        .category {
            border: 1px solid #ccc;
            padding: 10px;
            margin: 10px 0;
            cursor: pointer;
        }
        .products {
            display: none; /* Hide products by default */
            padding-left: 20px;
        }
    </style>
</head>
<body>

    <h1>Product Categories</h1>
    <div id="categories"></div>

    <script>
        // Sample data for product categories and products
        const categoriesData = [
            {
                name: "CBG",
                products: ["CBG Oil", "CBG Gummies", "CBG Capsules"]
            },
            {
                name: "CBD",
                products: ["CBD Oil", "CBD Cream", "CBD Vape"]
            },
            {
                name: "Cocktails",
                products: ["CBD Cocktail Mix", "CBG Cocktail Mix"]
            }
        ];

        // Function to create and display product categories
        function displayCategories(categories) {
            const categoriesContainer = document.getElementById('categories');

            categories.forEach(category => {
                // Create category element
                const categoryDiv = document.createElement('div');
                categoryDiv.className = 'category';
                categoryDiv.textContent = category.name;

                // Create products container
                const productsDiv = document.createElement('div');
                productsDiv.className = 'products';

                // Populate products for the category
                category.products.forEach(product => {
                    const productItem = document.createElement('div');
                    productItem.textContent = product;
                    productsDiv.appendChild(productItem);
                });

                // Event listener to toggle product visibility
                categoryDiv.addEventListener('click', () => {
                    // Toggle product display
                    const isVisible = productsDiv.style.display === 'block';
                    productsDiv.style.display = isVisible ? 'none' : 'block';
                });

                // Append category and products to the container
                categoriesContainer.appendChild(categoryDiv);
                categoriesContainer.appendChild(productsDiv);
            });
        }

        // Error handling for data fetching (if needed)
        try {
            displayCategories(categoriesData);
        } catch (error) {
            console.error("An error occurred while displaying categories:", error);
            alert("Unable to load categories. Please try again later.");
        }
    </script>

</body>
</html>
```
