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
/* Casa Amalfitana Menu Styling */
/* Styles for the menu page layout and typography */

/* Base Styles */
body {
    font-family: 'Playfair Display', serif;
    background-color: #f9f5f0;
    color: #333;
    line-height: 1.6;
    margin: 0;
    padding: 0;
}

/* Container for menu content */
.menu-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 2rem;
}

/* Menu Header */
.menu-header {
    text-align: center;
    margin-bottom: 3rem;
    border-bottom: 2px solid #d4a76a;
    padding-bottom: 1rem;
}

.menu-header h1 {
    font-size: 2.5rem;
    color: #8b4513;
    margin-bottom: 0.5rem;
}

.menu-header p {
    font-style: italic;
    color: #666;
}

/* Menu Sections */
.menu-section {
    margin-bottom: 3rem;
}

.section-title {
    font-size: 1.8rem;
    color: #8b4513;
    border-bottom: 1px dashed #d4a76a;
    padding-bottom: 0.5rem;
    margin-bottom: 1.5rem;
}

/* Menu Items */
.menu-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1.5rem;
    padding: 0.5rem;
    transition: background-color 0.3s ease;
}

.menu-item:hover {
    background-color: rgba(212, 167, 106, 0.1);
}

.item-name {
    font-weight: 700;
    font-size: 1.2rem;
    color: #5a3921;
}

.item-price {
    font-weight: 700;
    color: #8b4513;
}

.item-description {
    font-size: 0.9rem;
    color: #666;
    margin-top: 0.3rem;
    font-style: italic;
    width: 80%;
}

/* Special Tags */
.item-tag {
    display: inline-block;
    font-size: 0.7rem;
    padding: 0.2rem 0.5rem;
    margin-left: 0.5rem;
    border-radius: 3px;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}

.tag-italian {
    background-color: #f0e6d2;
    color: #8b4513;
    border: 1px solid #d4a76a;
}

.tag-sinaloense {
    background-color: #e8f0d2;
    color: #5a6e21;
    border: 1px solid #a7d46a;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .menu-item {
        flex-direction: column;
    }
    
    .item-description {
        width: 100%;
    }
    
    .item-price {
        margin-top: 0.5rem;
    }
}
```
