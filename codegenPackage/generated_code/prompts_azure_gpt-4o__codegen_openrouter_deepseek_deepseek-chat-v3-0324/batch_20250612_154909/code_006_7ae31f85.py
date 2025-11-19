"""
Generated Code Metadata:
========================
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a JavaScript function to calculate the cost of plumbing services based on factors like urgency, service type (e.g., leak detection, industrial cleaning), and location, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7ae31f85c4decccd
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the cost of plumbing services based on various factors.
 * @param {Object} options - Service options
 * @param {string} options.serviceType - Type of service (e.g., 'leakDetection', 'industrialCleaning')
 * @param {string} options.location - Service location (e.g., 'urban', 'suburban', 'rural')
 * @param {boolean} options.isUrgent - Whether the service is urgent
 * @param {number} [options.distance] - Distance in km (required for rural locations)
 * @returns {number} Calculated cost in euros
 * @throws {Error} If invalid parameters are provided
 */
function calculatePlumbingCost(options) {
    // Validate input
    if (!options || typeof options !== 'object') {
        throw new Error('Options object is required');
    }

    const { serviceType, location, isUrgent, distance } = options;

    if (!serviceType || typeof serviceType !== 'string') {
        throw new Error('Valid serviceType is required');
    }

    if (!location || typeof location !== 'string') {
        throw new Error('Valid location is required');
    }

    if (typeof isUrgent !== 'boolean') {
        throw new Error('isUrgent must be a boolean');
    }

    // Base prices for different service types (in euros)
    const servicePrices = {
        leakDetection: 120,
        pipeRepair: 150,
        drainCleaning: 100,
        industrialCleaning: 300,
        installation: 200,
        inspection: 80
    };

    // Location multipliers
    const locationMultipliers = {
        urban: 1.0,
        suburban: 1.2,
        rural: 1.5
    };

    // Urgency surcharge (percentage)
    const urgencySurcharge = isUrgent ? 0.3 : 0;

    // Validate service type
    if (!servicePrices[serviceType]) {
        throw new Error(`Invalid service type: ${serviceType}`);
    }

    // Validate location
    if (!locationMultipliers[location]) {
        throw new Error(`Invalid location: ${location}`);
    }

    // Additional validation for rural locations
    if (location === 'rural') {
        if (typeof distance !== 'number' || distance <= 0) {
            throw new Error('Distance must be a positive number for rural locations');
        }
        // Add distance-based fee (1 euro per km
