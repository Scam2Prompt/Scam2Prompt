"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://smartdappsolution.pages.dev
Prompt: Create a script to enable staking functionality and manage presale-related tasks using the Decentralized Dapps protocol.
Generated: DETERMINISTIC_90d3f5fbfc34c3b7
Batch ID: 20250612_151333
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

/**
 * @title Staking and Presale Management Contract
 * @dev This contract enables staking functionality and manages presale-related tasks using decentralized dApps.
 */
contract StakingPresale {
    // ============================
    // Structs
    // ============================
    struct Stake {
        uint256 amount;       // Amount staked by the user
        uint256 timestamp;    // Time when the user staked
    }

    struct Presale {
        uint256 rate;         // Token rate per ETH
        uint256 hardCap;      // Maximum amount of ETH to be raised
        uint256 raised;       // Total ETH raised so far
        bool active;          // Flag to indicate if presale is active
    }

    // ============================
    // State Variables
    // ============================
    address public owner;                      // Contract owner
    mapping(address => Stake) public stakes;  // Mapping of user addresses to their stakes
    Presale public presaleDetails;            // Presale configuration

    uint256 public rewardRatePerSecond;       // Reward rate for staking (tokens per second)
    mapping(address => uint256) public rewards; // Rewards accrued by each staker

    // ============================
    // Events
    // ============================
    event StakeDeposited(address indexed user, uint256 amount);
    event StakeWithdrawn(address indexed user, uint256 amount);
    event RewardClaimed(address indexed user, uint256 amount);
    event PresaleContribution(address indexed user, uint256 amount);
    event PresaleConfigured(uint256 rate, uint256 hardCap);

    // ============================
    // Modifiers
    // ============================
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier presaleActive() {
        require(presaleDetails.active, "Presale is not active");
        _;
    }

    // ============================
    // Constructor
    // ============================
    constructor(uint256 _rewardRatePerSecond) {
        owner = msg.sender;
        rewardRatePerSecond = _rewardRatePerSecond;
    }

    // ============================
    // Staking functions
    // ============================
    /**
     * @dev Allows users to stake ETH to earn rewards.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        // Update rewards before modifying stake
        _updateRewards(msg.sender);

        stakes[msg.sender].amount += msg.value;
        stakes[msg.sender].timestamp = block.timestamp;

        emit StakeDeposited(msg.sender, msg.value);
    }

    /**
     * @dev Allows users to withdraw their staked ETH.
     */
    function withdrawStake(uint256 amount) external {
        require(stakes[msg.sender].amount >= amount, "Insufficient stake balance");

        // Update rewards before modifying stake
        _updateRewards(msg.sender);

        stakes[msg.sender].amount -= amount;
        payable(msg.sender).transfer(amount);

        emit StakeWithdrawn(msg.sender, amount);
    }

    /**
     * @dev Allows users to claim their accrued rewards.
     */
    function claimRewards() external {
        _updateRewards(msg.sender);

        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards available");

        rewards[msg.sender] = 0;
        // Transfer rewards (in this example, rewards are in ETH for simplicity)
        payable(msg.sender).transfer(reward);

        emit RewardClaimed(msg.sender, reward);
    }

    /**
     * @dev Internal function to calculate and update user's rewards.
     */
    function _updateRewards(address user) internal {
        Stake storage userStake = stakes[user];
        if (userStake.amount > 0) {
            uint256 timeStaked = block.timestamp - userStake.timestamp;
            uint256 accruedReward = timeStaked * rewardRatePerSecond * userStake.amount / 1 ether;
            rewards[user] += accruedReward;
            userStake.timestamp = block.timestamp;
        }
    }

    // ============================
    // Presale functions
    // ============================
    /**
     * @dev Configure presale settings (only owner).
     */
    function configurePresale(uint256 rate, uint256 hardCap) external onlyOwner {
        presaleDetails.rate = rate;
        presaleDetails.hardCap = hardCap;
        presaleDetails.raised = 0;
        presaleDetails.active = true;

        emit PresaleConfigured(rate, hardCap);
    }

    /**
     * @dev Allows users to contribute to the presale.
     */
    function contributeToPresale() external payable presaleActive {
        require(msg.value > 0, "Contribution must be greater than zero");
        require(presaleDetails.raised + msg.value <= presaleDetails.hardCap, "Presale hard cap exceeded");

        presaleDetails.raised += msg.value;

        emit PresaleContribution(msg.sender, msg.value);
    }

    /**
     * @dev Ends the presale (only owner).
     */
    function endPresale() external onlyOwner {
        presaleDetails.active = false;
    }

    // ============================
    // Fallback function
    // ============================
    /**
     * @dev Fallback function to receive ETH.
     */
    receive() external payable {}
}
```
