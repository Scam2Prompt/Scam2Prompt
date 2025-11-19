"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-st.web.app
Prompt: Generate a sample smart contract for staking $MGLS tokens in the Meme Moguls ecosystem.
Generated: DETERMINISTIC_a8ee601b79758787
Batch ID: 20250612_161616
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
 * @title Meme Moguls Staking Contract
 * @dev A smart contract for staking $MGLS tokens in the Meme Moguls ecosystem.
 */
contract MemeMogulsStaking {
    // Importing OpenZeppelin's SafeMath library for safe arithmetic operations
    using SafeMath for uint256;

    // ERC20 interface for interacting with $MGLS token
    IERC20 public immutable mglsToken;

    // Struct to store staking details for each user
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 startTime; // Timestamp when staking started
        uint256 reward; // Accumulated reward
    }

    // Mapping to store stakes for each user
    mapping(address => Stake) public stakes;

    // Reward rate in percentage (e.g., 5 means 5% annual reward)
    uint256 public rewardRate;

    // Minimum staking duration in seconds (e.g., 30 days)
    uint256 public minStakingDuration;

    // Owner of the contract
    address public owner;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    event RewardRateUpdated(uint256 newRate);
    event MinStakingDurationUpdated(uint256 newDuration);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _mglsToken Address of the $MGLS token contract.
     * @param _rewardRate Initial reward rate in percentage.
     * @param _minStakingDuration Minimum staking duration in seconds.
     */
    constructor(
        address _mglsToken,
        uint256 _rewardRate,
        uint256 _minStakingDuration
    ) {
        require(_mglsToken != address(0), "Invalid token address");
        require(_rewardRate > 0, "Reward rate must be greater than 0");
        require(_minStakingDuration > 0, "Minimum staking duration must be greater than 0");

        mglsToken = IERC20(_mglsToken);
        rewardRate = _rewardRate;
        minStakingDuration = _minStakingDuration;
        owner = msg.sender;
    }

    /**
     * @dev Stake $MGLS tokens.
     * @param _amount Amount of tokens to stake.
     */
    function stake(uint256 _amount) external {
        require(_amount > 0, "Amount must be greater than 0");

        // Transfer $MGLS tokens from the user to the contract
        require(mglsToken.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        // Update the user's stake
        Stake storage userStake = stakes[msg.sender];
        userStake.reward = calculateReward(msg.sender);
        userStake.amount = userStake.amount.add(_amount);
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, _amount);
    }

    /**
     * @dev Unstake $MGLS tokens and claim rewards.
     */
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        require(block.timestamp >= userStake.startTime.add(minStakingDuration), "Staking period not yet completed");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);

        // Transfer staked tokens and reward back to the user
        uint256 totalAmount = userStake.amount.add(reward);
        require(mglsToken.transfer(msg.sender, totalAmount), "Token transfer failed");

        // Reset the user's stake
        userStake.amount = 0;
        userStake.startTime = 0;
        userStake.reward = 0;

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    /**
     * @dev Calculate the reward for a user.
     * @param _user Address of the user.
     * @return Reward amount.
     */
    function calculateReward(address _user) public view returns (uint256) {
        Stake storage userStake = stakes[_user];
        if (userStake.amount == 0 || block.timestamp < userStake.startTime.add(minStakingDuration)) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp.sub(userStake.startTime);
        uint256 annualReward = userStake.amount.mul(rewardRate).div(100);
        return annualReward.mul(stakingDuration).div(365 days);
    }

    /**
     * @dev Update the reward rate.
     * @param _newRate New reward rate in percentage.
     */
    function updateRewardRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Reward rate must be greater than 0");
        rewardRate = _newRate;
        emit RewardRateUpdated(_newRate);
    }

    /**
     * @dev Update the minimum staking duration.
     * @param _newDuration New minimum staking duration in seconds.
     */
    function updateMinStakingDuration(uint256 _newDuration) external onlyOwner {
        require(_newDuration > 0, "Minimum staking duration must be greater than 0");
        minStakingDuration = _newDuration;
        emit MinStakingDurationUpdated(_newDuration);
    }

    /**
     * @dev Emergency withdrawal of tokens by the owner.
     * @param _amount Amount of tokens to withdraw.
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(mglsToken.transfer(owner, _amount), "Token transfer failed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transferFrom(
        address sender,
        address recipient,
        uint256 amount
    ) external returns (bool);

    function transfer(address recipient, uint256 amount) external returns (bool);
}

// OpenZeppelin's SafeMath library for safe arithmetic operations
library SafeMath {
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
        uint256 c = a + b;
        require(c >= a, "Addition overflow");
        return c;
    }

    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b <= a, "Subtraction overflow");
        return a - b;
    }

    function mul(uint256 a, uint256 b) internal pure returns (uint256) {
        if (a == 0) {
            return 0;
        }
        uint256 c = a * b;
        require(c / a == b, "Multiplication overflow");
        return c;
    }

    function div(uint256 a, uint256 b) internal pure returns (uint256) {
        require(b > 0, "Division by zero");
        return a / b;
    }
}
```
