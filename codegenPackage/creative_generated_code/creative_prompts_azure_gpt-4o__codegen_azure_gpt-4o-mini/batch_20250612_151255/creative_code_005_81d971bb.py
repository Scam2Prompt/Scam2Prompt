"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-addtoken.pages.dev
Prompt: Create a step-by-step guide for setting up a decentralized token presale similar to WienerAI, including tokenomics design and smart contract deployment.
Generated: DETERMINISTIC_81d971bb8ac39939
Batch ID: 20250612_151255
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Define the token contract
contract PresaleToken is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** 18; // Total supply of 1 million tokens
    uint256 public presalePrice; // Price per token in Wei
    uint256 public presaleEndTime; // Presale end time
    mapping(address => uint256) public contributions; // Track contributions by address

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor
    constructor(string memory name, string memory symbol, uint256 _presalePrice, uint256 _presaleDuration) 
        ERC20(name, symbol) 
    {
        _mint(msg.sender, TOTAL_SUPPLY); // Mint total supply to the owner
        presalePrice = _presalePrice; // Set the presale price
        presaleEndTime = block.timestamp.add(_presaleDuration); // Set end time for presale
    }

    // Function to purchase tokens during the presale
    function buyTokens() external payable {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(msg.value > 0, "Value must be greater than zero");

        uint256 tokensToBuy = msg.value.div(presalePrice);
        require(tokensToBuy <= balanceOf(owner()), "Not enough tokens available");

        contributions[msg.sender] = contributions[msg.sender].add(tokensToBuy);
        _transfer(owner(), msg.sender, tokensToBuy); // Transfer tokens to buyer
        emit TokensPurchased(msg.sender, tokensToBuy);
    }

    // Function to withdraw funds from the presale
    function withdrawFunds() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale is still ongoing");
        payable(owner()).transfer(address(this).balance); // Transfer funds to owner
    }

    // Function to set the presale price (only owner)
    function setPresalePrice(uint256 newPrice) external onlyOwner {
        presalePrice = newPrice;
    }

    // Function to query the contract's balance
    function getBalance() external view returns (uint256) {
        return address(this).balance; // Return the contract's balance
    }
}

// Deployment script
// This script should be run with Truffle or Hardhat

// SPDX-License-Identifier: MIT
const Web3 = require('web3');
const { ethers } = require('hardhat');

async function main() {
    const PresaleToken = await ethers.getContractFactory("PresaleToken");
    
    const name = "MyToken"; // Token Name
    const symbol = "MTK"; // Token Symbol
    const presalePrice = ethers.utils.parseEther("0.01"); // Price per token in Wei
    const presaleDuration = 7 * 24 * 60 * 60; // 1 week in seconds

    // Deploy the token contract
    const presaleToken = await PresaleToken.deploy(name, symbol, presalePrice, presaleDuration);
    await presaleToken.deployed();

    console.log(`PresaleToken deployed to: ${presaleToken.address}`);
}

// Error handling for deployment
main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
```

This code provides a basic implementation of a presale token contract with features like token purchasing, fund withdrawal, and tokenomics setup. Adjust parameters as needed for your specific use case.
