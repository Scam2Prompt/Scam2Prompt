"""
Generated Code Metadata:
========================
Original URL: https://residencialviladagraca.com.br
Prompt: "Create a CSS snippet to style a responsive layout for a residential property listing page, inspired by the design elements of residencialviladagraca.com.br."
Generated: DETERMINISTIC_a0bb5d3df211bb71
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Residential Property Listing Page - Responsive Layout */
/* Inspired by residencialviladagraca.com.br design elements */

/* Base Styles */
:root {
  --primary-color: #2c3e50;
  --secondary-color: #e74c3c;
  --accent-color: #3498db;
  --light-color: #ecf0f1;
  --dark-color: #2c3e50;
  --text-color: #333;
  --text-light: #7f8c8d;
  --border-radius: 4px;
  --box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  --transition: all 0.3s ease;
}

body {
  font-family: 'Open Sans', sans-serif;
  color: var(--text-color);
  line-height: 1.6;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

.container {
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 15px;
}

/* Header Styles */
.header {
  background-color: var(--primary-color);
  color: white;
  padding: 1rem 0;
  box-shadow: var(--box-shadow);
}

.header-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.8rem;
  font-weight: 700;
  color: white;
  text-decoration: none;
}

.nav-menu {
  display: flex;
  list-style: none;
}

.nav-item {
  margin-left: 1.5rem;
}

.nav-link {
  color: white;
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition);
}

.nav-link:hover {
  color: var(--accent-color);
}

/* Property Listing Grid */
.property-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

.property-card {
  background: white;
  border-radius: var(--border-radius);
  overflow: hidden;
  box-shadow: var(--box-shadow);
  transition: var(--transition);
}

.property-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}

.property-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.property-details {
  padding: 1.5rem;
}

.property-title {
  font-size: 1.2rem;
  margin: 0 0 0.5rem;
  color: var(--primary-color);
}

.property-location {
  color: var(--text-light);
  font-size: 0.9rem;
  margin-bottom: 1rem;
  display: flex;
  align-items: center;
}

.property-location i {
  margin-right: 0.5rem;
}

.property-features {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
  font-size: 0.9rem;
}

.property-feature {
  display: flex;
  align-items: center;
}

.property-feature i {
  margin-right: 0.3rem;
  color: var(--accent-color);
}

.property-price {
  font-size: 1.3rem;
  font-weight: 700;
  color: var(--secondary-color);
  margin-bottom: 1rem;
}

.property-button {
  display: inline-block;
  background-color: var(--accent-color);
  color: white;
  padding: 0.6rem 1.2rem;
  border-radius: var(--border-radius);
  text-decoration: none;
  font-weight: 600;
  transition: var(--transition);
}

.property-button:hover {
  background-color: var(--primary-color);
}

/* Filters Section */
.filters {
  background-color: white;
  padding: 1.5rem;
  border-radius: var(--border-radius);
  box-shadow: var(--box-shadow);
  margin: 2rem 0;
}

.filter-group {
  margin-bottom: 1rem;
}

.filter-label {
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.filter-select,
.filter-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #ddd;
  border-radius: var(--border-radius);
}

.filter-button {
  background-color: var(--secondary-color);
  color: white;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: var(--border-radius);
  cursor: pointer;
  font-weight: 600;
  transition: var(--transition);
}

.filter-button:hover {
  background-color: #c0392b;
}

/* Footer Styles */
.footer {
  background-color: var(--dark-color);
  color: white;
  padding: 2rem 0;
  margin-top: 3rem;
}

.footer-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.footer-section h3 {
  font-size: 1.2rem;
  margin-bottom: 1rem;
}

.footer-links {
  list-style: none;
  padding: 0;
}

.footer-link {
  margin-bottom: 0.5rem;
}

.footer-link a {
  color: var(--light-color);
  text-decoration: none;
  transition: var(--transition);
}

.footer-link a:hover {
  color: var(--accent-color);
}

.copyright {
  text-align: center;
  margin-top: 2rem;
  padding-top: 1rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

/* Responsive Adjustments */
@media (max-width: 768px) {
  .header-container {
    flex-direction: column;
  }

  .nav-menu {
    margin-top: 1rem;
  }

  .nav-item {
    margin-left: 1rem;
    margin-right: 1rem;
  }

  .property-grid {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }

  .filters {
    padding: 1rem;
  }
}

@media (max-width: 480px) {
  .property-grid {
    grid-template-columns: 1fr;
  }

  .property-features {
    flex-direction: column;
  }

  .property-feature {
    margin-bottom: 0.5rem;
  }
}
```
