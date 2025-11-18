"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://everyworld-app.pages.dev
Prompt: Create a smart contract in Solidity that mimics Everyworld's dual incentivization model, allowing users to earn points and pledge them to environmental charities.
Generated: DETERMINISTIC_77fb36756e53193b
Batch ID: 20250612_152511
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

contract EnvironmentalCharity {

    // State variables
    address public owner;
    uint256 public totalPoints;
    
    // Mapping to hold user points
    mapping(address => uint256) public userPoints;

    // Structure to represent a charity
    struct Charity {
        string name;
        uint256 pledgedPoints;
        bool exists;
    }

    // Mapping to hold charity details
    mapping(uint256 => Charity) public charities;
    uint256 public charityCount;

    // Events
    event PointsEarned(address indexed user, uint256 points);
    event PointsPledged(address indexed user, uint256 charityId, uint256 points);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Constructor to initialize contract owner
    constructor() {
        owner = msg.sender;
    }

    // Function to earn points
    function earnPoints(uint256 _points) external {
        require(_points > 0, "Points must be greater than zero");
        userPoints[msg.sender] += _points;
        totalPoints += _points;

        emit PointsEarned(msg.sender, _points);
    }

    // Function to add a new charity
    function addCharity(string calldata _name) external onlyOwner {
        require(bytes(_name).length > 0, "Charity name cannot be empty");
        
        charities[charityCount] = Charity({
            name: _name,
            pledgedPoints: 0,
            exists: true
        });

        charityCount++;
    }

    // Function to pledge points to a charity
    function pledgePoints(uint256 _charityId, uint256 _points) external {
        require(charities[_charityId].exists, "Charity does not exist");
        require(_points > 0, "Points must be greater than zero");
        require(userPoints[msg.sender] >= _points, "Insufficient points to pledge");

        userPoints[msg.sender] -= _points;
        charities[_charityId].pledgedPoints += _points;

        emit PointsPledged(msg.sender, _charityId, _points);
    }

    // Function to view points of a user
    function viewPoints(address _user) external view returns (uint256) {
        return userPoints[_user];
    }

    // Function to view pledged points for a charity
    function viewCharityPledgedPoints(uint256 _charityId) external view returns (uint256) {
        require(charities[_charityId].exists, "Charity does not exist");
        return charities[_charityId].pledgedPoints;
    }
}
```
