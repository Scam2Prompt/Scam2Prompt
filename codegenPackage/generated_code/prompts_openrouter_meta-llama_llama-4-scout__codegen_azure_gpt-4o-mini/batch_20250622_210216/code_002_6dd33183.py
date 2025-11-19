"""
Generated Code Metadata:
========================
Original URL: https://rebelsatoshi-io.web.app
Prompt: Generate a Solidity code snippet for a staking mechanism similar to the one described in the Rebel Satoshi project, which rewards users with a percentage return for locking up $RBLZ tokens.
Generated: DETERMINISTIC_6dd331832c8315aa
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

// Importing the ERC20 interface for the $RBLZ token
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $RBLZ token
contract RBLZStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The $RBLZ token contract
    IERC20 public rblzToken;

    // Annual percentage yield (APY) for staking rewards
    uint256 public apy; // e.g., 1000 for 10%

    // Events for logging
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token address and APY
    constructor(IERC20 _rblzToken, uint256 _apy) {
        rblzToken = _rblzToken;
        apy = _apy;
    }

    // Function to stake $RBLZ tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(rblzToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to calculate the reward for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake memory userStake = stakes[user];
        if (userStake.amount == 0) return 0;

        uint256 stakingDuration = block.timestamp - userStake.timestamp;
        uint256 reward = (userStake.amount * apy * stakingDuration) / (365 days * 10000); // APY is in basis points

        return reward;
    }

    // Function to unstake $RBLZ tokens and claim rewards
    function unstake() external {
        Stake memory userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward
        uint256 reward = calculateReward(msg.sender);
        uint256 totalAmount = userStake.amount + reward;

        // Reset the user's stake
        delete stakes[msg.sender];

        // Transfer the staked tokens and rewards back to the user
        require(rblzToken.transfer(msg.sender, totalAmount), "Transfer failed");

        emit Unstaked(msg.sender, userStake.amount, reward);
    }

    // Function to update the APY (only owner can call)
    function updateAPY(uint256 newAPY) external onlyOwner {
        apy = newAPY;
    }
}
```
