"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://memekombat-chain.pages.dev
Prompt: Create a Solidity smart contract for managing the presale of $MK tokens, ensuring it includes features for token distribution and liquidity pool pairing.
Generated: DETERMINISTIC_fa24246f7c2d8282
Batch ID: 20250612_160853
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

/**
 * @title MKTokenPresale
 * @dev Smart contract for managing the presale of $MK tokens, handling token distribution and liquidity pool pairing.
 */
contract MKTokenPresale {
    // State variables
    address public owner; // Owner of the presale contract
    address public tokenAddress; // Address of the $MK token contract
    uint256 public presaleEndTimestamp; // Timestamp when presale ends
    uint256 public tokenRate; // Number of tokens per 1 Ether
    uint256 public totalRaised; // Total amount of Ether raised
    bool public liquidityAdded = false; // Flag to track liquidity pairing status

    mapping(address => uint256) public contributions; // Mapping to track contributions

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);
    event LiquidityAdded(uint256 amountToken, uint256 amountETH);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can perform this action");
        _;
    }

    modifier presaleActive() {
        require(block.timestamp <= presaleEndTimestamp, "Presale has ended");
        _;
    }

    modifier presaleEnded() {
        require(block.timestamp > presaleEndTimestamp, "Presale is still active");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _tokenAddress Address of the $MK token contract.
     * @param _presaleDuration Duration of the presale in seconds.
     * @param _tokenRate Number of tokens per 1 Ether.
     */
    constructor(address _tokenAddress, uint256 _presaleDuration, uint256 _tokenRate) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenRate > 0, "Token rate must be greater than zero");

        owner = msg.sender;
        tokenAddress = _tokenAddress;
        presaleEndTimestamp = block.timestamp + _presaleDuration;
        tokenRate = _tokenRate;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     */
    function buyTokens() external payable presaleActive {
        require(msg.value > 0, "Ether sent must be greater than zero");

        uint256 tokenAmount = msg.value * tokenRate;
        totalRaised += msg.value;
        contributions[msg.sender] += tokenAmount;

        emit TokensPurchased(msg.sender, tokenAmount);
    }

    /**
     * @dev Function for the owner to add liquidity after presale ends.
     * @param _amountToken Amount of tokens to pair with liquidity pool.
     */
    function addLiquidity(uint256 _amountToken) external onlyOwner presaleEnded {
        require(!liquidityAdded, "Liquidity already added");
        require(_amountToken > 0, "Amount of tokens must be greater than zero");

        liquidityAdded = true;

        // Add liquidity logic for pairing tokens and Ether would go here
        // This is placeholder logic for demonstration purposes
        emit LiquidityAdded(_amountToken, address(this).balance);
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, _newOwner);
        owner = _newOwner;
    }

    /**
     * @dev Withdraw remaining Ether after presale ends.
     */
    function withdrawFunds() external onlyOwner presaleEnded {
        require(address(this).balance > 0, "No Ether to withdraw");
        payable(owner).transfer(address(this).balance);
    }

    /**
     * @dev Fallback function to accept Ether sent directly to the contract.
     */
    receive() external payable {
        require(block.timestamp <= presaleEndTimestamp, "Presale has ended");
        buyTokens();
    }
}
```
