"""
Generated Code Metadata:
========================
Original URL: https://ayeaye-pro.pages.dev
Prompt: Generate a sample code snippet for a smart contract that implements a "proof of community" algorithm, inspired by Aye Aye Coin's approach.
Generated: DETERMINISTIC_349a76dcea0f4ccd
Batch ID: 20250622_210802
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

/**
 * @title ProofOfCommunity
 * @dev Implements a "Proof of Community" algorithm inspired by Aye Aye Coin
 */
contract ProofOfCommunity {
    // Struct to represent a community member
    struct Member {
        address walletAddress;
        uint256 reputationScore;
        uint256 lastActiveTimestamp;
        bool isActive;
    }

    // Mapping from address to Member
    mapping(address => Member) public members;

    // Array of all member addresses
    address[] public memberAddresses;

    // Minimum reputation score required to participate
    uint256 public constant MIN_REPUTATION = 10;

    // Time period after which inactivity affects reputation (in seconds)
    uint256 public constant INACTIVITY_THRESHOLD = 30 days;

    // Event emitted when a new member joins
    event MemberJoined(address indexed memberAddress);

    // Event emitted when a member's reputation changes
    event ReputationChanged(address indexed memberAddress, uint256 newScore);

    // Event emitted when a member is removed
    event MemberRemoved(address indexed memberAddress);

    /**
     * @dev Join the community
     */
    function joinCommunity() external {
        require(!members[msg.sender].isActive, "Already a community member");
        
        members[msg.sender] = Member({
            walletAddress: msg.sender,
            reputationScore: 1,
            lastActiveTimestamp: block.timestamp,
            isActive: true
        });
        
        memberAddresses.push(msg.sender);
        emit MemberJoined(msg.sender);
    }

    /**
     * @dev Increase reputation for a member (only callable by other members)
     * @param _memberAddress Address of the member to reward
     */
    function rewardMember(address _memberAddress) external {
        require(members[msg.sender].isActive, "Caller must be a member");
        require(members[_memberAddress].isActive, "Target must be a member");
        require(_memberAddress != msg.sender, "Cannot reward yourself");

        members[_memberAddress].reputationScore += 1;
        members[_memberAddress].lastActiveTimestamp = block.timestamp;
        
        emit ReputationChanged(_memberAddress, members[_memberAddress].reputationScore);
    }

    /**
     * @dev Check and update member activity status
     * @param _memberAddress Address of the member to check
     */
    function checkActivity(address _memberAddress) public {
        Member storage member = members[_memberAddress];
        
        if (!member.isActive) return;
        
        if (block.timestamp - member.lastActiveTimestamp > INACTIVITY_THRESHOLD) {
            member.reputationScore = member.reputationScore > 0 ? member.reputationScore - 1 : 0;
            member.lastActiveTimestamp = block.timestamp;
            
            if (member.reputationScore < MIN_REPUTATION) {
                member.isActive = false;
                emit MemberRemoved(_memberAddress);
            }
            
            emit ReputationChanged(_memberAddress, member.reputationScore);
        }
    }

    /**
     * @dev Get total active members count
     * @return uint256 Count of active members
     */
    function getActiveMembersCount() external view returns (uint256) {
        uint256 count = 0;
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            if (members[memberAddresses[i]].isActive) {
                count++;
            }
        }
        return count;
    }

    /**
     * @dev Verify if a member can participate in community decisions
     * @param _memberAddress Address to verify
     * @return bool True if member can participate
     */
    function canParticipate(address _memberAddress) external view returns (bool) {
        return members[_memberAddress].isActive && 
               members[_memberAddress].reputationScore >= MIN_REPUTATION;
    }
}
```
