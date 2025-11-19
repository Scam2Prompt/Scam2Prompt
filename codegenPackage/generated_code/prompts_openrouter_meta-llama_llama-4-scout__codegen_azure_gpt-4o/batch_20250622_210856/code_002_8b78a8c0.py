"""
Generated Code Metadata:
========================
Original URL: https://wallet-7dc15.web.app
Prompt: Generate a simple smart contract code in Solidity for handling $ATOR token staking and rewards on a blockchain platform.
Generated: DETERMINISTIC_8b78a8c00dbead58
Batch ID: 20250622_210856
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
 * @title ATOR Token Staking Contract
 * @dev This contract allows users to stake ATOR tokens and earn rewards.
 */
contract ATORStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public atorToken; // ATOR token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total tokens staked in the contract

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of last interaction
        uint256 rewards; // Accumulated rewards
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier updateRewards(address _user) {
        Stake storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 timeElapsed = block.timestamp - stake.timestamp;
            stake.rewards += timeElapsed * stake.amount * rewardRate / 1e18;
        }
        stake.timestamp = block.timestamp;
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _atorToken Address of the ATOR token contract.
     * @param _rewardRate Reward rate per second (scaled by 1e18).
     */
    constructor(address _atorToken, uint256 _rewardRate) {
        owner = msg.sender;
        atorToken = IERC20(_atorToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake ATOR tokens in the contract.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateRewards(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(atorToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        stakes[msg.sender].amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake ATOR tokens and claim rewards.
     */
    function unstake() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(stake.amount > 0, "No tokens staked");

        uint256 amountToUnstake = stake.amount;
        uint256 rewardsToClaim = stake.rewards;

        stake.amount = 0;
        stake.rewards = 0;
        totalStaked -= amountToUnstake;

        require(atorToken.transfer(msg.sender, amountToUnstake), "Token transfer failed");
        if (rewardsToClaim > 0) {
            require(atorToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");
        }

        emit Unstaked(msg.sender, amountToUnstake);
        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Claim accumulated rewards without unstaking.
     */
    function claimRewards() external updateRewards(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 rewardsToClaim = stake.rewards;
        require(rewardsToClaim > 0, "No rewards to claim");

        stake.rewards = 0;
        require(atorToken.transfer(msg.sender, rewardsToClaim), "Reward transfer failed");

        emit RewardsClaimed(msg.sender, rewardsToClaim);
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate New reward rate per second (scaled by 1e18).
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(atorToken.transfer(owner, _amount), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
