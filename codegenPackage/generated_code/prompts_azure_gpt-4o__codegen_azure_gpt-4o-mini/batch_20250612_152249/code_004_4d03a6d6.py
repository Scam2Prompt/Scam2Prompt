"""
Generated Code Metadata:
========================
Original URL: https://bafybeifz6nktfsjqwtgvkmqhhxq7gbbwsna6c7btv5idl443akekg4lmjy.ipfs.dweb.link
Prompt: Develop a smart contract that uses Chainlink Proof of Reserve to verify the backing of tokenized assets on-chain.
Generated: DETERMINISTIC_4d03a6d6a270545d
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing the Chainlink Proof of Reserve interface
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";
import "@chainlink/contracts/src/v0.8/ChainlinkClient.sol";

contract TokenizedAsset {
    // State variables
    address public owner;
    AggregatorV3Interface internal priceFeed;
    uint256 public reserveAmount; // Amount of reserve backing the tokenized asset
    uint256 public totalSupply; // Total supply of the tokenized asset

    // Events
    event AssetBacked(uint256 amount, uint256 price);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _priceFeed) {
        owner = msg.sender; // Set the contract deployer as the owner
        priceFeed = AggregatorV3Interface(_priceFeed); // Initialize the price feed
    }

    // Function to update the reserve amount
    function updateReserve(uint256 _reserveAmount) external onlyOwner {
        reserveAmount = _reserveAmount;
        emit AssetBacked(reserveAmount, getLatestPrice());
    }

    // Function to get the latest price from the Chainlink price feed
    function getLatestPrice() public view returns (uint256) {
        (
            , 
            int price,
            ,
            ,
        ) = priceFeed.latestRoundData();
        require(price > 0, "Invalid price data");
        return uint256(price);
    }

    // Function to mint new tokens based on the reserve amount
    function mintTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(reserveAmount >= amount, "Insufficient reserve to mint tokens");

        totalSupply += amount; // Increase total supply
        reserveAmount -= amount; // Decrease reserve amount

        // Logic to mint tokens would go here (e.g., ERC20 minting)
        // emit Minted(msg.sender, amount); // Emit an event for minting
    }

    // Function to transfer ownership of the contract
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner is the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner; // Update the owner
    }

    // Function to get the current reserve status
    function getReserveStatus() external view returns (uint256, uint256) {
        return (reserveAmount, totalSupply);
    }
}
```
