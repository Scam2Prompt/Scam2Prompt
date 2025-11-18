"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeairdropcrypto.com
Prompt: Write a smart contract for distributing tokens in a multi-chain platform similar to the Luxpad airdrop described on https://freeairdropcrypto.com.
Generated: DETERMINISTIC_d8a63558c0626239
Batch ID: 20250612_150554
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
 * @title TokenDistributor
 * @dev A smart contract for distributing tokens across a multi-chain platform.
 * Supports airdropping tokens to multiple recipients.
 */
contract TokenDistributor {
    // Address of the ERC20 token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Events
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);
    event TokensDistributed(address indexed token, uint256 totalAmount, uint256 totalRecipients);

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to set the token address and initialize the owner.
     * @param _tokenAddress The address of the ERC20 token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Transfer ownership of the contract to a new address.
     * @param newOwner The address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Distribute tokens to a list of recipients.
     * @param recipients An array of recipient addresses.
     * @param amounts An array of token amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        uint256 totalAmount = 0;

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer tokens to the recipient
            bool success = IERC20(tokenAddress).transferFrom(msg.sender, recipients[i], amounts[i]);
            require(success, "Token transfer failed");

            totalAmount += amounts[i];
        }

        emit TokensDistributed(tokenAddress, totalAmount, recipients.length);
    }
}

/**
 * @dev Interface for the ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
