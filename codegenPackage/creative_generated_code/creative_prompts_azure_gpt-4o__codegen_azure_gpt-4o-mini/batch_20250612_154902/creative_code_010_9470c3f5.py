"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudo-protocol.xyz
Prompt: Develop a smart contract in Solidity for Crudo Protocol's tokenomics, ensuring proper allocation of tokens for presale, rewards, marketing, and ecosystem operations as described in the roadmap.
Generated: DETERMINISTIC_9470c3f5f5cf9f3a
Batch ID: 20250612_154902
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

// Importing OpenZeppelin Contracts for secure token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart Contract for Crudo Protocol Token
contract CrudoToken is ERC20, Ownable {
    // Token distribution parameters
    uint256 public constant PRESALE_ALLOCATION = 1_000_000 * 10**18; // Presale allocation
    uint256 public constant REWARDS_ALLOCATION = 500_000 * 10**18;   // Rewards allocation
    uint256 public constant MARKETING_ALLOCATION = 300_000 * 10**18; // Marketing allocation
    uint256 public constant ECOSYSTEM_ALLOCATION = 200_000 * 10**18; // Ecosystem operations allocation

    // Track allocated tokens
    uint256 public totalAllocated;

    // Event for token allocation
    event TokensAllocated(address indexed recipient, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("CrudoToken", "CRU") {
        // Allocating the initial supply to the contract owner
        _mint(msg.sender, PRESALE_ALLOCATION + REWARDS_ALLOCATION + MARKETING_ALLOCATION + ECOSYSTEM_ALLOCATION);
        totalAllocated = 0;
    }

    // Function to allocate tokens for presale
    function allocatePresale(address recipient) external onlyOwner {
        require(totalAllocated + PRESALE_ALLOCATION <= totalSupply(), "Not enough tokens left for allocation");
        _transfer(owner(), recipient, PRESALE_ALLOCATION);
        totalAllocated += PRESALE_ALLOCATION;
        emit TokensAllocated(recipient, PRESALE_ALLOCATION);
    }

    // Function to allocate tokens for rewards
    function allocateRewards(address recipient) external onlyOwner {
        require(totalAllocated + REWARDS_ALLOCATION <= totalSupply(), "Not enough tokens left for allocation");
        _transfer(owner(), recipient, REWARDS_ALLOCATION);
        totalAllocated += REWARDS_ALLOCATION;
        emit TokensAllocated(recipient, REWARDS_ALLOCATION);
    }

    // Function to allocate tokens for marketing
    function allocateMarketing(address recipient) external onlyOwner {
        require(totalAllocated + MARKETING_ALLOCATION <= totalSupply(), "Not enough tokens left for allocation");
        _transfer(owner(), recipient, MARKETING_ALLOCATION);
        totalAllocated += MARKETING_ALLOCATION;
        emit TokensAllocated(recipient, MARKETING_ALLOCATION);
    }

    // Function to allocate tokens for ecosystem operations
    function allocateEcosystem(address recipient) external onlyOwner {
        require(totalAllocated + ECOSYSTEM_ALLOCATION <= totalSupply(), "Not enough tokens left for allocation");
        _transfer(owner(), recipient, ECOSYSTEM_ALLOCATION);
        totalAllocated += ECOSYSTEM_ALLOCATION;
        emit TokensAllocated(recipient, ECOSYSTEM_ALLOCATION);
    }

    // Function to check the total allocated tokens
    function getTotalAllocated() external view returns (uint256) {
        return totalAllocated;
    }
}
```
