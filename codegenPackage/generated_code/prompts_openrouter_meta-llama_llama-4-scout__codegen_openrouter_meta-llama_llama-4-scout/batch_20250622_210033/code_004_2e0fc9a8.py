"""
Generated Code Metadata:
========================
Original URL: https://casaamalfitana.com
Prompt: Create a CSS style sheet snippet to replicate the layout and visual styling of Casa Amalfitana's menu page, including their unique blend of Italian and Sinaloense cuisine descriptions.
Generated: DETERMINISTIC_2e0fc9a87e57272c
Batch ID: 20250622_210033
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
    Casa Amalfitana Menu Page Styles
    =================================
*/

/* Global Styles */
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: 'Open Sans', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f9f9f9;
}

/* Menu Container Styles */
.menu-container {
    max-width: 1200px;
    margin: 40px auto;
    padding: 20px;
    background-color: #fff;
    border: 1px solid #ddd;
    border-radius: 10px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* Menu Header Styles */
.menu-header {
    text-align: center;
    margin-bottom: 20px;
}

.menu-header h1 {
    font-size: 36px;
    font-weight: bold;
    color: #007bff;
}

/* Menu Section Styles */
.menu-section {
    margin-bottom: 40px;
}

.menu-section h2 {
    font-size: 24px;
    font-weight: bold;
    color: #6c757d;
    margin-bottom: 10px;
}

/* Menu Item Styles */
.menu-item {
    display: flex;
    margin-bottom: 20px;
    padding-bottom: 20px;
    border-bottom: 1px solid #ddd;
}

.menu-item:last-child {
    border-bottom: none;
}

.menu-item img {
    width: 100px;
    height: 100px;
    object-fit: cover;
    border-radius: 10px;
    margin-right: 20px;
}

.menu-item-details {
    flex-grow: 1;
}

.menu-item-name {
    font-size: 18px;
    font-weight: bold;
    color: #333;
}

.menu-item-description {
    font-size: 16px;
    color: #666;
}

.menu-item-price {
    font-size: 18px;
    font-weight: bold;
    color: #007bff;
}

/* Italian Cuisine Section Styles */
.italian-cuisine {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin-bottom: 40px;
}

.italian-cuisine h3 {
    font-size: 20px;
    font-weight: bold;
    color: #6c757d;
    margin-bottom: 10px;
}

.italian-cuisine-description {
    font-size: 16px;
    color: #666;
}

/* Sinaloense Cuisine Section Styles */
.sinaloense-cuisine {
    background-color: #f7f7f7;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 10px;
    margin-bottom: 40px;
}

.sinaloense-cuisine h3 {
    font-size: 20px;
    font-weight: bold;
    color: #6c757d;
    margin-bottom: 10px;
}

.sinaloense-cuisine-description {
    font-size: 16px;
    color: #666;
}

/* Responsive Design */
@media (max-width: 768px) {
    .menu-container {
        margin: 20px auto;
    }
    
    .menu-item {
        flex-direction: column;
    }
    
    .menu-item img {
        width: 100%;
        height: 150px;
        object-fit: cover;
        border-radius: 10px;
        margin-bottom: 20px;
    }
}

@media (max-width: 480px) {
    .menu-header h1 {
        font-size: 24px;
    }
    
    .menu-section h2 {
        font-size: 18px;
    }
    
    .menu-item-name {
        font-size: 16px;
    }
    
    .menu-item-description {
        font-size: 14px;
    }
    
    .menu-item-price {
        font-size: 16px;
    }
}
```
