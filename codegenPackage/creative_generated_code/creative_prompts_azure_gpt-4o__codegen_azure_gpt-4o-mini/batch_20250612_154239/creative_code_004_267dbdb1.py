"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bull-dogito-com.pages.dev
Prompt: Develop a Solidity smart contract function that allows Bulldogito Coin holders to vote on which real-world businesses should be included in the B2B Booster investment strategy.
Generated: DETERMINISTIC_267dbdb17a78c5f6
Batch ID: 20250612_154239
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

contract BulldogitoVoting {
    // Event emitted when a new vote is cast
    event VoteCasted(address indexed voter, uint256 indexed businessId);

    // Struct to represent a business
    struct Business {
        string name;
        uint256 voteCount;
    }

    // Mapping from business ID to Business details
    mapping(uint256 => Business) public businesses;
    // Mapping to track voted status for each voter
    mapping(address => bool) public hasVoted;

    // Counter for total businesses
    uint256 public businessCount;

    // Modifier to check if the voter has already voted
    modifier hasNotVoted() {
        require(!hasVoted[msg.sender], "You have already voted.");
        _;
    }

    // Function to add a business for voting (only owner can add businesses)
    function addBusiness(string memory _name) public {
        require(bytes(_name).length > 0, "Business name cannot be empty.");
        
        businessCount++;
        businesses[businessCount] = Business({
            name: _name,
            voteCount: 0
        });
    }

    // Function for Bulldogito Coin holders to vote for a business
    function vote(uint256 _businessId) public hasNotVoted {
        require(_businessId > 0 && _businessId <= businessCount, "Invalid business ID.");

        // Record the vote
        businesses[_businessId].voteCount++;
        hasVoted[msg.sender] = true;

        // Emit the vote cast event
        emit VoteCasted(msg.sender, _businessId);
    }

    // Function to get the vote count for a specific business
    function getVoteCount(uint256 _businessId) public view returns (uint256) {
        require(_businessId > 0 && _businessId <= businessCount, "Invalid business ID.");
        return businesses[_businessId].voteCount;
    }

    // Function to get business details
    function getBusiness(uint256 _businessId) public view returns (string memory, uint256) {
        require(_businessId > 0 && _businessId <= businessCount, "Invalid business ID.");
        Business memory business = businesses[_businessId];
        return (business.name, business.voteCount);
    }
}
```
