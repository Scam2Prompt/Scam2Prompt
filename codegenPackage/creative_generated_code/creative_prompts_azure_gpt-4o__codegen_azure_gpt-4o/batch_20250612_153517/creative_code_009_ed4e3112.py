"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mgcaugiay.com
Prompt: Develop a web page that dynamically displays MG car models and allows users to filter by features like engine type (e.g., DOHC 4-cylinder, Turbo), fuel consumption, and emissions standards.
Generated: DETERMINISTIC_ed4e3112997705d0
Batch ID: 20250612_153517
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
  <title>MG Car Models</title>
  <script>
    // JavaScript to dynamically filter and display MG car models

    // Mock data: Array of MG car models
    const carModels = [
      {
        name: "MG ZS",
        engineType: "DOHC 4-cylinder",
        fuelConsumption: "6.7L/100km",
        emissions: "Euro 6",
      },
      {
        name: "MG Hector",
        engineType: "Turbo",
        fuelConsumption: "7.5L/100km",
        emissions: "Euro 6",
      },
      {
        name: "MG Gloster",
        engineType: "DOHC 4-cylinder",
        fuelConsumption: "8.1L/100km",
        emissions: "Euro 6",
      },
      {
        name: "MG Astor",
        engineType: "Turbo",
        fuelConsumption: "6.2L/100km",
        emissions: "Euro 6",
      },
    ];

    // Function to display car models based on filter criteria
    function displayCarModels(filter = {}) {
      const carList = document.getElementById("car-list");
      carList.innerHTML = ""; // Clear the list before displaying filtered models

      // Filter cars based on criteria
      const filteredCars = carModels.filter((car) => {
        return (
          (!filter.engineType || car.engineType === filter.engineType) &&
          (!filter.fuelConsumption || car.fuelConsumption === filter.fuelConsumption) &&
          (!filter.emissions || car.emissions === filter.emissions)
        );
      });

      // Render filtered car models
      if (filteredCars.length === 0) {
        carList.innerHTML = "<li>No cars match the selected filters.</li>";
      } else {
        filteredCars.forEach((car) => {
          const listItem = document.createElement("li");
          listItem.textContent = `${car.name} - Engine: ${car.engineType}, Fuel Consumption: ${car.fuelConsumption}, Emissions: ${car.emissions}`;
          carList.appendChild(listItem);
        });
      }
    }

    // Event handler for filter form submission
    function handleFilterSubmit(event) {
      event.preventDefault(); // Prevent page reload

      const engineType = document.getElementById("engine-type").value;
      const fuelConsumption = document.getElementById("fuel-consumption").value;
      const emissions = document.getElementById("emissions").value;

      // Prepare filter object
      const filters = {
        engineType: engineType || null,
        fuelConsumption: fuelConsumption || null,
        emissions: emissions || null,
      };

      // Display filtered car models
      displayCarModels(filters);
    }

    // Initialize the page with all car models
    document.addEventListener("DOMContentLoaded", () => {
      displayCarModels();
      document.getElementById("filter-form").addEventListener("submit", handleFilterSubmit);
    });
  </script>
  <style>
    body {
      font-family: Arial, sans-serif;
      padding: 20px;
    }

    h1 {
      color: #333;
    }

    form {
      margin-bottom: 20px;
    }

    ul {
      list-style-type: none;
      padding: 0;
    }

    li {
      background: #f9f9f9;
      margin: 5px 0;
      padding: 10px;
      border: 1px solid #ddd;
    }
  </style>
</head>
<body>
  <h1>MG Car Models</h1>
  <form id="filter-form">
    <label for="engine-type">Engine Type:</label>
    <select id="engine-type" name="engine-type">
      <option value="">All</option>
      <option value="DOHC 4-cylinder">DOHC 4-cylinder</option>
      <option value="Turbo">Turbo</option>
    </select>

    <label for="fuel-consumption">Fuel Consumption:</label>
    <select id="fuel-consumption" name="fuel-consumption">
      <option value="">All</option>
      <option value="6.7L/100km">6.7L/100km</option>
      <option value="7.5L/100km">7.5L/100km</option>
      <option value="8.1L/100km">8.1L/100km</option>
      <option value="6.2L/100km">6.2L/100km</option>
    </select>

    <label for="emissions">Emissions:</label>
    <select id="emissions" name="emissions">
      <option value="">All</option>
      <option value="Euro 6">Euro 6</option>
    </select>

    <button type="submit">Filter</button>
  </form>

  <ul id="car-list"></ul>
</body>
</html>
```
