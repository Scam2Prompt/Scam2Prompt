"""
Generated Code Metadata:
========================
Original URL: https://purplepepesolana.pages.dev
Prompt: Develop a smart contract for $PURPE token transactions that includes features for community event participation and rewards distribution.
Generated: DETERMINISTIC_3dfba0d7a9b05a44
Batch ID: 20250612_145506
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract PURPEToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event structure
    struct CommunityEvent {
        uint256 id;
        string name;
        uint256 rewardAmount;
        uint256 startTime;
        uint256 endTime;
        uint256 maxParticipants;
        uint256 participantCount;
        bool isActive;
        mapping(address => bool) participants;
    }

    // Mapping of event ID to CommunityEvent
    mapping(uint256 => CommunityEvent) public events;

    // Counter for event IDs
    uint256 public eventCounter;

    // Reward distribution address
    address public rewardDistributionAddress;

    // Events
    event EventCreated(
        uint256 indexed eventId,
        string name,
        uint256 rewardAmount,
        uint256 startTime,
        uint256 endTime,
        uint256 maxParticipants
    );
    event EventParticipated(uint256 indexed eventId, address participant);
    event RewardDistributed(uint256 indexed eventId, address participant, uint256 amount);
    event RewardAddressUpdated(address newAddress);

    constructor(uint256 initialSupply) ERC20("PURPE Token", "PURPE") {
        _mint(msg.sender, initialSupply);
        rewardDistributionAddress = msg.sender;
        eventCounter = 1;
    }

    /**
     * @dev Create a new community event
     */
    function createEvent(
        string memory name,
        uint256 rewardAmount,
        uint256 startTime,
        uint256 endTime,
        uint256 maxParticipants
    ) external onlyOwner {
        require(startTime < endTime, "Invalid event duration");
        require(rewardAmount > 0, "Reward amount must be positive");

        uint256 eventId = eventCounter;
        CommunityEvent storage newEvent = events[eventId];
        
        newEvent.id = eventId;
        newEvent.name = name;
        newEvent.rewardAmount = rewardAmount;
        newEvent.startTime = startTime;
        newEvent.endTime = endTime;
        newEvent.maxParticipants = maxParticipants;
        newEvent.participantCount = 0;
        newEvent.isActive = true;

        eventCounter++;

        emit EventCreated(eventId, name, rewardAmount, startTime, endTime, maxParticipants);
    }

    /**
     * @dev Participate in an event
     */
    function participateInEvent(uint256 eventId) external {
        CommunityEvent storage communityEvent = events[eventId];
        
        require(communityEvent.isActive, "Event is not active");
        require(block.timestamp >= communityEvent.startTime, "Event has not started");
        require(block.timestamp <= communityEvent.endTime, "Event has ended");
        require(!communityEvent.participants[msg.sender], "Already participated");
        require(
            communityEvent.participantCount < communityEvent.maxParticipants,
            "Event is full"
        );

        communityEvent.participants[msg.sender] = true;
        communityEvent.participantCount++;

        emit EventParticipated(eventId, msg.sender);
    }

    /**
     * @dev Distribute rewards for an event
     */
    function distributeRewards(uint256 eventId) external onlyOwner {
        CommunityEvent storage communityEvent = events[eventId];
        
        require(block.timestamp > communityEvent.endTime, "Event not ended yet");
        require(communityEvent.isActive, "Event rewards already distributed");

        uint256 totalRewards = communityEvent.rewardAmount.mul(communityEvent.participantCount);
        require(
            balanceOf(rewardDistributionAddress) >= totalRewards,
            "Insufficient reward funds"
        );

        communityEvent.isActive = false;

        // Transfer rewards to participants
        for (uint256 i = 0; i < eventCounter; i++) {
            if (events[i].id == eventId) {
                CommunityEvent storage e = events[i];
                for (uint256 j = 0; j < e.participantCount; j++) {
                    address participant = e.participants[msg.sender] ? msg.sender : address(0);
                    if (participant != address(0)) {
                        _transfer(rewardDistributionAddress, participant, e.rewardAmount);
                        emit RewardDistributed(eventId, participant, e.rewardAmount);
                    }
                }
                break;
            }
        }
    }

    /**
     * @dev Update reward distribution address
     */
    function setRewardDistributionAddress(address newAddress) external onlyOwner {
        require(newAddress != address(0), "Invalid address");
        rewardDistributionAddress = newAddress;
        emit RewardAddressUpdated(newAddress);
    }

    /**
     * @dev Mint new tokens (only owner)
     */
    function mint(address to, uint256 amount) external onlyOwner {
        _mint(to, amount);
    }

    /**
     * @dev Burn tokens (only owner)
     */
    function burn(address from, uint256 amount) external onlyOwner {
        _burn(from, amount);
    }
}
```
