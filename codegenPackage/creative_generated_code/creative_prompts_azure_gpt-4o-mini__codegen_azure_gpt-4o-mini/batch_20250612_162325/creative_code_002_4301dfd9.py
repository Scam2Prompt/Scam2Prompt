"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mobleman-doostan.com
Prompt: Create a JavaScript function that dynamically displays a list of home furniture products like "میز ناهار خوری" and "کمد لباس" when a user selects a category from a dropdown menu.
Generated: DETERMINISTIC_4301dfd99fa1c161
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="fa">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home Furniture Selector</title>
    <style>
        /* Basic styling for the dropdown and product list */
        body {
            font-family: Arial, sans-serif;
        }
        #furnitureList {
            margin-top: 20px;
            border: 1px solid #ccc;
            padding: 10px;
            display: none; /* Initially hidden */
        }
    </style>
</head>
<body>
    <h1>انتخاب مبلمان منزل</h1>
    <label for="categorySelect">دسته بندی را انتخاب کنید:</label>
    <select id="categorySelect">
        <option value="">-- انتخاب کنید --</option>
        <option value="dining">میز ناهار خوری</option>
        <option value="wardrobe">کمد لباس</option>
    </select>

    <div id="furnitureList"></div>

    <script>
        // Object containing furniture products categorized by type
        const furnitureCatalog = {
            dining: [
                "میز ناهار خوری چوبی",
                "میز ناهار خوری شیشه‌ای",
                "میز ناهار خوری گرد"
            ],
            wardrobe: [
                "کمد لباس بزرگ",
                "کمد لباس کوچک",
                "کمد لباس با آینه"
            ]
        };

        /**
         * Function to display furniture products based on selected category
         */
        function displayFurniture() {
            // Get the selected category value
            const categorySelect = document.getElementById("categorySelect");
            const selectedCategory = categorySelect.value;

            // Get the furniture list container
            const furnitureListDiv = document.getElementById("furnitureList");
            furnitureListDiv.innerHTML = ""; // Clear previous results

            // Check if a category is selected
            if (selectedCategory && furnitureCatalog[selectedCategory]) {
                // Create a list of products
                const products = furnitureCatalog[selectedCategory];
                const ul = document.createElement("ul");

                // Populate the list with products
                products.forEach(product => {
                    const li = document.createElement("li");
                    li.textContent = product;
                    ul.appendChild(li);
                });

                furnitureListDiv.appendChild(ul);
                furnitureListDiv.style.display = "block"; // Show the list
            } else {
                // Hide the list if no valid category is selected
                furnitureListDiv.style.display = "none";
            }
        }

        // Add event listener to the dropdown menu
        document.getElementById("categorySelect").addEventListener("change", displayFurniture);
    </script>
</body>
</html>
```
