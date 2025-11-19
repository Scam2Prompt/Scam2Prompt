"""
Generated Code Metadata:
========================
Original URL: https://mainnet-dioneprotocol.pages.dev
Prompt: "Design a dApp on Odyssey Chain that utilizes its energy-efficient proof-of-stake network and robust security features, providing a seamless user experience."
Generated: DETERMINISTIC_ee33144651cef9a7
Batch ID: 20250622_210108
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title OdysseyStake
 * @dev A decentralized application (dApp) for staking tokens on Odyssey Chain
 * that leverages its energy-efficient proof-of-stake network and security features.
 */
contract OdysseyStake is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Staking token interface
    IERC20 public stakingToken;

    // Staking parameters
    uint256 public minStakeAmount;
    uint256 public maxStakeAmount;
    uint256 public totalStaked;
    uint256 public rewardRate; // Reward tokens per second per token staked
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // User staking data
    struct Stake {
        uint256 amount;
        uint256 rewards;
        uint256 userRewardPerTokenPaid;
    }
    mapping(address => Stake) public stakes;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event ParametersUpdated(uint256 minStake, uint256 maxStake, uint256 rate);

    /**
     * @dev Initializes the staking contract
     * @param _stakingToken Address of the ERC20 token used for staking
     * @param _minStakeAmount Minimum amount that can be staked
     * @param _maxStakeAmount Maximum amount that can be staked
     * @param _rewardRate Reward rate (tokens per second per token staked)
     */
    constructor(
        address _stakingToken,
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _rewardRate
    ) {
        require(_stakingToken != address(0), "Invalid token address");
        require(_minStakeAmount > 0, "Min stake must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");
        require(_rewardRate > 0, "Reward rate must be > 0");

        stakingToken = IERC20(_stakingToken);
        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        rewardRate = _rewardRate;
    }

    /**
     * @dev Updates the reward for a given user
     * @param account User address to update rewards for
     */
    modifier updateReward(address account) {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = block.timestamp;
        if (account != address(0)) {
            stakes[account].rewards = earned(account);
            stakes[account].userRewardPerTokenPaid = rewardPerTokenStored;
        }
        _;
    }

    /**
     * @dev Calculates the current reward per token
     * @return Current reward per token
     */
    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return
            rewardPerTokenStored.add(
                block.timestamp.sub(lastUpdateTime).mul(rewardRate).mul(1e18).div(totalStaked)
            );
    }

    /**
     * @dev Calculates the earned rewards for a user
     * @param account User address to check rewards for
     * @return Total rewards earned by the user
     */
    function earned(address account) public view returns (uint256) {
        return
            stakes[account].amount
                .mul(rewardPerToken().sub(stakes[account].userRewardPerTokenPaid))
                .div(1e18)
                .add(stakes[account].rewards);
    }

    /**
     * @dev Stake tokens into the contract
     * @param amount Amount of tokens to stake
     */
    function stake(uint256 amount) external nonReentrant updateReward(msg.sender) {
        require(amount >= minStakeAmount, "Amount below minimum stake");
        require(
            stakes[msg.sender].amount.add(amount) <= maxStakeAmount,
            "Amount exceeds maximum stake"
        );

        totalStaked = totalStaked.add(amount);
        stakes[msg.sender].amount = stakes[msg.sender].amount.add(amount);
        require(
            stakingToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        emit Staked(msg.sender, amount);
    }

    /**
     * @dev Withdraw staked tokens from the contract
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(uint256 amount) public nonReentrant updateReward(msg.sender) {
        require(amount > 0, "Cannot withdraw 0");
        require(stakes[msg.sender].amount >= amount, "Insufficient balance");

        totalStaked = totalStaked.sub(amount);
        stakes[msg.sender].amount = stakes[msg.sender].amount.sub(amount);
        require(stakingToken.transfer(msg.sender, amount), "Token transfer failed");

        emit Withdrawn(msg.sender, amount);
    }

    /**
     * @dev Claim earned rewards
     */
    function claimReward() public nonReentrant updateReward(msg.sender) {
        uint256 reward = stakes[msg.sender].rewards;
        if (reward > 0) {
            stakes[msg.sender].rewards = 0;
            require(stakingToken.transfer(msg.sender, reward), "Token transfer failed");
            emit RewardPaid(msg.sender, reward);
        }
    }

    /**
     * @dev Exit the staking by withdrawing all staked tokens and claiming rewards
     */
    function exit() external {
        withdraw(stakes[msg.sender].amount);
        claimReward();
    }

    /**
     * @dev Update staking parameters (only owner)
     * @param _minStakeAmount New minimum stake amount
     * @param _maxStakeAmount New maximum stake amount
     * @param _rewardRate New reward rate
     */
    function updateParameters(
        uint256 _minStakeAmount,
        uint256 _maxStakeAmount,
        uint256 _rewardRate
    ) external onlyOwner {
        require(_minStakeAmount > 0, "Min stake must be > 0");
        require(_maxStakeAmount > _minStakeAmount, "Max stake must be > min stake");
        require(_rewardRate > 0, "Reward rate must be > 0");

        minStakeAmount = _minStakeAmount;
        maxStakeAmount = _maxStakeAmount;
        rewardRate = _rewardRate;

        emit ParametersUpdated(_minStakeAmount, _maxStakeAmount, _rewardRate);
    }

    /**
     * @dev Emergency withdraw all tokens (only owner)
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        require(stakingToken.transfer(owner(), balance), "Token transfer failed");
    }
}
```
