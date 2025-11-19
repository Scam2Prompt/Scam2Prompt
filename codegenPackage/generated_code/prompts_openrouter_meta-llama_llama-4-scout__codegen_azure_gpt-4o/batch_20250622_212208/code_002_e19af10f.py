"""
Generated Code Metadata:
========================
Original URL: https://btcbull.io
Prompt: Develop a smart contract in Solidity for staking $BTCBULL on Ethereum, including dynamic APY calculation and reward distribution.
Generated: DETERMINISTIC_e19af10fe98dffd5
Batch ID: 20250622_212208
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
 * @title BTCBullStaking
 * @dev A smart contract for staking BTCBULL tokens with dynamic APY calculation and reward distribution.
 */
contract BTCBullStaking {
    // State variables
    address public owner; // Contract owner
    address public tokenAddress; // Address of the BTCBULL token contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public baseAPY; // Base APY (Annual Percentage Yield) in percentage (e.g., 10 for 10%)
    uint256 public rewardPool; // Total reward pool available for distribution

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 lastClaimedTime; // Timestamp of the last reward claim
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

    modifier hasStake(address _user) {
        require(stakes[_user].amount > 0, "No active stake found");
        _;
    }

    // Constructor
    constructor(address _tokenAddress, uint256 _baseAPY) {
        owner = msg.sender;
        tokenAddress = _tokenAddress;
        baseAPY = _baseAPY;
    }

    /**
     * @dev Stake BTCBULL tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");

        // Transfer tokens from the user to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        // Update staking information
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.startTime = block.timestamp;
        userStake.lastClaimedTime = block.timestamp;

        totalStaked += _amount;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake BTCBULL tokens.
     */
    function unstake() external hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 stakedAmount = userStake.amount;

        // Claim any pending rewards before unstaking
        claimReward();

        // Transfer staked tokens back to the user
        IERC20(tokenAddress).transfer(msg.sender, stakedAmount);

        // Update state variables
        totalStaked -= stakedAmount;
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, stakedAmount);
    }

    /**
     * @dev Claim staking rewards.
     */
    function claimReward() public hasStake(msg.sender) {
        Stake storage userStake = stakes[msg.sender];
        uint256 reward = calculateReward(msg.sender);

        require(reward > 0, "No rewards available to claim");
        require(rewardPool >= reward, "Insufficient reward pool");

        // Update last claimed time
        userStake.lastClaimedTime = block.timestamp;

        // Transfer reward to the user
        IERC20(tokenAddress).transfer(msg.sender, reward);

        rewardPool -= reward;

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Calculate the reward for a user based on their stake and staking duration.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        uint256 stakingDuration = block.timestamp - userStake.lastClaimedTime;

        // Dynamic APY calculation (can be adjusted based on business logic)
        uint256 dynamicAPY = baseAPY + (totalStaked / 1e18); // Example: APY increases with total staked

        // Reward formula: (staked amount * APY * duration) / (365 days * 100)
        uint256 reward = (userStake.amount * dynamicAPY * stakingDuration) / (365 days * 100);

        return reward;
    }

    /**
     * @dev Add rewards to the reward pool.
     * @param _amount Amount of tokens to add to the reward pool.
     */
    function addRewards(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Reward amount must be greater than zero");

        // Transfer tokens from the owner to the contract
        IERC20(tokenAddress).transferFrom(msg.sender, address(this), _amount);

        rewardPool += _amount;
    }

    /**
     * @dev Update the base APY.
     * @param _newAPY New base APY value.
     */
    function updateBaseAPY(uint256 _newAPY) external onlyOwner {
        require(_newAPY > 0, "APY must be greater than zero");
        baseAPY = _newAPY;
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
