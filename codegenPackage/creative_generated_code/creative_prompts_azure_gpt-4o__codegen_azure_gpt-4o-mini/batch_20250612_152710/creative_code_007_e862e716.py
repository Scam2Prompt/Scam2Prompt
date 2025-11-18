"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-d.pages.dev
Prompt: Write a Solidity contract for DOGE20 tokenomics, including fixed supply, staking rewards allocation, and liquidity provision, as outlined in the tokenomics section of Dogecoin20's website.
Generated: DETERMINISTIC_e862e71695e2c79d
Batch ID: 20250612_152710
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

// Import OpenZeppelin's ERC20 token implementation and Ownable contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// DOGE20 Token Contract
contract DOGE20 is ERC20, Ownable {
    // Total supply of the token
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10 ** 18; // 1 billion tokens (with 18 decimals)

    // Staking rewards allocation
    uint256 public constant STAKING_REWARDS = (TOTAL_SUPPLY * 20) / 100; // 20% for staking rewards
    uint256 public constant LIQUIDITY_PROVISION = (TOTAL_SUPPLY * 10) / 100; // 10% for liquidity provision

    // Variables to keep track of allocated rewards
    uint256 public stakingRewardsClaimed;
    uint256 public liquidityProvisionClaimed;

    // Events for logging purposes
    event RewardClaimed(address indexed user, uint256 amount);
    event LiquidityProvisionClaimed(address indexed user, uint256 amount);

    // Constructor to mint total supply to the contract owner
    constructor() ERC20("DOGE20", "DOGE20") {
        _mint(msg.sender, TOTAL_SUPPLY);
    }

    // Function to claim staking rewards
    function claimStakingRewards(uint256 amount) external onlyOwner {
        require(stakingRewardsClaimed + amount <= STAKING_REWARDS, "Exceeds staking rewards limit");
        stakingRewardsClaimed += amount;
        _transfer(owner(), msg.sender, amount);
        emit RewardClaimed(msg.sender, amount);
    }

    // Function to claim liquidity provision tokens
    function claimLiquidityProvision(uint256 amount) external onlyOwner {
        require(liquidityProvisionClaimed + amount <= LIQUIDITY_PROVISION, "Exceeds liquidity provision limit");
        liquidityProvisionClaimed += amount;
        _transfer(owner(), msg.sender, amount);
        emit LiquidityProvisionClaimed(msg.sender, amount);
    }

    // Function to stop accepting new claims (can be called by owner)
    function stopClaims() external onlyOwner {
        // Not implemented: Custom logic can be added to halt claims if required
    }

    // Function to withdraw leftover tokens (if any) after claims
    function withdrawLeftoverTokens() external onlyOwner {
        uint256 remainingBalance = balanceOf(address(this));
        require(remainingBalance > 0, "No leftover tokens to withdraw");
        _transfer(address(this), msg.sender, remainingBalance);
    }
}
```
