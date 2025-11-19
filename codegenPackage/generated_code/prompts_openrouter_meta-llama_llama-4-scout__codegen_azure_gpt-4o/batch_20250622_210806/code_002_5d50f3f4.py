"""
Generated Code Metadata:
========================
Original URL: https://my-greenbitcoin.pages.dev
Prompt: "Design a simple smart contract in Solidity to automate the staking and reward distribution for Green Bitcoin ($GBTC) holders on the Ethereum blockchain."
Generated: DETERMINISTIC_5d50f3f484f1d5fd
Batch ID: 20250622_210806
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
 * @title Green Bitcoin Staking Contract
 * @dev This contract allows $GBTC holders to stake their tokens and earn rewards.
 */
contract GreenBitcoinStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public gbtcToken; // $GBTC token contract
    uint256 public rewardRate; // Reward rate per second
    uint256 public totalStaked; // Total amount of tokens staked

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 rewardDebt; // Rewards already paid out
        uint256 lastUpdated; // Last time the stake was updated
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 reward);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
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
    constructor(address _gbtcToken, uint256 _rewardRate) {
        owner = msg.sender;
        gbtcToken = IERC20(_gbtcToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake $GBTC tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external updateReward(msg.sender) {
        require(_amount > 0, "Cannot stake zero tokens");
        require(gbtcToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage stake = stakes[msg.sender];
        stake.amount += _amount;
        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their $GBTC tokens.
     * @param _amount Amount of tokens to unstake.
     */
    function unstake(uint256 _amount) external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        require(_amount > 0, "Cannot unstake zero tokens");
        require(stake.amount >= _amount, "Insufficient staked balance");

        stake.amount -= _amount;
        totalStaked -= _amount;
        require(gbtcToken.transfer(msg.sender, _amount), "Token transfer failed");

        emit Unstaked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their staking rewards.
     */
    function claimReward() external updateReward(msg.sender) {
        Stake storage stake = stakes[msg.sender];
        uint256 reward = stake.rewardDebt;
        require(reward > 0, "No rewards available");

        stake.rewardDebt = 0;
        require(gbtcToken.transfer(msg.sender, reward), "Reward transfer failed");

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculates the pending reward for a user.
     * @param _user Address of the user.
     * @return Pending reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage stake = stakes[_user];
        uint256 timeElapsed = block.timestamp - stake.lastUpdated;
        return (stake.amount * rewardRate * timeElapsed) / 1e18;
    }

    /**
     * @dev Allows the owner to update the reward rate.
     * @param _newRewardRate New reward rate per second.
     */
    function updateRewardRate(uint256 _newRewardRate) external onlyOwner {
        rewardRate = _newRewardRate;
    }

    /**
     * @dev Allows the owner to withdraw excess tokens from the contract.
     * @param _amount Amount of tokens to withdraw.
     */
    function withdrawExcessTokens(uint256 _amount) external onlyOwner {
        require(gbtcToken.transfer(owner, _amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
