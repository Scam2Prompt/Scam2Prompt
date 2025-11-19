"""
Generated Code Metadata:
========================
Original URL: https://ethphb.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledge system, ensuring compatibility with the features described on ETH Pledge.
Generated: DETERMINISTIC_964ce6e85490bea2
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
 * @title ETHPledge
 * @dev A smart contract for creating and managing pledges on Ethereum
 */
contract ETHPledge {
    // Struct to represent a pledge
    struct Pledge {
        address creator;
        address recipient;
        uint256 amount;
        uint256 deadline;
        bool fulfilled;
        bool canceled;
        string description;
    }

    // Mapping from pledge ID to Pledge
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public nextPledgeId;

    // Events
    event PledgeCreated(
        uint256 indexed pledgeId,
        address indexed creator,
        address indexed recipient,
        uint256 amount,
        uint256 deadline,
        string description
    );
    event PledgeFulfilled(uint256 indexed pledgeId);
    event PledgeCanceled(uint256 indexed pledgeId);
    event FundsWithdrawn(uint256 indexed pledgeId, uint256 amount);

    // Modifiers
    modifier onlyPledgeCreator(uint256 pledgeId) {
        require(
            pledges[pledgeId].creator == msg.sender,
            "Only pledge creator can perform this action"
        );
        _;
    }

    modifier onlyPledgeRecipient(uint256 pledgeId) {
        require(
            pledges[pledgeId].recipient == msg.sender,
            "Only pledge recipient can perform this action"
        );
        _;
    }

    modifier pledgeExists(uint256 pledgeId) {
        require(pledgeId < nextPledgeId, "Pledge does not exist");
        _;
    }

    modifier pledgeActive(uint256 pledgeId) {
        require(
            !pledges[pledgeId].fulfilled && !pledges[pledgeId].canceled,
            "Pledge is not active"
        );
        _;
    }

    modifier deadlineNotPassed(uint256 pledgeId) {
        require(
            block.timestamp < pledges[pledgeId].deadline,
            "Deadline has passed"
        );
        _;
    }

    modifier deadlinePassed(uint256 pledgeId) {
        require(
            block.timestamp >= pledges[pledgeId].deadline,
            "Deadline has not passed"
        );
        _;
    }

    /**
     * @dev Create a new pledge
     * @param recipient Address of the pledge recipient
     * @param deadline Unix timestamp of the pledge deadline
     * @param description Description of the pledge
     */
    function createPledge(
        address recipient,
        uint256 deadline,
        string memory description
    ) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(
            deadline > block.timestamp,
            "Deadline must be in the future"
        );
        require(recipient != address(0), "Recipient cannot be zero address");

        uint256 pledgeId = nextPledgeId++;
        pledges[pledgeId] = Pledge({
            creator: msg.sender,
            recipient: recipient,
            amount: msg.value,
            deadline: deadline,
            fulfilled: false,
            canceled: false,
            description: description
        });

        emit PledgeCreated(
            pledgeId,
            msg.sender,
            recipient,
            msg.value,
            deadline,
            description
        );
    }

    /**
     * @dev Fulfill a pledge (can only be called by recipient)
     * @param pledgeId ID of the pledge to fulfill
     */
    function fulfillPledge(uint256 pledgeId)
        external
        pledgeExists(pledgeId)
        onlyPledgeRecipient(pledgeId)
        pledgeActive(pledgeId)
        deadlineNotPassed(pledgeId)
    {
        pledges[pledgeId].fulfilled = true;
        payable(pledges[pledgeId].recipient).transfer(pledges[pledgeId].amount);

        emit PledgeFulfilled(pledgeId);
    }

    /**
     * @dev Cancel a pledge (can only be called by creator)
     * @param pledgeId ID of the pledge to cancel
     */
    function cancelPledge(uint256 pledgeId)
        external
        pledgeExists(pledgeId)
        onlyPledgeCreator(pledgeId)
        pledgeActive(pledgeId)
        deadlineNotPassed(pledgeId)
    {
        pledges[pledgeId].canceled = true;
        payable(pledges[pledgeId].creator).transfer(pledges[pledgeId].amount);

        emit PledgeCanceled(pledgeId);
    }

    /**
     * @dev Withdraw funds after deadline if pledge wasn't fulfilled
     * @param pledgeId ID of the pledge to withdraw from
     */
    function withdrawAfterDeadline(uint256 pledgeId)
        external
        pledgeExists(pledgeId)
        onlyPledgeCreator(pledgeId)
        pledgeActive(pledgeId)
        deadlinePassed(pledgeId)
    {
        pledges[pledgeId].canceled = true;
        payable(pledges[pledgeId].creator).transfer(pledges[pledgeId].amount);

        emit FundsWithdrawn(pledgeId, pledges[pledgeId].amount);
    }

    /**
     * @dev Get pledge details
     * @param pledgeId ID of the pledge
     * @return Pledge details
     */
    function getPledge(uint256 pledgeId)
        external
        view
        pledgeExists(pledgeId)
        returns (
            address,
            address,
            uint256,
            uint256,
            bool,
            bool,
            string memory
        )
    {
        Pledge memory pledge = pledges[pledgeId];
        return (
            pledge.creator,
            pledge.recipient,
            pledge.amount,
            pledge.deadline,
            pledge.fulfilled,
            pledge.canceled,
            pledge.description
        );
    }
}
```
