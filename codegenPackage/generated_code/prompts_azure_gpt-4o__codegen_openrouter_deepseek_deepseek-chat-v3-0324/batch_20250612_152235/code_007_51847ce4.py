"""
Generated Code Metadata:
========================
Original URL: https://paal-ai.pages.dev
Prompt: Generate code to track and log staking activity, including APR changes and ETH rewards share updates, for the Paal AI staking platform.
Generated: DETERMINISTIC_51847ce40598dd19
Batch ID: 20250612_152235
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PaalStakingLogger is Ownable {
    using SafeMath for uint256;

    // Struct to represent a staking event
    struct StakingEvent {
        address user;
        uint256 amount;
        uint256 timestamp;
        uint256 currentAPR;
        uint256 ethRewardsShare;
        string eventType; // "STAKE", "UNSTAKE", "REWARD", "APR_UPDATE", "REWARDS_SHARE_UPDATE"
    }

    // Struct to represent APR history
    struct APRHistory {
        uint256 oldAPR;
        uint256 newAPR;
        uint256 timestamp;
    }

    // Struct to represent ETH rewards share history
    struct RewardsShareHistory {
        uint256 oldShare;
        uint256 newShare;
        uint256 timestamp;
    }

    // Current APR and ETH rewards share
    uint256 public currentAPR;
    uint256 public currentEthRewardsShare;

    // Mapping to store user staking events
    mapping(address => StakingEvent[]) public userStakingEvents;

    // APR and rewards share history
    APRHistory[] public aprHistory;
    RewardsShareHistory[] public rewardsShareHistory;

    // Events
    event Staked(address indexed user, uint256 amount, uint256 timestamp);
    event Unstaked(address indexed user, uint256 amount, uint256 timestamp);
    event RewardClaimed(address indexed user, uint256 amount, uint256 timestamp);
    event APRUpdated(uint256 oldAPR, uint256 newAPR, uint256 timestamp);
    event RewardsShareUpdated(uint256 oldShare, uint256 newShare, uint256 timestamp);

    constructor(uint256 initialAPR, uint256 initialRewardsShare) {
        currentAPR = initialAPR;
        currentEthRewardsShare = initialRewardsShare;
    }

    /**
     * @dev Log a staking event
     * @param user Address of the user
     * @param amount Amount staked/unstaked/rewarded
     * @param eventType Type of event ("STAKE", "UNSTAKE", "REWARD")
     */
    function logStakingEvent(address user, uint256 amount, string memory eventType) external onlyOwner {
        require(user != address(0), "Invalid user address");
        require(amount > 0, "Amount must be greater than 0");
        
        StakingEvent memory newEvent = StakingEvent({
            user: user,
            amount: amount,
            timestamp: block.timestamp,
            currentAPR: currentAPR,
            ethRewardsShare: currentEthRewardsShare,
            eventType: eventType
        });

        userStakingEvents[user].push(newEvent);

        if (keccak256(bytes(eventType)) == keccak256(bytes("STAKE"))) {
            emit Staked(user, amount, block.timestamp);
        } else if (keccak256(bytes(eventType)) == keccak256(bytes("UNSTAKE"))) {
            emit Unstaked(user, amount, block.timestamp);
        } else if (keccak256(bytes(eventType)) == keccak256(bytes("REWARD"))) {
            emit RewardClaimed(user, amount, block.timestamp);
        }
    }

    /**
     * @dev Update the APR and log the change
     * @param newAPR New APR value
     */
    function updateAPR(uint256 newAPR) external onlyOwner {
        require(newAPR != currentAPR, "New APR must be different from current");

        APRHistory memory history = APRHistory({
            oldAPR: currentAPR,
            newAPR: newAPR,
            timestamp: block.timestamp
        });

        aprHistory.push(history);
        currentAPR = newAPR;

        emit APRUpdated(history.oldAPR, history.newAPR, history.timestamp);
    }

    /**
     * @dev Update the ETH rewards share and log the change
     * @param newShare New ETH rewards share value
     */
    function updateEthRewardsShare(uint256 newShare) external onlyOwner {
        require(newShare != currentEthRewardsShare, "New share must be different from current");

        RewardsShareHistory memory history = RewardsShareHistory({
            oldShare: currentEthRewardsShare,
            newShare: newShare,
            timestamp: block.timestamp
        });

        rewardsShareHistory.push(history);
        currentEthRewardsShare = newShare;

        emit RewardsShareUpdated(history.oldShare, history.newShare, history.timestamp);
    }

    /**
     * @dev Get all staking events for a user
     * @param user Address of the user
     * @return Array of StakingEvent structs
     */
    function getUserStakingEvents(address user) external view returns (StakingEvent[] memory) {
        return userStakingEvents[user];
    }

    /**
     * @dev Get the full APR history
     * @return Array of APRHistory structs
     */
    function getAPRHistory() external view returns (APRHistory[] memory) {
        return aprHistory;
    }

    /**
     * @dev Get the full ETH rewards share history
     * @return Array of RewardsShareHistory structs
     */
    function getRewardsShareHistory() external view returns (RewardsShareHistory[] memory) {
        return rewardsShareHistory;
    }

    /**
     * @dev Get the current staking parameters
     * @return Current APR and ETH rewards share
     */
    function getCurrentParameters() external view returns (uint256, uint256) {
        return (currentAPR, currentEthRewardsShare);
    }
}
```
