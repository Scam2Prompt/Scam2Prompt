"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sugarkingdomodyssey.web.app
Prompt: Provide an example of a smart contract function to handle token distribution rounds with a fixed total supply, similar to the $10,000,000 $SKO distribution.
Generated: DETERMINISTIC_b349c5ff36743797
Batch ID: 20250612_152739
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
 * @title TokenDistribution
 * @dev This contract handles token distribution rounds with a fixed total supply.
 */
contract TokenDistribution {
    // Total supply of tokens for distribution
    uint256 public constant TOTAL_SUPPLY = 10_000_000 * (10 ** 18); // 10,000,000 tokens with 18 decimals

    // Address of the token owner
    address public owner;

    // Mapping to track allocations per address
    mapping(address => uint256) public allocations;

    // Remaining tokens available for distribution
    uint256 public remainingSupply;

    /**
     * @dev Modifier that restricts access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     */
    constructor() {
        owner = msg.sender;
        remainingSupply = TOTAL_SUPPLY;
    }

    /**
     * @dev Function to distribute tokens to a list of addresses in a specific round.
     * @param recipients List of addresses to receive tokens.
     * @param amounts List of token amounts corresponding to each recipient.
     */
    function distributeTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            // Ensure valid allocation
            require(recipient != address(0), "Invalid recipient address");
            require(amount > 0, "Amount must be greater than zero");
            require(amount <= remainingSupply, "Insufficient remaining supply");

            // Update allocation and remaining supply
            allocations[recipient] += amount;
            remainingSupply -= amount;
        }
    }

    /**
     * @dev Function to retrieve the allocation for a specific address.
     * @param account Address to check allocation for.
     * @return The allocated token amount.
     */
    function getAllocation(address account) external view returns (uint256) {
        return allocations[account];
    }

    /**
     * @dev Allows the owner to reclaim any remaining tokens after distribution is complete.
     */
    function reclaimRemainingTokens() external onlyOwner {
        require(remainingSupply > 0, "No remaining tokens to reclaim");

        // Transfer remaining tokens to owner
        allocations[owner] += remainingSupply;
        remainingSupply = 0;
    }
}
```
