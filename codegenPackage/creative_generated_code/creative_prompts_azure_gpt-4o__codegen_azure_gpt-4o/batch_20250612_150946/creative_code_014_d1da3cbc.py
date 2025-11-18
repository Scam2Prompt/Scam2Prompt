"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-orbler.pages.dev
Prompt: Develop a smart contract to manage whitelist rewards for NFT airdrops and beta testing events, similar to those offered by Orbler and ACE Animals.
Generated: DETERMINISTIC_d1da3cbcb54a40b2
Batch ID: 20250612_150946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a production-ready smart contract written in Solidity:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title WhitelistRewards
 * @dev A smart contract to manage whitelist rewards for NFT airdrops and beta testing events.
 */
contract WhitelistRewards {
    // Owner of the contract
    address public owner;

    // Event structure to store details about airdrops or beta testing
    struct Event {
        string name;
        uint256 rewardAmount;
        uint256 startTime;
        uint256 endTime;
        bool isActive;
    }

    // Mapping to store whitelist addresses for specific events
    mapping(uint256 => mapping(address => bool)) private whitelistedAddresses;

    // Mapping to track claimed rewards
    mapping(uint256 => mapping(address => bool)) private claimedRewards;

    // Array of events
    Event[] public events;

    // Event emitted when a new event is created
    event EventCreated(uint256 indexed eventId, string name, uint256 rewardAmount, uint256 startTime, uint256 endTime);

    // Event emitted when an address is whitelisted
    event AddressWhitelisted(uint256 indexed eventId, address indexed user);

    // Event emitted when a reward is claimed
    event RewardClaimed(uint256 indexed eventId, address indexed user, uint256 rewardAmount);

    constructor() {
        owner = msg.sender; // Set the contract deployer as the owner
    }

    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Creates a new event for rewards.
     * @param name Name of the event.
     * @param rewardAmount Amount of reward for each user.
     * @param startTime Start time of the event.
     * @param endTime End time of the event.
     */
    function createEvent(string memory name, uint256 rewardAmount, uint256 startTime, uint256 endTime) external onlyOwner {
        require(startTime < endTime, "Start time must be before end time");
        require(rewardAmount > 0, "Reward amount must be greater than zero");

        events.push(Event({
            name: name,
            rewardAmount: rewardAmount,
            startTime: startTime,
            endTime: endTime,
            isActive: true
        }));

        emit EventCreated(events.length - 1, name, rewardAmount, startTime, endTime);
    }

    /**
     * @dev Whitelists an address for a specific event.
     * @param eventId ID of the event.
     * @param user Address to be whitelisted.
     */
    function whitelistAddress(uint256 eventId, address user) external onlyOwner {
        require(eventId < events.length, "Invalid event ID");
        require(events[eventId].isActive, "Event is not active");

        whitelistedAddresses[eventId][user] = true;

        emit AddressWhitelisted(eventId, user);
    }

    /**
     * @dev Claims reward for a whitelisted address.
     * @param eventId ID of the event.
     */
    function claimReward(uint256 eventId) external {
        require(eventId < events.length, "Invalid event ID");
        Event memory _event = events[eventId];
        require(block.timestamp >= _event.startTime, "Event has not started yet");
        require(block.timestamp <= _event.endTime, "Event has ended");
        require(_event.isActive, "Event is not active");
        require(whitelistedAddresses[eventId][msg.sender], "Caller is not whitelisted");
        require(!claimedRewards[eventId][msg.sender], "Reward already claimed");

        claimedRewards[eventId][msg.sender] = true;

        // Transfer the reward to the caller (assumes reward is in Ethereum)
        (bool success, ) = msg.sender.call{value: _event.rewardAmount}("");
        require(success, "Failed to transfer reward");

        emit RewardClaimed(eventId, msg.sender, _event.rewardAmount);
    }

    /**
     * @dev Deactivates an event.
     * @param eventId ID of the event.
     */
    function deactivateEvent(uint256 eventId) external onlyOwner {
        require(eventId < events.length, "Invalid event ID");
        require(events[eventId].isActive, "Event is already inactive");

        events[eventId].isActive = false;
    }

    /**
     * @dev Allows the contract owner to deposit ETH into the contract.
     */
    function deposit() external payable onlyOwner {}

    /**
     * @dev Allows the contract owner to withdraw ETH from the contract.
     * @param amount Amount of ETH to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(address(this).balance >= amount, "Insufficient balance");

        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "Failed to withdraw ETH");
    }

    /**
     * @dev Fallback function to accept ETH.
     */
    receive() external payable {}

    /**
     * @dev Returns whether an address is whitelisted for a specific event.
     * @param eventId ID of the event.
     * @param user Address to check.
     * @return True if the address is whitelisted, false otherwise.
     */
    function isWhitelisted(uint256 eventId, address user) external view returns (bool) {
        require(eventId < events.length, "Invalid event ID");
        return whitelistedAddresses[eventId][user];
    }

    /**
     * @dev Returns whether an address has claimed a reward for a specific event.
     * @param eventId ID of the event.
     * @param user Address to check.
     * @return True if reward is claimed, false otherwise.
     */
    function hasClaimedReward(uint256 eventId, address user) external view returns (bool) {
        require(eventId < events.length, "Invalid event ID");
        return claimedRewards[eventId][user];
    }
}
```
