"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://snap-dioneprotocol.pages.dev
Prompt: Write a smart contract in Solidity that supports renewable energy trading, inspired by the principles of the Dione Protocol's Nebra platform.
Generated: DETERMINISTIC_3797f9862cb3324d
Batch ID: 20250612_152109
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

/// @title Renewable Energy Trading Smart Contract
/// @dev This contract facilitates trading of renewable energy certificates (RECs) between producers and consumers.
contract RenewableEnergyTrading {

    // Struct to hold information about each renewable energy certificate (REC)
    struct REC {
        uint256 id;
        address producer;
        address owner;
        uint256 energyAmount; // in kWh
        bool isActive;
    }

    // State variables
    uint256 public nextRECId; // ID counter for RECs
    mapping(uint256 => REC) public RECs; // Mapping of REC ID to REC details
    mapping(address => uint256[]) public ownedRECs; // Mapping of owner address to their owned REC IDs

    // Events
    event RECIssued(uint256 indexed id, address indexed producer, uint256 energyAmount);
    event RECTransferred(uint256 indexed id, address indexed from, address indexed to);
    event RECBurned(uint256 indexed id, address indexed owner);

    // Modifier to check if the caller is the owner of the REC
    modifier onlyOwner(uint256 _recId) {
        require(msg.sender == RECs[_recId].owner, "Caller is not the owner of the REC");
        _;
    }

    // Function to issue a new renewable energy certificate
    function issueREC(uint256 _energyAmount) external {
        require(_energyAmount > 0, "Energy amount must be greater than zero");

        // Create a new REC
        RECs[nextRECId] = REC({
            id: nextRECId,
            producer: msg.sender,
            owner: msg.sender,
            energyAmount: _energyAmount,
            isActive: true
        });

        // Emit an event for the issued REC
        emit RECIssued(nextRECId, msg.sender, _energyAmount);

        // Store the REC ID in the producer's owned RECs
        ownedRECs[msg.sender].push(nextRECId);

        // Increment the REC ID counter
        nextRECId++;
    }

    // Function to transfer ownership of a REC
    function transferREC(uint256 _recId, address _to) external onlyOwner(_recId) {
        require(_to != address(0), "Invalid address for transfer");
        require(RECs[_recId].isActive, "REC is no longer active");

        // Update the owner of the REC
        address previousOwner = RECs[_recId].owner;
        RECs[_recId].owner = _to;

        // Remove the REC from the previous owner's list
        _removeOwnedREC(previousOwner, _recId);

        // Add the REC to the new owner's list
        ownedRECs[_to].push(_recId);

        // Emit an event for the transfer
        emit RECTransferred(_recId, previousOwner, _to);
    }

    // Function to burn a REC (remove from circulation)
    function burnREC(uint256 _recId) external onlyOwner(_recId) {
        require(RECs[_recId].isActive, "REC is already inactive");

        // Mark the REC as inactive
        RECs[_recId].isActive = false;

        // Remove the REC from the owner's list
        _removeOwnedREC(msg.sender, _recId);

        // Emit an event for the burned REC
        emit RECBurned(_recId, msg.sender);
    }

    // Internal function to remove the REC ID from an owner's list
    function _removeOwnedREC(address _owner, uint256 _recId) internal {
        uint256[] storage owned = ownedRECs[_owner];
        for (uint256 i = 0; i < owned.length; i++) {
            if (owned[i] == _recId) {
                // Swap the last element with the current one and pop
                owned[i] = owned[owned.length - 1];
                owned.pop();
                break;
            }
        }
    }

    // Function to get the details of a REC
    function getRECDetails(uint256 _recId) external view returns (REC memory) {
        require(_recId < nextRECId, "REC does not exist");
        return RECs[_recId];
    }

    // Function to get the list of owned RECs for a specific address
    function getOwnedRECs(address _owner) external view returns (uint256[] memory) {
        return ownedRECs[_owner];
    }
}
```
