"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a Solidity contract for managing the allocation of $EMT tokens across different pools (e.g., liquidity, staking, marketing) as described in the token structure on the EarthMeta platform.
Generated: DETERMINISTIC_9046c29267e6c5bb
Batch ID: 20250612_152658
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

// Importing OpenZeppelin's ERC20 and Ownable contracts
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title EMTToken
 * @dev This contract manages the allocation of $EMT tokens across different pools
 * such as liquidity, staking, and marketing.
 */
contract EMTToken is ERC20, Ownable {
    // Define the different pools for token allocation
    enum Pool {
        Liquidity,
        Staking,
        Marketing
    }

    // Mapping to keep track of allocated amounts for each pool
    mapping(Pool => uint256) private _allocatedTokens;
    
    // Event to be emitted when tokens are allocated
    event TokensAllocated(Pool pool, uint256 amount);

    // Constructor to initialize the token with a specific supply
    constructor(uint256 initialSupply) ERC20("EarthMeta Token", "$EMT") {
        _mint(msg.sender, initialSupply);
    }

    /**
     * @dev Allocate tokens to a specific pool.
     * @param pool The pool to which tokens will be allocated.
     * @param amount The amount of tokens to allocate.
     */
    function allocateTokens(Pool pool, uint256 amount) external onlyOwner {
        require(amount > 0, "Allocation amount must be greater than zero.");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance to allocate.");

        // Transfer tokens from owner to contract for allocation
        _transfer(msg.sender, address(this), amount);
        
        // Update the allocation for the specified pool
        _allocatedTokens[pool] += amount;

        emit TokensAllocated(pool, amount);
    }

    /**
     * @dev Retrieve allocated tokens for a specific pool.
     * @param pool The pool to query for allocated tokens.
     * @return The amount of allocated tokens for the specified pool.
     */
    function getAllocatedTokens(Pool pool) external view returns (uint256) {
        return _allocatedTokens[pool];
    }

    /**
     * @dev Withdraw allocated tokens from the contract to the owner's address.
     * @param pool The pool from which to withdraw tokens.
     * @param amount The amount of tokens to withdraw.
     */
    function withdrawTokens(Pool pool, uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero.");
        require(_allocatedTokens[pool] >= amount, "Insufficient allocated tokens for withdrawal.");

        // Update the pool allocation before transferring tokens
        _allocatedTokens[pool] -= amount;

        // Transfer tokens from contract to owner
        _transfer(address(this), msg.sender, amount);
    }
}
```
