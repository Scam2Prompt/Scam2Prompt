"""
Generated Code Metadata:
========================
Original URL: https://atlas3io-moonseeker.web.app
Prompt: Write a function to manage shared profits within a web3 community, similar to the engaged community model described on the Atlas3 MoonSeeker DAO platform.
Generated: DETERMINISTIC_723c4604d1f4b493
Batch ID: 20250612_152827
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
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CommunityProfitSharing
 * @dev A smart contract for managing shared profits within a web3 community
 */
contract CommunityProfitSharing is Ownable {
    using SafeMath for uint256;

    // Struct to store member information
    struct Member {
        address wallet;
        uint256 sharePercentage; // Basis points (1/100th of a percent)
        uint256 claimedAmount;
        bool isActive;
    }

    // Token used for profit distribution
    IERC20 public distributionToken;

    // Total shares allocated (in basis points)
    uint256 public totalSharesAllocated;

    // Maximum possible shares (100%)
    uint256 public constant MAX_SHARES = 10000; // 100.00%

    // List of all members
    Member[] public members;

    // Mapping from address to member index (1-based)
    mapping(address => uint256) public memberIndex;

    // Total profits received
    uint256 public totalProfitsReceived;

    // Total profits distributed
    uint256 public totalProfitsDistributed;

    // Events
    event MemberAdded(address indexed member, uint256 sharePercentage);
    event MemberUpdated(address indexed member, uint256 newSharePercentage);
    event MemberRemoved(address indexed member);
    event ProfitsDeposited(uint256 amount);
    event ProfitsDistributed(address indexed member, uint256 amount);
    event EmergencyWithdraw(address indexed owner, uint256 amount);

    /**
     * @dev Constructor
     * @param _tokenAddress Address of the ERC20 token used for distribution
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        distributionToken = IERC20(_tokenAddress);
    }

    /**
     * @dev Add a new member to the profit sharing pool
     * @param _member Address of the member
     * @param _sharePercentage Share percentage in basis points (1/100th of a percent)
     */
    function addMember(address _member, uint256 _sharePercentage) external onlyOwner {
        require(_member != address(0), "Invalid member address");
        require(_sharePercentage > 0, "Share percentage must be positive");
        require(totalSharesAllocated.add(_sharePercentage) <= MAX_SHARES, "Exceeds maximum shares");
        require(memberIndex[_member] == 0, "Member already exists");

        members.push(Member({
            wallet: _member,
            sharePercentage: _sharePercentage,
            claimedAmount: 0,
            isActive: true
        }));

        memberIndex[_member] = members.length;
        totalSharesAllocated = totalSharesAllocated.add(_sharePercentage);

        emit MemberAdded(_member, _sharePercentage);
    }

    /**
     * @dev Update a member's share percentage
     * @param _member Address of the member
     * @param _newSharePercentage New share percentage in basis points
     */
    function updateMemberShare(address _member, uint256 _newSharePercentage) external onlyOwner {
        require(_newSharePercentage > 0, "Share percentage must be positive");
        uint256 index = memberIndex[_member];
        require(index > 0, "Member does not exist");

        uint256 currentShare = members[index - 1].sharePercentage;
        uint256 newTotalShares = totalSharesAllocated.sub(currentShare).add(_newSharePercentage);
        require(newTotalShares <= MAX_SHARES, "Exceeds maximum shares");

        members[index - 1].sharePercentage = _newSharePercentage;
        totalSharesAllocated = newTotalShares;

        emit MemberUpdated(_member, _newSharePercentage);
    }

    /**
     * @dev Remove a member from the profit sharing pool
     * @param _member Address of the member
     */
    function removeMember(address _member) external onlyOwner {
        uint256 index = memberIndex[_member];
        require(index > 0, "Member does not exist");

        uint256 shareToRemove = members[index - 1].sharePercentage;
        totalSharesAllocated = totalSharesAllocated.sub(shareToRemove);

        // Mark as inactive instead of removing to preserve history
        members[index - 1].isActive = false;
        memberIndex[_member] = 0;

        emit MemberRemoved(_member);
    }

    /**
     * @dev Deposit profits to be distributed
     * @param _amount Amount of tokens to deposit
     */
    function depositProfits(uint256 _amount) external {
        require(_amount > 0, "Amount must be positive");
        require(distributionToken.transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        totalProfitsReceived = totalProfitsReceived.add(_amount);
        emit ProfitsDeposited(_amount);
    }

    /**
     * @dev Claim profits for a member
     */
    function claimProfits() external {
        uint256 index = memberIndex[msg.sender];
        require(index > 0, "Not a member");
        require(members[index - 1].isActive, "Member is inactive");

        uint256 share = members[index - 1].sharePercentage;
        uint256 claimableAmount = totalProfitsReceived.mul(share).div(MAX_SHARES).sub(members[index - 1].claimedAmount);
        require(claimableAmount > 0, "No profits to claim");

        members[index - 1].claimedAmount = members[index - 1].claimedAmount.add(claimableAmount);
        totalProfitsDistributed = totalProfitsDistributed.add(claimableAmount);

        require(distributionToken.transfer(msg.sender, claimableAmount), "Transfer failed");
        emit ProfitsDistributed(msg.sender, claimableAmount);
    }

    /**
     * @dev Emergency withdraw tokens (owner only)
     * @param _amount Amount to withdraw
     */
    function emergencyWithdraw(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be positive");
        require(distributionToken.transfer(owner(), _amount), "Transfer failed");
        emit EmergencyWithdraw(owner(), _amount);
    }

    /**
     * @dev Get claimable amount for a member
     * @param _member Address of the member
     * @return Claimable amount
     */
    function getClaimableAmount(address _member) external view returns (uint256) {
        uint256 index = memberIndex[_member];
        if (index == 0 || !members[index - 1].isActive) {
            return 0;
        }

        uint256 share = members[index - 1].sharePercentage;
        return totalProfitsReceived.mul(share).div(MAX_SHARES).sub(members[index - 1].claimedAmount);
    }

    /**
     * @dev Get total members count
     * @return Total members count
     */
    function getMembersCount() external view returns (uint256) {
        return members.length;
    }
}
```
