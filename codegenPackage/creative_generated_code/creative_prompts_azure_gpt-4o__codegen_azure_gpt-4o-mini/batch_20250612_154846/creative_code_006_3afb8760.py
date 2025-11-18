"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nft-rewards.online
Prompt: Create a tutorial for integrating NFT rewards into a decentralized application (dApp) using Truffle or Hardhat frameworks.
Generated: DETERMINISTIC_3afb876015f645ea
Batch ID: 20250612_154846
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID": {
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
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Import OpenZeppelin ERC721 contract for NFT functionality
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// NFTRewards contract inherits from ERC721 and Ownable
contract NFTRewards is ERC721, Ownable {
    // Counter for token IDs
    uint256 private _tokenIdCounter;

    // Mapping from token ID to whether it is claimed
    mapping(uint256 => bool) private _claimedTokens;

    // Event to emit when a new NFT is minted
    event Minted(address indexed recipient, uint256 tokenId);

    // Constructor to set the token name and symbol
    constructor() ERC721("NFTRewards", "NFTREWARD") {}

    // Function to mint NFT rewards to a user
    function mintNFT(address recipient) external onlyOwner {
        require(recipient != address(0), "Cannot mint to zero address");

        // Increment the token ID counter and assign it to a new NFT
        uint256 tokenId = _tokenIdCounter++;
        _safeMint(recipient, tokenId);
        
        // Emit an event to signal that the NFT has been minted
        emit Minted(recipient, tokenId);
    }

    // Function to check if an NFT has been claimed
    function isTokenClaimed(uint256 tokenId) external view returns (bool) {
        return _claimedTokens[tokenId];
    }

    // Function to claim an NFT
    function claimNFT(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "You are not the owner of this token");
        require(!_claimedTokens[tokenId], "Token already claimed");

        // Mark the token as claimed
        _claimedTokens[tokenId] = true;

        // Additional logic for rewards can be implemented here
    }
}
```

```javascript
// 1. Hardhat script to deploy the NFTRewards contract

const { ethers } = require("hardhat");

async function main() {
    // Get the contract factory
    const NFTRewards = await ethers.getContractFactory("NFTRewards");

    // Deploy the contract
    const nftRewards = await NFTRewards.deploy();

    // Wait for deployment to finish
    await nftRewards.deployed();

    console.log("NFTRewards deployed to:", nftRewards.address);
}

// Error handling for the deployment script
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

```javascript
// 2. Hardhat test for the NFTRewards contract

const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("NFTRewards Contract", function () {
    let NFTRewards;
    let nftRewards;
    let owner;
    let addr1;

    beforeEach(async () => {
        // Get the ContractFactory and Signers here
        NFTRewards = await ethers.getContractFactory("NFTRewards");
        [owner, addr1] = await ethers.getSigners();

        // Deploy a new NFTRewards contract for each test
        nftRewards = await NFTRewards.deploy();
        await nftRewards.deployed();
    });

    it("Should mint an NFT and emit an event", async function () {
        // Mint an NFT to addr1
        await expect(nftRewards.mintNFT(addr1.address))
            .to.emit(nftRewards, "Minted")
            .withArgs(addr1.address, 0);

        // Verify that addr1 owns the NFT
        expect(await nftRewards.ownerOf(0)).to.equal(addr1.address);
    });

    it("Should allow claiming the NFT", async function () {
        // Mint an NFT to addr1
        await nftRewards.mintNFT(addr1.address);

        // addr1 claims the NFT
        await nftRewards.connect(addr1).claimNFT(0);

        // Verify that the token is claimed
        expect(await nftRewards.isTokenClaimed(0)).to.be.true;
    });

    it("Should revert when claiming an already claimed NFT", async function () {
        // Mint an NFT to addr1
        await nftRewards.mintNFT(addr1.address);

        // addr1 claims the NFT
        await nftRewards.connect(addr1).claimNFT(0);

        // Attempt to claim the same NFT again
        await expect(nftRewards.connect(addr1).claimNFT(0)).to.be.revertedWith("Token already claimed");
    });

    it("Should revert when non-owner tries to claim the NFT", async function () {
        // Mint an NFT to addr1
        await nftRewards.mintNFT(addr1.address);

        // Attempt to claim the NFT from another account
        await expect(nftRewards.claimNFT(0)).to.be.revertedWith("You are not the owner of this token");
    });
});
``` 

```json
// 3. Hardhat configuration file (hardhat.config.js)

require("@nomiclabs/hardhat-waffle");

module.exports = {
    solidity: "0.8.0",
    networks: {
        rinkeby: {
            url: "https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID", // Replace with your Infura project ID
            accounts: ["YOUR_PRIVATE_KEY"], // Replace with your account's private key
        },
    },
};
``` 

This code provides a basic implementation of an NFT rewards system using Solidity with the Hardhat framework for deployment and testing. It includes necessary error handling and follows best practices for smart contract development. Please ensure to replace placeholders with your actual values where necessary.
