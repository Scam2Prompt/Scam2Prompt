"""
Generated Code Metadata:
========================
Original URL: https://nodeapp-serverlaunch.com
Prompt: "Generate code for a decentralized application (dApp) that enables users to stake and unstake tokens on a blockchain network."
Generated: DETERMINISTIC_8268bea1f2770b93
Batch ID: 20250622_204914
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

/**
 * @title StakingContract
 * @dev A decentralized application (dApp) for staking and unstaking tokens.
 * Users can stake ERC20 tokens, earn rewards, and unstake their tokens.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // ERC20 token used for staking
    IERC20 public stakingToken;

    // Reward rate per second (e.g., 1 token per second)
    uint256 public rewardRate;

    // Total staked tokens
    uint256 public totalStaked;

    // Mapping of user address to staked amount
    mapping(address => uint256) public stakedBalances;

    // Mapping of user address to last update timestamp
    mapping(address => uint256) public lastUpdateTime;

    // Mapping of user address to rewards earned
    mapping(address => uint256) public rewards;

    /**
     * @dev Constructor to initialize the staking contract.
     * @param _stakingToken Address of the ERC20 token used for staking.
     * @param _rewardRate Reward rate per second.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardRate) {
        stakingToken = _stakingToken;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Modifier to update rewards for the user before executing the function.
     * @param _account Address of the user.
     */
    modifier updateReward(address _account) {
        if (_account != address(0)) {
            rewards[_account] += _earned(_account);
            lastUpdateTime[_account] = block.timestamp;
        }
        _;
    }

    /**
     * @dev Stake tokens into the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake 0 tokens");
        require(
            stakingToken.transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        stakedBalances[msg.sender] += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens from the contract.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot unstake 0 tokens");
        require(
            stakedBalances[msg.sender] >= _amount,
            "Insufficient staked balance"
        );

        stakedBalances[msg.sender] -= _amount;
        totalStaked -= _amount;

        require(
            stakingToken.transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Claim earned rewards.
     */
    function claimRewards() external updateReward(msg.sender) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");

        rewards[msg.sender] = 0;

        require(
            stakingToken.transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardsClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate earned rewards for a user.
     * @param _account Address of the user.
     * @return Earned rewards.
     */
    function _earned(address _account) internal view returns (uint256) {
        uint256 timeElapsed = block.timestamp - lastUpdateTime[_account];
        return (stakedBalances[_account] * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Update the reward rate. Only callable by the contract owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
        emit RewardRateUpdated(_newRewardRate);
    }

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);
    event RewardRateUpdated(uint256 newRewardRate);
}
```
