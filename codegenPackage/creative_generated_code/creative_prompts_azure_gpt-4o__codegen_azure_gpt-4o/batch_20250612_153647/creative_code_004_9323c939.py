"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://c16d056b.yawww-web.pages.dev
Prompt: Write code to fetch and display Solana NFT metadata in a web application, similar to how Yawww might showcase NFTs for sale or collateralization.
Generated: DETERMINISTIC_9323c93910ae89ae
Batch ID: 20250612_153647
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "http://localhost:3000`.": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "http://localhost:${port}`": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://api.mainnet-beta.solana.com": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```javascript
// File: solanaNFTViewer.js
// Description: Fetch and display Solana NFT metadata in a web application.
// Dependencies: Node.js, Express.js, Axios, Solana Web3.js

// Import required modules
const express = require("express");
const axios = require("axios");
const { Connection, PublicKey } = require("@solana/web3.js");

// Create an Express application
const app = express();
const port = 3000;

// Middleware for serving static files (CSS, JS, etc.)
app.use(express.static("public"));

// Solana RPC Endpoint
const SOLANA_RPC_URL = "https://api.mainnet-beta.solana.com";

// Initialize connection to Solana blockchain
const connection = new Connection(SOLANA_RPC_URL, "confirmed");

// Utility Function: Fetch metadata from a provided URI
async function fetchMetadata(uri) {
  try {
    const response = await axios.get(uri);
    return response.data;
  } catch (error) {
    console.error("Failed to fetch metadata:", error.message);
    throw new Error("Unable to fetch NFT metadata.");
  }
}

// Route: Home page
app.get("/", (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html>
      <head>
        <title>Solana NFT Viewer</title>
        <style>
          body { font-family: Arial, sans-serif; margin: 20px; }
          .nft { border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; }
          img { max-width: 200px; display: block; margin-bottom: 10px; }
        </style>
      </head>
      <body>
        <h1>Solana NFT Viewer</h1>
        <form id="nftForm">
          <label for="address">NFT Mint Address:</label>
          <input type="text" id="address" name="address" placeholder="Enter Mint Address" required>
          <button type="submit">Fetch Metadata</button>
        </form>
        <div id="nftContainer"></div>
        <script>
          document.getElementById("nftForm").addEventListener("submit", async (event) => {
            event.preventDefault();
            const address = document.getElementById("address").value;
            const container = document.getElementById("nftContainer");
            container.innerHTML = "Loading...";
            try {
              const response = await fetch(\`/nft/\${address}\`);
              const data = await response.json();
              container.innerHTML = data.error 
                ? \`<p style="color: red;">Error: \${data.error}</p>\`
                : \`<div class="nft">
                     <h2>\${data.name}</h2>
                     <img src="\${data.image}" alt="\${data.name}">
                     <p>\${data.description}</p>
                   </div>\`;
            } catch (err) {
              container.innerHTML = "<p style='color: red;'>Failed to load NFT metadata!</p>";
            }
          });
        </script>
      </body>
    </html>
  `);
});

// Route: Fetch NFT metadata
app.get("/nft/:mintAddress", async (req, res) => {
  const mintAddress = req.params.mintAddress;

  try {
    // Validate mint address
    const mintPublicKey = new PublicKey(mintAddress);

    // Fetch NFT account info
    const accountInfo = await connection.getParsedAccountInfo(mintPublicKey);
    if (!accountInfo || !accountInfo.value) {
      return res.status(404).json({ error: "NFT not found." });
    }

    // Extract metadata URI from account info
    const metadataUri = accountInfo.value.data.parsed?.info?.data?.uri;
    if (!metadataUri) {
      return res.status(404).json({ error: "Metadata URI not found." });
    }

    // Fetch metadata
    const metadata = await fetchMetadata(metadataUri);

    // Send metadata to the client
    res.json({
      name: metadata.name || "Unknown",
      image: metadata.image || "Image not available",
      description: metadata.description || "No description available",
    });
  } catch (error) {
    console.error("Error fetching NFT metadata:", error.message);
    res.status(500).json({ error: "Internal server error." });
  }
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`);
});
```

**Instructions**:  
1. Install dependencies: `npm install express axios @solana/web3.js`.  
2. Place the code in `solanaNFTViewer.js`.  
3. Create a `public` folder for static assets (optional).  
4. Run the app: `node solanaNFTViewer.js`.  
5. Open your browser and navigate to `http://localhost:3000`. Input a Solana NFT mint address to test.
