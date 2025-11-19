"""
Generated Code Metadata:
========================
Original URL: https://www.autocuyo.com.ar
Prompt: Generate HTML and CSS code for a simple car listing page inspired by the design of Autocuyo, including a responsive layout and basic styling.
Generated: DETERMINISTIC_104f20b38683670c
Batch ID: 20250622_210655
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
  <meta name="description" content="Car listing page inspired by Autocuyo">
  <title>Car Listing Page</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <!-- Header Section -->
  <header class="header">
    <div class="container">
      <h1 class="logo">Car Listings</h1>
      <nav class="nav">
        <ul class="nav-list">
          <li><a href="#home">Home</a></li>
          <li><a href="#listings">Listings</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </nav>
    </div>
  </header>

  <!-- Main Content Section -->
  <main class="main">
    <section id="listings" class="listings">
      <div class="container">
        <h2>Available Cars</h2>
        <div class="car-grid">
          <!-- Example Car Card -->
          <div class="car-card">
            <img src="car1.jpg" alt="Car Image" class="car-image">
            <div class="car-details">
              <h3 class="car-title">Toyota Corolla</h3>
              <p class="car-description">Year: 2020 | Mileage: 15,000 km | Price: $20,000</p>
              <button class="btn">View Details</button>
            </div>
          </div>
          <!-- Add more car cards as needed -->
        </div>
      </div>
    </section>
  </main>

  <!-- Footer Section -->
  <footer class="footer">
    <div class="container">
      <p>&copy; 2023 Car Listings. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```

```css
/* styles.css */

/* General Reset */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

/* Body Styling */
body {
  font-family: Arial, sans-serif;
  line-height: 1.6;
  color: #333;
  background-color: #f9f9f9;
}

/* Container */
.container {
  width: 90%;
  max-width: 1200px;
  margin: 0 auto;
}

/* Header */
.header {
  background-color: #0044cc;
  color: #fff;
  padding: 1rem 0;
}

.header .logo {
  font-size: 1.5rem;
  font-weight: bold;
}

.nav {
  margin-top: 0.5rem;
}

.nav-list {
  list-style: none;
  display: flex;
  gap: 1rem;
}

.nav-list a {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
}

.nav-list a:hover {
  text-decoration: underline;
}

/* Main Content */
.main {
  padding: 2rem 0;
}

.listings h2 {
  text-align: center;
  margin-bottom: 2rem;
}

.car-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.car-card {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

.car-image {
  width: 100%;
  height: auto;
}

.car-details {
  padding: 1rem;
}

.car-title {
  font-size: 1.25rem;
  margin-bottom: 0.5rem;
}

.car-description {
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.btn {
  display: inline-block;
  background-color: #0044cc;
  color: #fff;
  padding: 0.5rem 1rem;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-align: center;
}

.btn:hover {
  background-color: #003399;
}

/* Footer */
.footer {
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 1rem 0;
  margin-top: 2rem;
}

/* Responsive Design */
@media (max-width: 768px) {
  .nav-list {
    flex-direction: column;
    align-items: center;
  }

  .car-grid {
    grid-template-columns: 1fr;
  }
}
```
