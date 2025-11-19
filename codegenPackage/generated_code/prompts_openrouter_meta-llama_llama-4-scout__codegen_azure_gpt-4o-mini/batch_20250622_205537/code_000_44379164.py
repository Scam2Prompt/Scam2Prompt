"""
Generated Code Metadata:
========================
Original URL: https://eosgas.io
Prompt: "Write a smart contract that utilizes eosGAS tokens to measure electrical consumption for cryptocurrency mining, based on the power plant's energy output."
Generated: DETERMINISTIC_44379164bd66f520
Batch ID: 20250622_205537
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

// Importing the ERC20 interface for eosGAS token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract to measure electrical consumption for cryptocurrency mining
contract EnergyConsumptionTracker {
    // State variables
    address public owner; // Owner of the contract
    IERC20 public eosGASToken; // Instance of the eosGAS token contract

    // Struct to hold energy consumption data
    struct ConsumptionData {
        uint256 energyOutput; // Energy output from the power plant in kWh
        uint256 consumption;   // Energy consumption for mining in kWh
        uint256 timestamp;     // Timestamp of the recorded data
    }

    // Mapping to store consumption data by miner address
    mapping(address => ConsumptionData[]) public consumptionRecords;

    // Events for logging
    event EnergyConsumed(address indexed miner, uint256 energyOutput, uint256 consumption, uint256 timestamp);

    // Modifier to restrict access to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _eosGASToken) {
        owner = msg.sender; // Set the contract deployer as the owner
        eosGASToken = IERC20(_eosGASToken); // Set the eosGAS token contract address
    }

    // Function to record energy consumption
    function recordConsumption(uint256 _energyOutput, uint256 _consumption) external {
        require(_energyOutput > 0, "Energy output must be greater than zero");
        require(_consumption > 0, "Consumption must be greater than zero");
        require(_consumption <= _energyOutput, "Consumption cannot exceed energy output");

        // Create a new consumption record
        ConsumptionData memory newRecord = ConsumptionData({
            energyOutput: _energyOutput,
            consumption: _consumption,
            timestamp: block.timestamp
        });

        // Store the record in the mapping
        consumptionRecords[msg.sender].push(newRecord);

        // Emit an event for the recorded consumption
        emit EnergyConsumed(msg.sender, _energyOutput, _consumption, block.timestamp);
    }

    // Function to withdraw eosGAS tokens from the contract
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(eosGASToken.balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer eosGAS tokens to the owner
        eosGASToken.transfer(owner, amount);
    }

    // Function to get consumption records for a specific miner
    function getConsumptionRecords(address miner) external view returns (ConsumptionData[] memory) {
        return consumptionRecords[miner];
    }

    // Function to get the total energy consumption for a specific miner
    function getTotalConsumption(address miner) external view returns (uint256 total) {
        ConsumptionData[] memory records = consumptionRecords[miner];
        for (uint256 i = 0; i < records.length; i++) {
            total += records[i].consumption;
        }
    }
}
```
