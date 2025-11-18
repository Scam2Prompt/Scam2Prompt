"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://scotty-theai-def.web.app
Prompt: Create a smart contract in Solidity for staking $SCOTTY tokens, ensuring it supports reward multipliers based on lock periods as described in Scotty AI's staking mechanism.
Generated: DETERMINISTIC_335d156cb39dd5bd
Batch ID: 20250612_152656
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Staking contract for SCOTTY tokens
contract ScottyStaking is Ownable {
    using SafeMath for uint256;

    // Token to be staked
    IERC20 public scottyToken;

    // Struct to hold staking data
    struct Stake {
        uint256 amount;        // Amount of tokens staked
        uint256 lockTime;      // Time when the tokens were staked
        uint256 multiplier;    // Reward multiplier based on lock period
    }

    // Mapping for user stakes
    mapping(address => Stake) public stakes;

    // Events for logging activities
    event Staked(address indexed user, uint256 amount, uint256 lockTime, uint256 multiplier);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);
    
    // Reward multipliers based on lock periods (in seconds)
    uint256 constant SHORT_TERM = 30 days;  // 1x multiplier
    uint256 constant MEDIUM_TERM = 60 days; // 2x multiplier
    uint256 constant LONG_TERM = 90 days;    // 3x multiplier

    // Constructor to set the SCOTTY token address
    constructor(IERC20 _scottyToken) {
        scottyToken = _scottyToken;
    }

    // Stake tokens with a specified lock period
    function stake(uint256 amount, uint256 lockDuration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(lockDuration == SHORT_TERM || lockDuration == MEDIUM_TERM || lockDuration == LONG_TERM,
                "Invalid lock duration");

        // Transfer tokens from user to the contract
        require(scottyToken.transferFrom(msg.sender, address(this), amount), "Token transfer failed");

        // Determine multiplier based on lock duration
        uint256 multiplier = 1; // Default multiplier
        if (lockDuration == MEDIUM_TERM) {
            multiplier = 2;
        } else if (lockDuration == LONG_TERM) {
            multiplier = 3;
        }

        // Update user's stake information
        stakes[msg.sender] = Stake(amount, block.timestamp.add(lockDuration), multiplier);

        emit Staked(msg.sender, amount, block.timestamp.add(lockDuration), multiplier);
    }

    // Calculate reward for a user based on the staked amount and multiplier
    function calculateReward(address user) internal view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (block.timestamp < userStake.lockTime) {
            return 0; // Cannot claim until lock period ends
        }
        return userStake.amount.mul(userStake.multiplier).div(1); // Reward calculation
    }

    // Unstake tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No active stake");
        require(block.timestamp >= userStake.lockTime, "Lock period not yet ended");

        // Calculate reward based on the current stake
        uint256 reward = calculateReward(msg.sender);
        
        // Transfer staked tokens back to the user
        require(scottyToken.transfer(msg.sender, userStake.amount), "Token transfer failed");

        // Transfer rewards to the user if any
        if (reward > 0) {
            require(scottyToken.transfer(msg.sender, reward), "Reward transfer failed");
        }

        // Reset user's stake
        delete stakes[msg.sender];

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to withdraw tokens in case of emergency
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        require(scottyToken.transfer(msg.sender, amount), "Emergency withdrawal failed");
    }
}
```
