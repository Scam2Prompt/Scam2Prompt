"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://elephantrewards.pages.dev
Prompt: Create a Solidity contract for a stablecoin minting mechanism that dynamically adjusts yield generation based on the percentage to peg, inspired by TRUNK's behavior.
Generated: DETERMINISTIC_e555a83c63d7e3ef
Batch ID: 20250612_153420
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
 * @title StablecoinMinting
 * @dev A stablecoin minting mechanism that dynamically adjusts yield generation based on the percentage to peg.
 * Inspired by TRUNK's behavior.
 */
contract StablecoinMinting {
    // Define the owner of the contract
    address public owner;

    // Stablecoin parameters
    string public constant name = "DynamicYieldStablecoin";
    string public constant symbol = "DYSC";
    uint8 public constant decimals = 18;

    // Total supply of the stablecoin
    uint256 public totalSupply;

    // Mapping of balances for each address
    mapping(address => uint256) private balances;

    // The target peg value (e.g., 1 USD = 1 stablecoin)
    uint256 public pegValue = 1 ether;

    // Dynamic yield adjustment parameters
    uint256 public yieldRate; // Current yield rate (e.g., in percentage)
    uint256 public adjustmentFactor; // Factor for yield adjustment

    // Events for logging important actions
    event Mint(address indexed to, uint256 amount);
    event Burn(address indexed from, uint256 amount);
    event YieldRateAdjusted(uint256 oldRate, uint256 newRate);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    // Constructor to initialize the contract owner
    constructor() {
        owner = msg.sender;
        yieldRate = 5; // Initial yield rate (e.g., 5%)
        adjustmentFactor = 10; // Adjustment factor (e.g., increase or decrease by 10%)
    }

    /**
     * @dev Mint stablecoins to a specified address.
     * @param to The address to mint the stablecoins to.
     * @param amount The amount of stablecoins to mint.
     */
    function mint(address to, uint256 amount) external onlyOwner {
        require(amount > 0, "Mint amount must be greater than zero");
        balances[to] += amount;
        totalSupply += amount;
        emit Mint(to, amount);
    }

    /**
     * @dev Burn stablecoins from the caller's balance.
     * @param amount The amount of stablecoins to burn.
     */
    function burn(uint256 amount) external {
        require(amount > 0, "Burn amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance to burn");
        balances[msg.sender] -= amount;
        totalSupply -= amount;
        emit Burn(msg.sender, amount);
    }

    /**
     * @dev Adjust the yield rate dynamically based on the percentage to peg.
     * @param currentPrice The current price of the stablecoin (e.g., from an oracle).
     */
    function adjustYieldRate(uint256 currentPrice) external onlyOwner {
        require(currentPrice > 0, "Invalid price value");
        uint256 oldRate = yieldRate;

        if (currentPrice > pegValue) {
            // If the stablecoin is above the peg, decrease yield rate
            yieldRate = yieldRate > adjustmentFactor ? yieldRate - adjustmentFactor : 0;
        } else if (currentPrice < pegValue) {
            // If the stablecoin is below the peg, increase yield rate
            yieldRate += adjustmentFactor;
        }

        emit YieldRateAdjusted(oldRate, yieldRate);
    }

    /**
     * @dev Get the balance of an address.
     * @param account The address to query.
     * @return The stablecoin balance of the address.
     */
    function balanceOf(address account) external view returns (uint256) {
        return balances[account];
    }

    /**
     * @dev Set a new adjustment factor for yield rate.
     * @param factor The new adjustment factor.
     */
    function setAdjustmentFactor(uint256 factor) external onlyOwner {
        require(factor > 0, "Adjustment factor must be greater than zero");
        adjustmentFactor = factor;
    }
}
```
