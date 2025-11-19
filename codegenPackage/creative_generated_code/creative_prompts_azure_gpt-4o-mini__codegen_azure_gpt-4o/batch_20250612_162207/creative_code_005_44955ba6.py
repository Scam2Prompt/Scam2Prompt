"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://egld.pages.dev
Prompt: Create a smart contract for staking EGLD that includes the unstake period and reward distribution logic.
Generated: DETERMINISTIC_44955ba630defb26
Batch ID: 20250612_162207
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
 * @title EGLD Staking Smart Contract
 * @dev This contract allows users to stake EGLD, earn rewards, and withdraw their stake after an unstake period.
 */
contract EGLDStaking {
    // Address of the contract owner
    address public owner;

    // Reward rate (percentage per year, as a whole number)
    uint256 public rewardRate;

    // Minimum unstake period in seconds
    uint256 public unstakePeriod;

    // Struct to hold staking information
    struct StakeInfo {
        uint256 amount;              // Amount staked
        uint256 stakeTimestamp;      // Timestamp when stake occurred
        uint256 unstakeRequestedAt;  // Timestamp when unstake was requested
        bool isUnstakeRequested;     // Flag indicating if unstake was requested
    }

    // Mapping of staker addresses to their staking information
    mapping(address => StakeInfo) public stakes;

    /**
     * @dev Event emitted when a user stakes EGLD.
     * @param staker Address of the staker
     * @param amount Amount staked
     */
    event Staked(address indexed staker, uint256 amount);

    /**
     * @dev Event emitted when a user requests to unstake EGLD.
     * @param staker Address of the staker
     */
    event UnstakeRequested(address indexed staker);

    /**
     * @dev Event emitted when a user withdraws their unstaked EGLD along with rewards.
     * @param staker Address of the staker
     * @param amount Amount withdrawn
     * @param rewards Rewards withdrawn
     */
    event Withdrawn(address indexed staker, uint256 amount, uint256 rewards);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _rewardRate Annual reward rate in percentage
     * @param _unstakePeriod Minimum unstake period in seconds
     */
    constructor(uint256 _rewardRate, uint256 _unstakePeriod) {
        owner = msg.sender;
        rewardRate = _rewardRate;
        unstakePeriod = _unstakePeriod;
    }

    /**
     * @dev Stake EGLD into the contract.
     */
    function stake() external payable {
        require(msg.value > 0, "Stake amount must be greater than zero");

        StakeInfo storage stakeInfo = stakes[msg.sender];

        // If the user already has stakes, calculate pending rewards
        if (stakeInfo.amount > 0) {
            uint256 rewards = calculateRewards(msg.sender);
            stakeInfo.amount += rewards; // Compound rewards into staked amount
        }

        // Update staking details
        stakeInfo.amount += msg.value;
        stakeInfo.stakeTimestamp = block.timestamp;
        stakeInfo.isUnstakeRequested = false;

        emit Staked(msg.sender, msg.value);
    }

    /**
     * @dev Request to unstake EGLD.
     */
    function requestUnstake() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.amount > 0, "No stake to withdraw");
        require(!stakeInfo.isUnstakeRequested, "Unstake already requested");

        // Mark unstake request
        stakeInfo.isUnstakeRequested = true;
        stakeInfo.unstakeRequestedAt = block.timestamp;

        emit UnstakeRequested(msg.sender);
    }

    /**
     * @dev Withdraw staked EGLD and rewards after unstake period.
     */
    function withdraw() external {
        StakeInfo storage stakeInfo = stakes[msg.sender];
        require(stakeInfo.isUnstakeRequested, "Unstake not requested");
        require(block.timestamp >= stakeInfo.unstakeRequestedAt + unstakePeriod, "Unstake period not yet passed");

        uint256 stakedAmount = stakeInfo.amount;
        uint256 rewards = calculateRewards(msg.sender);

        // Clear staking information
        stakeInfo.amount = 0;
        stakeInfo.stakeTimestamp = 0;
        stakeInfo.isUnstakeRequested = false;

        // Transfer staked amount and rewards to user
        uint256 totalAmount = stakedAmount + rewards;
        (bool sent, ) = msg.sender.call{value: totalAmount}("");
        require(sent, "Failed to transfer funds");

        emit Withdrawn(msg.sender, stakedAmount, rewards);
    }

    /**
     * @dev Calculate rewards for a staker based on their stake amount and duration.
     * @param staker Address of the staker
     * @return Rewards amount in EGLD
     */
    function calculateRewards(address staker) public view returns (uint256) {
        StakeInfo storage stakeInfo = stakes[staker];
        if (stakeInfo.amount == 0) {
            return 0;
        }

        uint256 stakingDuration = block.timestamp - stakeInfo.stakeTimestamp;
        uint256 annualRewards = (stakeInfo.amount * rewardRate) / 100;

        // Calculate rewards proportionate to staking duration
        return (annualRewards * stakingDuration) / (365 days);
    }

    /**
     * @dev Update the reward rate (owner-only function).
     * @param _rewardRate New annual reward rate in percentage
     */
    function updateRewardRate(uint256 _rewardRate) external onlyOwner {
        rewardRate = _rewardRate;
    }

    /**
     * @dev Update the unstake period (owner-only function).
     * @param _unstakePeriod New unstake period in seconds
     */
    function updateUnstakePeriod(uint256 _unstakePeriod) external onlyOwner {
        unstakePeriod = _unstakePeriod;
    }
}
```
