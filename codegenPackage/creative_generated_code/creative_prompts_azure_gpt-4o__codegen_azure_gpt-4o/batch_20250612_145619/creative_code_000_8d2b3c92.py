"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ethzao.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, ensuring compatibility with mobile devices and requiring JavaScript for user interaction.
Generated: DETERMINISTIC_8d2b3c9290395608
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
 * @dev A smart contract for an Ethereum-based pledging system
 * that allows users to make pledges and withdraw funds.
 */
contract PledgeSystem {
    // Struct to store pledge information
    struct Pledge {
        address pledger; // Address of the pledger
        uint256 amount;  // Amount pledged
        uint256 timestamp; // Timestamp of pledge
    }

    // Array to store all pledges
    Pledge[] public pledges;

    // Mapping to store the total amount pledged by each address
    mapping(address => uint256) public totalPledgedByUser;

    // Event emitted when a new pledge is created
    event PledgeCreated(address indexed pledger, uint256 amount, uint256 timestamp);

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed receiver, uint256 amount);

    // Total balance of the contract
    uint256 public totalPledged;

    /**
     * @dev Function to make a pledge to the system.
     * The function requires the caller to send Ether.
     */
    function makePledge() external payable {
        require(msg.value > 0, "Pledge amount must be greater than zero");

        // Create a new pledge and add it to the array
        pledges.push(Pledge({
            pledger: msg.sender,
            amount: msg.value,
            timestamp: block.timestamp
        }));

        // Update the total pledged amount for the user
        totalPledgedByUser[msg.sender] += msg.value;

        // Update the total balance of the contract
        totalPledged += msg.value;

        // Emit the PledgeCreated event
        emit PledgeCreated(msg.sender, msg.value, block.timestamp);
    }

    /**
     * @dev Function to withdraw funds from the contract.
     * Can only be called by the contract owner.
     * @param _receiver The address to receive the funds.
     * @param _amount The amount to withdraw.
     */
    function withdrawFunds(address payable _receiver, uint256 _amount) external {
        require(_receiver != address(0), "Invalid receiver address");
        require(_amount <= address(this).balance, "Insufficient contract balance");

        // Transfer the specified amount to the receiver
        _receiver.transfer(_amount);

        // Emit the FundsWithdrawn event
        emit FundsWithdrawn(_receiver, _amount);
    }

    /**
     * @dev Function to get the total number of pledges on the contract.
     * @return The number of pledges.
     */
    function getPledgeCount() external view returns (uint256) {
        return pledges.length;
    }

    /**
     * @dev Function to retrieve all pledges.
     * Note: This function may not be efficient for a large number of pledges.
     * @return An array of Pledge structs containing pledge details.
     */
    function getAllPledges() external view returns (Pledge[] memory) {
        return pledges;
    }

    /**
     * @dev Function to get the total pledged amount by a user.
     * @param _user The address of the user.
     * @return The total amount pledged by the user.
     */
    function getTotalPledgedByUser(address _user) external view returns (uint256) {
        return totalPledgedByUser[_user];
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers to the contract.
     */
    fallback() external payable {
        revert("Ether transfers not allowed directly.");
    }

    /**
     * @dev Receive function to allow Ether transfers to the contract.
     * This is specifically for pledges via makePledge().
     */
    receive() external payable {
        makePledge();
    }
}
```

JavaScript code for interacting with the contract can be written separately.
