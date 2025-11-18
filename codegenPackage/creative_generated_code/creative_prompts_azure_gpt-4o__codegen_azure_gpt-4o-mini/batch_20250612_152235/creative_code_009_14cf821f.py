"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://demo777-33v.pages.dev
Prompt: Develop a smart contract that utilizes Harvest's auto-compounding features for staking and reward management.
Generated: DETERMINISTIC_14cf821facd58bd2
Batch ID: 20250612_152235
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

// Importing necessary interfaces
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Harvest Finance's vault
interface IHarvestVault {
    function deposit(uint256 _amount) external;
    function withdraw(uint256 _shares) external;
    function balanceOf(address _account) external view returns (uint256);
    function getPricePerFullShare() external view returns (uint256);
}

contract AutoCompoundingStaker is Ownable {
    // State variables
    IHarvestVault public vault; // The Harvest vault for auto-compounding
    IERC20 public rewardToken; // The token received as rewards

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    constructor(address _vault, address _rewardToken) {
        vault = IHarvestVault(_vault);
        rewardToken = IERC20(_rewardToken);
    }

    // Function to stake tokens in the Harvest vault
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens from the user to the contract
        rewardToken.transferFrom(msg.sender, address(this), _amount);
        
        // Approve the vault to spend the tokens
        rewardToken.approve(address(vault), _amount);
        
        // Deposit the tokens into the Harvest vault
        vault.deposit(_amount);
        
        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked tokens from the Harvest vault
    function withdraw(uint256 _shares) external {
        require(_shares > 0, "Shares must be greater than zero");
        
        // Withdraw tokens from the Harvest vault
        vault.withdraw(_shares);

        // Transfer withdrawn tokens back to the user
        uint256 amount = rewardToken.balanceOf(address(this));
        require(amount > 0, "No tokens to withdraw");
        rewardToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the user's staked balance
    function stakedBalance() external view returns (uint256) {
        return vault.balanceOf(msg.sender) * vault.getPricePerFullShare() / 1e18; // Adjusting for decimals
    }

    // Function to claim rewards (could be integrated with a reward distribution mechanism)
    function claimRewards() external {
        uint256 rewardAmount = rewardToken.balanceOf(address(this));
        require(rewardAmount > 0, "No rewards to claim");

        // Transfer rewards to the user
        rewardToken.transfer(msg.sender, rewardAmount);
        
        emit RewardsClaimed(msg.sender, rewardAmount);
    }

    // Function to set a new vault (onlyOwner)
    function setVault(address _newVault) external onlyOwner {
        vault = IHarvestVault(_newVault);
    }

    // Function to set a new reward token (onlyOwner)
    function setRewardToken(address _newRewardToken) external onlyOwner {
        rewardToken = IERC20(_newRewardToken);
    }
}
```
