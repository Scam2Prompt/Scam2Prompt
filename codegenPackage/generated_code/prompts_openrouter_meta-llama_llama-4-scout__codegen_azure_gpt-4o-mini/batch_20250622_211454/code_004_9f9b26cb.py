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

/// @title PresaleContributionManager
/// @notice This contract manages contributions for a presale project
contract PresaleContributionManager {
    // Struct to hold contributor information
    struct Contributor {
        uint256 amount; // Amount contributed by the contributor
        bool exists;    // Flag to check if contributor exists
    }

    // Mapping to store contributors' information
    mapping(address => Contributor) private contributors;

    // Total contributions received
    uint256 public totalContributions;

    // Event emitted when a contribution is made or updated
    event ContributionUpdated(address indexed contributor, uint256 amount);

    /// @notice Allows a contributor to add or update their contribution
    /// @param _amount The amount to contribute
    /// @dev Reverts if the amount is zero
    function contribute(uint256 _amount) external payable {
        require(_amount > 0, "Contribution amount must be greater than zero");
        require(msg.value == _amount, "Sent value must match contribution amount");

        // Update contributor's contribution
        if (contributors[msg.sender].exists) {
            totalContributions -= contributors[msg.sender].amount; // Deduct previous contribution
        } else {
            contributors[msg.sender].exists = true; // Mark contributor as existing
        }

        contributors[msg.sender].amount = _amount; // Update contribution amount
        totalContributions += _amount; // Update total contributions

        emit ContributionUpdated(msg.sender, _amount); // Emit event
    }

    /// @notice Allows the owner to withdraw the total contributions
    /// @dev Only the contract owner can call this function
    function withdraw() external onlyOwner {
        uint256 amount = address(this).balance; // Get contract balance
        require(amount > 0, "No funds to withdraw");
        payable(owner()).transfer(amount); // Transfer funds to owner
    }

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Function to get the contribution amount of a specific contributor
    /// @param _contributor The address of the contributor
    /// @return The contribution amount of the specified contributor
    function getContribution(address _contributor) external view returns (uint256) {
        return contributors[_contributor].amount;
    }

    // Function to check if an address is a contributor
    /// @param _contributor The address of the contributor
    /// @return True if the address is a contributor, false otherwise
    function isContributor(address _contributor) external view returns (bool) {
        return contributors[_contributor].exists;
    }
}
```
