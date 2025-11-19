"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cham-transfers.com
Prompt: Write a JavaScript function that retrieves flight information and suggests the best transfer options from Geneva to Chamonix based on arrival times.
Generated: DETERMINISTIC_50255008324290ba
Batch ID: 20250612_135754
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to retrieve flight information and suggest the best transfer options
 * from Geneva to Chamonix based on arrival times.
 */

// Mock data for demonstration purposes (replace with real API data in production)
const flightData = [
  { flightNumber: "UA123", arrivalTime: "2023-10-20T14:30:00Z" },
  { flightNumber: "BA456", arrivalTime: "2023-10-20T16:00:00Z" },
  { flightNumber: "LH789", arrivalTime: "2023-10-20T18:15:00Z" },
];

const transferOptions = [
  { provider: "Shuttle A", departureTime: "2023-10-20T15:00:00Z", durationHours: 1.5 },
  { provider: "Shuttle B", departureTime: "2023-10-20T16:30:00Z", durationHours: 1.5 },
  { provider: "Shuttle C", departureTime: "2023-10-20T19:00:00Z", durationHours: 1.5 },
];

/**
 * Parses ISO datetime strings and returns Date objects.
 * @param {string} isoString - ISO datetime string.
 * @return {Date} - JavaScript Date object.
 */
function parseISODate(isoString) {
  return new Date(isoString);
}

/**
 * Finds the best transfer options from Geneva to Chamonix based on flight arrival times.
 * @param {Array<object>} flights - List of flights with arrival times.
 * @param {Array<object>} transfers - List of transfer options with departure times.
 * @return {Array<object>} - Best transfer options for each flight.
 */
function getBestTransferOptions(flights, transfers) {
  // Ensure input data is valid
  if (!Array.isArray(flights) || !Array.isArray(transfers)) {
    throw new Error("Invalid input: flights and transfers must be arrays.");
  }

  const results = [];

  flights.forEach((flight) => {
    const flightArrival = parseISODate(flight.arrivalTime);

    // Filter transfer options based on a reasonable time window (e.g., 30 minutes after arrival)
    const availableTransfers = transfers.filter((transfer) => {
      const transferDeparture = parseISODate(transfer.departureTime);
      return transferDeparture > flightArrival && 
             transferDeparture - flightArrival >= 30 * 60 * 1000; // Minimum 30 minutes buffer
    });

    // Sort available transfers by departure time to find the earliest option
    availableTransfers.sort((a, b) => 
      parseISODate(a.departureTime) - parseISODate(b.departureTime)
    );

    // Add the best transfer option (if available) to the results
    if (availableTransfers.length > 0) {
      results.push({
        flight: flight.flightNumber,
        bestTransfer: availableTransfers[0],
      });
    } else {
      results.push({
        flight: flight.flightNumber,
        bestTransfer: null, // No suitable transfer found
      });
    }
  });

  return results;
}

/**
 * Example usage
 */
try {
  const bestTransfers = getBestTransferOptions(flightData, transferOptions);
  console.log("Best Transfer Options:", bestTransfers);
} catch (error) {
  console.error("Error retrieving transfer options:", error.message);
}
```
