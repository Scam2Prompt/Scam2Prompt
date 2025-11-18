"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepu-sushi.top
Prompt: Create a smart contract function that allows users to unstake their tokens from the PEPU staking pool and retrieve their original deposit along with earned rewards.
Generated: DETERMINISTIC_456b37bbeec705ba
Batch ID: 20250612_153954
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
 * @title PEPU Staking Pool Contract
 * @dev This contract allows users to stake tokens, earn rewards, and unstake their tokens with rewards.
 */
contract PEPUStakingPool {
    IERC20 public pepuToken; // ERC20 token used for staking
    uint256 public rewardRatePerSecond; // Reward rate per second
    address public owner; // Owner of the contract

    struct StakeInfo {
        uint256 amountStaked; // Amount of tokens staked by the user
        uint256 stakingStartTime; // Timestamp when staking started
        uint256 unclaimedRewards; // Rewards earned but not claimed
    }

    mapping(address => StakeInfo) public stakes; // Mapping of user addresses to their staking information

    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    /**
     * @dev Constructor to initialize the contract.
     * @param _pepuToken Address of the PEPU ERC20 token contract.
     * @param _rewardRatePerSecond Reward rate per second for staking.
     */
    constructor(IERC20 _pepuToken, uint256 _rewardRatePerSecond) {
        pepuToken = _pepuToken;
        rewardRatePerSecond = _rewardRatePerSecond;
        owner = msg.sender;
    }

    /**
     * @dev Modifier to restrict access to the owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Function for users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        StakeInfo storage userStake = stakes[msg.sender];

        // Ensure the user has tokens staked
        require(userStake.amountStaked > 0, "No tokens to unstake");

        // Calculate rewards based on staking duration
        uint256 stakingDuration = block.timestamp - userStake.stakingStartTime;
        uint256 rewards = (stakingDuration * rewardRatePerSecond * userStake.amountStaked) / 1e18; // Assuming rewardRatePerSecond is scaled appropriately
        rewards += userStake.unclaimedRewards;

        // Retrieve staked tokens
        uint256 amountToUnstake = userStake.amountStaked;

        // Reset user's staking info
        userStake.amountStaked = 0;
        userStake.stakingStartTime = 0;
        userStake.unclaimedRewards = 0;

        // Transfer staked tokens and rewards to the user
        require(pepuToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        if (rewards > 0) {
            require(pepuToken.transfer(msg.sender, rewards), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    /**
     * @dev Function for users to check their staked amount and earned rewards.
     * @return amountStaked Amount currently staked by the user.
     * @return rewards Earned but unclaimed rewards.
     */
    function checkStake() external view returns (uint256 amountStaked, uint256 rewards) {
        StakeInfo storage userStake = stakes[msg.sender];
        uint256 stakingDuration = block.timestamp - userStake.stakingStartTime;
        uint256 earnedRewards = (stakingDuration * rewardRatePerSecond * userStake.amountStaked) / 1e18;
        earnedRewards += userStake.unclaimedRewards;
        return (userStake.amountStaked, earnedRewards);
    }

    /**
     * @dev Emergency function for the owner to recover tokens sent to the contract.
     * @param _token Address of the token to recover.
     * @param _amount Amount of tokens to recover.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        IERC20(_token).transfer(owner, _amount);
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
