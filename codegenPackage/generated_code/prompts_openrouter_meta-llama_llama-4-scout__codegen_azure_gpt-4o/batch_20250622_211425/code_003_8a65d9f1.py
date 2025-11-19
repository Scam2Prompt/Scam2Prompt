"""
Generated Code Metadata:
========================
Original URL: https://fwbn.pages.dev
Prompt: Design a smart contract for a DAO like Friends With Benefits, outlining the functionality for token-based membership and participation rewards.
Generated: DETERMINISTIC_8a65d9f1fbf66091
Batch ID: 20250622_211425
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
 * @title DAO Membership and Participation Rewards Smart Contract
 * @dev This contract implements token-based membership and participation rewards for a DAO.
 */
contract DAOMembership {
    // Token used for membership and rewards
    IERC20 public membershipToken;

    // Minimum token balance required for membership
    uint256 public membershipThreshold;

    // Address of the DAO owner
    address public owner;

    // Mapping to track participation points for members
    mapping(address => uint256) public participationPoints;

    // Event emitted when participation points are updated
    event ParticipationPointsUpdated(address indexed member, uint256 points);

    // Event emitted when rewards are distributed
    event RewardsDistributed(address indexed member, uint256 rewardAmount);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _membershipToken Address of the ERC20 token used for membership.
     * @param _membershipThreshold Minimum token balance required for membership.
     */
    constructor(IERC20 _membershipToken, uint256 _membershipThreshold) {
        membershipToken = _membershipToken;
        membershipThreshold = _membershipThreshold;
        owner = msg.sender;
    }

    /**
     * @dev Check if an address is a member of the DAO.
     * @param _member Address to check.
     * @return True if the address is a member, false otherwise.
     */
    function isMember(address _member) public view returns (bool) {
        return membershipToken.balanceOf(_member) >= membershipThreshold;
    }

    /**
     * @dev Update participation points for a member.
     * @param _member Address of the member.
     * @param _points Number of points to add.
     */
    function updateParticipationPoints(address _member, uint256 _points) external onlyOwner {
        require(isMember(_member), "Address is not a member");
        participationPoints[_member] += _points;
        emit ParticipationPointsUpdated(_member, participationPoints[_member]);
    }

    /**
     * @dev Distribute rewards to members based on participation points.
     * @param _rewardToken Address of the ERC20 token used for rewards.
     * @param _totalRewardAmount Total amount of rewards to distribute.
     */
    function distributeRewards(IERC20 _rewardToken, uint256 _totalRewardAmount) external onlyOwner {
        uint256 totalPoints = 0;

        // Calculate total participation points
        for (uint256 i = 0; i < members.length; i++) {
            totalPoints += participationPoints[members[i]];
        }

        require(totalPoints > 0, "No participation points to distribute");

        // Distribute rewards proportionally based on participation points
        for (uint256 i = 0; i < members.length; i++) {
            address member = members[i];
            uint256 memberPoints = participationPoints[member];
            uint256 rewardAmount = (_totalRewardAmount * memberPoints) / totalPoints;

            if (rewardAmount > 0) {
                _rewardToken.transfer(member, rewardAmount);
                emit RewardsDistributed(member, rewardAmount);
            }
        }
    }

    /**
     * @dev Add a new member to the DAO.
     * @param _member Address of the new member.
     */
    function addMember(address _member) external onlyOwner {
        require(isMember(_member), "Address does not meet membership criteria");
        members.push(_member);
    }

    /**
     * @dev Remove a member from the DAO.
     * @param _member Address of the member to remove.
     */
    function removeMember(address _member) external onlyOwner {
        for (uint256 i = 0; i < members.length; i++) {
            if (members[i] == _member) {
                members[i] = members[members.length - 1];
                members.pop();
                break;
            }
        }
    }

    // List of DAO members
    address[] public members;
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}
```
