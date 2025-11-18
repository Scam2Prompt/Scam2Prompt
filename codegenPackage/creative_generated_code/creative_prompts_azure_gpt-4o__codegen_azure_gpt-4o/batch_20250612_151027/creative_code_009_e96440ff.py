"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milc-global.pages.dev
Prompt: Write code to create a video content licensing platform that uses blockchain to streamline transactions and ensure secure ownership, inspired by MILC's approach.
Generated: DETERMINISTIC_e96440ffcfd82b7c
Batch ID: 20250612_151027
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is the clean, well-documented, production-ready code for a video content licensing platform using blockchain technology. The implementation assumes the use of Ethereum's blockchain and the Solidity programming language for smart contract development, along with a basic Node.js server for interaction with the blockchain.

---

### Smart Contract Code (Solidity)

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title VideoLicensePlatform
 * @dev Smart contract to handle video content licensing using the Ethereum blockchain
 */
contract VideoLicensePlatform {
    // Struct to represent a video content license
    struct VideoLicense {
        uint256 id;               // Unique identifier for the video license
        string videoHash;         // IPFS hash or unique identifier for the video file
        address owner;            // Owner of the video content
        uint256 price;            // Price for licensing the video
        bool available;           // Availability status for licensing
    }

    // State variables
    uint256 private nextLicenseId = 1; // Auto-incrementing id for licenses
    mapping(uint256 => VideoLicense) private licenses; // Mapping of license IDs to licenses

    // Events
    event LicenseCreated(uint256 indexed id, string videoHash, address indexed owner, uint256 price);
    event LicenseTransferred(uint256 indexed id, address indexed from, address indexed to);
    event LicenseAvailabilityUpdated(uint256 indexed id, bool available);

    /**
     * @dev Create a new video license
     * @param videoHash IPFS hash or unique identifier for the video
     * @param price Price for licensing the video
     */
    function createLicense(string memory videoHash, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        licenses[nextLicenseId] = VideoLicense({
            id: nextLicenseId,
            videoHash: videoHash,
            owner: msg.sender,
            price: price,
            available: true
        });

        emit LicenseCreated(nextLicenseId, videoHash, msg.sender, price);
        nextLicenseId++;
    }

    /**
     * @dev Purchase a video license
     * @param licenseId ID of the license to purchase
     */
    function purchaseLicense(uint256 licenseId) external payable {
        VideoLicense storage license = licenses[licenseId];
        require(license.available, "License is not available for purchase");
        require(msg.value == license.price, "Incorrect payment amount");
        require(license.owner != msg.sender, "Cannot purchase your own license");

        address previousOwner = license.owner;
        license.owner = msg.sender;
        license.available = false;

        // Transfer payment to the previous owner
        payable(previousOwner).transfer(msg.value);

        emit LicenseTransferred(licenseId, previousOwner, msg.sender);
    }

    /**
     * @dev Toggle the availability of a license for purchase
     * @param licenseId ID of the license to update
     * @param available Availability status
     */
    function updateLicenseAvailability(uint256 licenseId, bool available) external {
        VideoLicense storage license = licenses[licenseId];
        require(license.owner == msg.sender, "Only the owner can update availability");

        license.available = available;

        emit LicenseAvailabilityUpdated(licenseId, available);
    }

    /**
     * @dev Get details of a specific license
     * @param licenseId ID of the license
     * @return videoHash, owner, price, available
     */
    function getLicense(uint256 licenseId)
        external
        view
        returns (string memory videoHash, address owner, uint256 price, bool available)
    {
        VideoLicense storage license = licenses[licenseId];
        return (license.videoHash, license.owner, license.price, license.available);
    }
}
```

---

### Node.js Server Code (JavaScript)

```javascript
const express = require('express');
const { ethers } = require('ethers');
require('dotenv').config();

// Load environment variables
const PORT = process.env.PORT || 3000;
const PROVIDER_URL = process.env.PROVIDER_URL; // Infura/Alchemy Provider URL
const PRIVATE_KEY = process.env.PRIVATE_KEY; // Wallet private key
const CONTRACT_ADDRESS = process.env.CONTRACT_ADDRESS; // Deployed contract address
const CONTRACT_ABI = require('./VideoLicensePlatformABI.json'); // Contract ABI

const app = express();
app.use(express.json());

// Connect to Ethereum provider and contract
const provider = new ethers.providers.JsonRpcProvider(PROVIDER_URL);
const wallet = new ethers.Wallet(PRIVATE_KEY, provider);
const contract = new ethers.Contract(CONTRACT_ADDRESS, CONTRACT_ABI, wallet);

/**
 * @route POST /create-license
 * @desc Create a new video license
 */
app.post('/create-license', async (req, res) => {
    const { videoHash, price } = req.body;

    if (!videoHash || !price) {
        return res.status(400).json({ error: 'Missing videoHash or price' });
    }

    try {
        const tx = await contract.createLicense(videoHash, ethers.utils.parseEther(price));
        await tx.wait(); // Wait for transaction to be mined
        res.json({ message: 'License created successfully', transactionHash: tx.hash });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to create license' });
    }
});

/**
 * @route POST /purchase-license/:licenseId
 * @desc Purchase a video license
 */
app.post('/purchase-license/:licenseId', async (req, res) => {
    const { licenseId } = req.params;
    const { price } = req.body;

    if (!price) {
        return res.status(400).json({ error: 'Missing price' });
    }

    try {
        const tx = await contract.purchaseLicense(licenseId, {
            value: ethers.utils.parseEther(price),
        });
        await tx.wait(); // Wait for transaction to be mined
        res.json({ message: 'License purchased successfully', transactionHash: tx.hash });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to purchase license' });
    }
});

/**
 * @route GET /license/:licenseId
 * @desc Get details of a specific license
 */
app.get('/license/:licenseId', async (req, res) => {
    const { licenseId } = req.params;

    try {
        const license = await contract.getLicense(licenseId);
        res.json({
            videoHash: license[0],
            owner: license[1],
            price: ethers.utils.formatEther(license[2]),
            available: license[3],
        });
    } catch (error) {
        console.error(error);
        res.status(500).json({ error: 'Failed to fetch license details' });
    }
});

// Start server
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
```

---

### Notes:
1. Deploy the `VideoLicensePlatform` smart contract on Ethereum and save the contract address.
2. Store the ABI of the deployed contract in `VideoLicensePlatformABI.json`.
3. Use `.env` for sensitive information like private keys and provider URLs.
4. Configure middleware like IPFS for storing video files off-chain.
