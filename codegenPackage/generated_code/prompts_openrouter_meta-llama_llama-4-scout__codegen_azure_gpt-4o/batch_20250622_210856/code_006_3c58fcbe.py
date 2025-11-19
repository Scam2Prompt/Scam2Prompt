"""
Generated Code Metadata:
========================
Original URL: https://intudesa.com
Prompt: "Create a simple webpage using HTML and CSS that allows users to search for properties by location and price range, inspired by Intudesa's search functionality."
Generated: DETERMINISTIC_3c58fcbe3460615e
Batch ID: 20250622_210856
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
  <title>Property Search</title>
  <style>
    /* General styles for the webpage */
    body {
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
      background-color: #f4f4f4;
    }

    header {
      background-color: #0078d7;
      color: white;
      padding: 1rem;
      text-align: center;
    }

    main {
      max-width: 800px;
      margin: 2rem auto;
      background: white;
      padding: 2rem;
      border-radius: 8px;
      box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }

    h1 {
      text-align: center;
      color: #333;
    }

    form {
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    label {
      font-weight: bold;
      margin-bottom: 0.5rem;
    }

    input, select, button {
      padding: 0.5rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      font-size: 1rem;
    }

    button {
      background-color: #0078d7;
      color: white;
      border: none;
      cursor: pointer;
    }

    button:hover {
      background-color: #005fa3;
    }

    .results {
      margin-top: 2rem;
    }

    .property {
      padding: 1rem;
      border: 1px solid #ccc;
      border-radius: 4px;
      margin-bottom: 1rem;
      background-color: #f9f9f9;
    }
  </style>
</head>
<body>
  <!-- Header section -->
  <header>
    <h1>Property Search</h1>
  </header>

  <!-- Main content -->
  <main>
    <h1>Find Your Dream Property</h1>
    <form id="searchForm">
      <!-- Location input -->
      <div>
        <label for="location">Location:</label>
        <input type="text" id="location" name="location" placeholder="Enter location" required>
      </div>

      <!-- Price range inputs -->
      <div>
        <label for="minPrice">Minimum Price:</label>
        <input type="number" id="minPrice" name="minPrice" placeholder="Enter minimum price" required>
      </div>
      <div>
        <label for="maxPrice">Maximum Price:</label>
        <input type="number" id="maxPrice" name="maxPrice" placeholder="Enter maximum price" required>
      </div>

      <!-- Submit button -->
      <button type="submit">Search</button>
    </form>

    <!-- Results section -->
    <div class="results" id="results">
      <!-- Results will be dynamically inserted here -->
    </div>
  </main>

  <script>
    // Handle form submission
    document.getElementById('searchForm').addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent page reload

      // Get form values
      const location = document.getElementById('location').value.trim();
      const minPrice = parseFloat(document.getElementById('minPrice').value);
      const maxPrice = parseFloat(document.getElementById('maxPrice').value);

      // Validate inputs
      if (!location || isNaN(minPrice) || isNaN(maxPrice) || minPrice > maxPrice) {
        alert('Please enter valid search criteria.');
        return;
      }

      // Simulate search results (replace with actual API call in production)
      const properties = [
        { id: 1, location: 'New York', price: 500000 },
        { id: 2, location: 'Los Angeles', price: 750000 },
        { id: 3, location: 'Chicago', price: 300000 },
        { id: 4, location: 'Houston', price: 450000 },
      ];

      // Filter properties based on search criteria
      const filteredProperties = properties.filter(property =>
        property.location.toLowerCase().includes(location.toLowerCase()) &&
        property.price >= minPrice &&
        property.price <= maxPrice
      );

      // Display results
      const resultsContainer = document.getElementById('results');
      resultsContainer.innerHTML = ''; // Clear previous results

      if (filteredProperties.length === 0) {
        resultsContainer.innerHTML = '<p>No properties found matching your criteria.</p>';
      } else {
        filteredProperties.forEach(property => {
          const propertyDiv = document.createElement('div');
          propertyDiv.className = 'property';
          propertyDiv.innerHTML = `
            <p><strong>Location:</strong> ${property.location}</p>
            <p><strong>Price:</strong> $${property.price.toLocaleString()}</p>
          `;
          resultsContainer.appendChild(propertyDiv);
        });
      }
    });
  </script>
</body>
</html>
```
