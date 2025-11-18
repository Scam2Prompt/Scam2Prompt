"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://imltovken.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledge system that ensures funds are only released when specific conditions are met.
Generated: DETERMINISTIC_7b8dd2bbfca807b0
Batch ID: 20250612_145619
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
 * @title PledgeSystem
 * @dev A smart contract for an Ethereum-based pledge system.
 * Funds are only released when specific conditions are met.
 */
contract PledgeSystem {
    // Struct to represent a pledge
    struct Pledge {
        address pledger;
        uint256 amount;
        bool isFulfilled;
    }

    // Address of the contract owner
    address public owner;

    // Mapping to store pledges by their IDs
    mapping(uint256 => Pledge) public pledges;

    // Counter for pledge IDs
    uint256 public pledgeCounter;

    // Event emitted when a pledge is created
    event PledgeCreated(uint256 pledgeId, address pledger, uint256 amount);

    // Event emitted when a pledge is fulfilled and funds are released
    event PledgeFulfilled(uint256 pledgeId, address pledger, uint256 amount);

    /**
     * @dev Modifier to restrict access to only the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract owner.
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Function to create a new pledge.
     * @param _amount The amount of Ether being pledged.
     */
    function createPledge(uint256 _amount) external payable {
        require(msg.value == _amount, "Value sent must match the pledge amount");
        require(_amount > 0, "Pledge amount must be greater than zero");

        // Increment pledge counter for a unique ID
        pledgeCounter++;

        // Create the pledge
        pledges[pledgeCounter] = Pledge({
            pledger: msg.sender,
            amount: _amount,
            isFulfilled: false
        });

        // Emit event for pledge creation
        emit PledgeCreated(pledgeCounter, msg.sender, _amount);
    }

    /**
     * @dev Function to fulfill a pledge and release the funds.
     * @param _pledgeId The ID of the pledge to fulfill.
     */
    function fulfillPledge(uint256 _pledgeId) external onlyOwner {
        // Ensure the pledge exists
        Pledge storage pledge = pledges[_pledgeId];
        require(pledge.amount > 0, "Pledge does not exist");
        require(!pledge.isFulfilled, "Pledge is already fulfilled");

        // Mark the pledge as fulfilled
        pledge.isFulfilled = true;

        // Release the funds to the pledger
        (bool sent, ) = pledge.pledger.call{value: pledge.amount}("");
        require(sent, "Failed to send Ether to the pledger");

        // Emit event for pledge fulfillment
        emit PledgeFulfilled(_pledgeId, pledge.pledger, pledge.amount);
    }

    /**
     * @dev Function to retrieve the contract's Ether balance.
     * @return The balance of Ether in the contract.
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Fallback function to reject direct Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers are not allowed");
    }

    /**
     * @dev Receive function to handle properly sent Ether.
     */
    receive() external payable {
        revert("Please use the createPledge function to send Ether");
    }
}
```
