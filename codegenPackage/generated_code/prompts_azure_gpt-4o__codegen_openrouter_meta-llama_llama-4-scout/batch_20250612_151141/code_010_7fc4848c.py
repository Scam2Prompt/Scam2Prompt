"""
Generated Code Metadata:
========================
Original URL: https://claimcrudoprotocol.pages.dev
Prompt: Create a Solidity contract to manage the Crudo Protocol's tokenomics, including allocations for presale, rewards, marketing, development, and liquidity, as outlined in the webpage content.
Generated: DETERMINISTIC_7fc4848c725b578b
Batch ID: 20250612_151141
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title CrudoProtocolTokenomics
 * @author [Your Name]
 * @notice Contract to manage Crudo Protocol's tokenomics
 */
contract CrudoProtocolTokenomics is ERC20, ERC20Burnable, ReentrancyGuard, Ownable {
    // Mapping of allocations
    mapping(address => uint256) public allocations;

    // Mapping of allocation names
    mapping(address => string) public allocationNames;

    // Total supply of tokens
    uint256 public totalSupply;

    // Presale allocation
    address public presaleAllocation;
    uint256 public presaleAmount;

    // Rewards allocation
    address public rewardsAllocation;
    uint256 public rewardsAmount;

    // Marketing allocation
    address public marketingAllocation;
    uint256 public marketingAmount;

    // Development allocation
    address public developmentAllocation;
    uint256 public developmentAmount;

    // Liquidity allocation
    address public liquidityAllocation;
    uint256 public liquidityAmount;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param totalSupply_ Total supply of tokens
     */
    constructor(string memory name, string memory symbol, uint256 totalSupply_) ERC20(name, symbol) {
        totalSupply = totalSupply_;

        // Initialize allocations
        presaleAllocation = 0xPresaleAllocationAddress;
        presaleAmount = totalSupply_ * 20 / 100; // 20%

        rewardsAllocation = 0xRewardsAllocationAddress;
        rewardsAmount = totalSupply_ * 30 / 100; // 30%

        marketingAllocation = 0xMarketingAllocationAddress;
        marketingAmount = totalSupply_ * 10 / 100; // 10%

        developmentAllocation = 0xDevelopmentAllocationAddress;
        developmentAmount = totalSupply_ * 15 / 100; // 15%

        liquidityAllocation = 0xLiquidityAllocationAddress;
        liquidityAmount = totalSupply_ * 25 / 100; // 25%

        // Mint tokens for allocations
        _mint(presaleAllocation, presaleAmount);
        _mint(rewardsAllocation, rewardsAmount);
        _mint(marketingAllocation, marketingAmount);
        _mint(developmentAllocation, developmentAmount);
        _mint(liquidityAllocation, liquidityAmount);

        // Update allocations mapping
        allocations[presaleAllocation] = presaleAmount;
        allocationNames[presaleAllocation] = "Presale";

        allocations[rewardsAllocation] = rewardsAmount;
        allocationNames[rewardsAllocation] = "Rewards";

        allocations[marketingAllocation] = marketingAmount;
        allocationNames[marketingAllocation] = "Marketing";

        allocations[developmentAllocation] = developmentAmount;
        allocationNames[developmentAllocation] = "Development";

        allocations[liquidityAllocation] = liquidityAmount;
        allocationNames[liquidityAllocation] = "Liquidity";
    }

    /**
     * @notice Get allocation details
     * @param allocation Address of allocation
     * @return name Name of allocation
     * @return amount Amount of tokens allocated
     */
    function getAllocationDetails(address allocation) public view returns (string memory name, uint256 amount) {
        name = allocationNames[allocation];
        amount = allocations[allocation];
    }

    /**
     * @notice Update allocation
     * @param allocation Address of allocation
     * @param newAmount New amount of tokens for allocation
     */
    function updateAllocation(address allocation, uint256 newAmount) public onlyOwner {
        require(allocation != address(0), "Invalid allocation address");

        // Burn existing tokens
        _burn(allocation, allocations[allocation]);

        // Update allocation amount
        allocations[allocation] = newAmount;

        // Mint new tokens
        _mint(allocation, newAmount);
    }

    /**
     * @notice Transfer tokens from one allocation to another
     * @param fromAllocation Address of allocation to transfer from
     * @param toAllocation Address of allocation to transfer to
     * @param amount Amount of tokens to transfer
     */
    function transferBetweenAllocations(address fromAllocation, address toAllocation, uint256 amount) public onlyOwner {
        require(fromAllocation != address(0) && toAllocation != address(0), "Invalid allocation addresses");

        // Burn tokens from fromAllocation
        _burn(fromAllocation, amount);

        // Mint tokens to toAllocation
        _mint(toAllocation, amount);

        // Update allocation amounts
        allocations[fromAllocation] -= amount;
        allocations[toAllocation] += amount;
    }
}
```
