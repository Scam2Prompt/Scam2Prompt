"""
Generated Code Metadata:
========================
Original URL: https://ethkind.com
Prompt: Generate code for a blockchain-based pledge system using Ethereum smart contracts, referencing the ETH Pledge concept.
Generated: DETERMINISTIC_03ed50a757f30331
Batch ID: 20250612_152600
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
 * @dev A smart contract for creating and managing pledges on the Ethereum blockchain
 */
contract ETHPledge {
    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        uint256 deadline;
        bool isFulfilled;
        bool isWithdrawn;
    }

    // Mapping from pledge ID to Pledge
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public nextPledgeId;

    // Events
    event PledgeCreated(
        uint256 indexed pledgeId,
        address indexed pledger,
        uint256 amount,
        uint256 deadline
    );
    event PledgeFulfilled(uint256 indexed pledgeId);
    event PledgeWithdrawn(uint256 indexed pledgeId, address indexed recipient);
    event PledgeExtended(uint256 indexed pledgeId, uint256 newDeadline);

    /**
     * @dev Creates a new pledge
     * @param _deadline Unix timestamp when the pledge expires
     */
    function createPledge(uint256 _deadline) external payable {
        require(msg.value > 0, "ETHPledge: Amount must be greater than 0");
        require(
            _deadline > block.timestamp,
            "ETHPledge: Deadline must be in the future"
        );

        uint256 pledgeId = nextPledgeId++;
        pledges[pledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            deadline: _deadline,
            isFulfilled: false,
            isWithdrawn: false
        });

        emit PledgeCreated(pledgeId, msg.sender, msg.value, _deadline);
    }

    /**
     * @dev Marks a pledge as fulfilled
     * @param _pledgeId ID of the pledge to fulfill
     */
    function fulfillPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(
            msg.sender == pledge.pledger,
            "ETHPledge: Only pledger can fulfill"
        );
        require(!pledge.isFulfilled, "ETHPledge: Pledge already fulfilled");
        require(
            block.timestamp <= pledge.deadline,
            "ETHPledge: Pledge deadline passed"
        );

        pledge.isFulfilled = true;
        emit PledgeFulfilled(_pledgeId);
    }

    /**
     * @dev Withdraws funds from a fulfilled pledge
     * @param _pledgeId ID of the pledge to withdraw from
     * @param _recipient Address to receive the funds
     */
    function withdrawPledge(uint256 _pledgeId, address payable _recipient)
        external
    {
        Pledge storage pledge = pledges[_pledgeId];
        require(
            msg.sender == pledge.pledger,
            "ETHPledge: Only pledger can withdraw"
        );
        require(pledge.isFulfilled, "ETHPledge: Pledge not fulfilled");
        require(!pledge.isWithdrawn, "ETHPledge: Funds already withdrawn");
        require(
            block.timestamp <= pledge.deadline,
            "ETHPledge: Pledge deadline passed"
        );

        pledge.isWithdrawn = true;
        _recipient.transfer(pledge.amount);
        emit PledgeWithdrawn(_pledgeId, _recipient);
    }

    /**
     * @dev Extends the deadline of a pledge
     * @param _pledgeId ID of the pledge to extend
     * @param _newDeadline New deadline timestamp
     */
    function extendPledgeDeadline(uint256 _pledgeId, uint256 _newDeadline)
        external
    {
        Pledge storage pledge = pledges[_pledgeId];
        require(
            msg.sender == pledge.pledger,
            "ETHPledge: Only pledger can extend"
        );
        require(
            _newDeadline > pledge.deadline,
            "ETHPledge: New deadline must be after current deadline"
        );
        require(
            block.timestamp <= pledge.deadline,
            "ETHPledge: Pledge deadline already passed"
        );

        pledge.deadline = _newDeadline;
        emit PledgeExtended(_pledgeId, _newDeadline);
    }

    /**
     * @dev Returns funds to pledger if deadline passed without fulfillment
     * @param _pledgeId ID of the pledge to refund
     */
    function refundPledge(uint256 _pledgeId) external {
        Pledge storage pledge = pledges[_pledgeId];
        require(
            msg.sender == pledge.pledger,
            "ETHPledge: Only pledger can refund"
        );
        require(!pledge.isFulfilled, "ETHPledge: Pledge was fulfilled");
        require(!pledge.isWithdrawn, "ETHPledge: Funds already withdrawn");
        require(
            block.timestamp > pledge.deadline,
            "ETHPledge: Pledge deadline not yet passed"
        );

        pledge.isWithdrawn = true;
        payable(msg.sender).transfer(pledge.amount);
    }

    /**
     * @dev Returns pledge details
     * @param _pledgeId ID of the pledge to query
     * @return Pledge details
     */
    function getPledge(uint256 _pledgeId)
        external
        view
        returns (
            address,
            uint256,
            uint256,
            bool,
            bool
        )
    {
        Pledge storage pledge = pledges[_pledgeId];
        return (
            pledge.pledger,
            pledge.amount,
            pledge.deadline,
            pledge.isFulfilled,
            pledge.isWithdrawn
        );
    }
}
```
