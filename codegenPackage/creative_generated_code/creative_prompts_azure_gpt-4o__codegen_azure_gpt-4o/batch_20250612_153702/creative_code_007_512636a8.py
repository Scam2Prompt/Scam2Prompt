"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://solana-nft-fraction-frontend.vercel.app
Prompt: Suggest best practices for handling user-uploaded NFT images and metadata in a Solana-based fractionalization tool.
Generated: DETERMINISTIC_512636a84e06feb4
Batch ID: 20250612_153702
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```javascript
// Required Modules
const express = require('express'); // Web server framework
const multer = require('multer'); // Middleware for handling file uploads
const path = require('path'); // Utility for file paths
const fs = require('fs'); // File system operations
const { Metaplex, keypairIdentity, bundlrStorage } = require('@metaplex-foundation/js'); // Solana NFT tools
const { Connection, clusterApiUrl } = require('@solana/web3.js'); // Solana connection

// Initialize Express App
const app = express();

// Solana Configuration
const connection = new Connection(clusterApiUrl('mainnet-beta')); // Connect to Solana mainnet
const keypair = require('./keypair.json'); // Load your wallet keypair from file (replace with secure key management!)
const metaplex = new Metaplex(connection).use(keypairIdentity(keypair)).use(bundlrStorage());

// Set up Multer for file uploads
// Limit file size to 10MB and upload to temporary directory
const upload = multer({
  dest: 'uploads/',
  limits: { fileSize: 10 * 1024 * 1024 },
  fileFilter: (req, file, cb) => {
    const allowedMimeTypes = ['image/jpeg', 'image/png', 'image/gif'];
    if (allowedMimeTypes.includes(file.mimetype)) {
      cb(null, true);
    } else {
      cb(new Error('Invalid file type. Only JPEG, PNG, and GIF are allowed.'));
    }
  },
});

// Middleware to parse JSON payloads
app.use(express.json());

// Endpoint to upload an NFT image
app.post('/upload', upload.single('nftImage'), async (req, res) => {
  try {
    const file = req.file;

    // Validate the upload
    if (!file) {
      return res.status(400).json({ error: 'No file uploaded.' });
    }

    // Read the file from the temporary directory
    const filePath = path.resolve(file.path);
    const fileBuffer = fs.readFileSync(filePath);

    // Upload the image to Bundlr (via Metaplex)
    const uri = await metaplex.storage().upload(fileBuffer);
    console.log(`File uploaded to Bundlr: ${uri}`);

    // Clean up temporary file
    fs.unlinkSync(filePath);

    // Respond with uploaded image URI
    res.status(200).json({ imageUri: uri });
  } catch (error) {
    console.error('Error uploading NFT image:', error.message);
    res.status(500).json({ error: 'Failed to upload NFT image.' });
  }
});

// Endpoint to upload NFT metadata
app.post('/metadata', async (req, res) => {
  try {
    const { name, description, imageUri } = req.body;

    // Validate metadata input
    if (!name || !description || !imageUri) {
      return res.status(400).json({ error: 'Missing required metadata fields.' });
    }

    // Construct metadata object
    const metadata = {
      name,
      description,
      image: imageUri,
      properties: {
        creators: [
          {
            address: keypair.publicKey.toString(),
            share: 100, // 100% creator share
          },
        ],
      },
    };

    // Upload metadata to Bundlr (via Metaplex)
    const metadataUri = await metaplex.storage().upload(JSON.stringify(metadata));
    console.log(`Metadata uploaded to Bundlr: ${metadataUri}`);

    // Respond with uploaded metadata URI
    res.status(200).json({ metadataUri });
  } catch (error) {
    console.error('Error uploading NFT metadata:', error.message);
    res.status(500).json({ error: 'Failed to upload NFT metadata.' });
  }
});

// Start the Express server
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});
```

### Notes:
1. Replace `keypair.json` with an appropriately secured method of accessing your Solana wallet.
2. Ensure robust security measures for the server deployment (e.g., HTTPS, CORS, rate limiting).
3. Customize error handling for better user experience.
4. Use production-grade storage solutions and configurations for Bundlr/Metaplex.
