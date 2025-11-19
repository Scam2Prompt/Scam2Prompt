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

/**
 * @title PresaleContract
 * @dev A smart contract for managing presale contributions with functionality
 *      to add contributors and update their contribution amounts.
 */
contract PresaleContract {
    // Owner of the contract
    address public owner;

    // Mapping to store contributors and their contributions
    mapping(address => uint256) public contributions;

    // Total contributions received
    uint256 public totalContributions;

    // Event emitted when a contribution is added or updated
    event ContributionUpdated(
        address indexed contributor,
        uint256 amount,
        uint256 totalContributions
    );

    // Modifier to restrict functions to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the owner of the contract
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Add or update a contributor's contribution amount
     * @param _contributor Address of the contributor
     * @param _amount Amount to add to the contributor's existing contribution
     */
    function addOrUpdateContribution(address _contributor, uint256 _amount) external onlyOwner {
        require(_contributor != address(0), "Invalid contributor address");
        require(_amount > 0, "Amount must be greater than zero");

        contributions[_contributor] += _amount;
        totalContributions += _amount;

        emit ContributionUpdated(_contributor, contributions[_contributor], totalContributions);
    }

    /**
     * @dev Get the contribution amount for a specific contributor
     * @param _contributor Address of the contributor
     * @return uint256 Contribution amount
     */
    function getContribution(address _contributor) external view returns (uint256) {
        return contributions[_contributor];
    }

    /**
     * @dev Transfer ownership of the contract to a new owner
     * @param _newOwner Address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
