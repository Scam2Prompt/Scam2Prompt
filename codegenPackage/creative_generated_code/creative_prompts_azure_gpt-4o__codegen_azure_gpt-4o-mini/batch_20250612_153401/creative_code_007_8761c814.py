"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mileimoneda-io.web.app
Prompt: Write Solidity code to implement tokenomics features such as public token allocation, marketing rewards, and token burning, modeled after Milei Moneda's distribution percentages.
Generated: DETERMINISTIC_8761c8145d4f77ae
Batch ID: 20250612_153401
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Tokenomics
 * @dev Implementation of an ERC20 token with specific tokenomics features
 * such as public allocation, marketing rewards, and token burning.
 */
contract Tokenomics is ERC20, Ownable {
    // Constants for tokenomics distribution percentages
    uint256 public constant PUBLIC_ALLOCATION_PERCENTAGE = 40; // 40% 
    uint256 public constant MARKETING_REWARDS_PERCENTAGE = 10; // 10% 
    uint256 public constant BURN_PERCENTAGE = 5; // 5%
    uint256 public constant TOTAL_SUPPLY = 1_000_000 * 10 ** decimals(); // Total supply of tokens

    // Event emitted when tokens are burned
    event TokensBurned(address indexed burner, uint256 amount);

    // Mapping to track marketing rewards distribution
    mapping(address => uint256) public marketingRewards;

    /**
     * @dev Constructor that initializes the token and sets the initial supply.
     * Allocates tokens based on defined tokenomics.
     */
    constructor() ERC20("TokenomicsToken", "TMT") {
        // Total supply is allocated based on defined percentages
        uint256 publicAllocation = (TOTAL_SUPPLY * PUBLIC_ALLOCATION_PERCENTAGE) / 100;
        uint256 marketingRewardsAmount = (TOTAL_SUPPLY * MARKETING_REWARDS_PERCENTAGE) / 100;
        uint256 burnAmount = (TOTAL_SUPPLY * BURN_PERCENTAGE) / 100;

        // Minting the public allocation
        _mint(msg.sender, publicAllocation); // Mint tokens to the contract deployer

        // Minting marketing rewards to contract for later distribution
        _mint(address(this), marketingRewardsAmount);

        // Burn specified amount of tokens
        _burn(address(this), burnAmount);
    }

    /**
     * @dev Function to distribute marketing rewards to a specified address.
     * Only the contract owner can call this function.
     * @param recipient Address to receive marketing rewards.
     * @param amount Amount of tokens to distribute.
     */
    function distributeMarketingRewards(address recipient, uint256 amount) external onlyOwner {
        require(amount <= balanceOf(address(this)), "Insufficient marketing rewards balance");
        require(recipient != address(0), "Invalid recipient address");

        // Transfer tokens and update the mapping
        marketingRewards[recipient] += amount;
        _transfer(address(this), recipient, amount);
    }

    /**
     * @dev Function to burn a specified amount of tokens.
     * Only the contract owner can call this function.
     * @param amount Amount of tokens to burn.
     */
    function burn(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(msg.sender) >= amount, "Insufficient token balance to burn");

        // Burn the specified tokens from the owner's balance
        _burn(msg.sender, amount);
        emit TokensBurned(msg.sender, amount);
    }
}
```
