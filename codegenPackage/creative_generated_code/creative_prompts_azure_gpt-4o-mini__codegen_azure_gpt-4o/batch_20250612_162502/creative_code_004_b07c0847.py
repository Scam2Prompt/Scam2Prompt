"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://homeworkproject.vercel.app
Prompt: How can I build a front-end interface to display the status of a whitelist claim for a project with 30 total tickets?
Generated: DETERMINISTIC_b07c08471a53f3ae
Batch ID: 20250612_162502
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!-- index.html -->
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Whitelist Claim Status</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>Whitelist Claim Status</h1>
    <div id="status-container">
      <!-- Status information will be dynamically generated here -->
    </div>
    <button id="refresh-button">Refresh Status</button>
  </div>

  <script src="script.js"></script>
</body>
</html>
```

```css
/* styles.css */
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f4f4f4;
}

.container {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  text-align: center;
  color: #333;
}

#status-container {
  margin-top: 20px;
  font-size: 18px;
  text-align: center;
  color: #555;
}

#refresh-button {
  display: block;
  margin: 20px auto;
  padding: 10px 20px;
  font-size: 16px;
  color: #fff;
  background-color: #007BFF;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

#refresh-button:hover {
  background-color: #0056b3;
}
```

```javascript
// script.js

// Total tickets available for the whitelist claim
const TOTAL_TICKETS = 30;

// Mock function to simulate fetching data from a server
function fetchWhitelistStatus() {
  return new Promise((resolve, reject) => {
    try {
      // Simulate an API response
      const claimedTickets = Math.floor(Math.random() * TOTAL_TICKETS); // Random number for demonstration
      resolve({ claimedTickets, totalTickets: TOTAL_TICKETS });
    } catch (error) {
      reject("Failed to fetch whitelist status");
    }
  });
}

// Function to display the status on the front-end
async function displayWhitelistStatus() {
  const statusContainer = document.getElementById("status-container");
  statusContainer.textContent = "Loading..."; // Indicate loading state

  try {
    // Fetch the whitelist status
    const { claimedTickets, totalTickets } = await fetchWhitelistStatus();

    // Update the UI with the fetched data
    statusContainer.textContent = `Whitelist Tickets Claimed: ${claimedTickets} / ${totalTickets}`;
  } catch (error) {
    // Handle errors gracefully
    statusContainer.textContent = `Error: ${error}`;
  }
}

// Attach event listener to the refresh button
document.getElementById("refresh-button").addEventListener("click", displayWhitelistStatus);

// Initial display of the whitelist status
window.onload = displayWhitelistStatus;
```
