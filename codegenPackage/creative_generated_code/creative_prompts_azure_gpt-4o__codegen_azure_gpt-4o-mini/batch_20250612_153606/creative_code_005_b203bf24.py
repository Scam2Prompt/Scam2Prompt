"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gofurs-cash.pages.dev
Prompt: Develop a tutorial for deploying an ERC404-compliant smart contract on Ethereum, including steps for testing the minting and burning of NFTs based on token balance changes.
Generated: DETERMINISTIC_b203bf24f9feaaea
Batch ID: 20250612_153606
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";

/**
 * @title ERC404Tokens
 * @dev Implements a simple ERC721 compliant NFT contract with minting and burning capabilities
 */
contract ERC404Tokens is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    
    Counters.Counter private _tokenIdCounter; // Counter for tracking token IDs
    mapping(uint256 => bool) private _burnedTokens; // Mapping to track burned tokens

    event TokenMinted(address indexed to, uint256 indexed tokenId);
    event TokenBurned(address indexed owner, uint256 indexed tokenId);

    /**
     * @dev Constructor to initialize the ERC721 token with a name and symbol.
     * @param name The name of the token.
     * @param symbol The symbol of the token.
     */
    constructor(string memory name, string memory symbol) ERC721(name, symbol) {}

    /**
     * @dev Mint a new token to the specified address.
     * @param to The address to mint the token to.
     */
    function mint(address to) external onlyOwner {
        require(to != address(0), "Invalid address: Zero address cannot receive tokens.");
        
        uint256 tokenId = _tokenIdCounter.current();
        _mint(to, tokenId);
        _tokenIdCounter.increment();

        emit TokenMinted(to, tokenId);
    }

    /**
     * @dev Burn a token with the specified tokenId.
     * @param tokenId The ID of the token to burn.
     */
    function burn(uint256 tokenId) external {
        require(_exists(tokenId), "Token does not exist.");
        require(ownerOf(tokenId) == msg.sender, "You do not own this token.");

        _burn(tokenId);
        _burnedTokens[tokenId] = true; // Mark token as burned

        emit TokenBurned(msg.sender, tokenId);
    }

    /**
     * @dev Check if a token has been burned.
     * @param tokenId The ID of the token to check.
     * @return bool indicating if the token is burned.
     */
    function isTokenBurned(uint256 tokenId) external view returns (bool) {
        return _burnedTokens[tokenId];
    }

    /**
     * @dev Override base implementation of _beforeTokenTransfer to manage burned tokens.
     * @param from The address transferring the token.
     * @param to The address receiving the token.
     * @param tokenId The ID of the token being transferred.
     */
    function _beforeTokenTransfer(address from, address to, uint256 tokenId) internal override {
        require(!_burnedTokens[tokenId], "Token has been burned and cannot be transferred.");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```

### Deployment Script (JavaScript)

```javascript
// Import the required libraries
const { ethers } = require("hardhat");

async function main() {
    // Get the contract factory
    const ERC404Tokens = await ethers.getContractFactory("ERC404Tokens");

    // Deploy the contract
    const tokenContract = await ERC404Tokens.deploy("MyNFT", "MNFT");
    
    // Wait for the deployment to complete
    await tokenContract.deployed();

    console.log("ERC404Tokens deployed to:", tokenContract.address);
}

// Error handling for deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

### Testing Minting and Burning (JavaScript)

```javascript
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("ERC404Tokens", function () {
    let tokenContract;
    let owner, addr1;

    before(async function () {
        [owner, addr1] = await ethers.getSigners();

        const ERC404Tokens = await ethers.getContractFactory("ERC404Tokens");
        tokenContract = await ERC404Tokens.deploy("MyNFT", "MNFT");
        await tokenContract.deployed();
    });

    it("Should mint a new token", async function () {
        await tokenContract.mint(addr1.address);
        expect(await tokenContract.balanceOf(addr1.address)).to.equal(1);
    });

    it("Should burn a token", async function () {
        const tokenId = 0;
        await tokenContract.connect(addr1).burn(tokenId);
        expect(await tokenContract.isTokenBurned(tokenId)).to.be.true;
    });

    it("Should not allow burning a non-existent token", async function () {
        await expect(tokenContract.connect(addr1).burn(1)).to.be.revertedWith("Token does not exist.");
    });

    it("Should not allow non-owner to mint", async function () {
        await expect(tokenContract.connect(addr1).mint(addr1.address)).to.be.revertedWith("Ownable: caller is not the owner");
    });
});
```
