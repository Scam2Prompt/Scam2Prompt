"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://platform-juno-digital-pj-helfen.blogspot.com
Prompt: Generate HTML and CSS code for a responsive car listing page that mimics the layout and style of Helfen Motors' vehicle inventory.
Generated: DETERMINISTIC_7b4149c0cf2bd6fc
Batch ID: 20250612_151408
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
  <title>Car Listing Page - Helfen Motors</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1>Helfen Motors</h1>
      <nav>
        <ul class="nav-menu">
          <li><a href="#home">Home</a></li>
          <li><a href="#inventory">Inventory</a></li>
          <li><a href="#contact">Contact Us</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content Section -->
  <main>
    <section id="inventory" class="inventory-section">
      <div class="container">
        <h2>Available Cars</h2>
        <div class="car-listing">
          <!-- Card for each car -->
          <div class="car-card">
            <img src="car1.jpg" alt="Car 1" class="car-image">
            <div class="car-details">
              <h3>2023 Toyota Corolla</h3>
              <p>Price: $20,000</p>
              <p>Mileage: 10,000 miles</p>
              <button class="btn">View Details</button>
            </div>
          </div>
          <div class="car-card">
            <img src="car2.jpg" alt="Car 2" class="car-image">
            <div class="car-details">
              <h3>2022 Honda Civic</h3>
              <p>Price: $18,000</p>
              <p>Mileage: 15,000 miles</p>
              <button class="btn">View Details</button>
            </div>
          </div>
          <div class="car-card">
            <img src="car3.jpg" alt="Car 3" class="car-image">
            <div class="car-details">
              <h3>2023 Ford Mustang</h3>
              <p>Price: $30,000</p>
              <p>Mileage: 5,000 miles</p>
              <button class="btn">View Details</button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Helfen Motors. All Rights Reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General styles */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  background-color: #f9f9f9;
}

.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header styles */
.header {
  background-color: #333;
  color: white;
  padding: 1rem 0;
}

.header h1 {
  margin: 0;
  text-align: center;
}

.nav-menu {
  list-style: none;
  padding: 0;
  display: flex;
  justify-content: center;
  gap: 1rem;
}

.nav-menu li a {
  color: white;
  text-decoration: none;
  font-weight: bold;
}

/* Inventory Section */
.inventory-section {
  padding: 2rem 0;
}

.inventory-section h2 {
  text-align: center;
  margin-bottom: 1rem;
}

.car-listing {
  display: flex;
  flex-wrap: wrap;
  gap: 1.5rem;
  justify-content: center;
}

.car-card {
  background-color: white;
  border: 1px solid #ddd;
  border-radius: 5px;
  overflow: hidden;
  width: 300px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.car-image {
  width: 100%;
  height: auto;
}

.car-details {
  padding: 1rem;
  text-align: center;
}

.car-details h3 {
  margin: 0.5rem 0;
  font-size: 1.25rem;
}

.car-details p {
  margin: 0.5rem 0;
  color: #555;
}

.btn {
  display: inline-block;
  background-color: #007bff;
  color: white;
  padding: 0.5rem 1rem;
  margin-top: 1rem;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
}

.btn:hover {
  background-color: #0056b3;
}

/* Footer styles */
.footer {
  background-color: #333;
  color: white;
  text-align: center;
  padding: 1rem 0;
  margin-top: 2rem;
}

/* Responsive styles */
@media (max-width: 768px) {
  .car-listing {
    flex-direction: column;
    align-items: center;
  }
}
```
