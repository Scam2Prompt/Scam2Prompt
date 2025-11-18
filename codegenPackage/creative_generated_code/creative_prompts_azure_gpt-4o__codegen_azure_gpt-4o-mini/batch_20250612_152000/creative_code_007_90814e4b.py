"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autopecasbrazz.blogspot.com
Prompt: Write JavaScript code to implement a filter-by-vehicle feature, allowing users to select vehicle type, brand, model, and year, as demonstrated on "autopecasbrazz."
Generated: DETERMINISTIC_90814e4b17219bc6
Batch ID: 20250612_152000
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Vehicle Filter Class
class VehicleFilter {
    constructor(vehicles) {
        // Initialize the filter with an array of vehicle objects
        this.vehicles = vehicles;
        this.filteredVehicles = vehicles;
    }

    // Method to filter vehicles by type
    filterByType(type) {
        if (type) {
            this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.type === type);
        }
        return this;
    }

    // Method to filter vehicles by brand
    filterByBrand(brand) {
        if (brand) {
            this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.brand === brand);
        }
        return this;
    }

    // Method to filter vehicles by model
    filterByModel(model) {
        if (model) {
            this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.model === model);
        }
        return this;
    }

    // Method to filter vehicles by year
    filterByYear(year) {
        if (year) {
            this.filteredVehicles = this.filteredVehicles.filter(vehicle => vehicle.year === year);
        }
        return this;
    }

    // Method to get the final filtered vehicle list
    getResults() {
        return this.filteredVehicles;
    }
}

// Example usage
(function() {
    // Sample vehicle data
    const vehicles = [
        { type: 'car', brand: 'Toyota', model: 'Corolla', year: 2020 },
        { type: 'car', brand: 'Honda', model: 'Civic', year: 2021 },
        { type: 'truck', brand: 'Ford', model: 'F-150', year: 2019 },
        { type: 'car', brand: 'Tesla', model: 'Model 3', year: 2021 },
        { type: 'truck', brand: 'Chevrolet', model: 'Silverado', year: 2020 }
    ];

    // Filter instance
    const vehicleFilter = new VehicleFilter(vehicles);

    // Example filter operations
    try {
        const filteredVehicles = vehicleFilter
            .filterByType('car') // Filter by type
            .filterByBrand('Tesla') // Filter by brand
            .filterByYear(2021) // Filter by year
            .getResults(); // Retrieve final results

        console.log(filteredVehicles); // Output the filtered vehicle list
    } catch (error) {
        console.error('Error filtering vehicles:', error);
    }
})();
```
