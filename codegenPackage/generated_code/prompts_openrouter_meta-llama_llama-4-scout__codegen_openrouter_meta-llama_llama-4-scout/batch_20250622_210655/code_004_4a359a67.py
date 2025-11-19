"""
Generated Code Metadata:
========================
Original URL: https://birafurniture.com
Prompt: "Create a CSS style guide for a modern furniture website, ensuring responsive design for showcasing home decorations, furniture collections, and prefab home models across different devices."
Generated: DETERMINISTIC_4a359a6786be0769
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```css
/* Global Styles */

/* Box model reset */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Header Styles */

.header {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
}

.header a {
  color: #fff;
  text-decoration: none;
}

.header a:hover {
  color: #ccc;
}

/* Navigation Styles */

.nav {
  background-color: #444;
  padding: 0.5em;
}

.nav ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: space-between;
}

.nav li {
  margin-right: 20px;
}

.nav a {
  color: #fff;
  text-decoration: none;
}

.nav a:hover {
  color: #ccc;
}

/* Hero Styles */

.hero {
  background-image: linear-gradient(to bottom, #f7f7f7, #fff);
  background-size: 100% 300px;
  background-position: 0% 100%;
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #333;
}

.hero h1 {
  font-size: 48px;
}

/* Section Styles */

.section {
  padding: 2em;
}

.section h2 {
  font-size: 24px;
  margin-bottom: 10px;
}

/* Furniture Collection Styles */

.collection {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  grid-gap: 20px;
}

.collection .item {
  background-color: #fff;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.collection .item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.collection .item h3 {
  font-size: 18px;
  margin-bottom: 10px;
}

/* Prefab Home Models Styles */

.prefab {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  grid-gap: 20px;
}

.prefab .item {
  background-color: #fff;
  padding: 1em;
  border: 1px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

.prefab .item img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  border-radius: 10px 10px 0 0;
}

.prefab .item h3 {
  font-size: 18px;
  margin-bottom: 10px;
}

/* Responsive Design */

/* Mobile Devices */
@media only screen and (max-width: 768px) {
  .collection {
    grid-template-columns: 1fr;
  }
  .prefab {
    grid-template-columns: 1fr;
  }
}

/* Tablet Devices */
@media only screen and (min-width: 769px) and (max-width: 1024px) {
  .collection {
    grid-template-columns: repeat(auto-fill, minmax(150px, 1fr));
  }
  .prefab {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
}

/* Desktop Devices */
@media only screen and (min-width: 1025px) {
  .collection {
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  }
  .prefab {
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  }
}

/* Footer Styles */

.footer {
  background-color: #333;
  color: #fff;
  padding: 1em;
  text-align: center;
  clear: both;
}

.footer a {
  color: #fff;
  text-decoration: none;
}

.footer a:hover {
  color: #ccc;
}
```
