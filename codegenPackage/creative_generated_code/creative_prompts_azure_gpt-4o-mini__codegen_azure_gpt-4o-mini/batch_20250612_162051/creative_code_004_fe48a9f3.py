"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://restauranteycoffeeshopsancarlos.com
Prompt: Illustrate how to implement a wishlist feature for menu items using HTML and JavaScript, inspired by the functionalities of Restaurante y Coffee Shop San Carlos.
Generated: DETERMINISTIC_fe48a9f381aff8ed
Batch ID: 20250612_162051
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
    <title>Restaurant Wishlist Feature</title>
    <style>
        /* Basic styling for the wishlist feature */
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }

        .menu-item {
            border: 1px solid #ccc;
            padding: 15px;
            margin: 10px 0;
            background-color: #fff;
            border-radius: 5px;
        }

        .wishlist {
            margin-top: 20px;
            border: 1px solid #007bff;
            padding: 10px;
            border-radius: 5px;
            background-color: #e9f5ff;
        }

        .button {
            padding: 10px 15px;
            background-color: #007bff;
            color: white;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }

        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>

<body>
    <h1>Restaurant Menu</h1>
    <div id="menu">
        <!-- Sample menu items -->
        <div class="menu-item" data-name="Coffee" data-price="3.00">
            <h2>Coffee</h2>
            <p>Price: $3.00</p>
            <button class="button add-to-wishlist">Add to Wishlist</button>
        </div>
        <div class="menu-item" data-name="Sandwich" data-price="5.50">
            <h2>Sandwich</h2>
            <p>Price: $5.50</p>
            <button class="button add-to-wishlist">Add to Wishlist</button>
        </div>
        <div class="menu-item" data-name="Cake" data-price="4.00">
            <h2>Cake</h2>
            <p>Price: $4.00</p>
            <button class="button add-to-wishlist">Add to Wishlist</button>
        </div>
    </div>

    <div class="wishlist">
        <h2>Your Wishlist</h2>
        <ul id="wishlist-items"></ul>
    </div>

    <script>
        // Initialize an empty wishlist
        const wishlist = [];

        // Function to update the wishlist display
        function updateWishlistDisplay() {
            const wishlistItems = document.getElementById('wishlist-items');
            wishlistItems.innerHTML = ''; // Clear existing items

            // Check if wishlist is empty
            if (wishlist.length === 0) {
                wishlistItems.innerHTML = '<li>No items in your wishlist.</li>';
                return;
            }

            // Populate the wishlist
            wishlist.forEach(item => {
                const listItem = document.createElement('li');
                listItem.textContent = `${item.name} - $${item.price}`;
                wishlistItems.appendChild(listItem);
            });
        }

        // Function to handle adding items to the wishlist
        function addToWishlist(event) {
            // Get the menu item details from the data attributes
            const menuItem = event.target.closest('.menu-item');
            const itemName = menuItem.getAttribute('data-name');
            const itemPrice = menuItem.getAttribute('data-price');

            // Create a new wishlist item object
            const newItem = {
                name: itemName,
                price: parseFloat(itemPrice) // Convert price to a number
            };

            // Check if the item is already in the wishlist
            const isAlreadyInWishlist = wishlist.some(item => item.name === newItem.name);
            if (isAlreadyInWishlist) {
                alert(`${newItem.name} is already in your wishlist!`);
                return; // Prevent adding duplicates
            }

            // Add the new item to the wishlist
            wishlist.push(newItem);
            updateWishlistDisplay(); // Update the display
        }

        // Attach event listeners to the 'Add to Wishlist' buttons
        const addButtons = document.querySelectorAll('.add-to-wishlist');
        addButtons.forEach(button => {
            button.addEventListener('click', addToWishlist);
        });
    </script>
</body>

</html>
```
