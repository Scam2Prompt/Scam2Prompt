"""
Generated Code Metadata:
========================
Original URL: https://hydrofinance-dapp.pages.dev
Prompt: Design a smart contract for a Farming feature that allows users to stake their hINJ LSTs and earn superior yields, using a platform like Injective Network.
Generated: DETERMINISTIC_7bdf8acfc13a56b8
Batch ID: 20250622_210216
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
 * @title FarmingContract
 * @dev A smart contract for staking hINJ tokens and earning rewards on the Injective Network.
 */
contract FarmingContract {
    // State variables
    address public owner; // Contract owner
    address public hINJToken; // Address of the hINJ token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of hINJ tokens staked

    struct Stake {
        uint256 amount; // Amount of hINJ tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier updateReward(address _user) {
        Stake storage stake = stakes[_user];
        if (stake.amount > 0) {
            uint256 pendingReward = calculateReward(_user);
            stake.rewardDebt += pendingReward;
        }
        stake.lastUpdated = block.timestamp;
        _;
    }

    // Constructor
    constructor(address _hINJToken, uint256 _rewardRate) {
        require(_hINJToken != address(0), "Invalid hINJ token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        hINJToken = _hINJToken;
        rewardRate = _rewardRate;
    }

    // Function to stake hINJ tokens
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");

        // Transfer hINJ tokens from the user to the contract
        require(
            IERC20(hINJToken).transferFrom(msg.sender, address(this), _amount),
            "Token transfer failed"
        );

        // Update user's stake
        Stake storage stake = stakes[msg.sender];
        stake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    // Function to withdraw staked hINJ tokens
    function withdraw(uint256 _amount) external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(_amount > 0, "Cannot withdraw zero tokens");
        require(stake.amount >= _amount, "Insufficient staked balance");

        // Update user's stake
        stake.amount -= _amount;
        totalStaked -= _amount;

        // Transfer hINJ tokens back to the user
        require(
            IERC20(hINJToken).transfer(msg.sender, _amount),
            "Token transfer failed"
        );

        emit Withdrawn(msg.sender, _amount);
    }

    // Function to claim rewards
    function claimReward() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 reward = stake.rewardDebt;
        require(reward > 0, "No rewards to claim");

        // Reset reward debt
        stake.rewardDebt = 0;

        // Transfer rewards to the user
        require(
            IERC20(hINJToken).transfer(msg.sender, reward),
            "Reward transfer failed"
        );

        emit RewardClaimed(msg.sender, reward);
    }

    // Function to calculate pending rewards for a user
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage stake = stakes[_user];
        if (stake.amount == 0) {
            return 0;
        }
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        return (stake.amount * rewardRate * timeElapsed) / 1e18;
    }

    // Function to update the reward rate (only owner)
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        require(_newRewardRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRewardRate;
    }

    // Function to recover tokens sent to the contract by mistake (only owner)
    function recoverTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != hINJToken, "Cannot recover staked tokens");
        require(
            IERC20(_token).transfer(owner, _amount),
            "Token recovery failed"
        );
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);

    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);
}
```
