"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://patenteimpresa.it
Prompt: Provide code to implement a dynamic dropdown menu for selecting regions (e.g., Abruzzo, Lombardia) during the registration process, as seen on the "Patente d'Impresa" website.
Generated: DETERMINISTIC_85ac447c6b01ca24
Batch ID: 20250612_152249
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
  <title>Dynamic Region Dropdown</title>
  <style>
    /* Simple styling for the form */
    body {
      font-family: Arial, sans-serif;
      margin: 20px;
    }

    form {
      max-width: 400px;
      margin: 0 auto;
    }

    label {
      display: block;
      margin-bottom: 8px;
      font-weight: bold;
    }

    select {
      width: 100%;
      padding: 8px;
      margin-bottom: 16px;
      border: 1px solid #ccc;
      border-radius: 4px;
    }

    button {
      padding: 10px 20px;
      background-color: #007BFF;
      color: white;
      border: none;
      border-radius: 4px;
      cursor: pointer;
    }

    button:disabled {
      background-color: #ccc;
      cursor: not-allowed;
    }
  </style>
</head>
<body>
  <form id="registration-form">
    <label for="region-select">Select a Region:</label>
    <select id="region-select" required>
      <!-- Default option -->
      <option value="" disabled selected>Select a region...</option>
    </select>
    <button type="submit" id="submit-button" disabled>Submit</button>
  </form>

  <script>
    // List of regions; could be fetched from a server in production environments
    const regions = [
      "Abruzzo",
      "Basilicata",
      "Calabria",
      "Campania",
      "Emilia-Romagna",
      "Friuli Venezia Giulia",
      "Lazio",
      "Liguria",
      "Lombardia",
      "Marche",
      "Molise",
      "Piemonte",
      "Puglia",
      "Sardegna",
      "Sicilia",
      "Toscana",
      "Trentino-Alto Adige",
      "Umbria",
      "Valle d'Aosta",
      "Veneto"
    ];

    // Populate the dropdown menu dynamically
    const selectElement = document.getElementById('region-select');
    regions.forEach(region => {
      const option = document.createElement('option');
      option.value = region;
      option.textContent = region;
      selectElement.appendChild(option);
    });

    // Enable the submit button when a region is selected
    const submitButton = document.getElementById('submit-button');
    selectElement.addEventListener('change', () => {
      submitButton.disabled = !selectElement.value; // Disable if no value is selected
    });

    // Handle form submission
    const form = document.getElementById('registration-form');
    form.addEventListener('submit', event => {
      event.preventDefault(); // Prevent default form submission

      // Get the selected region
      const selectedRegion = selectElement.value;

      // Perform further actions with the selected region
      // Example: Send data to the server using AJAX
      console.log(`Selected Region: ${selectedRegion}`);

      // Display a confirmation message
      alert(`You have successfully selected the region: ${selectedRegion}`);
    });
  </script>
</body>
</html>
```
