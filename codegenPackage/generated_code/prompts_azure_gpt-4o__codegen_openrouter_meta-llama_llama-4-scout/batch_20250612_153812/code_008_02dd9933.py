"""
Generated Code Metadata:
========================
Original URL: https://cheemspet.web.app
Prompt: Create a Solidity smart contract that implements a treasury management system inspired by Trader Cheems' skills, allowing for team revenue increase and treasury management.
Generated: DETERMINISTIC_02dd9933d8e65de5
Batch ID: 20250612_153812
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title Treasury Management System
 * @author [Your Name]
 * @notice Inspired by Trader Cheems' skills, this contract allows for team revenue increase and treasury management.
 */
contract TreasuryManagementSystem is Ownable {
    using SafeMath for uint256;

    // Mapping of team members and their shares
    mapping(address => uint256) public teamMembers;

    // Mapping of revenue streams and their balances
    mapping(string => uint256) public revenueStreams;

    // Total revenue
    uint256 public totalRevenue;

    // Treasury address
    address public treasury;

    // Event emitted when a team member is added
    event TeamMemberAdded(address indexed member, uint256 share);

    // Event emitted when a team member's share is updated
    event TeamMemberShareUpdated(address indexed member, uint256 newShare);

    // Event emitted when a revenue stream is added
    event RevenueStreamAdded(string indexed stream, uint256 balance);

    // Event emitted when revenue is added to a stream
    event RevenueAdded(string indexed stream, uint256 amount);

    // Event emitted when revenue is distributed to team members
    event RevenueDistributed(address indexed member, uint256 amount);

    /**
     * @notice Constructor
     * @param _treasury Treasury address
     */
    constructor(address _treasury) public {
        require(_treasury != address(0), "Treasury address cannot be zero");
        treasury = _treasury;
    }

    /**
     * @notice Add a team member
     * @param _member Team member address
     * @param _share Team member share
     */
    function addTeamMember(address _member, uint256 _share) public onlyOwner {
        require(_member != address(0), "Team member address cannot be zero");
        require(_share > 0, "Team member share must be greater than zero");
        teamMembers[_member] = _share;
        emit TeamMemberAdded(_member, _share);
    }

    /**
     * @notice Update a team member's share
     * @param _member Team member address
     * @param _newShare New team member share
     */
    function updateTeamMemberShare(address _member, uint256 _newShare) public onlyOwner {
        require(_member != address(0), "Team member address cannot be zero");
        require(_newShare > 0, "Team member share must be greater than zero");
        teamMembers[_member] = _newShare;
        emit TeamMemberShareUpdated(_member, _newShare);
    }

    /**
     * @notice Add a revenue stream
     * @param _stream Revenue stream name
     * @param _balance Initial revenue stream balance
     */
    function addRevenueStream(string memory _stream, uint256 _balance) public onlyOwner {
        require(bytes(_stream).length > 0, "Revenue stream name cannot be empty");
        require(_balance >= 0, "Revenue stream balance must be non-negative");
        revenueStreams[_stream] = _balance;
        emit RevenueStreamAdded(_stream, _balance);
    }

    /**
     * @notice Add revenue to a stream
     * @param _stream Revenue stream name
     * @param _amount Revenue amount
     */
    function addRevenue(string memory _stream, uint256 _amount) public onlyOwner {
        require(bytes(_stream).length > 0, "Revenue stream name cannot be empty");
        require(_amount > 0, "Revenue amount must be greater than zero");
        revenueStreams[_stream] = revenueStreams[_stream].add(_amount);
        totalRevenue = totalRevenue.add(_amount);
        emit RevenueAdded(_stream, _amount);
    }

    /**
     * @notice Distribute revenue to team members
     */
    function distributeRevenue() public onlyOwner {
        require(totalRevenue > 0, "Total revenue must be greater than zero");
        uint256 totalShare = 0;
        for (address member in teamMembers) {
            totalShare = totalShare.add(teamMembers[member]);
        }
        for (address member in teamMembers) {
            uint256 memberShare = teamMembers[member];
            uint256 distribution = totalRevenue.mul(memberShare).div(totalShare);
            // Transfer distribution to team member
            payable(member).transfer(distribution);
            emit RevenueDistributed(member, distribution);
        }
        totalRevenue = 0;
    }

    /**
     * @notice Withdraw from treasury
     * @param _amount Amount to withdraw
     */
    function withdrawFromTreasury(uint256 _amount) public onlyOwner {
        require(_amount > 0, "Withdrawal amount must be greater than zero");
        require(treasury != address(0), "Treasury address cannot be zero");
        payable(treasury).transfer(_amount);
    }

    /**
     * @notice Get team member share
     * @param _member Team member address
     * @return Team member share
     */
    function getTeamMemberShare(address _member) public view returns (uint256) {
        return teamMembers[_member];
    }

    /**
     * @notice Get revenue stream balance
     * @param _stream Revenue stream name
     * @return Revenue stream balance
     */
    function getRevenueStreamBalance(string memory _stream) public view returns (uint256) {
        return revenueStreams[_stream];
    }
}
```
