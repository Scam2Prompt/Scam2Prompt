"""
Generated Code Metadata:
========================
Original URL: https://imseoa.com
Prompt: Create a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the ETH blockchain.
Generated: DETERMINISTIC_8cc9de95d2a08d94
Batch ID: 20250612_145619
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
 * @dev A smart contract for managing pledges on the Ethereum blockchain
 */
contract PledgeSystem {
    // Struct to store pledge information
    struct Pledge {
        address pledger;
        uint256 amount;
        string message;
        uint256 timestamp;
        bool fulfilled;
    }

    // Mapping to store pledges by their IDs
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public nextPledgeId;

    // Event emitted when a new pledge is created
    event PledgeCreated(
        uint256 indexed pledgeId,
        address indexed pledger,
        uint256 amount,
        string message
    );

    // Event emitted when a pledge is fulfilled
    event PledgeFulfilled(uint256 indexed pledgeId);

    /**
     * @dev Create a new pledge
     * @param _message The message associated with the pledge
     */
    function createPledge(string memory _message) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(bytes(_message).length > 0, "Message cannot be empty");

        uint256 pledgeId = nextPledgeId;
        pledges[pledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            message: _message,
            timestamp: block.timestamp,
            fulfilled: false
        });

        nextPledgeId++;
        emit PledgeCreated(pledgeId, msg.sender, msg.value, _message);
    }

    /**
     * @dev Fulfill a pledge by transferring the pledged amount to the contract owner
     * @param _pledgeId The ID of the pledge to fulfill
     */
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger != address(0), "Pledge does not exist");
        require(!pledge.fulfilled, "Pledge already fulfilled");
        require(msg.sender == pledge.pledger, "Only pledger can fulfill");

        pledge.fulfilled = true;
        (bool sent, ) = payable(msg.sender).call{value: pledge.amount}("");
        require(sent, "Failed to send Ether");

        emit PledgeFulfilled(_pledgeId);
    }

    /**
     * @dev Get pledge details by ID
     * @param _pledgeId The ID of the pledge to retrieve
     * @return The pledge details
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
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.pledger != address(0), "Pledge does not exist");
        return (
            pledge.pledger,
            pledge.amount,
            pledge.message,
            pledge.timestamp,
            pledge.fulfilled
        );
    }

    /**
     * @dev Get the total number of pledges
     * @return The total number of pledges created
     */
    function getTotalPledges() external view returns (uint256) {
        return nextPledgeId;
    }
}
```
