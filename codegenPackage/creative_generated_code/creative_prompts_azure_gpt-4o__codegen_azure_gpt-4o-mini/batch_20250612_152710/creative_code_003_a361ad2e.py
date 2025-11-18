"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://greenbitcoin-st.pages.dev
Prompt: Create a smart contract in Solidity for staking $GBTC tokens and calculating exponential rewards based on the Green Bitcoin gamified staking model.
Generated: DETERMINISTIC_a361ad2eb0746080
Batch ID: 20250612_152710
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

// Importing OpenZeppelin's SafeMath library for safe arithmetic operations
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ERC20 token (GBTC)
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for staking GBTC tokens
contract GreenBitcoinStaking is Ownable {
    using SafeMath for uint256;

    // Struct to hold staking data for each user
    struct Stake {
        uint256 amount;        // Amount of GBTC staked
        uint256 startTime;     // Timestamp when the staking started
        uint256 rewards;       // Accumulated rewards
    }

    // Mapping of user addresses to their respective stake data
    mapping(address => Stake) public stakes;

    // Token to be staked (GBTC)
    IERC20 public gbtcToken;

    // Exponential reward parameters
    uint256 public rewardRate;       // Base reward rate
    uint256 public rewardMultiplier; // Multiplier for exponential growth

    // Event to log staking actions
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 rewards);

    // Constructor to initialize the contract with the token address and reward parameters
    constructor(IERC20 _gbtcToken, uint256 _rewardRate, uint256 _rewardMultiplier) {
        gbtcToken = _gbtcToken;
        rewardRate = _rewardRate;
        rewardMultiplier = _rewardMultiplier;
    }

    // Function to stake GBTC tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(gbtcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Stake storage userStake = stakes[msg.sender];

        // If the user has an existing stake, calculate current rewards before updating
        if (userStake.amount > 0) {
            userStake.rewards = calculateRewards(msg.sender);
        }

        // Update the user's stake
        userStake.amount = userStake.amount.add(amount);
        userStake.startTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GBTC tokens and claim rewards
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");

        // Calculate rewards before unstaking
        uint256 rewards = calculateRewards(msg.sender);
        uint256 amountToUnstake = userStake.amount;

        // Reset user stake data
        userStake.amount = 0;
        userStake.rewards = 0;

        // Transfer staked tokens and rewards to the user
        require(gbtcToken.transfer(msg.sender, amountToUnstake), "Transfer failed");
        require(gbtcToken.transfer(msg.sender, rewards), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake, rewards);
    }

    // Function to calculate rewards based on the time staked
    function calculateRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];

        // Calculate the duration of the stake in seconds
        uint256 duration = block.timestamp.sub(userStake.startTime);

        // Exponential growth calculation
        uint256 reward = userStake.amount.mul(rewardRate).mul(rewardMultiplier ** (duration / 1 days));
        return reward.add(userStake.rewards);
    }

    // Function to update reward parameters (only owner can call)
    function updateRewardParameters(uint256 _rewardRate, uint256 _rewardMultiplier) external onlyOwner {
        rewardRate = _rewardRate;
        rewardMultiplier = _rewardMultiplier;
    }
}
```
