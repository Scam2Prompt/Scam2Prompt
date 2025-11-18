"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://w-magiceden-world-app-helo.blogspot.com
Prompt: Generate code for a search form that allows users to filter tires by rim size, as demonstrated in the "Busque pneus pelo aro" functionality on the "Dal Cortivo Pneus" website.
Generated: DETERMINISTIC_e6dae81e45dc4fa6
Batch ID: 20250612_151334
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
  <title>Search Tires by Rim Size</title>
  <style>
    /* Basic styling for the search form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      margin-bottom: 20px;
    }

    label {
      margin-right: 10px;
    }

    select, button {
      padding: 5px;
      font-size: 16px;
    }

    .results {
      margin-top: 20px;
    }
  </style>
</head>
<body>
  <h1>Search Tires by Rim Size</h1>

  <!-- Search form -->
  <form id="tireSearchForm">
    <label for="rimSize">Select Rim Size:</label>
    <select id="rimSize" name="rimSize" required>
      <option value="" disabled selected>Select</option>
      <option value="15">15</option>
      <option value="16">16</option>
      <option value="17">17</option>
      <option value="18">18</option>
      <option value="19">19</option>
      <option value="20">20</option>
    </select>
    <button type="submit">Search</button>
  </form>

  <!-- Container for displaying search results -->
  <div class="results" id="searchResults"></div>

  <script>
    // List of tires (mocked data for demonstration purposes)
    const tires = [
      { id: 1, name: "Tire Model A", rimSize: 15 },
      { id: 2, name: "Tire Model B", rimSize: 16 },
      { id: 3, name: "Tire Model C", rimSize: 17 },
      { id: 4, name: "Tire Model D", rimSize: 18 },
      { id: 5, name: "Tire Model E", rimSize: 19 },
      { id: 6, name: "Tire Model F", rimSize: 20 },
    ];

    // Reference to the form and results container
    const form = document.getElementById('tireSearchForm');
    const resultsContainer = document.getElementById('searchResults');

    // Event listener for form submission
    form.addEventListener('submit', function(event) {
      event.preventDefault(); // Prevent page reload

      // Get the selected rim size value
      const selectedRimSize = parseInt(document.getElementById('rimSize').value);

      if (!selectedRimSize) {
        resultsContainer.innerHTML = '<p>Please select a valid rim size.</p>';
        return;
      }

      // Filter tires based on the selected rim size
      const filteredTires = tires.filter(tire => tire.rimSize === selectedRimSize);

      // Display the results
      if (filteredTires.length > 0) {
        resultsContainer.innerHTML = `
          <h2>Search Results:</h2>
          <ul>
            ${filteredTires.map(tire => `<li>${tire.name} (Rim Size: ${tire.rimSize})</li>`).join('')}
          </ul>
        `;
      } else {
        resultsContainer.innerHTML = '<p>No tires found for the selected rim size.</p>';
      }
    });
  </script>
</body>
</html>
```
