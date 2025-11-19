"""
Generated Code Metadata:
========================
Original URL: https://fabricarecosmeticos.ind.br
Prompt: Develop a JavaScript function that manages the logistics of storing and transporting cosmetic products, based on the logistics solutions provided by Fabricare.
Generated: DETERMINISTIC_6fd94c7362952433
Batch ID: 20250612_162325
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Fabricare Logistics Manager
 * 
 * This module provides functions to manage the logistics of storing and transporting cosmetic products.
 * 
 * @module fabricare-logistics
 */

// Define a class to represent a cosmetic product
class CosmeticProduct {
    /**
     * Creates a new CosmeticProduct instance.
     * 
     * @param {string} id - Unique product identifier.
     * @param {string} name - Product name.
     * @param {number} weight - Product weight in kilograms.
     * @param {number} quantity - Product quantity.
     */
    constructor(id, name, weight, quantity) {
        this.id = id;
        this.name = name;
        this.weight = weight;
        this.quantity = quantity;
    }
}

// Define a class to represent a storage location
class StorageLocation {
    /**
     * Creates a new StorageLocation instance.
     * 
     * @param {string} id - Unique storage location identifier.
     * @param {number} capacity - Storage location capacity in kilograms.
     */
    constructor(id, capacity) {
        this.id = id;
        this.capacity = capacity;
        this.availableCapacity = capacity;
        this.products = [];
    }

    /**
     * Adds a product to the storage location.
     * 
     * @param {CosmeticProduct} product - Product to add.
     * @throws {Error} If the product exceeds the available capacity.
     */
    addProduct(product) {
        if (this.availableCapacity >= product.weight * product.quantity) {
            this.products.push(product);
            this.availableCapacity -= product.weight * product.quantity;
        } else {
            throw new Error(`Insufficient capacity to store ${product.quantity} units of ${product.name}`);
        }
    }

    /**
     * Removes a product from the storage location.
     * 
     * @param {string} productId - ID of the product to remove.
     * @throws {Error} If the product is not found.
     */
    removeProduct(productId) {
        const productIndex = this.products.findIndex(product => product.id === productId);
        if (productIndex !== -1) {
            const removedProduct = this.products.splice(productIndex, 1)[0];
            this.availableCapacity += removedProduct.weight * removedProduct.quantity;
        } else {
            throw new Error(`Product ${productId} not found in storage location ${this.id}`);
        }
    }
}

// Define a class to represent a transportation vehicle
class TransportationVehicle {
    /**
     * Creates a new TransportationVehicle instance.
     * 
     * @param {string} id - Unique vehicle identifier.
     * @param {number} capacity - Vehicle capacity in kilograms.
     */
    constructor(id, capacity) {
        this.id = id;
        this.capacity = capacity;
        this.availableCapacity = capacity;
        this.products = [];
    }

    /**
     * Loads a product onto the vehicle.
     * 
     * @param {CosmeticProduct} product - Product to load.
     * @throws {Error} If the product exceeds the available capacity.
     */
    loadProduct(product) {
        if (this.availableCapacity >= product.weight * product.quantity) {
            this.products.push(product);
            this.availableCapacity -= product.weight * product.quantity;
        } else {
            throw new Error(`Insufficient capacity to transport ${product.quantity} units of ${product.name}`);
        }
    }

    /**
     * Unloads a product from the vehicle.
     * 
     * @param {string} productId - ID of the product to unload.
     * @throws {Error} If the product is not found.
     */
    unloadProduct(productId) {
        const productIndex = this.products.findIndex(product => product.id === productId);
        if (productIndex !== -1) {
            const removedProduct = this.products.splice(productIndex, 1)[0];
            this.availableCapacity += removedProduct.weight * removedProduct.quantity;
        } else {
            throw new Error(`Product ${productId} not found in vehicle ${this.id}`);
        }
    }
}

// Define the FabricareLogisticsManager class
class FabricareLogisticsManager {
    /**
     * Creates a new FabricareLogisticsManager instance.
     */
    constructor() {
        this.storageLocations = {};
        this.transportationVehicles = {};
    }

    /**
     * Adds a storage location.
     * 
     * @param {StorageLocation} storageLocation - Storage location to add.
     */
    addStorageLocation(storageLocation) {
        this.storageLocations[storageLocation.id] = storageLocation;
    }

    /**
     * Adds a transportation vehicle.
     * 
     * @param {TransportationVehicle} transportationVehicle - Transportation vehicle to add.
     */
    addTransportationVehicle(transportationVehicle) {
        this.transportationVehicles[transportationVehicle.id] = transportationVehicle;
    }

    /**
     * Stores a product in a storage location.
     * 
     * @param {string} storageLocationId - ID of the storage location.
     * @param {CosmeticProduct} product - Product to store.
     * @throws {Error} If the storage location is not found.
     */
    storeProduct(storageLocationId, product) {
        if (this.storageLocations[storageLocationId]) {
            this.storageLocations[storageLocationId].addProduct(product);
        } else {
            throw new Error(`Storage location ${storageLocationId} not found`);
        }
    }

    /**
     * Transports a product using a transportation vehicle.
     * 
     * @param {string} transportationVehicleId - ID of the transportation vehicle.
     * @param {CosmeticProduct} product - Product to transport.
     * @throws {Error} If the transportation vehicle is not found.
     */
    transportProduct(transportationVehicleId, product) {
        if (this.transportationVehicles[transportationVehicleId]) {
            this.transportationVehicles[transportationVehicleId].loadProduct(product);
        } else {
            throw new Error(`Transportation vehicle ${transportationVehicleId} not found`);
        }
    }
}

// Example usage:
function main() {
    const logisticsManager = new FabricareLogisticsManager();

    const storageLocation1 = new StorageLocation('SL1', 1000);
    logisticsManager.addStorageLocation(storageLocation1);

    const transportationVehicle1 = new TransportationVehicle('TV1', 500);
    logisticsManager.addTransportationVehicle(transportationVehicle1);

    const product1 = new CosmeticProduct('P1', 'Product 1', 10, 50);
    logisticsManager.storeProduct('SL1', product1);

    const product2 = new CosmeticProduct('P2', 'Product 2', 20, 20);
    logisticsManager.transportProduct('TV1', product2);

    console.log('Storage Location 1:');
    console.log(`Available Capacity: ${storageLocation1.availableCapacity} kg`);
    console.log(`Products: ${storageLocation1.products.length}`);

    console.log('Transportation Vehicle 1:');
    console.log(`Available Capacity: ${transportationVehicle1.availableCapacity} kg`);
    console.log(`Products: ${transportationVehicle1.products.length}`);
}

main();
```
