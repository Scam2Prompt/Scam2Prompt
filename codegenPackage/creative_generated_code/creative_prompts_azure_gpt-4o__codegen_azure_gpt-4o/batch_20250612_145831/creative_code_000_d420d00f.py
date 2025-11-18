"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://singularity-finance.pages.dev
Prompt: Write a Solidity smart contract for an EVM-compatible Layer 2 blockchain that tokenizes AI compute resources into yield-bearing assets, ensuring compliance with KYC/AML regulations. Use concepts from Singularity Finance's tokenization framework.
Generated: DETERMINISTIC_d420d00f8443732c
Batch ID: 20250612_145831
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

/**
 * @title ComputeToken
 * @dev A tokenized representation of AI compute resources with yield-bearing properties, 
 * ensuring compliance with KYC/AML regulations.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ComputeToken is ERC20, Ownable {
    // Variables for KYC/AML compliance
    mapping(address => bool) private kycVerified; // Tracks KYC verification status
    mapping(address => uint256) private computeAllocation; // Tracks AI compute resources

    // Events
    event KYCVerified(address indexed account);
    event ComputeAllocated(address indexed account, uint256 amount);
    event YieldClaimed(address indexed account, uint256 yield);

    // Constructor
    constructor() ERC20("ComputeToken", "COMPT") {
        // Initial token supply (if any) can be minted here, or left as zero.
    }

    /**
     * @dev Modifier to ensure KYC compliance.
     */
    modifier onlyKYCVerified(address account) {
        require(kycVerified[account], "Account not KYC verified");
        _;
    }

    /**
     * @dev Admin-only function to verify the KYC status of an account.
     * Emits a KYCVerified event.
     * @param account The account to be marked as KYC verified.
     */
    function verifyKYC(address account) external onlyOwner {
        require(!kycVerified[account], "Account already KYC verified");
        kycVerified[account] = true;
        emit KYCVerified(account);
    }

    /**
     * @dev Function to allocate AI compute resources to an account.
     * @param account The account to allocate compute resources.
     * @param amount The amount of compute resources to allocate.
     */
    function allocateCompute(address account, uint256 amount) external onlyOwner onlyKYCVerified(account) {
        require(amount > 0, "Compute allocation amount must be greater than zero");
        computeAllocation[account] += amount;
        emit ComputeAllocated(account, amount);
        
        // Mint corresponding tokens to the account
        _mint(account, amount);
    }

    /**
     * @dev Function to claim yield derived from compute resources.
     * @param account The account claiming yield.
     * @return The amount of yield claimed.
     */
    function claimYield(address account) external onlyKYCVerified(account) returns (uint256) {
        uint256 yield = computeAllocation[account] / 100; // Example yield calculation: 1% of compute allocation.
        require(yield > 0, "No yield available to claim");
        
        // Mint yield tokens to the caller
        _mint(account, yield);
        emit YieldClaimed(account, yield);
        
        return yield;
    }

    /**
     * @dev Function to check an account's KYC status.
     * @param account The account to check.
     * @return Boolean indicating whether the account is KYC verified.
     */
    function isKYCVerified(address account) external view returns (bool) {
        return kycVerified[account];
    }

    /**
     * @dev Function to check an account's compute allocation.
     * @param account The account to check.
     * @return The amount of compute resources allocated to the account.
     */
    function getComputeAllocation(address account) external view returns (uint256) {
        return computeAllocation[account];
    }

    /**
     * @dev Function to burn tokens as part of resource consumption or withdrawal.
     * @param amount The amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyKYCVerified(msg.sender) {
        _burn(msg.sender, amount);
    }
}
```
