"""
Generated Code Metadata:
========================
Original URL: https://growtoken.xyz
Prompt: "Generate a smart contract code for staking and LST utilities on a blockchain platform similar to GROW DAO's offerings."
Generated: DETERMINISTIC_36480e74bc148603
Batch ID: 20250622_212444
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
 * @title Staking and LST Utilities Smart Contract
 * @dev This contract allows users to stake tokens and earn rewards. It also supports Liquid Staking Tokens (LST).
 */
contract StakingContract {
    // State variables
    address public owner; // Contract owner
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardRate; // Reward rate per second
    uint256 public constant MINIMUM_STAKE = 1 ether; // Minimum stake amount

    struct Stake {
        uint256 amount; // Amount staked
        uint256 timestamp; // Timestamp of staking
    }

    mapping(address => Stake) public stakes; // Mapping of user stakes
    mapping(address => uint256) public rewards; // Mapping of user rewards

    IERC20 public stakingToken; // ERC20 token used for staking
    IERC20 public lstToken; // ERC20 Liquid Staking Token (LST)

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No stake found for user");
        _;
    }

    // Constructor
    constructor(address _stakingToken, address _lstToken, uint256 _rewardRate) {
        owner = msg.sender;
        stakingToken = IERC20(_stakingToken);
        lstToken = IERC20(_lstToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Stake tokens to earn rewards.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount >= MINIMUM_STAKE, "Stake amount is below minimum");
        require(stakingToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Calculate pending rewards for the user
        _updateRewards(msg.sender);

        // Update stake
        stakes[msg.sender].amount += _amount;
        stakes[msg.sender].timestamp = block.timestamp;

        totalStaked += _amount;

        // Mint LST tokens to the user
        lstToken.transfer(msg.sender, _amount);

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake tokens and claim rewards.
     */
    function unstake() external hasStake(msg.sender) {
        uint256 stakedAmount = stakes[msg.sender].amount;

        // Calculate pending rewards
        _updateRewards(msg.sender);

        // Transfer staked tokens back to the user
        require(stakingToken.transfer(msg.sender, stakedAmount), "Token transfer failed");

        // Burn LST tokens from the user
        require(lstToken.transferFrom(msg.sender, address(this), stakedAmount), "LST burn failed");

        // Reset stake
        stakes[msg.sender].amount = 0;
        stakes[msg.sender].timestamp = 0;

        totalStaked -= stakedAmount;

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim accumulated rewards.
     */
    function claimRewards() external hasStake(msg.sender) {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;

        // Transfer rewards to the user
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Update rewards for a user.
     * @param _user Address of the user.
     */
    function _updateRewards(address _user) internal {
        Stake storage userStake = stakes[_user];
        uint256 stakedDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on staked duration and reward rate
        uint256 reward = (userStake.amount * rewardRate * stakedDuration) / 1 ether;
        rewards[_user] += reward;

        // Update timestamp
        userStake.timestamp = block.timestamp;
    }

    /**
     * @dev Update the reward rate. Only callable by the owner.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Emergency withdrawal of tokens from the contract. Only callable by the owner.
     * @param _token Address of the token to withdraw.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(address _token, uint256 _amount) external onlyOwner {
        require(IERC20(_token).transfer(owner, _amount), "Token transfer failed");
    }
}

// Interface for ERC20 tokens
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
