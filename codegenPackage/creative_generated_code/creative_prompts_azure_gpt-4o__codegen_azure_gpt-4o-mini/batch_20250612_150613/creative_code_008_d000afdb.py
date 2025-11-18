"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://on-oeth.pages.dev
Prompt: Create a Solidity contract that implements a bug bounty mechanism for OUSD smart contracts, offering rewards through Immunefi as described in the documentation.
Generated: DETERMINISTIC_d000afdb01543ee2
Batch ID: 20250612_150613
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
 * @title OUSD Bug Bounty Contract
 * @dev This contract implements a bug bounty mechanism for OUSD smart contracts, 
 * rewarding users for reporting vulnerabilities through Immunefi.
 */

contract BugBounty {
    // Struct to store information about each bounty
    struct Bounty {
        uint256 id;
        string description;
        uint256 reward;
        address payable reporter;
        bool resolved;
    }

    // Mapping to store bounties by their ID
    mapping(uint256 => Bounty) public bounties;
    // Counter for bounty IDs
    uint256 public bountyCounter;
    // Event emitted when a new bounty is created
    event BountyCreated(uint256 id, string description, uint256 reward);
    // Event emitted when a bounty is claimed
    event BountyClaimed(uint256 id, address claimant);
    // Event emitted when a bounty is resolved
    event BountyResolved(uint256 id);

    /**
     * @dev Creates a new bounty.
     * @param _description A description of the bounty.
     * @param _reward The reward amount for the bounty.
     */
    function createBounty(string memory _description, uint256 _reward) external payable {
        require(msg.value == _reward, "Incorrect reward amount sent");
        require(_reward > 0, "Reward must be greater than zero");

        bountyCounter++;
        bounties[bountyCounter] = Bounty({
            id: bountyCounter,
            description: _description,
            reward: _reward,
            reporter: payable(msg.sender),
            resolved: false
        });

        emit BountyCreated(bountyCounter, _description, _reward);
    }

    /**
     * @dev Claims a bounty after reporting a vulnerability.
     * @param _id The ID of the bounty to claim.
     */
    function claimBounty(uint256 _id) external {
        Bounty storage bounty = bounties[_id];
        require(bounty.id != 0, "Bounty does not exist");
        require(!bounty.resolved, "Bounty already resolved");
        require(bounty.reporter == msg.sender, "Only the reporter can claim the bounty");

        bounty.resolved = true;
        (bool success, ) = bounty.reporter.call{value: bounty.reward}("");
        require(success, "Transfer failed");

        emit BountyClaimed(_id, msg.sender);
        emit BountyResolved(_id);
    }

    /**
     * @dev Gets the details of a bounty by ID.
     * @param _id The ID of the bounty.
     * @return id The ID of the bounty.
     * @return description The description of the bounty.
     * @return reward The reward amount for the bounty.
     * @return reporter The address of the reporter.
     * @return resolved The resolution status of the bounty.
     */
    function getBounty(uint256 _id) external view returns (
        uint256 id,
        string memory description,
        uint256 reward,
        address reporter,
        bool resolved
    ) {
        Bounty storage bounty = bounties[_id];
        require(bounty.id != 0, "Bounty does not exist");
        
        return (bounty.id, bounty.description, bounty.reward, bounty.reporter, bounty.resolved);
    }

    /**
     * @dev Allows the contract owner to withdraw funds in case of contract upgrade or migration.
     */
    function withdraw() external {
        // Only the contract owner should call this. Implement access control as needed.
        // For simplicity, this example does not include ownership controls.
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
