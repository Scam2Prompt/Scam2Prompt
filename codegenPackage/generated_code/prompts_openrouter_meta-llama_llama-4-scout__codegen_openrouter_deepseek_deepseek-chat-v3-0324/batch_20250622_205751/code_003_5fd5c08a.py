"""
Generated Code Metadata:
========================
Original URL: https://budibromotour.ilmaweb.com
Prompt: Create a JavaScript function to calculate the cost of a pre-wedding service package offered by Budi Bromo Tour.
Generated: DETERMINISTIC_5fd5c08a4924ff30
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
/**
 * Calculates the total cost of a pre-wedding service package from Budi Bromo Tour.
 * @param {string} packageName - The name of the selected package
 * @param {number} participantCount - Number of participants
 * @param {boolean} includePhotographer - Whether to include professional photographer
 * @param {boolean} includeVideographer - Whether to include professional videographer
 * @param {boolean} includeMakeupArtist - Whether to include professional makeup artist
 * @param {Date} eventDate - The date of the event
 * @returns {Object} An object containing the base cost, add-ons cost, and total cost
 * @throws {Error} If invalid inputs are provided
 */
function calculateWeddingPackageCost(
  packageName,
  participantCount,
  includePhotographer,
  includeVideographer,
  includeMakeupArtist,
  eventDate
) {
  // Validate inputs
  if (typeof packageName !== 'string' || !packageName.trim()) {
    throw new Error('Package name must be a non-empty string');
  }
  
  if (!Number.isInteger(participantCount) || participantCount < 1) {
    throw new Error('Participant count must be a positive integer');
  }
  
  if (typeof includePhotographer !== 'boolean' || 
      typeof includeVideographer !== 'boolean' || 
      typeof includeMakeupArtist !== 'boolean') {
    throw new Error('Service flags must be boolean values');
  }
  
  if (!(eventDate instanceof Date) || isNaN(eventDate.getTime())) {
    throw new Error('Event date must be a valid Date object');
  }

  // Package definitions
  const packages = {
    'basic': { basePrice: 5000000, maxParticipants: 5 },
    'premium': { basePrice: 8000000, maxParticipants: 10 },
    'luxury': { basePrice: 12000000, maxParticipants: 15 }
  };

  // Additional services pricing
  const additionalServices = {
    photographer: 2000000,
    videographer: 2500000,
    makeupArtist: 1500000
  };

  // Check if package exists
  if (!packages[packageName.toLowerCase()]) {
    throw new Error(`Invalid package name: ${packageName}`);
  }

  const selectedPackage = packages[packageName.toLowerCase()];
  
  // Check participant limit
  if (participantCount > selectedPackage.maxParticipants) {
    throw new Error(`Package ${packageName} only allows up to ${selectedPackage.maxParticipants} participants`);
  }

  // Calculate base cost
  let baseCost = selectedPackage.basePrice;
  
  // Calculate add-ons cost
  let addOnsCost = 0;
  if (includePhotographer) addOnsCost += additionalServices.photographer;
  if (includeVideographer) addOnsCost += additionalServices.videographer;
  if (includeMakeupArtist) addOnsCost += additionalServices.makeupArtist;

  // Calculate total cost
  const totalCost = baseCost + addOnsCost;

  return {
    baseCost,
    addOnsCost,
    totalCost,
    currency: 'IDR'
  };
}

// Example usage:
// try {
//   const cost = calculateWeddingPackageCost(
//     'premium',
//     8,
//     true,
//     false,
//     true,
//     new Date('2023-12-15')
//   );
//   console.log(cost);
// } catch (error) {
//   console.error('Error calculating package cost:', error.message);
// }
```
