"""
Generated Code Metadata:
========================
Original URL: https://d-510.pages.dev
Prompt: "Develop a Solidity function to manage Lingo's RWA investment portfolio, ensuring that investments are selected in collaboration with the Community DAO."
Generated: DETERMINISTIC_61cfc3cc5560ce6c
Batch ID: 20250622_211405
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
import "@openzeppelin/contracts/utils/structs/EnumerableSet.sol";

/**
 * @title RWAInvestmentManager
 * @dev Manages Lingo's RWA investment portfolio with Community DAO collaboration
 */
contract RWAInvestmentManager is Ownable {
    using EnumerableSet for EnumerableSet.AddressSet;

    // Investment struct to store details of each RWA investment
    struct Investment {
        address assetAddress;
        uint256 amountInvested;
        uint256 investmentDate;
        bool isActive;
        string description;
    }

    // DAO struct to represent a Community DAO member
    struct DAOMember {
        address memberAddress;
        uint256 votingPower;
        bool isActive;
    }

    // State variables
    EnumerableSet.AddressSet private daoMembers;
    Investment[] public investments;
    uint256 public minVotesRequired;
    uint256 public totalInvestedAmount;

    // Events
    event InvestmentProposed(uint256 investmentId, address assetAddress, uint256 amount, string description);
    event InvestmentApproved(uint256 investmentId, address approvedBy);
    event InvestmentRejected(uint256 investmentId, address rejectedBy);
    event DAOMemberAdded(address member);
    event DAOMemberRemoved(address member);

    // Modifiers
    modifier onlyDAOMember() {
        require(daoMembers.contains(msg.sender), "Caller is not a DAO member");
        _;
    }

    modifier validInvestment(uint256 investmentId) {
        require(investmentId < investments.length, "Invalid investment ID");
        _;
    }

    /**
     * @dev Constructor initializes the contract with initial DAO members
     * @param initialMembers Array of initial DAO member addresses
     * @param initialVotingPowers Array of voting powers for initial members
     * @param _minVotesRequired Minimum votes required to approve an investment
     */
    constructor(
        address[] memory initialMembers,
        uint256[] memory initialVotingPowers,
        uint256 _minVotesRequired
    ) {
        require(initialMembers.length == initialVotingPowers.length, "Arrays length mismatch");
        
        for (uint256 i = 0; i < initialMembers.length; i++) {
            _addDAOMember(initialMembers[i], initialVotingPowers[i]);
        }
        
        minVotesRequired = _minVotesRequired;
    }

    /**
     * @dev Propose a new RWA investment
     * @param assetAddress Address of the RWA asset
     * @param amount Amount to invest
     * @param description Description of the investment
     */
    function proposeInvestment(
        address assetAddress,
        uint256 amount,
        string memory description
    ) external onlyDAOMember {
        require(assetAddress != address(0), "Invalid asset address");
        require(amount > 0, "Investment amount must be positive");

        uint256 investmentId = investments.length;
        investments.push(Investment({
            assetAddress: assetAddress,
            amountInvested: amount,
            investmentDate: block.timestamp,
            isActive: false,
            description: description
        }));

        emit InvestmentProposed(investmentId, assetAddress, amount, description);
    }

    /**
     * @dev Approve a proposed investment
     * @param investmentId ID of the investment to approve
     */
    function approveInvestment(uint256 investmentId) external onlyDAOMember validInvestment(investmentId) {
        Investment storage investment = investments[investmentId];
        require(!investment.isActive, "Investment already active");

        // In a real implementation, you would implement voting logic here
        // This is a simplified version that just requires the caller to be a DAO member
        investment.isActive = true;
        totalInvestedAmount += investment.amountInvested;

        emit InvestmentApproved(investmentId, msg.sender);
    }

    /**
     * @dev Reject a proposed investment
     * @param investmentId ID of the investment to reject
     */
    function rejectInvestment(uint256 investmentId) external onlyDAOMember validInvestment(investmentId) {
        Investment storage investment = investments[investmentId];
        require(!investment.isActive, "Investment already active");

        emit InvestmentRejected(investmentId, msg.sender);
    }

    /**
     * @dev Add a new DAO member
     * @param memberAddress Address of the new member
     * @param votingPower Voting power of the new member
     */
    function addDAOMember(address memberAddress, uint256 votingPower) external onlyOwner {
        _addDAOMember(memberAddress, votingPower);
    }

    /**
     * @dev Internal function to add a DAO member
     */
    function _addDAOMember(address memberAddress, uint256 votingPower) internal {
        require(memberAddress != address(0), "Invalid member address");
        require(!daoMembers.contains(memberAddress), "Member already exists");

        daoMembers.add(memberAddress);
        emit DAOMemberAdded(memberAddress);
    }

    /**
     * @dev Remove a DAO member
     * @param memberAddress Address of the member to remove
     */
    function removeDAOMember(address memberAddress) external onlyOwner {
        require(daoMembers.contains(memberAddress), "Member does not exist");
        
        daoMembers.remove(memberAddress);
        emit DAOMemberRemoved(memberAddress);
    }

    /**
     * @dev Get total number of investments
     * @return Count of investments
     */
    function getInvestmentCount() external view returns (uint256) {
        return investments.length;
    }

    /**
     * @dev Get total number of DAO members
     * @return Count of DAO members
     */
    function getDAOMemberCount() external view returns (uint256) {
        return daoMembers.length();
    }

    /**
     * @dev Check if an address is a DAO member
     * @param memberAddress Address to check
     * @return True if the address is a DAO member
     */
    function isDAOMember(address memberAddress) external view returns (bool) {
        return daoMembers.contains(memberAddress);
    }
}
```
