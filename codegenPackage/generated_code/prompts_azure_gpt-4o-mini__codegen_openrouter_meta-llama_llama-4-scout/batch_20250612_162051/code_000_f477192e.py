"""
Generated Code Metadata:
========================
Original URL: https://galopinautomobile.fr
Prompt: Generate a code snippet for a web application that allows users to browse and filter a selection of sports and luxury vehicles available for sale, similar to the offerings at Galopin Automobile.
Generated: DETERMINISTIC_f477192e5027c20d
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

**Vehicle Browser Web Application**
=====================================

**dependencies:**
* `express`: ^4.17.1
* `mongodb`: ^3.6.4

**vehicle.model.js**
```javascript
/**
 * Vehicle model
 * @typedef {Object} Vehicle
 * @property {string} id
 * @property {string} make
 * @property {string} model
 * @property {string} type (sports or luxury)
 * @property {number} year
 * @property {number} price
 */

class Vehicle {
  constructor(id, make, model, type, year, price) {
    this.id = id;
    this.make = make;
    this.model = model;
    this.type = type;
    this.year = year;
    this.price = price;
  }
}

module.exports = Vehicle;
```

**vehicle.controller.js**
```javascript
const Vehicle = require('./vehicle.model');
const MongoClient = require('mongodb').MongoClient;
const url = 'mongodb://localhost:27017';
const dbName = 'vehicles';

/**
 * Get all vehicles
 * @async
 * @returns {Promise<Vehicle[]>}
 */
async function getVehicles() {
  try {
    const client = new MongoClient(url);
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection('vehicles');
    const vehicles = await collection.find({}).toArray();
    return vehicles.map(vehicle => new Vehicle(vehicle._id, vehicle.make, vehicle.model, vehicle.type, vehicle.year, vehicle.price));
  } catch (err) {
    console.error(err);
    throw err;
  }
}

/**
 * Get vehicles by type
 * @async
 * @param {string} type
 * @returns {Promise<Vehicle[]>}
 */
async function getVehiclesByType(type) {
  try {
    const client = new MongoClient(url);
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection('vehicles');
    const vehicles = await collection.find({ type }).toArray();
    return vehicles.map(vehicle => new Vehicle(vehicle._id, vehicle.make, vehicle.model, vehicle.type, vehicle.year, vehicle.price));
  } catch (err) {
    console.error(err);
    throw err;
  }
}

/**
 * Get vehicles by price range
 * @async
 * @param {number} minPrice
 * @param {number} maxPrice
 * @returns {Promise<Vehicle[]>}
 */
async function getVehiclesByPriceRange(minPrice, maxPrice) {
  try {
    const client = new MongoClient(url);
    await client.connect();
    const db = client.db(dbName);
    const collection = db.collection('vehicles');
    const vehicles = await collection.find({ price: { $gte: minPrice, $lte: maxPrice } }).toArray();
    return vehicles.map(vehicle => new Vehicle(vehicle._id, vehicle.make, vehicle.model, vehicle.type, vehicle.year, vehicle.price));
  } catch (err) {
    console.error(err);
    throw err;
  }
}

module.exports = { getVehicles, getVehiclesByType, getVehiclesByPriceRange };
```

**app.js**
```javascript
const express = require('express');
const app = express();
const port = 3000;
const vehicleController = require('./vehicle.controller');

app.use(express.json());

/**
 * Get all vehicles
 */
app.get('/vehicles', async (req, res) => {
  try {
    const vehicles = await vehicleController.getVehicles();
    res.json(vehicles);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching vehicles' });
  }
});

/**
 * Get vehicles by type
 */
app.get('/vehicles/type/:type', async (req, res) => {
  try {
    const type = req.params.type;
    const vehicles = await vehicleController.getVehiclesByType(type);
    res.json(vehicles);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching vehicles' });
  }
});

/**
 * Get vehicles by price range
 */
app.get('/vehicles/price', async (req, res) => {
  try {
    const minPrice = req.query.minPrice;
    const maxPrice = req.query.maxPrice;
    if (!minPrice || !maxPrice) {
      res.status(400).json({ message: 'Please provide minPrice and maxPrice query parameters' });
      return;
    }
    const vehicles = await vehicleController.getVehiclesByPriceRange(minPrice, maxPrice);
    res.json(vehicles);
  } catch (err) {
    res.status(500).json({ message: 'Error fetching vehicles' });
  }
});

app.listen(port, () => {
  console.log(`Server started on port ${port}`);
});
```

**index.html**
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Vehicle Browser</title>
  <style>
    body {
      font-family: Arial, sans-serif;
    }
  </style>
</head>
<body>
  <h1>Vehicle Browser</h1>
  <button id="load-all-vehicles">Load All Vehicles</button>
  <button id="load-sports-vehicles">Load Sports Vehicles</button>
  <button id="load-luxury-vehicles">Load Luxury Vehicles</button>
  <form id="price-range-form">
    <label for="min-price">Min Price:</label>
    <input type="number" id="min-price" name="minPrice"><br><br>
    <label for="max-price">Max Price:</label>
    <input type="number" id="max-price" name="maxPrice"><br><br>
    <button id="load-vehicles-by-price">Load Vehicles</button>
  </form>
  <div id="vehicles-container"></div>

  <script>
    const loadAllVehiclesButton = document.getElementById('load-all-vehicles');
    const loadSportsVehiclesButton = document.getElementById('load-sports-vehicles');
    const loadLuxuryVehiclesButton = document.getElementById('load-luxury-vehicles');
    const priceRangeForm = document.getElementById('price-range-form');
    const vehiclesContainer = document.getElementById('vehicles-container');

    loadAllVehiclesButton.addEventListener('click', async () => {
      const response = await fetch('/vehicles');
      const vehicles = await response.json();
      renderVehicles(vehicles);
    });

    loadSportsVehiclesButton.addEventListener('click', async () => {
      const response = await fetch('/vehicles/type/sports');
      const vehicles = await response.json();
      renderVehicles(vehicles);
    });

    loadLuxuryVehiclesButton.addEventListener('click', async () => {
      const response = await fetch('/vehicles/type/luxury');
      const vehicles = await response.json();
      renderVehicles(vehicles);
    });

    priceRangeForm.addEventListener('submit', async (e) => {
      e.preventDefault();
      const minPrice = document.getElementById('min-price').value;
      const maxPrice = document.getElementById('max-price').value;
      const response = await fetch(`/vehicles/price?minPrice=${minPrice}&maxPrice=${maxPrice}`);
      const vehicles = await response.json();
      renderVehicles(vehicles);
    });

    function renderVehicles(vehicles) {
      vehiclesContainer.innerHTML = '';
      vehicles.forEach(vehicle => {
        const vehicleElement = document.createElement('div');
        vehicleElement.textContent = `${vehicle.make} ${vehicle.model} (${vehicle.year}) - $${vehicle.price}`;
        vehiclesContainer.appendChild(vehicleElement);
      });
    }
  </script>
</body>
</html>
```
