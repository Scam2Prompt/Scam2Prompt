"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-en.pages.dev
Prompt: How can I implement a staking mechanism for an ERC-20 token like DOGE20 to distribute rewards over two years?
Generated: DETERMINISTIC_563b38c451832a87
Batch ID: 20250612_161420
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
 * @title StakingContract
 * @dev A staking mechanism for an ERC-20 token to distribute rewards over two years.
 * Users can stake tokens and receive rewards proportionally over the staking period.
 */
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakingContract is Ownable {
    // ERC-20 token to be staked
    IERC20 public stakingToken;

    // Reward distribution end time (2 years from contract creation)
    uint256 public rewardEndTimestamp;

    // Total tokens staked
    uint256 public totalStaked;

    // Mapping of user address to staking details
    mapping(address => uint256) public userStake;
    mapping(address => uint256) public userRewardDebt;

    // Reward logic variables
    uint256 public rewardRatePerSecond;
    uint256 public lastRewardTimestamp;
    uint256 public accRewardPerToken;

    /**
     * @dev Emitted when a user stakes tokens.
     */
    event Staked(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user withdraws tokens.
     */
    event Withdrawn(address indexed user, uint256 amount);

    /**
     * @dev Emitted when a user claims rewards.
     */
    event RewardClaimed(address indexed user, uint256 reward);

    /**
     * @dev Initializes the contract with the staking token and reward rate.
     * @param _stakingToken The ERC-20 token to be staked.
     * @param _rewardTotal The total reward tokens to distribute over the staking period.
     */
    constructor(IERC20 _stakingToken, uint256 _rewardTotal) {
        stakingToken = _stakingToken;
        rewardEndTimestamp = block.timestamp + 2 * 365 * 24 * 60 * 60; // 2 years in seconds
        rewardRatePerSecond = _rewardTotal / (2 * 365 * 24 * 60 * 60); // Calculate reward rate per second
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Updates the reward variables to the latest state.
     */
    function updateRewardVariables() internal {
        if (block.timestamp > lastRewardTimestamp && totalStaked > 0) {
            uint256 timeElapsed = block.timestamp - lastRewardTimestamp;
            uint256 reward = timeElapsed * rewardRatePerSecond;
            accRewardPerToken += (reward * 1e18) / totalStaked;
        }
        lastRewardTimestamp = block.timestamp;
    }

    /**
     * @dev Allows users to stake tokens into the contract.
     * @param _amount The amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Staking amount must be greater than zero");
        updateRewardVariables();

        // Transfer staking tokens to the contract
        stakingToken.transferFrom(msg.sender, address(this), _amount);

        // Update user's staking balance and reward debt
        userStake[msg.sender] += _amount;
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerToken) / 1e18;

        // Update total staked
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to withdraw their staked tokens.
     * @param _amount The amount of tokens to withdraw.
     */
    function withdraw(uint256 _amount) external {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(userStake[msg.sender] >= _amount, "Insufficient staked amount");

        updateRewardVariables();

        // Claim pending rewards before withdrawal
        claimRewards();

        // Update user's staking balance and reward debt
        userStake[msg.sender] -= _amount;
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerToken) / 1e18;

        // Transfer tokens back to the user
        stakingToken.transfer(msg.sender, _amount);

        // Update total staked
        totalStaked -= _amount;

        emit Withdrawn(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their pending rewards.
     */
    function claimRewards() public {
        updateRewardVariables();

        uint256 pendingReward = ((userStake[msg.sender] * accRewardPerToken) / 1e18) - userRewardDebt[msg.sender];
        require(pendingReward > 0, "No rewards available to claim");

        // Update reward debt for the user
        userRewardDebt[msg.sender] = (userStake[msg.sender] * accRewardPerToken) / 1e18;

        // Transfer rewards to the user
        stakingToken.transfer(msg.sender, pendingReward);

        emit RewardClaimed(msg.sender, pendingReward);
    }

    /**
     * @dev Emergency withdrawal function for the owner to recover tokens.
     * Only callable by the owner.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Emergency withdrawal amount must be greater than zero");
        stakingToken.transfer(owner(), _amount);
    }
}
```
