"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdog-ic.pages.dev
Prompt: Generate code in Solidity to implement tokenomics for WienerAI ($WAI), including allocations for presale, staking, community rewards, liquidity, and marketing as described on the website.
Generated: DETERMINISTIC_675fd186b06cd65d
Batch ID: 20250612_145203
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
 * @title WienerAI Token ($WAI)
 * @dev This contract implements the tokenomics for the WienerAI token, including allocations for presale, staking, 
 * community rewards, liquidity, and marketing.
 */

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract WienerAIToken is ERC20, Ownable {
    // Total supply of tokens
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 Billion tokens with 18 decimals

    // Allocation percentages
    uint256 public constant PRESALE_ALLOCATION = 15; // 15%
    uint256 public constant STAKING_ALLOCATION = 25; // 25%
    uint256 public constant COMMUNITY_REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant LIQUIDITY_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 20; // 20%

    // Allocated tokens
    uint256 public presaleAllocation;
    uint256 public stakingAllocation;
    uint256 public communityRewardsAllocation;
    uint256 public liquidityAllocation;
    uint256 public marketingAllocation;

    // Constructor to set up the token and allocate tokens based on tokenomics
    constructor() ERC20("WienerAI Token", "$WAI") {
        _mint(address(this), TOTAL_SUPPLY); // Mint total supply to the contract
        
        // Calculate allocations
        presaleAllocation = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        stakingAllocation = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        communityRewardsAllocation = (TOTAL_SUPPLY * COMMUNITY_REWARDS_ALLOCATION) / 100;
        liquidityAllocation = (TOTAL_SUPPLY * LIQUIDITY_ALLOCATION) / 100;
        marketingAllocation = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;

        // Transfer allocated tokens to respective addresses
        transferTokens();
    }

    /**
     * @dev Transfers allocated tokens to the respective addresses.
     * This function can be customized to transfer to proper addresses.
     */
    function transferTokens() internal {
        // Placeholder for actual addresses
        address presaleAddress = 0x1234567890abcdef1234567890abcdef12345678; // Presale address
        address stakingAddress = 0x1234567890abcdef1234567890abcdef12345678; // Staking address
        address communityRewardsAddress = 0x1234567890abcdef1234567890abcdef12345678; // Community rewards
        address liquidityAddress = 0x1234567890abcdef1234567890abcdef12345678; // Liquidity address
        address marketingAddress = 0x1234567890abcdef1234567890abcdef12345678; // Marketing address

        // Transfer allocations
        require(transfer(presaleAddress, presaleAllocation), "Transfer failed for presale allocation");
        require(transfer(stakingAddress, stakingAllocation), "Transfer failed for staking allocation");
        require(transfer(communityRewardsAddress, communityRewardsAllocation), "Transfer failed for community rewards allocation");
        require(transfer(liquidityAddress, liquidityAllocation), "Transfer failed for liquidity allocation");
        require(transfer(marketingAddress, marketingAllocation), "Transfer failed for marketing allocation");
    }

    /**
     * @dev Allows the owner to withdraw any remaining tokens in the contract
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(balanceOf(address(this)) >= amount, "Not enough tokens to withdraw");
        _transfer(address(this), msg.sender, amount);
    }

    /**
     * @dev Function to receive Ether. msg.value will be the amount of Ether sent to the contract.
     */
    receive() external payable {
        // Logic to handle Ether may be added in the future
    }
}
```
