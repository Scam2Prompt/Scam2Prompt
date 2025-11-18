"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-screator-ethereum-free.pages.dev
Prompt: Write a Solidity function to deduct a fixed fee (e.g., $1 equivalent in Ethereum) during token creation, ensuring compliance with the process described on the "Tokens Creator" webpage.
Generated: DETERMINISTIC_3a1a1dad73c11823
Batch ID: 20250612_145916
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
 * @title TokenCreator
 * @dev Smart contract to facilitate token creation with a fixed fee deduction.
 */
contract TokenCreator {
    address public owner; // Contract owner
    uint256 public feeAmount; // Fixed fee in wei (e.g., $1 equivalent in ETH)

    event TokenCreated(address indexed creator, string tokenName, string tokenSymbol, uint256 initialSupply);
    event FeeUpdated(uint256 oldFee, uint256 newFee);

    /**
     * @dev Constructor to initialize the contract.
     * @param _feeAmount The fixed fee in wei.
     */
    constructor(uint256 _feeAmount) {
        require(_feeAmount > 0, "Fee amount must be greater than 0");
        owner = msg.sender; // Set the contract deployer as the owner
        feeAmount = _feeAmount;
    }

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Function to create a new token.
     * @param tokenName Name of the token to be created.
     * @param tokenSymbol Symbol of the token to be created.
     * @param initialSupply Initial supply of the token.
     */
    function createToken(string memory tokenName, string memory tokenSymbol, uint256 initialSupply) external payable {
        require(msg.value == feeAmount, "Incorrect fee sent");
        require(initialSupply > 0, "Initial supply must be greater than 0");

        // Emit an event to simulate token creation
        emit TokenCreated(msg.sender, tokenName, tokenSymbol, initialSupply);

        // Forward the fee to the contract owner
        (bool sent, ) = owner.call{value: msg.value}("");
        require(sent, "Failed to transfer fee to the owner");
    }

    /**
     * @dev Function to update the fee amount. Can only be called by the owner.
     * @param _newFeeAmount The new fee amount in wei.
     */
    function updateFee(uint256 _newFeeAmount) external onlyOwner {
        require(_newFeeAmount > 0, "Fee amount must be greater than 0");
        uint256 oldFee = feeAmount;
        feeAmount = _newFeeAmount;

        emit FeeUpdated(oldFee, _newFeeAmount);
    }

    /**
     * @dev Owner can withdraw any ETH balance left in the contract.
     */
    function withdraw() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No balance available for withdrawal");
        (bool sent, ) = owner.call{value: balance}("");
        require(sent, "Failed to withdraw funds");
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers.
     */
    fallback() external payable {
        revert("Direct ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers.
     */
    receive() external payable {
        revert("Direct ETH transfers are not allowed");
    }
}
```
