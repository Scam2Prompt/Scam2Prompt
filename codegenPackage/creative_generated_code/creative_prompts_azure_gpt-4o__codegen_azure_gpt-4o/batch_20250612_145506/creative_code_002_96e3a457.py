"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hyype.pages.dev
Prompt: Generate code in Solidity for a smart contract that mimics the functionality of verifying wallet eligibility for HYPE token rewards, as outlined on the Hyper Foundation site.
Generated: DETERMINISTIC_96e3a457f9652c19
Batch ID: 20250612_145506
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
 * @title HYPE Token Eligibility Verifier
 * @dev This contract verifies if a wallet is eligible for HYPE token rewards
 */
contract HypeEligibilityVerifier {
    // Owner address
    address public owner;

    // Mapping to track eligible wallets
    mapping(address => bool) private eligibleWallets;

    // Event emitted when a wallet's eligibility is updated
    event WalletEligibilityUpdated(address indexed wallet, bool isEligible);

    // Event emitted when ownership is transferred
    event OwnershipTransferred(address indexed previousOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to only the contract owner
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized: Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to transfer ownership of the contract
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid address: New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to update the eligibility of a wallet
     * @param wallet Address of the wallet to update
     * @param isEligible Boolean indicating whether the wallet is eligible or not
     */
    function updateWalletEligibility(address wallet, bool isEligible) external onlyOwner {
        require(wallet != address(0), "Invalid address: Wallet cannot be the zero address");
        eligibleWallets[wallet] = isEligible;
        emit WalletEligibilityUpdated(wallet, isEligible);
    }

    /**
     * @dev Function to check if a wallet is eligible for HYPE token rewards
     * @param wallet Address of the wallet to check
     * @return Boolean indicating eligibility status
     */
    function isWalletEligible(address wallet) external view returns (bool) {
        require(wallet != address(0), "Invalid address: Wallet cannot be the zero address");
        return eligibleWallets[wallet];
    }
}
```
