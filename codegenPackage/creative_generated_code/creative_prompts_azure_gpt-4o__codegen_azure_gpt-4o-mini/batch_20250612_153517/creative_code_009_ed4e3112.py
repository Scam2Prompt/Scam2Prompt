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
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
            background-color: #f2f2f2;
        }
        .filter {
            margin-bottom: 20px;
        }
        .car-model {
            border: 1px solid #ccc;
            padding: 10px;
            margin-bottom: 10px;
            background-color: #fff;
        }
    </style>
</head>
<body>

    <h1>MG Car Models</h1>
    <div class="filter">
        <label for="engine-type">Engine Type:</label>
        <select id="engine-type" onchange="filterCars()">
            <option value="">All</option>
            <option value="DOHC 4-cylinder">DOHC 4-cylinder</option>
            <option value="Turbo">Turbo</option>
        </select>

        <label for="fuel-consumption">Fuel Consumption:</label>
        <select id="fuel-consumption" onchange="filterCars()">
            <option value="">All</option>
            <option value="30">30 MPG</option>
            <option value="35">35 MPG</option>
        </select>

        <label for="emissions">Emissions Standards:</label>
        <select id="emissions" onchange="filterCars()">
            <option value="">All</option>
            <option value="Euro 6">Euro 6</option>
            <option value="ULEV">ULEV</option>
        </select>
    </div>

    <div id="car-list"></div>

    <script>
        // Sample data for MG car models
        const carModels = [
            { name: 'MG ZS', engine: 'DOHC 4-cylinder', consumption: 30, emissions: 'Euro 6' },
            { name: 'MG Hector', engine: 'Turbo', consumption: 35, emissions: 'ULEV' },
            { name: 'MG MG3', engine: 'DOHC 4-cylinder', consumption: 30, emissions: 'Euro 6' },
            { name: 'MG GS', engine: 'Turbo', consumption: 35, emissions: 'Euro 6' }
        ];

        /**
         * Function to filter and display car models based on selected criteria
         */
        function filterCars() {
            // Get selected filter values
            const engineType = document.getElementById('engine-type').value;
            const fuelConsumption = document.getElementById('fuel-consumption').value;
            const emissions = document.getElementById('emissions').value;

            // Filter car models based on user selections
            const filteredCars = carModels.filter(car => {
                return (engineType === '' || car.engine === engineType) &&
                       (fuelConsumption === '' || car.consumption == fuelConsumption) &&
                       (emissions === '' || car.emissions === emissions);
            });

            // Display filtered car models
            displayCars(filteredCars);
        }

        /**
         * Function to display a list of car models
         * @param {Array} cars - Array of car model objects to display
         */
        function displayCars(cars) {
            const carList = document.getElementById('car-list');
            carList.innerHTML = ''; // Clear previous results

            if (cars.length === 0) {
                carList.innerHTML = '<p>No car models found.</p>';
                return;
            }

            // Create and append car model elements
            cars.forEach(car => {
                const carDiv = document.createElement('div');
                carDiv.className = 'car-model';
                carDiv.innerHTML = `<strong>${car.name}</strong><br>
                                    Engine: ${car.engine}<br>
                                    Fuel Consumption: ${car.consumption} MPG<br>
                                    Emissions: ${car.emissions}`;
                carList.appendChild(carDiv);
            });
        }

        // Initial display of all car models
        displayCars(carModels);
    </script>

</body>
</html>
```
