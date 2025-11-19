"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ittastours.com
Prompt: Write a JavaScript function that filters available tailor-made holiday packages on ITTAS Tours based on destination and travel dates.
Generated: DETERMINISTIC_d067f118293290c3
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Filters tailor-made holiday packages based on destination and travel dates.
 * 
 * @param {Array} packages - List of available holiday packages.
 * @param {string} destination - Desired destination to filter by.
 * @param {Date} startDate - Desired travel start date.
 * @param {Date} endDate - Desired travel end date.
 * @returns {Array} Filtered holiday packages matching the criteria.
 */
function filterHolidayPackages(packages, destination, startDate, endDate) {
    // Validate input parameters
    if (!Array.isArray(packages)) {
        throw new TypeError("Expected 'packages' to be an array.");
    }
    if (typeof destination !== "string") {
        throw new TypeError("Expected 'destination' to be a string.");
    }
    if (!(startDate instanceof Date) || !(endDate instanceof Date)) {
        throw new TypeError("Expected 'startDate' and 'endDate' to be Date objects.");
    }
    if (startDate > endDate) {
        throw new Error("'startDate' cannot be later than 'endDate'.");
    }

    // Filter packages using the criteria
    return packages.filter(package => {
        try {
            // Check if package matches the destination
            const matchesDestination = package.destination.toLowerCase() === destination.toLowerCase();

            // Check if package travel dates overlap with desired dates
            const packageStartDate = new Date(package.startDate);
            const packageEndDate = new Date(package.endDate);
            const matchesTravelDates =
                (packageStartDate <= endDate && packageEndDate >= startDate);

            // Return true if both conditions are met
            return matchesDestination && matchesTravelDates;
        } catch (error) {
            console.error("Error processing package:", package, error);
            return false; // Exclude packages with invalid data
        }
    });
}

// Example usage:
const holidayPackages = [
    { id: 1, destination: "Paris", startDate: "2023-12-01", endDate: "2023-12-10" },
    { id: 2, destination: "London", startDate: "2023-12-05", endDate: "2023-12-15" },
    { id: 3, destination: "Paris", startDate: "2023-12-20", endDate: "2023-12-25" },
];

const filteredPackages = filterHolidayPackages(
    holidayPackages,
    "Paris",
    new Date("2023-12-01"),
    new Date("2023-12-15")
);

console.log(filteredPackages); // Output: Packages matching the criteria
```
