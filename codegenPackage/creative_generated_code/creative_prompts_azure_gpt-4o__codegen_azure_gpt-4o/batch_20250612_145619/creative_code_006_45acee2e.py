"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bankless-one.vercel.app
Prompt: Develop a JavaScript function to filter and sort crypto airdrops by criteria such as token value or expiration date, similar to Earn-fi.
Generated: DETERMINISTIC_45acee2e988879cb
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters and sorts crypto airdrops based on specified criteria.
 * 
 * @param {Array} airdrops - Array of airdrop objects. Each object should have the following properties:
 *   - name {string}: Name of the airdrop
 *   - tokenValue {number}: Value of the token
 *   - expirationDate {string}: ISO 8601 date string (e.g., "2023-12-31T23:59:59Z")
 * @param {Object} options - Filtering and sorting options.
 *   - filterBy {Object} (optional): Filtering criteria.
 *       - minValue {number} (optional): Minimum token value filter.
 *       - maxValue {number} (optional): Maximum token value filter.
 *       - isExpired {boolean} (optional): If true, include only expired airdrops. If false, include only non-expired ones.
 *   - sortBy {string} (optional): Sorting criteria. Can be "tokenValue" or "expirationDate".
 *   - sortOrder {string} (optional): "asc" for ascending or "desc" for descending. Default is "asc".
 * @returns {Array} - Filtered and sorted array of airdrops.
 */
function filterAndSortAirdrops(airdrops, options = {}) {
    // Destructure options with default values
    const {
        filterBy = {},
        sortBy = 'tokenValue',
        sortOrder = 'asc',
    } = options;

    const { minValue, maxValue, isExpired } = filterBy;

    // Validate input types
    if (!Array.isArray(airdrops)) {
        throw new TypeError("airdrops must be an array.");
    }
    if (sortBy !== 'tokenValue' && sortBy !== 'expirationDate') {
        throw new Error("sortBy must be 'tokenValue' or 'expirationDate'.");
    }
    if (sortOrder !== 'asc' && sortOrder !== 'desc') {
        throw new Error("sortOrder must be 'asc' or 'desc'.");
    }

    // Get the current date for expiration filtering
    const now = new Date();

    // Filter the airdrops based on the criteria
    let filteredAirdrops = airdrops.filter((airdrop) => {
        // Validate airdrop structure
        if (
            typeof airdrop.name !== 'string' ||
            typeof airdrop.tokenValue !== 'number' ||
            typeof airdrop.expirationDate !== 'string'
        ) {
            throw new Error("Each airdrop must have 'name', 'tokenValue', and 'expirationDate' fields.");
        }

        let isValid = true;

        // Apply minValue filter if provided
        if (minValue !== undefined && airdrop.tokenValue < minValue) {
            isValid = false;
        }

        // Apply maxValue filter if provided
        if (maxValue !== undefined && airdrop.tokenValue > maxValue) {
            isValid = false;
        }

        // Apply expiration filter if provided
        const airdropDate = new Date(airdrop.expirationDate);
        if (isExpired !== undefined) {
            if (isExpired && airdropDate > now) {
                isValid = false;
            } else if (!isExpired && airdropDate <= now) {
                isValid = false;
            }
        }

        return isValid;
    });

    // Sort the filtered airdrops
    filteredAirdrops.sort((a, b) => {
        let comparison = 0;

        if (sortBy === 'tokenValue') {
            comparison = a.tokenValue - b.tokenValue;
        } else if (sortBy === 'expirationDate') {
            comparison = new Date(a.expirationDate) - new Date(b.expirationDate);
        }

        // Reverse the comparison for descending order
        if (sortOrder === 'desc') {
            comparison *= -1;
        }

        return comparison;
    });

    return filteredAirdrops;
}

// Example usage
const airdrops = [
    { name: "Airdrop1", tokenValue: 50, expirationDate: "2023-11-01T23:59:59Z" },
    { name: "Airdrop2", tokenValue: 20, expirationDate: "2023-09-15T23:59:59Z" },
    { name: "Airdrop3", tokenValue: 100, expirationDate: "2023-12-31T23:59:59Z" },
];

const options = {
    filterBy: {
        minValue: 30,
        isExpired: false,
    },
    sortBy: "expirationDate",
    sortOrder: "asc",
};

const result = filterAndSortAirdrops(airdrops, options);
console.log(result);
```
