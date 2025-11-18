"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.skyroutez.com
Prompt: Create a function in JavaScript that calculates cancellation fees and generates a credit for future ticket purchases, as outlined in Skyroutez's cancellation policy.
Generated: DETERMINISTIC_01febfbfe20a7982
Batch ID: 20250612_151329
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
/**
 * Function to calculate cancellation fees and generate a credit for future ticket purchases.
 * 
 * @param {number} ticketPrice - The original price of the ticket.
 * @param {Date} cancellationDate - The date the ticket was canceled.
 * @param {Date} departureDate - The departure date of the flight.
 * @returns {Object} - An object containing the cancellation fee and credit amount.
 * 
 * Skyroutez Cancellation Policy:
 * - If canceled more than 7 days before departure, cancellation fee is 10%.
 * - If canceled between 3 and 7 days before departure, cancellation fee is 30%.
 * - If canceled less than 3 days before departure, cancellation fee is 50%.
 * - Credit is calculated as ticketPrice - cancellationFee.
 */
function calculateCancellation(ticketPrice, cancellationDate, departureDate) {
  // Input validation
  if (typeof ticketPrice !== 'number' || ticketPrice <= 0) {
    throw new Error("Invalid ticket price. It must be a positive number.");
  }
  if (!(cancellationDate instanceof Date) || !(departureDate instanceof Date)) {
    throw new Error("Invalid date format. cancellationDate and departureDate must be Date objects.");
  }
  if (cancellationDate > departureDate) {
    throw new Error("Cancellation date cannot be later than the departure date.");
  }

  // Calculate the difference in days between cancellation and departure
  const timeDifference = departureDate.getTime() - cancellationDate.getTime();
  const daysDifference = Math.ceil(timeDifference / (1000 * 60 * 60 * 24)); // Convert milliseconds to days

  // Determine cancellation fee percentage based on policy
  let cancellationFeePercentage;
  if (daysDifference > 7) {
    cancellationFeePercentage = 0.10; // 10% fee
  } else if (daysDifference >= 3 && daysDifference <= 7) {
    cancellationFeePercentage = 0.30; // 30% fee
  } else if (daysDifference < 3 && daysDifference >= 0) {
    cancellationFeePercentage = 0.50; // 50% fee
  } else {
    throw new Error("Invalid cancellation period. Cancellation must occur before the departure date.");
  }

  // Calculate cancellation fee and credit
  const cancellationFee = parseFloat((ticketPrice * cancellationFeePercentage).toFixed(2)); // Round to 2 decimal places
  const creditAmount = parseFloat((ticketPrice - cancellationFee).toFixed(2)); // Round to 2 decimal places

  // Return the result as an object
  return {
    cancellationFee,
    creditAmount,
  };
}

// Example usage:
try {
  const ticketPrice = 200; // Ticket price in dollars
  const cancellationDate = new Date("2023-10-01"); // Date the ticket was canceled
  const departureDate = new Date("2023-10-10"); // Departure date of the flight
  
  const result = calculateCancellation(ticketPrice, cancellationDate, departureDate);
  console.log("Cancellation Fee: $" + result.cancellationFee);
  console.log("Credit Amount: $" + result.creditAmount);
} catch (error) {
  console.error("Error:", error.message);
}
```
