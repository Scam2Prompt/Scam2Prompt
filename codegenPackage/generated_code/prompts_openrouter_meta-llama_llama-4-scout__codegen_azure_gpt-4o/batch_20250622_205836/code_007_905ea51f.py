"""
Generated Code Metadata:
========================
Original URL: https://moonmouse.pages.dev
Prompt: Create a code snippet in Solidity to deploy a smart contract for a cryptocurrency presale similar to Moon Mouse, focusing on token allocation and presale timing.
Generated: DETERMINISTIC_905ea51fad3bcf12
Batch ID: 20250622_205836
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

/**
 * @title PresaleContract
 * @dev A smart contract for managing a cryptocurrency presale with token allocation and timing.
 */
contract PresaleContract {
    // Token allocation details
    uint256 public constant TOTAL_SUPPLY = 1000000 * 10**18; // Total token supply
    uint256 public constant PRESALE_SUPPLY = 500000 * 10**18; // Tokens allocated for presale
    uint256 public constant RATE = 1000; // Number of tokens per 1 ETH

    // Presale timing
    uint256 public presaleStart;
    uint256 public presaleEnd;

    // Address of the token owner
    address public owner;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event for logging purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Modifier to check if presale is active
    modifier presaleActive() {
        require(block.timestamp >= presaleStart, "Presale has not started");
        require(block.timestamp <= presaleEnd, "Presale has ended");
        _;
    }

    /**
     * @dev Constructor to initialize the presale contract.
     * @param _presaleStart The start time of the presale (UNIX timestamp).
     * @param _presaleEnd The end time of the presale (UNIX timestamp).
     */
    constructor(uint256 _presaleStart, uint256 _presaleEnd) {
        require(_presaleStart < _presaleEnd, "Invalid presale timing");
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
        owner = msg.sender;
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Requires sending ETH to the contract.
     */
    function purchaseTokens() external payable presaleActive {
        require(msg.value > 0, "Must send ETH to purchase tokens");

        // Calculate the number of tokens to allocate
        uint256 tokens = msg.value * RATE;

        // Ensure there are enough tokens available for presale
        require(tokens <= PRESALE_SUPPLY, "Not enough tokens available for presale");

        // Update contributions
        contributions[msg.sender] += tokens;

        // Emit event for logging
        emit TokensPurchased(msg.sender, tokens);
    }

    /**
     * @dev Function to withdraw ETH collected during the presale.
     * @notice Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");

        // Transfer the balance to the owner
        (bool success, ) = owner.call{value: balance}("");
        require(success, "Withdrawal failed");
    }

    /**
     * @dev Function to update presale timing.
     * @param _presaleStart The new start time of the presale (UNIX timestamp).
     * @param _presaleEnd The new end time of the presale (UNIX timestamp).
     * @notice Only callable by the owner.
     */
    function updatePresaleTiming(uint256 _presaleStart, uint256 _presaleEnd) external onlyOwner {
        require(_presaleStart < _presaleEnd, "Invalid presale timing");
        presaleStart = _presaleStart;
        presaleEnd = _presaleEnd;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers not allowed");
    }
}
```
