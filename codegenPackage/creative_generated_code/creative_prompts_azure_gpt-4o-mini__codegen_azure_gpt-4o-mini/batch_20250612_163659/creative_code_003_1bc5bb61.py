"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iqratechpoint.pages.dev
Prompt: Generate a sample smart contract for managing scholarships and grants using IQRA Token on the Binance Smart Chain.
Generated: DETERMINISTIC_1bc5bb618d3296a1
Batch ID: 20250612_163659
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

// Interface for the IQRA Token
interface IIqraToken {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

// Smart contract for managing scholarships and grants
contract ScholarshipManager {
    // State variables
    IIqraToken public iqraToken; // Instance of the IQRA Token
    address public owner;         // Owner of the contract
    uint256 public totalGrants;  // Total grants distributed

    // Struct to represent a scholarship
    struct Scholarship {
        uint256 id;
        address recipient;
        uint256 amount;
        bool isActive;
    }

    // Mapping to store scholarships
    mapping(uint256 => Scholarship) public scholarships;

    // Events for logging actions
    event ScholarshipCreated(uint256 id, address recipient, uint256 amount);
    event ScholarshipDistributed(uint256 id, address recipient, uint256 amount);
    event ScholarshipCancelled(uint256 id);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to set the IQRA Token address and the owner
    constructor(address _iqraToken) {
        iqraToken = IIqraToken(_iqraToken);
        owner = msg.sender;
    }

    // Function to create a new scholarship
    function createScholarship(address _recipient, uint256 _amount) external onlyOwner {
        require(_recipient != address(0), "Invalid recipient");
        require(_amount > 0, "Amount must be greater than zero");

        totalGrants++;
        scholarships[totalGrants] = Scholarship(totalGrants, _recipient, _amount, true);
        emit ScholarshipCreated(totalGrants, _recipient, _amount);
    }

    // Function to distribute a scholarship
    function distributeScholarship(uint256 _scholarshipId) external onlyOwner {
        Scholarship storage scholarship = scholarships[_scholarshipId];
        require(scholarship.isActive, "Scholarship not active");
        require(iqraToken.balanceOf(address(this)) >= scholarship.amount, "Insufficient balance");

        scholarship.isActive = false; // Mark scholarship as distributed
        require(iqraToken.transfer(scholarship.recipient, scholarship.amount), "Transfer failed");
        emit ScholarshipDistributed(_scholarshipId, scholarship.recipient, scholarship.amount);
    }

    // Function to cancel a scholarship
    function cancelScholarship(uint256 _scholarshipId) external onlyOwner {
        Scholarship storage scholarship = scholarships[_scholarshipId];
        require(scholarship.isActive, "Scholarship not active");

        scholarship.isActive = false; // Mark the scholarship as cancelled
        emit ScholarshipCancelled(_scholarshipId);
    }

    // Function to retrieve scholarship details
    function getScholarship(uint256 _scholarshipId) external view returns (Scholarship memory) {
        return scholarships[_scholarshipId];
    }

    // Function to withdraw any remaining IQRA Tokens from the contract
    function withdrawTokens() external onlyOwner {
        uint256 balance = iqraToken.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(iqraToken.transfer(owner, balance), "Transfer failed");
    }
}
```
