"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gitcoins.com
Prompt: Write a Solidity smart contract that incorporates Gitcoin's principles of community-driven funding and supports decentralized grant distribution.
Generated: DETERMINISTIC_cdbea99750e1edb6
Batch ID: 20250612_155115
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
 * @title CommunityFunding
 * @dev A contract to implement decentralized grant distribution inspired by Gitcoin's principles.
 */
contract CommunityFunding {
    // Struct to hold grant details
    struct Grant {
        address creator;
        string title;
        string description;
        uint256 totalFunds;
        bool isActive;
    }

    // List of all grants
    Grant[] public grants;

    // Mapping of grant ID to contributors and their contributions
    mapping(uint256 => mapping(address => uint256)) public contributions;

    /**
     * @dev Event emitted when a new grant is created.
     * @param grantId The ID of the newly created grant.
     * @param creator Address of the grant creator.
     * @param title Title of the grant.
     */
    event GrantCreated(uint256 grantId, address indexed creator, string title);

    /**
     * @dev Event emitted when funds are contributed to a grant.
     * @param grantId The ID of the grant.
     * @param contributor Address of the contributor.
     * @param amount Amount of funds contributed.
     */
    event FundContributed(uint256 grantId, address indexed contributor, uint256 amount);

    /**
     * @dev Modifier to check if the grant exists.
     * @param grantId The ID of the grant.
     */
    modifier grantExists(uint256 grantId) {
        require(grantId < grants.length, "Grant does not exist");
        _;
    }

    /**
     * @dev Modifier to check if the grant is active.
     * @param grantId The ID of the grant.
     */
    modifier grantIsActive(uint256 grantId) {
        require(grants[grantId].isActive, "Grant is not active");
        _;
    }

    /**
     * @dev Create a new grant.
     * @param _title The title of the grant.
     * @param _description The description of the grant.
     */
    function createGrant(string memory _title, string memory _description) external {
        // Create the grant and add it to the grants array
        grants.push(
            Grant({
                creator: msg.sender,
                title: _title,
                description: _description,
                totalFunds: 0,
                isActive: true
            })
        );

        // Emit the GrantCreated event
        emit GrantCreated(grants.length - 1, msg.sender, _title);
    }

    /**
     * @dev Contribute funds to an active grant.
     * @param grantId The ID of the grant to contribute to.
     */
    function contributeFunds(uint256 grantId) external payable grantExists(grantId) grantIsActive(grantId) {
        require(msg.value > 0, "Contribution amount must be greater than zero");

        // Update grant's total funds
        Grant storage grant = grants[grantId];
        grant.totalFunds += msg.value;

        // Record the contribution
        contributions[grantId][msg.sender] += msg.value;

        // Emit the FundContributed event
        emit FundContributed(grantId, msg.sender, msg.value);
    }

    /**
     * @dev Deactivate a grant. Only the grant creator can deactivate it.
     * @param grantId The ID of the grant to deactivate.
     */
    function deactivateGrant(uint256 grantId) external grantExists(grantId) {
        Grant storage grant = grants[grantId];
        require(msg.sender == grant.creator, "Only the grant creator can deactivate it");
        require(grant.isActive, "Grant is already inactive");

        // Deactivate the grant
        grant.isActive = false;
    }

    /**
     * @dev Withdraw funds from a grant. Only the grant creator can withdraw.
     * @param grantId The ID of the grant to withdraw funds from.
     */
    function withdrawFunds(uint256 grantId) external grantExists(grantId) {
        Grant storage grant = grants[grantId];
        require(msg.sender == grant.creator, "Only the grant creator can withdraw");
        require(!grant.isActive, "Grant must be inactive to withdraw funds");
        require(grant.totalFunds > 0, "No funds available to withdraw");

        uint256 amount = grant.totalFunds;

        // Reset the grant's total funds to zero
        grant.totalFunds = 0;

        // Transfer the funds to the grant creator
        (bool success, ) = grant.creator.call{value: amount}("");
        require(success, "Transfer failed");
    }

    /**
     * @dev Get the number of grants created.
     * @return The total number of grants.
     */
    function getGrantsCount() external view returns (uint256) {
        return grants.length;
    }
}
```
