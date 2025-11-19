"""
Generated Code Metadata:
========================
Original URL: https://bafybeietwuxjz6bdpyiuv52eesrug4x6gocpsj32wdcvv4l4z6rzgjgf5a.ipfs.dweb.link
Prompt: Generate code to integrate sUSD into a decentralized application using Synthetix's liquidity interfaces. Ensure the code supports staking and earning rewards.
Generated: DETERMINISTIC_28f1d1c4c191072b
Batch ID: 20250612_150228
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

// Import necessary interfaces from Synthetix
import "@synthetixio/core-contracts/contracts/interfaces/IERC20.sol";
import "@synthetixio/core-contracts/contracts/interfaces/IERC20Permit.sol";
import "@synthetixio/core-contracts/contracts/interfaces/IStakingRewards.sol";

contract SUSDLiquidityIntegration {
    IERC20 public sUSD;
    IStakingRewards public stakingRewards;

    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    /**
     * @dev Initialize contract with sUSD and StakingRewards addresses
     * @param _sUSD Address of sUSD token
     * @param _stakingRewards Address of StakingRewards contract
     */
    constructor(address _sUSD, address _stakingRewards) {
        require(_sUSD != address(0), "Invalid sUSD address");
        require(_stakingRewards != address(0), "Invalid StakingRewards address");
        
        sUSD = IERC20(_sUSD);
        stakingRewards = IStakingRewards(_stakingRewards);
    }

    /**
     * @dev Stake sUSD tokens to earn rewards
     * @param amount Amount of sUSD to stake
     */
    function stake(uint256 amount) external {
        require(amount > 0, "Cannot stake 0");
        
        // Transfer sUSD from user to this contract
        bool success = sUSD.transferFrom(msg.sender, address(this), amount);
        require(success, "Transfer failed");
        
        // Approve staking contract to spend sUSD
        sUSD.approve(address(stakingRewards), amount);
        
        // Stake the tokens
        stakingRewards.stake(amount);
        
        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked sUSD tokens
     * @param amount Amount of sUSD to withdraw
     */
    function withdraw(uint256 amount) external {
        require(amount > 0, "Cannot withdraw 0");
        
        // Withdraw from staking contract
        stakingRewards.withdraw(amount);
        
        // Transfer sUSD back to user
        bool success = sUSD.transfer(msg.sender, amount);
        require(success, "Transfer failed");
        
        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimRewards() external {
        uint256 reward = stakingRewards.earned(msg.sender);
        require(reward > 0, "No rewards to claim");
        
        stakingRewards.getReward();
        
        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Get the current staked balance for a user
     * @param user Address of the user
     * @return uint256 Staked balance
     */
    function balanceOf(address user) external view returns (uint256) {
        return stakingRewards.balanceOf(user);
    }

    /**
     * @dev Get the current earned rewards for a user
     * @param user Address of the user
     * @return uint256 Earned rewards
     */
    function earned(address user) external view returns (uint256) {
        return stakingRewards.earned(user);
    }

    /**
     * @dev Get the total staked amount in the pool
     * @return uint256 Total staked amount
     */
    function totalStaked() external view returns (uint256) {
        return stakingRewards.totalSupply();
    }
}
```
