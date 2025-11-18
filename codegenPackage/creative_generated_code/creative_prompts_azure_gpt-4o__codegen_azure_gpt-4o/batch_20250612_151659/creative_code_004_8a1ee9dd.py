"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://coolcatspetsnft.pages.dev
Prompt: Write a JavaScript script that displays a message to users if JavaScript is disabled, preventing them from minting "Coolcats Pets" NFTs.
Generated: DETERMINISTIC_8a1ee9dd235c9205
Batch ID: 20250612_151659
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Coolcats Pets NFT Minting</title>
  <style>
    /* Styling for the "JavaScript Disabled" message */
    .no-js-message {
      display: none; /* Default is hidden */
      color: #ff0000;
      font-size: 1.2em;
      padding: 10px;
      border: 2px solid #ff0000;
      border-radius: 5px;
      margin: 20px;
      text-align: center;
      background-color: #fef0f0;
    }
  </style>
</head>
<body>
  <!-- Placeholder for the JavaScript disabled message -->
  <div id="no-js-message" class="no-js-message">
    JavaScript is disabled in your browser. Please enable JavaScript to mint Coolcats Pets NFTs.
  </div>

  <!-- Main content for users who have JavaScript enabled -->
  <div id="main-content">
    <h1>Welcome to Coolcats Pets NFT Minting</h1>
    <p>Mint your own Coolcats Pets NFTs using the button below!</p>
    <button id="mint-button">Mint Coolcats Pets NFT</button>
  </div>

  <!-- Add a <noscript> block for users without JavaScript -->
  <noscript>
    <style>
      #main-content {
        display: none; /* Hide the main content if JavaScript is disabled */
      }
      .no-js-message {
        display: block; /* Show the warning message if JavaScript is disabled */
      }
    </style>
  </noscript>

  <!-- JavaScript script -->
  <script>
    // Wait for DOM content to be fully loaded
    document.addEventListener("DOMContentLoaded", function () {
      // Hide the "JavaScript Disabled" message since JS is enabled
      const noJsMessage = document.getElementById("no-js-message");
      if (noJsMessage) {
        noJsMessage.style.display = "none";
      }

      // Add functionality to the mint button
      const mintButton = document.getElementById("mint-button");
      if (mintButton) {
        mintButton.addEventListener("click", function () {
          // Simulate minting process (replace with actual minting logic)
          alert("Minting your Coolcats Pets NFT... Please wait!");
        });
      }
    });
  </script>
</body>
</html>
```
