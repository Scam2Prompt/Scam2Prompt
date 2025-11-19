"""
Generated Code Metadata:
========================
Original URL: https://worldmobile-token.pages.dev
Prompt: Develop a smart contract in Solidity that facilitates staking WMTx tokens and calculates rewards based on network transactions.
Generated: DETERMINISTIC_acd33986d26a2abe
Batch ID: 20250612_153954
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

// Importing the ERC20 interface for WMTx token interaction
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Staking contract for WMTx tokens
contract WMTxStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their stakes
    mapping(address => Stake) public stakes;

    // The WMTx token contract
    IERC20 public wmtxToken;

    // Reward rate per second (in wei)
    uint256 public rewardRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount, uint256 reward);

    // Constructor to initialize the contract with the WMTx token address and reward rate
    constructor(address _wmtxToken, uint256 _rewardRate) {
        wmtxToken = IERC20(_wmtxToken);
        rewardRate = _rewardRate;
    }

    // Function to stake WMTx tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(wmtxToken.balanceOf(msg.sender) >= amount, "Insufficient WMTx balance");

        // Transfer WMTx tokens from the user to the contract
        wmtxToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to withdraw staked tokens and claim rewards
    function withdraw() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        // Calculate the reward based on the time staked
        uint256 reward = calculateReward(msg.sender);

        // Reset the user's stake information
        uint256 amountToWithdraw = userStake.amount;
        userStake.amount = 0;
        userStake.timestamp = 0;

        // Transfer the staked tokens and rewards back to the user
        wmtxToken.transfer(msg.sender, amountToWithdraw);
        wmtxToken.transfer(msg.sender, reward);

        emit Withdrawn(msg.sender, amountToWithdraw, reward);
    }

    // Function to calculate rewards for a user
    function calculateReward(address user) public view returns (uint256) {
        Stake storage userStake = stakes[user];
        if (userStake.amount == 0) {
            return 0;
        }
        uint256 stakedDuration = block.timestamp - userStake.timestamp;
        return (stakedDuration * userStake.amount * rewardRate) / 1e18; // Adjust reward calculation as needed
    }

    // Function to update the reward rate (only owner can call)
    function updateRewardRate(uint256 newRate) external onlyOwner {
        rewardRate = newRate;
    }
}
```
