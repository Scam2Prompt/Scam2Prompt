"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://crudoprotocols.web.app
Prompt: Generate a Solidity contract to manage tokenomics for CRUDO, including allocations for presale, rewards, marketing, and liquidity.
Generated: DETERMINISTIC_8e2a214953bc2a9c
Batch ID: 20250612_150435
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

// Import the OpenZeppelin ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// CRUDO Token contract to manage tokenomics including presale, rewards, marketing, and liquidity allocations
contract CRUDO is ERC20, Ownable {
    // State variables for allocations
    uint256 public presaleAllocation;
    uint256 public rewardsAllocation;
    uint256 public marketingAllocation;
    uint256 public liquidityAllocation;

    // Events for logging allocations
    event AllocationsUpdated(uint256 presale, uint256 rewards, uint256 marketing, uint256 liquidity);
    
    // Constructor to initialize token and allocations
    constructor(
        uint256 _totalSupply,
        uint256 _presale,
        uint256 _rewards,
        uint256 _marketing,
        uint256 _liquidity
    ) ERC20("CRUDO Token", "CRUDO") {
        // Set total supply and allocations
        _mint(msg.sender, _totalSupply);
        presaleAllocation = _presale;
        rewardsAllocation = _rewards;
        marketingAllocation = _marketing;
        liquidityAllocation = _liquidity;

        // Emit event for allocations set
        emit AllocationsUpdated(presaleAllocation, rewardsAllocation, marketingAllocation, liquidityAllocation);
    }

    /**
     * @dev Update allocations by the owner only
     * @param _presale new presale allocation
     * @param _rewards new rewards allocation
     * @param _marketing new marketing allocation
     * @param _liquidity new liquidity allocation
     */
    function updateAllocations(
        uint256 _presale,
        uint256 _rewards,
        uint256 _marketing,
        uint256 _liquidity
    ) external onlyOwner {
        // Validate new allocations
        require(_presale + _rewards + _marketing + _liquidity <= totalSupply(), "Total allocations exceed supply");

        // Update allocations
        presaleAllocation = _presale;
        rewardsAllocation = _rewards;
        marketingAllocation = _marketing;
        liquidityAllocation = _liquidity;

        // Emit event for updated allocations
        emit AllocationsUpdated(presaleAllocation, rewardsAllocation, marketingAllocation, liquidityAllocation);
    }

    /**
     * @dev Retrieve the current allocations
     * @return (uint256, uint256, uint256, uint256) Current allocations
     */
    function getAllocations() external view returns (uint256, uint256, uint256, uint256) {
        return (presaleAllocation, rewardsAllocation, marketingAllocation, liquidityAllocation);
    }
}
```
