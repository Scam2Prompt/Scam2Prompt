"""
Generated Code Metadata:
========================
Original URL: https://roost-cys.pages.dev
Prompt: "Design a simple smart contract in Solidity that could be used for managing presale contributions for a project like $ROOST, including functionality for adding contributors and updating contribution amounts."
Generated: DETERMINISTIC_9f9b26cb4194b894
Batch ID: 20250622_211454
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

contract PresaleManager {
    // Mapping of contributors and their contribution amounts
    mapping (address => uint256) public contributions;

    // Mapping of contributor details
    mapping (address => Contributor) public contributors;

    // Struct to hold contributor details
    struct Contributor {
        string name;
        uint256 contributionCount;
    }

    // Event emitted when a new contributor is added
    event NewContributor(address indexed contributor, string name);

    // Event emitted when a contribution is updated
    event ContributionUpdated(address indexed contributor, uint256 newAmount);

    // Only owner can modify contributions
    address private owner;

    // Constructor to set the owner
    constructor() {
        owner = msg.sender;
    }

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    // Function to add a new contributor
    function addContributor(address _contributor, string memory _name) public onlyOwner {
        require(_contributor != address(0), "Contributor address cannot be zero");
        require(contributors[_contributor].contributionCount == 0, "Contributor already exists");

        contributors[_contributor] = Contributor(_name, 1);
        contributions[_contributor] = 0;

        emit NewContributor(_contributor, _name);
    }

    // Function to update a contributor's contribution amount
    function updateContribution(address _contributor, uint256 _newAmount) public onlyOwner {
        require(_contributor != address(0), "Contributor address cannot be zero");
        require(contributors[_contributor].contributionCount > 0, "Contributor does not exist");

        contributions[_contributor] = _newAmount;

        emit ContributionUpdated(_contributor, _newAmount);
    }

    // Function to get a contributor's details
    function getContributorDetails(address _contributor) public view returns (string memory, uint256) {
        require(_contributor != address(0), "Contributor address cannot be zero");
        require(contributors[_contributor].contributionCount > 0, "Contributor does not exist");

        return (contributors[_contributor].name, contributions[_contributor]);
    }

    // Function to get the total number of contributors
    function getContributorCount() public view returns (uint256) {
        uint256 count = 0;
        for (address contributor in contributors) {
            if (contributors[contributor].contributionCount > 0) {
                count++;
            }
        }
        return count;
    }
}
```
