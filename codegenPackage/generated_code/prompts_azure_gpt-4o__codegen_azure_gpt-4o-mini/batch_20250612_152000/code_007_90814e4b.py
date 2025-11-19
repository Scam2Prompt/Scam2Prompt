"""
Generated Code Metadata:
========================
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write JavaScript code to implement a filter-by-vehicle feature, allowing users to select vehicle type, brand, model, and year, as demonstrated on "autopecasbrazz."
Generated: DETERMINISTIC_90814e4b17219bc6
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// VehicleFilter class to handle filtering of vehicles
class VehicleFilter {
    constructor(vehicles) {
        // Initialize with a list of vehicles
        this.vehicles = vehicles;
        this.filteredVehicles = vehicles; // Start with all vehicles
    }

    // Method to filter vehicles based on selected criteria
    filter(criteria) {
        try {
            // Reset filtered vehicles to the original list
            this.filteredVehicles = this.vehicles;

            // Apply filters based on provided criteria
            if (criteria.type) {
                this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.type === criteria.type);
            }
            if (criteria.brand) {
                this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.brand === criteria.brand);
            }
            if (criteria.model) {
                this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.model === criteria.model);
            }
            if (criteria.year) {
                this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.year === criteria.year);
            }

            return this.filteredVehicles; // Return the filtered list
        } catch (error) {
            console.error("Error filtering vehicles:", error);
            return []; // Return an empty array in case of error
        }
    }
}

// Sample vehicle data
const vehicles = [
    { type: 'car', brand: 'Toyota', model: 'Camry', year: 2020 },
    { type: 'car', brand: 'Honda', model: 'Civic', year: 2019 },
    { type: 'truck', brand: 'Ford', model: 'F-150', year: 2021 },
    { type: 'car', brand: 'Toyota', model: 'Corolla', year: 2020 },
    { type: 'motorcycle', brand: 'Harley-Davidson', model: 'Street 750', year: 2018 },
];

// Instantiate the VehicleFilter with the sample data
const vehicleFilter = new VehicleFilter(vehicles);

// Example usage of the filter method
const criteria = {
    type: 'car',
    brand: 'Toyota',
    model: 'Camry',
    year: 2020
};

// Get filtered vehicles based on criteria
const filteredVehicles = vehicleFilter.filter(criteria);

// Log the filtered vehicles to the console
console.log("Filtered Vehicles:", filteredVehicles);
```
