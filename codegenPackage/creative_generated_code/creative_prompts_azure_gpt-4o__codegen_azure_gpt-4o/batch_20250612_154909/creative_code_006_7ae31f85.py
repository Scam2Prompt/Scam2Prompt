"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.limpiezadetuboscostablanca.net
Prompt: Write a JavaScript function to calculate the cost of plumbing services based on factors like urgency, service type (e.g., leak detection, industrial cleaning), and location, as described by Limpieza de Tubos Costablanca.
Generated: DETERMINISTIC_7ae31f85c4decccd
Batch ID: 20250612_154909
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate the cost of plumbing services.
 * 
 * @param {string} serviceType - The type of plumbing service (e.g., 'leak detection', 'industrial cleaning').
 * @param {string} location - The location where the service is required (e.g., 'urban', 'rural').
 * @param {boolean} isUrgent - Whether the service is urgent (true for urgent, false for non-urgent).
 * @returns {number} - The total cost of the plumbing service.
 * 
 * Example Usage:
 * const cost = calculatePlumbingCost('leak detection', 'urban', true);
 * console.log('Total cost:', cost);
 */
function calculatePlumbingCost(serviceType, location, isUrgent) {
  // Base costs for different types of services
  const serviceCosts = {
    'leak detection': 100,
    'industrial cleaning': 150,
    'pipe installation': 120,
    'general maintenance': 80,
  };

  // Location adjustment factor
  const locationMultiplier = {
    urban: 1.0, // No adjustment for urban area
    rural: 1.2, // 20% surcharge for rural area
  };

  // Urgency adjustment factor
  const urgencyMultiplier = isUrgent ? 1.5 : 1.0; // 50% increase for urgent services

  try {
    // Validate service type
    if (!serviceCosts[serviceType]) {
      throw new Error(`Invalid service type: ${serviceType}`);
    }

    // Validate location
    if (!locationMultiplier[location]) {
      throw new Error(`Invalid location: ${location}`);
    }

    // Calculate base cost based on service type
    const baseCost = serviceCosts[serviceType];

    // Apply location and urgency multipliers
    const totalCost = baseCost * locationMultiplier[location] * urgencyMultiplier;

    // Return the computed total cost
    return totalCost;
  } catch (error) {
    console.error('Error calculating plumbing cost:', error.message);
    return 0; // Return 0 as fallback cost in case of error
  }
}

// Example usage
const cost = calculatePlumbingCost('leak detection', 'rural', true);
console.log('Total cost:', cost);
```
