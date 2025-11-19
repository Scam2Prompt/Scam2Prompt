"""
Generated Code Metadata:
========================
Original URL: https://ethzao.com
Prompt: Write a smart contract in Solidity for an Ethereum-based pledging system, ensuring compatibility with mobile devices and requiring JavaScript for user interaction.
Generated: DETERMINISTIC_8d2b3c9290395608
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
 * @title PledgeContract
 * @dev A smart contract for managing pledges on Ethereum blockchain
 */
contract PledgeContract {
    // Struct to store pledge information
    struct Pledge {
        address pledger;
        uint256 amount;
        string message;
        uint256 timestamp;
    }

    // Mapping to store pledges by their IDs
    mapping(uint256 => Pledge) public pledges;

    // Counter for total pledges
    uint256 public totalPledges;

    // Event emitted when a new pledge is made
    event PledgeCreated(
        uint256 indexed pledgeId,
        address indexed pledger,
        uint256 amount,
        string message,
        uint256 timestamp
    );

    // Event emitted when funds are withdrawn
    event FundsWithdrawn(address indexed recipient, uint256 amount);

    // Address of the contract owner
    address public owner;

    // Modifier to restrict access to owner only
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor sets the contract owner
     */
    constructor() {
        owner = msg.sender;
    }

    /**
     * @dev Create a new pledge
     * @param _message The message associated with the pledge
     */
    function createPledge(string memory _message) external payable {
        require(msg.value > 0, "Pledge amount must be greater than 0");
        require(bytes(_message).length > 0, "Message cannot be empty");

        uint256 pledgeId = totalPledges + 1;
        pledges[pledgeId] = Pledge({
            pledger: msg.sender,
            amount: msg.value,
            message: _message,
            timestamp: block.timestamp
        });

        totalPledges = pledgeId;
        emit PledgeCreated(pledgeId, msg.sender, msg.value, _message, block.timestamp);
    }

    /**
     * @dev Get pledge details by ID
     * @param _pledgeId The ID of the pledge to retrieve
     * @return Pledge details
     */
    function getPledge(uint256 _pledgeId) external view returns (Pledge memory) {
        require(_pledgeId > 0 && _pledgeId <= totalPledges, "Invalid pledge ID");
        return pledges[_pledgeId];
    }

    /**
     * @dev Withdraw funds from the contract (owner only)
     * @param _amount The amount to withdraw
     */
    function withdrawFunds(uint256 _amount) external onlyOwner {
        require(_amount <= address(this).balance, "Insufficient contract balance");
        payable(owner).transfer(_amount);
        emit FundsWithdrawn(owner, _amount);
    }

    /**
     * @dev Get contract balance
     * @return The current balance of the contract
     */
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Transfer ownership of the contract
     * @param _newOwner The address of the new owner
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```
