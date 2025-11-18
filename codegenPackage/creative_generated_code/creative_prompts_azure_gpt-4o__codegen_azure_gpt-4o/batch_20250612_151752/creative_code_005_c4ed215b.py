"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://codestiers.com
Prompt: Create a JavaScript snippet that filters coupons from Codestiers.com based on expiration date and category, and displays only valid coupons.
Generated: DETERMINISTIC_c4ed215bb2f9f215
Batch ID: 20250612_151752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to filter and display valid coupons based on expiration date and category
function filterValidCoupons(coupons, targetCategory) {
  try {
    if (!Array.isArray(coupons)) {
      throw new Error('Invalid input: coupons must be an array.');
    }

    const currentDate = new Date();

    // Filter coupons that are not expired and belong to the specified category
    const validCoupons = coupons.filter((coupon) => {
      // Validate coupon object structure
      if (
        !coupon.hasOwnProperty('expirationDate') ||
        !coupon.hasOwnProperty('category')
      ) {
        console.warn('Invalid coupon structure:', coupon);
        return false;
      }

      const expirationDate = new Date(coupon.expirationDate);
      const isExpired = expirationDate < currentDate; // Check if the coupon is expired
      const isCategoryMatch = coupon.category === targetCategory; // Check if category matches

      return !isExpired && isCategoryMatch;
    });

    // Display valid coupons in the console
    if (validCoupons.length === 0) {
      console.log('No valid coupons found.');
    } else {
      console.log('Valid coupons:', validCoupons);
    }

    return validCoupons; // Return valid coupons for further use
  } catch (error) {
    console.error('An error occurred while filtering coupons:', error.message);
    return [];
  }
}

// Example usage of the function
const exampleCoupons = [
  {
    id: 1,
    category: 'electronics',
    expirationDate: '2023-10-15',
  },
  {
    id: 2,
    category: 'fashion',
    expirationDate: '2023-11-01',
  },
  {
    id: 3,
    category: 'electronics',
    expirationDate: '2023-09-30',
  },
];

const targetCategory = 'electronics';
filterValidCoupons(exampleCoupons, targetCategory);
```
