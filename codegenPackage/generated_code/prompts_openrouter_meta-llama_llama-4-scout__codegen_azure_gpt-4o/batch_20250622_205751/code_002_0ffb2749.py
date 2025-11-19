"""
Generated Code Metadata:
========================
Original URL: https://hehe-dapps.pages.dev
Prompt: Develop a simple smart contract in Solidity that allows users to stake $HEHE tokens and earn a percentage boost in rewards, as described in the $HEHE ecosystem.
Generated: DETERMINISTIC_0ffb27497a9d804a
Batch ID: 20250622_205751
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
 * @title HEHE Staking Contract
 * @dev A simple smart contract for staking $HEHE tokens and earning rewards.
 */
contract HEHEStaking {
    // State variables
    address public owner; // Contract owner
    IERC20 public heheToken; // $HEHE token contract
    uint256 public rewardRate; // Reward rate in percentage (e.g., 5 for 5%)
    uint256 public constant REWARD_DIVISOR = 100; // Divisor for percentage calculation

    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp when tokens were staked
    }

    mapping(address => Stake) public stakes; // Mapping of user addresses to their stakes

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _heheToken Address of the $HEHE token contract.
     * @param _rewardRate Initial reward rate in percentage.
     */
    constructor(address _heheToken, uint256 _rewardRate) {
        require(_heheToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than zero");

        owner = msg.sender;
        heheToken = IERC20(_heheToken);
        rewardRate = _rewardRate;
    }

    /**
     * @dev Allows users to stake $HEHE tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Stake amount must be greater than zero");
        require(heheToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        Stake storage userStake = stakes[msg.sender];
        userStake.amount += _amount;
        userStake.timestamp = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Allows users to unstake their tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 stakedAmount = userStake.amount;
        uint256 stakingDuration = block.timestamp - userStake.timestamp;

        // Calculate rewards based on the reward rate and staking duration
        uint256 reward = (stakedAmount * rewardRate * stakingDuration) / (REWARD_DIVISOR * 1 days);

        // Reset user's stake
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer staked tokens and rewards back to the user
        require(heheToken.transfer(msg.sender, stakedAmount + reward), "Token transfer failed");

        emit Unstaked(msg.sender, stakedAmount, reward);
    }

    /**
     * @dev Updates the reward rate. Only callable by the owner.
     * @param _newRate New reward rate in percentage.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than zero");
        rewardRate = _newRate;

        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Emergency function to withdraw all tokens from the contract. Only callable by the owner.
     */
    function emergencyWithdraw() external onlyOwner {
        uint256 contractBalance = heheToken.balanceOf(address(this));
        require(heheToken.transfer(owner, contractBalance), "Token transfer failed");
    }
}

/**
 * @dev Interface for ERC20 token standard.
 */
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
