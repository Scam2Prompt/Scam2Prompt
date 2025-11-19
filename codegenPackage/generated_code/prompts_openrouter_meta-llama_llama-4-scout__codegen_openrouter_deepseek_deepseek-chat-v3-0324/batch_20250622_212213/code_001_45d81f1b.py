"""
Generated Code Metadata:
========================
Original URL: https://springbokinfo.co.za
Prompt: Recommend a suitable web design for a business listing on Springbok Info, incorporating the directory's categories and search functionality.
Generated: DETERMINISTIC_45d81f1b2700f933
Batch ID: 20250622_212213
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
    <title>Business Listing - Springbok Info</title>
    <style>
        /* Reset and base styles */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f5f5f5;
            color: #333;
            line-height: 1.6;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 20px;
        }
        
        /* Header styles */
        header {
            background-color: #2c3e50;
            color: white;
            padding: 20px 0;
            margin-bottom: 30px;
        }
        
        .logo {
            font-size: 24px;
            font-weight: bold;
        }
        
        /* Search bar */
        .search-container {
            margin: 20px 0;
            display: flex;
            justify-content: center;
        }
        
        .search-bar {
            width: 70%;
            padding: 12px;
            border: none;
            border-radius: 4px 0 0 4px;
            font-size: 16px;
        }
        
        .search-btn {
            padding: 12px 20px;
            background-color: #3498db;
            color: white;
            border: none;
            border-radius: 0 4px 4px 0;
            cursor: pointer;
            font-size: 16px;
        }
        
        .search-btn:hover {
            background-color: #2980b9;
        }
        
        /* Categories */
        .categories {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin-bottom: 30px;
        }
        
        .category-btn {
            padding: 8px 16px;
            background-color: #ecf0f1;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            transition: background-color 0.3s;
        }
        
        .category-btn:hover, .category-btn.active {
            background-color: #3498db;
            color: white;
        }
        
        /* Business listing */
        .business-card {
            background-color: white;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            padding: 20px;
            margin-bottom: 20px;
            display: flex;
            flex-direction: column;
        }
        
        .business-header {
            display: flex;
            justify-content: space-between;
            margin-bottom: 15px;
        }
        
        .business-name {
            font-size: 20px;
            font-weight: bold;
            color: #2c3e50;
        }
        
        .business-category {
            background-color: #e8f4fc;
            color: #3498db;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 14px;
        }
        
        .business-details {
            margin-bottom: 15px;
        }
        
        .business-contact {
            display: flex;
            flex-direction: column;
            gap: 5px;
        }
        
        .business-contact span {
            display: flex;
            align-items: center;
            gap: 5px;
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .search-bar {
                width: 60%;
            }
            
            .business-header {
                flex-direction: column;
                gap: 10px;
            }
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">Springbok Info</div>
        </div>
    </header>
    
    <div class="container">
        <!-- Search functionality -->
        <div class="search-container">
            <input type="text" class="search-bar" placeholder="Search for businesses..." id="searchInput">
            <button class="search-btn" onclick="searchBusinesses()">Search</button>
        </div>
        
        <!-- Categories filter -->
        <div class="categories">
            <button class="category-btn active" onclick="filterByCategory('all')">All</button>
            <button class="category-btn" onclick="filterByCategory('restaurants')">Restaurants</button>
            <button class="category-btn" onclick="filterByCategory('retail')">Retail</button>
            <button class="category-btn" onclick="filterByCategory('services')">Services</button>
            <button class="category-btn" onclick="filterByCategory('health')">Health & Wellness</button>
            <button class="category-btn" onclick="filterByCategory('automotive')">Automotive</button>
        </div>
        
        <!-- Business listings -->
        <div id="businessListings">
            <!-- Sample business card - would be dynamically generated in production -->
            <div class="business-card" data-category="restaurants">
                <div class="business-header">
                    <div class="business-name">The Green Plate</div>
                    <div class="business-category">Restaurants</div>
                </div>
                <div class="business-details">
                    Organic vegetarian restaurant specializing in farm-to-table dining experience.
                </div>
                <div class="business-contact">
                    <span>📍 123 Main Street, Springbok</span>
                    <span>📞 (555) 123-4567</span>
                    <span>🌐 www.greenplate.com</span>
                </div>
            </div>
            
            <div class="business-card" data-category="retail">
                <div class="business-header">
                    <div class="business-name">Springbok Outfitters</div>
                    <div class="business-category">Retail</div>
                </div>
                <div class="business-details">
                    Outdoor gear and apparel for hiking, camping, and adventure sports.
                </div>
                <div class="business-contact">
                    <span>📍 456 Oak Avenue, Springbok</span>
                    <span>📞 (555) 234-5678</span>
                    <span>🌐 www.springbokoutfitters.com</span>
                </div>
            </div>
        </div>
    </div>
    
    <script>
        // Search functionality
        function searchBusinesses() {
            const searchTerm = document.getElementById('searchInput').value.toLowerCase();
            const businessCards = document.querySelectorAll('.business-card');
            
            businessCards.forEach(card => {
                const cardText = card.textContent.toLowerCase();
                if (cardText.includes(searchTerm)) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        }
        
        // Category filter functionality
        function filterByCategory(category) {
            const businessCards = document.querySelectorAll('.business-card');
            const categoryButtons = document.querySelectorAll('.category-btn');
            
            // Update active button
            categoryButtons.forEach(btn => {
                btn.classList.remove('active');
                if (btn.textContent.toLowerCase() === category || 
                    (category === 'all' && btn.textContent.toLowerCase() === 'all')) {
                    btn.classList.add('active');
                }
            });
            
            // Filter cards
            businessCards.forEach(card => {
                if (category === 'all' || card.dataset.category === category) {
                    card.style.display = 'flex';
                } else {
                    card.style.display = 'none';
                }
            });
        }
        
        // Allow search on Enter key press
        document.getElementById('searchInput').addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                searchBusinesses();
            }
        });
    </script>
</body>
</html>
```
