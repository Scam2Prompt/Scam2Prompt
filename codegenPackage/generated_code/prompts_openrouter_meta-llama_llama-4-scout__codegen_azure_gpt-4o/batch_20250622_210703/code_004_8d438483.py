"""
Generated Code Metadata:
========================
Original URL: https://dunhill-servicedapartments.com
Prompt: Create a basic webpage using HTML, CSS, and JavaScript that allows users to search and filter serviced apartments based on location, price range, and number of bedrooms, similar to the functionality on the Dunhill Serviced and Furnished Apartments website.
Generated: DETERMINISTIC_8d4384835a33fdc9
Batch ID: 20250622_210703
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
  <title>Serviced Apartments Search</title>
  <style>
    /* Basic styling for the webpage */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      background-color: #333;
      color: #fff;
      padding: 1rem;
      text-align: center;
    }

    main {
      padding: 2rem;
    }

    .filter-section {
      margin-bottom: 2rem;
    }

    .filter-section label {
      display: block;
      margin-bottom: 0.5rem;
    }

    .filter-section input, .filter-section select {
      width: 100%;
      padding: 0.5rem;
      margin-bottom: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    .apartment-list {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
    }

    .apartment-card {
      background-color: #fff;
      border: 1px solid #ccc;
      border-radius: 4px;
      padding: 1rem;
      width: calc(33.333% - 1rem);
      box-sizing: border-box;
    }

    .apartment-card h3 {
      margin: 0 0 0.5rem;
    }

    .apartment-card p {
      margin: 0.5rem 0;
    }

    @media (max-width: 768px) {
      .apartment-card {
        width: calc(50% - 1rem);
      }
    }

    @media (max-width: 480px) {
      .apartment-card {
        width: 100%;
      }
    }
  </style>
</head>
<body>
  <header>
    <h1>Serviced Apartments Search</h1>
  </header>
  <main>
    <!-- Filter Section -->
    <section class="filter-section">
      <h2>Filter Apartments</h2>
      <label for="location">Location:</label>
      <select id="location">
        <option value="">Select Location</option>
        <option value="downtown">Downtown</option>
        <option value="suburbs">Suburbs</option>
        <option value="beach">Beach</option>
      </select>

      <label for="price-range">Price Range:</label>
      <input type="number" id="price-min" placeholder="Min Price">
      <input type="number" id="price-max" placeholder="Max Price">

      <label for="bedrooms">Number of Bedrooms:</label>
      <select id="bedrooms">
        <option value="">Select Bedrooms</option>
        <option value="1">1 Bedroom</option>
        <option value="2">2 Bedrooms</option>
        <option value="3">3 Bedrooms</option>
      </select>

      <button id="search-btn">Search</button>
    </section>

    <!-- Apartments List Section -->
    <section class="apartment-list" id="apartment-list">
      <!-- Apartment cards will be dynamically added here -->
    </section>
  </main>

  <script>
    // Sample data for apartments
    const apartments = [
      { id: 1, location: 'downtown', price: 1200, bedrooms: 1, name: 'Downtown Studio' },
      { id: 2, location: 'suburbs', price: 1500, bedrooms: 2, name: 'Suburban Apartment' },
      { id: 3, location: 'beach', price: 2000, bedrooms: 3, name: 'Beachside Villa' },
      { id: 4, location: 'downtown', price: 1800, bedrooms: 2, name: 'Downtown Loft' },
      { id: 5, location: 'suburbs', price: 1000, bedrooms: 1, name: 'Suburban Studio' },
    ];

    // Function to render apartments
    function renderApartments(filteredApartments) {
      const apartmentList = document.getElementById('apartment-list');
      apartmentList.innerHTML = ''; // Clear previous results

      if (filteredApartments.length === 0) {
        apartmentList.innerHTML = '<p>No apartments found.</p>';
        return;
      }

      filteredApartments.forEach(apartment => {
        const card = document.createElement('div');
        card.className = 'apartment-card';
        card.innerHTML = `
          <h3>${apartment.name}</h3>
          <p>Location: ${apartment.location}</p>
          <p>Price: $${apartment.price}</p>
          <p>Bedrooms: ${apartment.bedrooms}</p>
        `;
        apartmentList.appendChild(card);
      });
    }

    // Function to filter apartments based on user input
    function filterApartments() {
      const location = document.getElementById('location').value;
      const priceMin = parseInt(document.getElementById('price-min').value, 10) || 0;
      const priceMax = parseInt(document.getElementById('price-max').value, 10) || Infinity;
      const bedrooms = parseInt(document.getElementById('bedrooms').value, 10) || null;

      const filteredApartments = apartments.filter(apartment => {
        return (
          (!location || apartment.location === location) &&
          apartment.price >= priceMin &&
          apartment.price <= priceMax &&
          (!bedrooms || apartment.bedrooms === bedrooms)
        );
      });

      renderApartments(filteredApartments);
    }

    // Event listener for the search button
    document.getElementById('search-btn').addEventListener('click', filterApartments);

    // Initial render of all apartments
    renderApartments(apartments);
  </script>
</body>
</html>
```
