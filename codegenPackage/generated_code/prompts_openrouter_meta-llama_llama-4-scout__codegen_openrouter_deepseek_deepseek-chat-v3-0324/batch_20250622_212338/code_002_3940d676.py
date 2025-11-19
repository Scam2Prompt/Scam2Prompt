"""
Generated Code Metadata:
========================
Original URL: https://ebrasilbrazz.blogspot.com
Prompt: Generate a JavaScript code to create a product catalog page similar to the one on ebrasilbrazz, which displays products with images, names, and prices, and allows users to sort and filter products.
Generated: DETERMINISTIC_3940d676c8830638
Batch ID: 20250622_212338
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// Product Catalog Page for ebrasilbrazz
document.addEventListener('DOMContentLoaded', function() {
    // Sample product data
    const products = [
        { id: 1, name: 'Brazilian Coffee', price: 12.99, category: 'beverages', image: 'coffee.jpg', rating: 4.5 },
        { id: 2, name: 'Acai Bowl', price: 8.50, category: 'food', image: 'acai.jpg', rating: 4.8 },
        { id: 3, name: 'Havaianas Flip Flops', price: 24.99, category: 'clothing', image: 'flipflops.jpg', rating: 4.2 },
        { id: 4, name: 'Cachaça', price: 15.75, category: 'beverages', image: 'cachaca.jpg', rating: 4.7 },
        { id: 5, name: 'Brigadeiro', price: 5.25, category: 'food', image: 'brigadeiro.jpg', rating: 4.9 },
        { id: 6, name: 'Brazil Nut', price: 7.99, category: 'food', image: 'brazilnut.jpg', rating: 4.3 }
    ];

    // DOM elements
    const productContainer = document.getElementById('product-container');
    const sortSelect = document.getElementById('sort-select');
    const categoryFilter = document.getElementById('category-filter');
    const searchInput = document.getElementById('search-input');

    // Initialize the page
    renderProducts(products);
    populateCategoryFilter();

    // Event listeners
    sortSelect.addEventListener('change', handleSortChange);
    categoryFilter.addEventListener('change', handleFilterChange);
    searchInput.addEventListener('input', handleSearch);

    // Render products to the page
    function renderProducts(productsToRender) {
        productContainer.innerHTML = '';
        
        if (productsToRender.length === 0) {
            productContainer.innerHTML = '<p class="no-products">No products found matching your criteria.</p>';
            return;
        }

        productsToRender.forEach(product => {
            const productElement = document.createElement('div');
            productElement.className = 'product-card';
            productElement.innerHTML = `
                <div class="product-image">
                    <img src="images/${product.image}" alt="${product.name}" onerror="this.src='images/default.jpg'">
                </div>
                <div class="product-info">
                    <h3>${product.name}</h3>
                    <div class="product-meta">
                        <span class="price">$${product.price.toFixed(2)}</span>
                        <span class="rating">${'★'.repeat(Math.floor(product.rating))}${'☆'.repeat(5 - Math.floor(product.rating))}</span>
                    </div>
                    <button class="add-to-cart" data-id="${product.id}">Add to Cart</button>
                </div>
            `;
            productContainer.appendChild(productElement);
        });

        // Add event listeners to all "Add to Cart" buttons
        document.querySelectorAll('.add-to-cart').forEach(button => {
            button.addEventListener('click', addToCart);
        });
    }

    // Populate category filter dropdown
    function populateCategoryFilter() {
        const categories = [...new Set(products.map(product => product.category))];
        categories.unshift('all'); // Add "All Categories" option
        
        categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category;
            option.textContent = category === 'all' ? 'All Categories' : category.charAt(0).toUpperCase() + category.slice(1);
            categoryFilter.appendChild(option);
        });
    }

    // Handle sorting
    function handleSortChange() {
        const sortValue = sortSelect.value;
        let sortedProducts = [...products];
        
        switch(sortValue) {
            case 'price-low':
                sortedProducts.sort((a, b) => a.price - b.price);
                break;
            case 'price-high':
                sortedProducts.sort((a, b) => b.price - a.price);
                break;
            case 'name-asc':
                sortedProducts.sort((a, b) => a.name.localeCompare(b.name));
                break;
            case 'name-desc':
                sortedProducts.sort((a, b) => b.name.localeCompare(a.name));
                break;
            case 'rating':
                sortedProducts.sort((a, b) => b.rating - a.rating);
                break;
            default:
                // No sorting
                break;
        }
        
        renderProducts(applyFilters(sortedProducts));
    }

    // Handle category filtering
    function handleFilterChange() {
        renderProducts(applyFilters(products));
    }

    // Handle search
    function handleSearch() {
        renderProducts(applyFilters(products));
    }

    // Apply all active filters
    function applyFilters(productList) {
        const searchTerm = searchInput.value.toLowerCase();
        const category = categoryFilter.value;
        
        return productList.filter(product => {
            const matchesSearch = product.name.toLowerCase().includes(searchTerm);
            const matchesCategory = category === 'all' || product.category === category;
            return matchesSearch && matchesCategory;
        });
    }

    // Add to cart functionality
    function addToCart(event) {
        const productId = parseInt(event.target.getAttribute('data-id'));
        const product = products.find(p => p.id === productId);
        
        if (product) {
            // In a real application, you would add to cart storage or send to server
            console.log(`Added ${product.name} to cart`);
            event.target.textContent = 'Added!';
            event.target.disabled = true;
            
            setTimeout(() => {
                event.target.textContent = 'Add to Cart';
                event.target.disabled = false;
            }, 2000);
        }
    }
});

// HTML structure would look like this:
/*
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Product Catalog</title>
    <style>
        .product-container {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
            gap: 20px;
            padding: 20px;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            transition: transform 0.2s;
        }
        .product-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
        }
        .product-image img {
            width: 100%;
            height: 200px;
            object-fit: cover;
            border-radius: 5px;
        }
        .product-info h3 {
            margin: 10px 0;
            font-size: 1.1rem;
        }
        .product-meta {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        .price {
            font-weight: bold;
            color: #e63946;
        }
        .rating {
            color: #ffc107;
        }
        .add-to-cart {
            width: 100%;
            padding: 8px;
            background-color: #2a9d8f;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.2s;
        }
        .add-to-cart:hover {
            background-color: #21867a;
        }
        .add-to-cart:disabled {
            background-color: #ccc;
            cursor: not-allowed;
        }
        .controls {
            display: flex;
            gap: 15px;
            padding: 20px;
            background-color: #f8f9fa;
            margin-bottom: 20px;
        }
        select, input {
            padding: 8px;
            border-radius: 4px;
            border: 1px solid #ddd;
        }
        .no-products {
            text-align: center;
            grid-column: 1 / -1;
            padding: 40px;
            color: #666;
        }
    </style>
</head>
<body>
    <div class="controls">
        <select id="sort-select">
            <option value="default">Default</option>
            <option value="price-low">Price: Low to High</option>
            <option value="price-high">Price: High to Low</option>
            <option value="name-asc">Name: A-Z</option>
            <option value="name-desc">Name: Z-A</option>
            <option value="rating">Highest Rating</option>
        </select>
        
        <select id="category-filter">
            <!-- Dynamically populated -->
        </select>
        
        <input type="text" id="search-input" placeholder="Search products...">
    </div>
    
    <div id="product-container" class="product-container">
        <!-- Products will be rendered here -->
    </div>
    
    <script src="catalog.js
