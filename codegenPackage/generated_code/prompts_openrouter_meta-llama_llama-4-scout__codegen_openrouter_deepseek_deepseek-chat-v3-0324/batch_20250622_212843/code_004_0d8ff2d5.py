"""
Generated Code Metadata:
========================
Original URL: https://ethbvt.com
Prompt: Design a basic smart contract for an Ethereum pledge system using Solidity.
Generated: DETERMINISTIC_0d8ff2d536dc21a1
Batch ID: 20250622_212843
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
 * @title PledgeSystem
 * @dev A smart contract for managing pledges (commitments) on Ethereum
 */
contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        string description;
        uint256 timestamp;
        bool fulfilled;
    }

    // Mapping from pledge ID to Pledge
    mapping(uint256 => Pledge) public pledges;

    // Counter for total pledges
    uint256 public totalPledges;

    // Event emitted when a new pledge is created
    event PledgeCreated(
        uint256 indexed id,
        address indexed pledger,
        uint256 amount,
        string description,
        uint256 timestamp
    );

    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed id, uint256 timestamp);

    /**
     * @dev Create a new pledge
     * @param _description Description of the pledge
     */
    function createPledge(string memory _description) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(bytes(_description).length > 0, "Description cannot be empty");

        uint256 newPledgeId = totalPledges + 1;
        pledges[newPledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            description: _description,
            timestamp: block.timestamp,
            fulfilled: false
        });

        totalPledges = newPledgeId;
        emit PledgeCreated(
            newPledgeId,
            msg.sender,
            msg.value,
            _description,
            block.timestamp
        );
    }

    /**
     * @dev Fulfill a pledge
     * @param _pledgeId ID of the pledge to fulfill
     */
    function fulfillPledge(uint256 _pledgeId) external {
        require(_pledgeId > 0 && _pledgeId <= totalPledges, "Invalid pledge ID");
        Pledge storage pledge = pledges[_pledgeId];
        require(msg.sender == pledge.pledger, "Only pledger can fulfill");
        require(!pledge.fulfilled, "Pledge already fulfilled");

        pledge.fulfilled = true;
        emit PledgeFulfilled(_pledgeId, block.timestamp);
    }

    /**
     * @dev Get pledge details
     * @param _pledgeId ID of the pledge to retrieve
     * @return Pledge details
     */
    function getPledge(uint256 _pledgeId)
        external
        view
        returns (
            address,
            uint256,
            string memory,
            uint256,
            bool
        )
    {
        require(_pledgeId > 0 && _pledgeId <= totalPledges, "Invalid pledge ID");
        Pledge memory pledge = pledges[_pledgeId];
        return (
            pledge.pledger,
            pledge.amount,
            pledge.description,
            pledge.timestamp,
            pledge.fulfilled
        );
    }
}
```
