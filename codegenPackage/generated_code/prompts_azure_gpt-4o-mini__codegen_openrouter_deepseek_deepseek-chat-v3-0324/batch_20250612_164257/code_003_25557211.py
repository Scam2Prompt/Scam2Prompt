"""
Generated Code Metadata:
========================
Original URL: https://poocoinswapse.blogspot.com
Prompt: Develop a CSS style sheet that enhances the presentation of a shoe catalog, focusing on categories like "tenis de esporte" and "chuteira," as highlighted in the content of Poocoinswapse.
Generated: DETERMINISTIC_25557211a31519fd
Batch ID: 20250612_164257
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* 
 * Shoe Catalog Styles for Poocoinswapse
 * Focused on Sport Shoes (tenis de esporte) and Cleats (chuteira)
 */

/* Base Styles */
:root {
  --primary-color: #2c3e50;
  --secondary-color: #e74c3c;
  --accent-color: #f39c12;
  --light-color: #ecf0f1;
  --dark-color: #2c3e50;
  --shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

/* Catalog Container */
.shoe-catalog {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 2rem;
  padding: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

/* Category Header */
.category-header {
  grid-column: 1 / -1;
  text-align: center;
  margin-bottom: 1.5rem;
  padding-bottom: 0.5rem;
  border-bottom: 2px solid var(--accent-color);
}

.category-header h2 {
  color: var(--primary-color);
  font-size: 2rem;
  text-transform: uppercase;
}

/* Shoe Card */
.shoe-card {
  background: white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: var(--shadow);
  transition: var(--transition);
}

.shoe-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.15);
}

.shoe-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.shoe-info {
  padding: 1.5rem;
}

.shoe-title {
  font-size: 1.2rem;
  color: var(--dark-color);
  margin-bottom: 0.5rem;
}

.shoe-category {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: bold;
  margin-bottom: 0.75rem;
}

/* Category Specific Styles */
.shoe-category.tenis-de-esporte {
  background-color: #3498db;
  color: white;
}

.shoe-category.chuteira {
  background-color: #27ae60;
  color: white;
}

.shoe-price {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--secondary-color);
  margin: 0.5rem 0;
}

.shoe-actions {
  display: flex;
  justify-content: space-between;
  margin-top: 1rem;
}

.btn {
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-weight: bold;
  transition: var(--transition);
}

.btn-primary {
  background-color: var(--accent-color);
  color: white;
}

.btn-primary:hover {
  background-color: #e67e22;
}

.btn-secondary {
  background-color: var(--light-color);
  color: var(--dark-color);
}

.btn-secondary:hover {
  background-color: #bdc3c7;
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .shoe-catalog {
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 1.5rem;
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .shoe-catalog {
    grid-template-columns: 1fr;
  }
  
  .category-header h2 {
    font-size: 1.5rem;
  }
}
```
