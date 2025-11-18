"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://website1-beo.pages.dev
Prompt: Write a Solidity smart contract that facilitates strong relationships between stakeholders in a crypto project, inspired by Innodapter ApS's emphasis on meaningful and transparent partnerships.
Generated: DETERMINISTIC_cc0edec3123723c9
Batch ID: 20250612_150226
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

contract StakeholderRelationship {
    // Structure to represent a stakeholder
    struct Stakeholder {
        address walletAddress;
        string name;
        string role;
        uint256 reputationScore; // Score to measure trustworthiness
        bool isActive; // Status of the stakeholder
    }

    // Mapping to store stakeholders by their address
    mapping(address => Stakeholder) public stakeholders;
    // Array to keep track of all stakeholders
    address[] public stakeholderList;

    // Event to log the addition of a new stakeholder
    event StakeholderAdded(address indexed walletAddress, string name, string role);
    // Event to log updates to a stakeholder's reputation score
    event ReputationUpdated(address indexed walletAddress, uint256 newScore);
    // Event to log the deactivation of a stakeholder
    event StakeholderDeactivated(address indexed walletAddress);

    // Modifier to check if the caller is an active stakeholder
    modifier onlyActiveStakeholder() {
        require(stakeholders[msg.sender].isActive, "You must be an active stakeholder.");
        _;
    }

    // Function to add a new stakeholder
    function addStakeholder(string memory _name, string memory _role) public {
        require(bytes(_name).length > 0, "Name cannot be empty.");
        require(bytes(_role).length > 0, "Role cannot be empty.");
        require(stakeholders[msg.sender].walletAddress == address(0), "Stakeholder already exists.");

        stakeholders[msg.sender] = Stakeholder({
            walletAddress: msg.sender,
            name: _name,
            role: _role,
            reputationScore: 0,
            isActive: true
        });

        stakeholderList.push(msg.sender);
        emit StakeholderAdded(msg.sender, _name, _role);
    }

    // Function to update the reputation score of a stakeholder
    function updateReputationScore(address _stakeholder, uint256 _newScore) public onlyActiveStakeholder {
        require(stakeholders[_stakeholder].walletAddress != address(0), "Stakeholder does not exist.");
        
        stakeholders[_stakeholder].reputationScore = _newScore;
        emit ReputationUpdated(_stakeholder, _newScore);
    }

    // Function to deactivate a stakeholder
    function deactivateStakeholder(address _stakeholder) public onlyActiveStakeholder {
        require(stakeholders[_stakeholder].walletAddress != address(0), "Stakeholder does not exist.");
        
        stakeholders[_stakeholder].isActive = false;
        emit StakeholderDeactivated(_stakeholder);
    }

    // Function to get the details of a stakeholder
    function getStakeholderDetails(address _stakeholder) public view returns (Stakeholder memory) {
        require(stakeholders[_stakeholder].walletAddress != address(0), "Stakeholder does not exist.");
        return stakeholders[_stakeholder];
    }

    // Function to get the total number of stakeholders
    function getTotalStakeholders() public view returns (uint256) {
        return stakeholderList.length;
    }
}
```
