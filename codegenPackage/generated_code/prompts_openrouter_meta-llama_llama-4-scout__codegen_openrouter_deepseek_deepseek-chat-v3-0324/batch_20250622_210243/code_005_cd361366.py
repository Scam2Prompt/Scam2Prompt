"""
Generated Code Metadata:
========================
Original URL: https://detaljreklam.se
Prompt: "Write a CSS template for a webpage that features a gallery of printed materials, such as stickers, postcards, and posters, with a layout similar to Detalj Reklam's gallery section."
Generated: DETERMINISTIC_cd361366ac128ee1
Batch ID: 20250622_210243
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Gallery Layout CSS for Printed Materials */
/* Inspired by Detalj Reklam's gallery style */

:root {
    --primary-color: #333;
    --secondary-color: #f5f5f5;
    --accent-color: #ff6b6b;
    --text-color: #222;
    --light-text: #777;
    --spacing-unit: 20px;
    --border-radius: 8px;
    --transition-speed: 0.3s;
}

/* Base Styles */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--secondary-color);
    margin: 0;
    padding: 0;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--spacing-unit);
}

/* Gallery Header */
.gallery-header {
    text-align: center;
    margin-bottom: calc(var(--spacing-unit) * 2);
}

.gallery-header h1 {
    font-size: 2.5rem;
    margin-bottom: var(--spacing-unit);
    color: var(--primary-color);
}

.gallery-header p {
    color: var(--light-text);
    max-width: 600px;
    margin: 0 auto;
}

/* Gallery Grid */
.gallery-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: var(--spacing-unit);
    margin: 0 auto;
}

.gallery-item {
    position: relative;
    overflow: hidden;
    border-radius: var(--border-radius);
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    transition: transform var(--transition-speed) ease;
    background-color: white;
}

.gallery-item:hover {
    transform: translateY(-5px);
}

.gallery-item img {
    width: 100%;
    height: auto;
    display: block;
    transition: opacity var(--transition-speed) ease;
}

.gallery-item:hover img {
    opacity: 0.9;
}

/* Item Overlay */
.item-overlay {
    position: absolute;
    bottom: 0;
    left: 0;
    right: 0;
    background: rgba(0, 0, 0, 0.7);
    color: white;
    padding: var(--spacing-unit);
    transform: translateY(100%);
    transition: transform var(--transition-speed) ease;
}

.gallery-item:hover .item-overlay {
    transform: translateY(0);
}

.item-overlay h3 {
    margin: 0 0 5px 0;
    font-size: 1.2rem;
}

.item-overlay p {
    margin: 0;
    font-size: 0.9rem;
    color: #ddd;
}

/* Category Filters */
.filter-controls {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: calc(var(--spacing-unit) * 1.5);
}

.filter-btn {
    padding: 8px 16px;
    background: white;
    border: 1px solid #ddd;
    border-radius: var(--border-radius);
    cursor: pointer;
    transition: all var(--transition-speed) ease;
}

.filter-btn:hover, .filter-btn.active {
    background: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
    .gallery-grid {
        grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    }
}

@media (max-width: 480px) {
    .gallery-grid {
        grid-template-columns: 1fr;
    }
    
    .gallery-header h1 {
        font-size: 2rem;
    }
}
```
