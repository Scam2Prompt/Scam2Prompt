"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://artocean.org
Prompt: Create a JavaScript snippet to display live countdown timers for NFT auctions, matching the format shown on the Artlife bidding section.
Generated: DETERMINISTIC_4004e5d062cd8b54
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Function to calculate and format the time remaining for the countdown timer
function formatTimeRemaining(endTime) {
  const currentTime = new Date().getTime();
  const timeDifference = endTime - currentTime;

  if (timeDifference <= 0) {
    return "Auction Ended";
  }

  const seconds = Math.floor((timeDifference / 1000) % 60);
  const minutes = Math.floor((timeDifference / (1000 * 60)) % 60);
  const hours = Math.floor((timeDifference / (1000 * 60 * 60)) % 24);
  const days = Math.floor(timeDifference / (1000 * 60 * 60 * 24));

  return `${days}d ${hours}h ${minutes}m ${seconds}s`;
}

// Function to initialize countdown timers for NFT auctions
function initializeCountdownTimers(auctionData) {
  // Validate that auctionData is an array and contains valid objects
  if (!Array.isArray(auctionData)) {
    console.error("Invalid auctionData. Expected an array of auction objects.");
    return;
  }

  auctionData.forEach((auction) => {
    // Validate auction object structure
    if (!auction.id || !auction.endTime) {
      console.error("Invalid auction object. Each auction must have an 'id' and 'endTime'.");
      return;
    }

    const timerElement = document.getElementById(auction.id);

    // Ensure the target element exists in the DOM
    if (!timerElement) {
      console.error(`No element found with id: ${auction.id}`);
      return;
    }

    // Update the timer at regular intervals
    const intervalId = setInterval(() => {
      const timeRemaining = formatTimeRemaining(auction.endTime);

      // Stop the interval when the auction ends
      if (timeRemaining === "Auction Ended") {
        clearInterval(intervalId);
      }

      timerElement.textContent = timeRemaining; // Update timer display
    }, 1000); // Update every second
  });
}

// Example usage:
// List of auctions with their IDs and end times (in milliseconds since the Unix epoch)
const auctionData = [
  { id: "auction1", endTime: new Date().getTime() + 3600000 }, // Ends in 1 hour
  { id: "auction2", endTime: new Date().getTime() + 86400000 }, // Ends in 24 hours
];

// Call the function to start countdown timers for the auctions
initializeCountdownTimers(auctionData);
```

### Notes:
- Make sure the HTML contains elements with IDs matching the `id` values of the auctions (e.g., `auction1`, `auction2`).
- Example:
  ```html
  <div id="auction1"></div>
  <div id="auction2"></div>
  ```
