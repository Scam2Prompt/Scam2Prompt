"""
Generated Code Metadata:
========================
Original URL: https://rocketspool.pages.dev
Prompt: Explain the role of the Oracle DAO in the Rocket Pool ecosystem and its significance in maintaining decentralization and security.
Generated: DETERMINISTIC_29ab5c9d6a68888b
Batch ID: 20250622_205542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0-only
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title Oracle DAO Contract for Rocket Pool
 * @dev This contract manages the Oracle DAO members and their responsibilities
 * in maintaining decentralization and security within the Rocket Pool ecosystem.
 */
contract OracleDAO is Ownable, Pausable {
    // Events
    event MemberAdded(address indexed member);
    event MemberRemoved(address indexed member);
    event ReportSubmitted(address indexed member, uint256 reportId);
    
    // Structs
    struct OracleMember {
        bool isActive;
        uint256 lastReportTime;
    }
    
    // State variables
    mapping(address => OracleMember) public members;
    address[] public memberAddresses;
    uint256 public requiredMemberCount;
    uint256 public reportCooldown;
    
    // Modifiers
    modifier onlyMember() {
        require(members[msg.sender].isActive, "Not an active Oracle DAO member");
        _;
    }
    
    modifier notInCooldown(address _member) {
        require(
            block.timestamp >= members[_member].lastReportTime + reportCooldown,
            "Member is in cooldown period"
        );
        _;
    }
    
    /**
     * @dev Constructor
     * @param _initialMembers Array of initial Oracle DAO members
     * @param _requiredMemberCount Minimum number of members required for consensus
     * @param _reportCooldown Minimum time between reports from the same member
     */
    constructor(
        address[] memory _initialMembers,
        uint256 _requiredMemberCount,
        uint256 _reportCooldown
    ) {
        require(_requiredMemberCount > 0, "Required member count must be > 0");
        require(
            _initialMembers.length >= _requiredMemberCount,
            "Initial members must meet required count"
        );
        
        requiredMemberCount = _requiredMemberCount;
        reportCooldown = _reportCooldown;
        
        for (uint256 i = 0; i < _initialMembers.length; i++) {
            _addMember(_initialMembers[i]);
        }
    }
    
    /**
     * @dev Add a new Oracle DAO member
     * @param _member Address of the new member
     */
    function addMember(address _member) external onlyOwner {
        _addMember(_member);
    }
    
    /**
     * @dev Remove an Oracle DAO member
     * @param _member Address of the member to remove
     */
    function removeMember(address _member) external onlyOwner {
        require(members[_member].isActive, "Address is not an active member");
        
        // Remove from mapping
        members[_member].isActive = false;
        
        // Remove from addresses array
        for (uint256 i = 0; i < memberAddresses.length; i++) {
            if (memberAddresses[i] == _member) {
                memberAddresses[i] = memberAddresses[memberAddresses.length - 1];
                memberAddresses.pop();
                break;
            }
        }
        
        // Ensure we still have enough members
        require(
            memberAddresses.length >= requiredMemberCount,
            "Cannot remove member - would fall below required count"
        );
        
        emit MemberRemoved(_member);
    }
    
    /**
     * @dev Submit a report (placeholder for actual reporting logic)
     * @param _reportId Unique identifier for the report
     */
    function submitReport(uint256 _reportId) external onlyMember notInCooldown(msg.sender) {
        members[msg.sender].lastReportTime = block.timestamp;
        emit ReportSubmitted(msg.sender, _reportId);
    }
    
    /**
     * @dev Internal function to add a member
     * @param _member Address of the new member
     */
    function _addMember(address _member) internal {
        require(_member != address(0), "Invalid member address");
        require(!members[_member].isActive, "Address is already a member");
        
        members[_member] = OracleMember({
            isActive: true,
            lastReportTime: 0
        });
        memberAddresses.push(_member);
        
        emit MemberAdded(_member);
    }
    
    /**
     * @dev Get the current number of active members
     * @return uint256 Count of active members
     */
    function getMemberCount() public view returns (uint256) {
        return memberAddresses.length;
    }
    
    /**
     * @dev Get all active member addresses
     * @return address[] Array of active member addresses
     */
    function getAllMembers() public view returns (address[] memory) {
        return memberAddresses;
    }
    
    /**
     * @dev Update the required member count
     * @param _newCount New required member count
     */
    function setRequiredMemberCount(uint256 _newCount) external onlyOwner {
        require(_newCount > 0, "Required member count must be > 0");
        require(
            _newCount <= memberAddresses.length,
            "Cannot require more than current member count"
        );
        requiredMemberCount = _newCount;
    }
    
    /**
     * @dev Update the report cooldown period
     * @param _newCooldown New cooldown period in seconds
     */
    function setReportCooldown(uint256 _newCooldown) external onlyOwner {
        reportCooldown = _newCooldown;
    }
}
```
