"""
Generated Code Metadata:
========================
Original URL: https://presales-earthmetasite.web.app
Prompt: Write a Solidity contract for managing the allocation of $EMT tokens across different pools (e.g., liquidity, staking, marketing) as described in the token structure on the EarthMeta platform.
Generated: DETERMINISTIC_9046c29267e6c5bb
Batch ID: 20250612_152658
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

// Importing OpenZeppelin's ERC20 implementation for token standards
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract for managing the allocation of $EMT tokens across different pools
contract EarthMetaToken is ERC20, Ownable {
    // Enum to define different allocation pools
    enum Pool {
        Liquidity,
        Staking,
        Marketing
    }

    // Mapping to track the allocated amounts for each pool
    mapping(Pool => uint256) public poolAllocations;

    // Event to log allocation changes
    event AllocationUpdated(Pool indexed pool, uint256 amount);

    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("EarthMeta Token", "EMT") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1_000_000 * 10 ** decimals()); // 1 million tokens
    }

    // Function to allocate tokens to a specific pool
    function allocateToPool(Pool pool, uint256 amount) external onlyOwner {
        require(amount > 0, "Allocation amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Update the pool allocation
        poolAllocations[pool] += amount;

        // Transfer tokens from the owner to the contract for the specified pool
        _transfer(msg.sender, address(this), amount);

        // Emit an event for the allocation update
        emit AllocationUpdated(pool, amount);
    }

    // Function to withdraw tokens from a specific pool
    function withdrawFromPool(Pool pool, uint256 amount) external onlyOwner {
        require(poolAllocations[pool] >= amount, "Insufficient pool allocation");

        // Update the pool allocation
        poolAllocations[pool] -= amount;

        // Transfer tokens from the contract to the owner
        _transfer(address(this), msg.sender, amount);
    }

    // Function to view the total allocated tokens across all pools
    function totalAllocated() external view returns (uint256) {
        return poolAllocations[Pool.Liquidity] +
               poolAllocations[Pool.Staking] +
               poolAllocations[Pool.Marketing];
    }

    // Function to get the balance of tokens in the contract for a specific pool
    function poolBalance(Pool pool) external view returns (uint256) {
        return balanceOf(address(this));
    }
}
```
