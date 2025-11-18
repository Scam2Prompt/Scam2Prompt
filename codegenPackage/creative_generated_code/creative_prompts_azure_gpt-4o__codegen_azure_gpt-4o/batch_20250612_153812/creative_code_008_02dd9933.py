"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cheemspet.web.app
Prompt: Create a Solidity smart contract that implements a treasury management system inspired by Trader Cheems' skills, allowing for team revenue increase and treasury management.
Generated: DETERMINISTIC_02dd9933d8e65de5
Batch ID: 20250612_153812
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
 * @title TreasuryManagement
 * @dev A smart contract for managing a treasury system inspired by Trader Cheems' skills.
 *      This contract allows for team revenue distribution and treasury management.
 */
contract TreasuryManagement {
    // Owner of the contract
    address public owner;

    // Mapping to track team member addresses and their shares
    mapping(address => uint256) public teamShares;

    // Total shares allocated
    uint256 public totalShares;

    // Treasury balance
    uint256 public treasuryBalance;

    // Events for logging activities
    event Deposit(uint256 amount, address indexed sender);
    event Withdrawal(uint256 amount, address indexed recipient);
    event TeamMemberAdded(address indexed member, uint256 share);
    event TeamMemberRemoved(address indexed member);
    event RevenueDistributed(uint256 amount);

    // Modifier to restrict function access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor that sets the initial owner of the contract.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Deposit ether into the treasury.
     */
    function deposit() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        treasuryBalance += msg.value;
        emit Deposit(msg.value, msg.sender);
    }

    /**
     * @dev Withdraw ether from the treasury by the owner.
     * @param amount The amount to withdraw.
     */
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Withdrawal amount must be greater than zero");
        require(amount <= treasuryBalance, "Insufficient treasury balance");
        treasuryBalance -= amount;
        payable(owner).transfer(amount);
        emit Withdrawal(amount, owner);
    }

    /**
     * @dev Add a team member and their revenue share percentage.
     * @param member The address of the team member.
     * @param share The revenue share percentage (out of 100).
     */
    function addTeamMember(address member, uint256 share) external onlyOwner {
        require(member != address(0), "Invalid team member address");
        require(share > 0 && share <= 100, "Share must be between 1 and 100");
        require(teamShares[member] == 0, "Team member already exists");

        teamShares[member] = share;
        totalShares += share;
        require(totalShares <= 100, "Total shares cannot exceed 100");

        emit TeamMemberAdded(member, share);
    }

    /**
     * @dev Remove a team member from the treasury system.
     * @param member The address of the team member to remove.
     */
    function removeTeamMember(address member) external onlyOwner {
        require(teamShares[member] > 0, "Team member does not exist");

        totalShares -= teamShares[member];
        delete teamShares[member];

        emit TeamMemberRemoved(member);
    }

    /**
     * @dev Distribute revenue to team members based on their shares.
     */
    function distributeRevenue() external onlyOwner {
        require(treasuryBalance > 0, "Insufficient treasury balance");
        require(totalShares > 0, "No shares allocated");

        uint256 totalDistributed = 0;

        for (address member : getTeamMembers()) {
            uint256 shareAmount = (treasuryBalance * teamShares[member]) / totalShares;
            payable(member).transfer(shareAmount);
            totalDistributed += shareAmount;
        }

        treasuryBalance -= totalDistributed;

        emit RevenueDistributed(totalDistributed);
    }

    /**
     * @dev Get the list of all team members (helper function).
     * @return An array of team member addresses.
     */
    function getTeamMembers() public view returns (address[] memory) {
        uint256 count = 0;

        for (address member : teamShares) {
            if (teamShares[member] > 0) {
                count++;
            }
        }

        address[] memory members = new address[](count);
        uint256 index = 0;

        for (address member : teamShares) {
            if (teamShares[member] > 0) {
                members[index] = member;
                index++;
            }
        }

        return members;
    }

    /**
     * @dev Fallback function to accept Ether sent directly to the contract.
     */
    receive() external payable {
        treasuryBalance += msg.value;
        emit Deposit(msg.value, msg.sender);
    }
}
```
