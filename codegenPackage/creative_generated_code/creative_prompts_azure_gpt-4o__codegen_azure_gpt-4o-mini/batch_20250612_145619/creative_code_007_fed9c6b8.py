"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bac-games.vercel.app
Prompt: Develop a smart contract for managing Blast Auto Clubs in the BAC ecosystem, ensuring compliance with Ethereum standards.
Generated: DETERMINISTIC_fed9c6b88032597c
Batch ID: 20250612_145619
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

/// @title Blast Auto Clubs (BAC) Smart Contract
/// @author Your Name
/// @notice This contract manages memberships and activities of Blast Auto Clubs in the BAC ecosystem
/// @dev This contract complies with the Ethereum standards

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract BlastAutoClub is Ownable {
    using Counters for Counters.Counter;

    // Struct to represent a member
    struct Member {
        uint256 id;
        address account;
        uint256 joinedAt;
        bool isActive;
    }

    // Mapping of member ID to Member details
    mapping(uint256 => Member) private members;
    // Counter for member IDs
    Counters.Counter private memberIdCounter;

    // Event to log new membership
    event MemberAdded(uint256 indexed memberId, address indexed account);
    // Event to log membership deactivation
    event MemberDeactivated(uint256 indexed memberId, address indexed account);

    /// @notice Adds a new member to the Blast Auto Club
    /// @param _account The address of the new member
    function addMember(address _account) external onlyOwner {
        require(_account != address(0), "Invalid address");
        uint256 newMemberId = memberIdCounter.current();
        members[newMemberId] = Member(newMemberId, _account, block.timestamp, true);
        memberIdCounter.increment();
        emit MemberAdded(newMemberId, _account);
    }

    /// @notice Deactivates a member in the Blast Auto Club
    /// @param _memberId The ID of the member to deactivate
    function deactivateMember(uint256 _memberId) external onlyOwner {
        Member storage member = members[_memberId];
        require(member.isActive, "Member is already inactive");
        member.isActive = false;
        emit MemberDeactivated(_memberId, member.account);
    }

    /// @notice Gets details of a member by ID
    /// @param _memberId The ID of the member
    /// @return account The address of the member
    /// @return joinedAt The timestamp of when the member joined
    /// @return isActive The active status of the member
    function getMember(uint256 _memberId) external view returns (address account, uint256 joinedAt, bool isActive) {
        Member memory member = members[_memberId];
        require(member.account != address(0), "Member does not exist");
        return (member.account, member.joinedAt, member.isActive);
    }

    /// @notice Returns the total number of members
    /// @return totalMembers Total member count
    function totalMembers() external view returns (uint256) {
        return memberIdCounter.current();
    }
}
```
