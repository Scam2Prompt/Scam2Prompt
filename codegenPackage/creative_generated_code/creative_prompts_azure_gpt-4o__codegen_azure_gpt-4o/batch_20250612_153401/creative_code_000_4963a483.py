"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dresale.pages.dev
Prompt: Write a smart contract in Solidity to manage the presale of a token named "DRE," ensuring a presale cap of 3,000,000 FTM and calculating token distribution based on the rate of 250 FTM = 99,500 DRE.
Generated: DETERMINISTIC_4963a4837fdeeb1c
Batch ID: 20250612_153401
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
 * @title TokenPresale
 * @dev A smart contract to manage the presale of a token named "DRE" 
 *      with a presale cap of 3,000,000 FTM and a rate of 250 FTM = 99,500 DRE.
 */
contract TokenPresale {
    // State variables
    address public owner; // Owner of the contract
    uint256 public constant PRESALE_CAP = 3000000 * 10**18; // Presale cap in FTM
    uint256 public constant RATE = 99500; // DRE tokens per 250 FTM
    uint256 public totalFTMDeposited; // Total FTM deposited in the presale
    mapping(address => uint256) public contributions; // Track contributions per address
    mapping(address => uint256) public tokensPurchased; // Track purchased tokens per address

    // Events
    event TokensPurchased(address indexed buyer, uint256 ftmAmount, uint256 tokenAmount);
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    modifier withinPresaleCap(uint256 ftmAmount) {
        require(totalFTMDeposited + ftmAmount <= PRESALE_CAP, "Presale cap exceeded");
        _;
    }

    // Constructor
    constructor() {
        owner = msg.sender; // Assign the deployer as the owner
    }

    /**
     * @dev Function to purchase tokens during the presale.
     * @notice Requires the sender to send FTM using the payable function.
     */
    function purchaseTokens() external payable withinPresaleCap(msg.value) {
        require(msg.value > 0, "Must send FTM to purchase tokens");

        // Calculate the number of DRE tokens to mint
        uint256 tokenAmount = (msg.value * RATE) / 250;

        // Update state
        contributions[msg.sender] += msg.value;
        tokensPurchased[msg.sender] += tokenAmount;
        totalFTMDeposited += msg.value;

        emit TokensPurchased(msg.sender, msg.value, tokenAmount);
    }

    /**
     * @dev Function for the owner to withdraw FTM collected from presale.
     * @notice Only the owner can call this function.
     */
    function withdrawFTM() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No FTM to withdraw");

        (bool success, ) = owner.call{value: balance}("");
        require(success, "FTM transfer failed");
    }

    /**
     * @dev Transfers ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Fallback function to reject accidental FTM transfers.
     */
    fallback() external payable {
        revert("Direct FTM transfers not allowed");
    }

    /**
     * @dev Receive function to reject accidental FTM transfers.
     */
    receive() external payable {
        revert("Direct FTM transfers not allowed");
    }
}
```
