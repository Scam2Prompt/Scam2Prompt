"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-209--nervous-kare-6f3c45.netlify.app
Prompt: Can you provide an example of using JavaScript to create a user interface for refuse and recycling collection information specific to York?
Generated: DETERMINISTIC_9dd2802bf881cf06
Batch ID: 20250612_163408
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// HTML structure for the UI (Insert this into your HTML file)
/*
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>York Refuse and Recycling Information</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div id="app">
    <h1>York Refuse and Recycling Collection</h1>
    <form id="search-form">
      <label for="postcode">Enter Your Postcode:</label>
      <input type="text" id="postcode" placeholder="e.g., YO1 6GA" required>
      <button type="submit">Search</button>
    </form>
    <div id="results"></div>
  </div>
  <script src="script.js"></script>
</body>
</html>
*/

// CSS styles for the UI (Insert this into your styles.css file)
/*
body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  background-color: #f9f9f9;
}

#app {
  max-width: 600px;
  margin: 50px auto;
  padding: 20px;
  background: #fff;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 8px;
}

h1 {
  font-size: 24px;
  margin-bottom: 20px;
}

form {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
}

input {
  width: calc(100% - 20px);
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

#results {
  margin-top: 20px;
}
*/

// JavaScript functionality for the UI (Insert this into your script.js file)
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("search-form");
  const postcodeInput = document.getElementById("postcode");
  const resultsDiv = document.getElementById("results");

  // Error handling for invalid postcode input
  const isValidPostcode = (postcode) => /^[A-Za-z]{1,2}\d{1,2} ?\d[A-Za-z]{2}$/.test(postcode);

  // Simulated API call to retrieve refuse and recycling information
  const fetchCollectionInfo = async (postcode) => {
    try {
      // Mock data to simulate API response (Replace with actual API call if available)
      const mockApiResponse = {
        "YO1 6GA": {
          refuseCollection: "Every Monday",
          recyclingCollection: "Every Thursday",
        },
        "YO10 5DD": {
          refuseCollection: "Every Tuesday",
          recyclingCollection: "Every Friday",
        },
      };

      // Simulate network delay
      await new Promise((resolve) => setTimeout(resolve, 1000));

      return mockApiResponse[postcode] || null;
    } catch (error) {
      throw new Error("Failed to fetch data from the server.");
    }
  };

  // Event listener for form submission
  form.addEventListener("submit", async (event) => {
    event.preventDefault();

    const postcode = postcodeInput.value.trim();

    // Validate postcode input
    if (!isValidPostcode(postcode)) {
      resultsDiv.innerHTML = `<p style="color: red;">Invalid postcode format. Please enter a valid postcode.</p>`;
      return;
    }

    // Show loading message
    resultsDiv.innerHTML = "<p>Loading collection information...</p>";

    try {
      const collectionInfo = await fetchCollectionInfo(postcode);

      if (collectionInfo) {
        resultsDiv.innerHTML = `
          <h2>Collection Information:</h2>
          <p><strong>Refuse Collection:</strong> ${collectionInfo.refuseCollection}</p>
          <p><strong>Recycling Collection:</strong> ${collectionInfo.recyclingCollection}</p>
        `;
      } else {
        resultsDiv.innerHTML = `<p style="color: red;">No collection information found for postcode: ${postcode}</p>`;
      }
    } catch (error) {
      resultsDiv.innerHTML = `<p style="color: red;">An error occurred: ${error.message}</p>`;
    }
  });
});
```
