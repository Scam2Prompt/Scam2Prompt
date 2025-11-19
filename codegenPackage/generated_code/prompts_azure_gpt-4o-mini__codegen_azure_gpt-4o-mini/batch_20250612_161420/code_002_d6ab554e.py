"""
Generated Code Metadata:
========================
Original URL: https://smogtokencoin.pages.dev
Prompt: Explain how to implement a smart contract for staking $SMOG tokens on Ethereum to earn APY, based on the staking information provided by Smog Token.
Generated: DETERMINISTIC_d6ab554e20cb78f4
Batch ID: 20250612_161420
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

// Importing OpenZeppelin's ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for $SMOG tokens
contract SmogStaking is Ownable {
    // Token to be staked
    IERC20 public smogToken;

    // Struct to hold user staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of the stake
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // Annual Percentage Yield (APY) in basis points (e.g., 500 = 5%)
    uint256 public apyBasisPoints;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the token address and APY
    constructor(IERC20 _smogToken, uint256 _apyBasisPoints) {
        smogToken = _smogToken;
        apyBasisPoints = _apyBasisPoints;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(smogToken.balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Transfer tokens from the user to the contract
        smogToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens along with rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the staked amount and time
        uint256 reward = calculateReward(userStake.amount, userStake.timestamp);

        // Reset the user's stake information
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer the staked tokens and rewards to the user
        smogToken.transfer(msg.sender, amountToWithdraw + reward);

        emit Withdrawn(msg.sender, amountToWithdraw, reward);
    }

    // Function to calculate the reward based on staked amount and time
    function calculateReward(uint256 amount, uint256 timestamp) internal view returns (uint256) {
        uint256 stakingDuration = block.timestamp - timestamp; // Duration in seconds
        uint256 reward = (amount * apyBasisPoints * stakingDuration) / (365 days * 10000); // APY calculation
        return reward;
    }

    // Function to update the APY (only owner can call this)
    function updateAPY(uint256 newAPY) external onlyOwner {
        apyBasisPoints = newAPY;
    }

    // Function to withdraw tokens in case of emergency (only owner can call this)
    function emergencyWithdraw(uint256 amount) external onlyOwner {
        require(smogToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");
        smogToken.transfer(msg.sender, amount);
    }
}
```
