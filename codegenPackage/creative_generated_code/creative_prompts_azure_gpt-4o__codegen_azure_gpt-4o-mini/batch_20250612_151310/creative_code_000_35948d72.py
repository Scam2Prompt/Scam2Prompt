"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-99bitcoinspresale.pages.dev
Prompt: Write a smart contract in Solidity to enable staking of $99BTC tokens, ensuring dynamic rewards are calculated based on the staking pool percentage and distributed per Ethereum block as described on the 99Bitcoins platform.
Generated: DETERMINISTIC_35948d72428804e6
Batch ID: 20250612_151310
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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract Staking {
    // Struct to hold information about each staker
    struct Stake {
        uint256 amount; // Amount staked
        uint256 rewardDebt; // Reward debt for the staker
    }

    // State variables
    IERC20 public btcToken; // The $99BTC token contract
    address public owner; // Owner of the contract
    uint256 public totalStaked; // Total amount of tokens staked
    uint256 public rewardPerBlock; // Reward distribution per block
    mapping(address => Stake) private stakes; // Mapping of addresses to their stakes
    uint256 public lastRewardBlock; // The last block number that rewards were distributed

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RewardsClaimed(address indexed user, uint256 amount);

    // Modifier to ensure only the owner can execute certain functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    // Constructor to initialize the contract with the token address and initial reward per block
    constructor(IERC20 _btcToken, uint256 _rewardPerBlock) {
        btcToken = _btcToken;
        owner = msg.sender;
        rewardPerBlock = _rewardPerBlock;
        lastRewardBlock = block.number;
    }

    // Function to stake tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        // Transfer the tokens from the user to this contract
        require(btcToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update total staked amount
        totalStaked += amount;

        // Update staking info for the user
        Stake storage userStake = stakes[msg.sender];
        userStake.amount += amount;
        userStake.rewardDebt += calculatePendingRewards(msg.sender);

        // Emit the staking event
        emit Staked(msg.sender, amount);
    }

    // Function to unstake tokens
    function unstake(uint256 amount) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount >= amount, "Not enough staked tokens");

        // Update reward debt before unstaking
        userStake.rewardDebt += calculatePendingRewards(msg.sender);
        userStake.amount -= amount;

        // Update total staked amount
        totalStaked -= amount;

        // Transfer the tokens back to the user
        require(btcToken.transfer(msg.sender, amount), "Transfer failed");

        // Emit the unstaking event
        emit Unstaked(msg.sender, amount);
    }

    // Function to claim rewards
    function claimRewards() external {
        uint256 pendingRewards = calculatePendingRewards(msg.sender);
        
        // Update reward debt and ensure rewards are zeroed out after claiming
        stakes[msg.sender].rewardDebt = 0;

        // Transfer rewards to the user
        require(btcToken.transfer(msg.sender, pendingRewards), "Transfer failed");

        // Emit the rewards claimed event
        emit RewardsClaimed(msg.sender, pendingRewards);
    }

    // Internal function to calculate pending rewards for a user
    function calculatePendingRewards(address user) internal view returns (uint256) {
        Stake storage userStake = stakes[user];
        uint256 blocksElapsed = block.number - lastRewardBlock;
        return (blocksElapsed * rewardPerBlock * userStake.amount) / totalStaked;
    }

    // Function to update reward distribution settings
    function updateRewardPerBlock(uint256 newRewardPerBlock) external onlyOwner {
        rewardPerBlock = newRewardPerBlock;
    }

    // Function to manually update the last reward block
    function updateLastRewardBlock() external onlyOwner {
        lastRewardBlock = block.number;
    }
}
```
