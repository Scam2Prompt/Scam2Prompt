"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aave.org
Prompt: Write a tutorial on staking AAVE tokens within the Safety Module to earn rewards and provide a backstop against shortfall events.
Generated: DETERMINISTIC_01a99f31195bcbda
Batch ID: 20250612_154742
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the AAVE Token
interface IAaveToken is IERC20 {
    function stake(uint256 amount) external;
    function withdraw(uint256 amount) external;
}

// Interface for the Safety Module
interface ISafetyModule {
    function stakeAAVE(uint256 amount) external;
    function withdrawAAVE(uint256 amount) external;
    function getRewards() external view returns (uint256);
}

// AAVE Staking Contract
contract AaveStaking is Ownable {
    // State variables
    IAaveToken public aaveToken; // AAVE token contract
    ISafetyModule public safetyModule; // Safety Module contract
    mapping(address => uint256) public stakedAmounts; // Tracking user stakes

    // Event declaration for staking
    event Staked(address indexed user, uint256 amount);
    // Event declaration for withdrawing
    event Withdrawn(address indexed user, uint256 amount);
    // Event for rewards claiming
    event RewardsClaimed(address indexed user, uint256 amount);

    // Constructor to set the AAVE token and Safety Module addresses
    constructor(address _aaveToken, address _safetyModule) {
        aaveToken = IAaveToken(_aaveToken);
        safetyModule = ISafetyModule(_safetyModule);
    }

    // Function to stake AAVE tokens in the Safety Module
    function stakeTokens(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(aaveToken.balanceOf(msg.sender) >= amount, "Insufficient AAVE balance");

        // Transfer AAVE tokens from user to contract
        aaveToken.transferFrom(msg.sender, address(this), amount);
        
        // Stake tokens within the Safety Module
        safetyModule.stakeAAVE(amount);
        
        // Update user's staked amount
        stakedAmounts[msg.sender] += amount;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked AAVE tokens from the Safety Module
    function withdrawTokens(uint256 amount) external {
        require(stakedAmounts[msg.sender] >= amount, "Insufficient staked amount");

        // Withdraw tokens from the Safety Module
        safetyModule.withdrawAAVE(amount);
        
        // Transfer AAVE tokens back to the user
        aaveToken.transfer(msg.sender, amount);
        
        // Update user's staked amount
        stakedAmounts[msg.sender] -= amount;

        emit Withdrawn(msg.sender, amount);
    }

    // Function to claim rewards from staked tokens
    function claimRewards() external {
        uint256 rewards = safetyModule.getRewards();
        require(rewards > 0, "No rewards available");

        // Transfer rewards to the user (assuming rewards are AAVE tokens)
        aaveToken.transfer(msg.sender, rewards);

        emit RewardsClaimed(msg.sender, rewards);
    }

    // Function to allow the owner to withdraw any AAVE tokens in case of emergencies
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(aaveToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        aaveToken.transfer(msg.sender, amount);
    }
}
```
