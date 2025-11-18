"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethwish.com
Prompt: Write a smart contract in Solidity that allows users to create an ETH pledge with customizable conditions for withdrawal. Include functionality for tracking pledges and validating conditions.
Generated: DETERMINISTIC_56280e016fe83837
Batch ID: 20250612_152600
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
 * @title ETHPledge
 * @dev A smart contract for users to create ETH pledges with customizable withdrawal conditions.
 */
contract ETHPledge {
    // Struct to store information about each pledge
    struct Pledge {
        address creator;       // Address of the pledge creator
        uint256 amount;        // Amount of ETH pledged
        bool withdrawn;        // Whether the pledge has been withdrawn
        string condition;      // Withdrawal condition defined by the creator
    }

    // Mapping to store pledges using a unique ID
    mapping(uint256 => Pledge) public pledges;

    // Counter to generate unique IDs for each pledge
    uint256 public pledgeCounter;

    // Event emitted when a new pledge is created
    event PledgeCreated(
        uint256 indexed pledgeId,
        address indexed creator,
        uint256 amount,
        string condition
    );

    // Event emitted when a pledge is withdrawn
    event PledgeWithdrawn(uint256 indexed pledgeId, address indexed recipient);

    /**
     * @dev Allows a user to create a pledge with ETH and a withdrawal condition.
     * @param _condition The condition for withdrawing the funds.
     */
    function createPledge(string memory _condition) external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Increment the pledge counter to generate a new ID
        pledgeCounter++;

        // Store the new pledge in the mapping
        pledges[pledgeCounter] = Pledge({
            creator: msg.sender,
            amount: msg.value,
            withdrawn: false,
            condition: _condition
        });

        // Emit the PledgeCreated event
        emit PledgeCreated(pledgeCounter, msg.sender, msg.value, _condition);
    }

    /**
     * @dev Allows the creator of a pledge to withdraw their funds if conditions are met.
     * @param _pledgeId The ID of the pledge to withdraw.
     * @param _conditionValidation True if the withdrawal condition is met, provided by the caller.
     */
    function withdrawPledge(uint256 _pledgeId, bool _conditionValidation) external {
        // Ensure the pledge exists
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.amount > 0, "Pledge does not exist");
        require(!pledge.withdrawn, "Pledge already withdrawn");
        require(pledge.creator == msg.sender, "Only the pledge creator can withdraw");

        // Check if the withdrawal condition is met
        require(_conditionValidation, "Withdrawal condition not met");

        // Mark the pledge as withdrawn
        pledge.withdrawn = true;

        // Transfer the pledged amount to the creator
        (bool success, ) = msg.sender.call{value: pledge.amount}("");
        require(success, "Transfer failed");

        // Emit the PledgeWithdrawn event
        emit PledgeWithdrawn(_pledgeId, msg.sender);
    }

    /**
     * @dev Returns details of a specific pledge.
     * @param _pledgeId The ID of the pledge to retrieve.
     * @return creator The address of the pledge creator.
     * @return amount The amount of ETH pledged.
     * @return withdrawn Whether the pledge has been withdrawn.
     * @return condition The withdrawal condition of the pledge.
     */
    function getPledge(uint256 _pledgeId)
        external
        view
        returns (
            address creator,
            uint256 amount,
            bool withdrawn,
            string memory condition
        )
    {
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.amount > 0, "Pledge does not exist");
        return (pledge.creator, pledge.amount, pledge.withdrawn, pledge.condition);
    }
}
```
