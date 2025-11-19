"""
Generated Code Metadata:
========================
Original URL: https://rocket-pool.xyz
Prompt: Create a Solidity contract that facilitates the migration of solo Ethereum validators to Rocket Pool, converting 32 ETH validators to 8 ETH validators. Include functionality for interacting with Rocket Pool's migration tools.
Generated: DETERMINISTIC_a7b86ac6a6ae8c36
Batch ID: 20250612_153821
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Pausable.sol";

/**
 * @title Rocket Pool Migration Contract
 * @author [Your Name]
 * @notice Facilitates the migration of solo Ethereum validators to Rocket Pool
 */
contract RocketPoolMigration {
    using SafeMath for uint256;

    // Mapping of validator addresses to their migration status
    mapping(address => bool) public validatorMigrationStatus;

    // Address of the Rocket Pool migration tool contract
    address public rocketPoolMigrationTool;

    // Address of the Rocket Pool contract
    address public rocketPoolContract;

    // Mapping of 32 ETH validator addresses to their corresponding 8 ETH validator addresses
    mapping(address => address[]) public validatorMapping;

    /**
     * @dev Constructor
     * @param _rocketPoolMigrationTool Address of the Rocket Pool migration tool contract
     * @param _rocketPoolContract Address of the Rocket Pool contract
     */
    constructor(address _rocketPoolMigrationTool, address _rocketPoolContract) public {
        require(_rocketPoolMigrationTool != address(0), "Invalid Rocket Pool migration tool address");
        require(_rocketPoolContract != address(0), "Invalid Rocket Pool contract address");

        rocketPoolMigrationTool = _rocketPoolMigrationTool;
        rocketPoolContract = _rocketPoolContract;
    }

    /**
     * @dev Migrate a 32 ETH validator to 8 ETH validators
     * @param _validator Address of the 32 ETH validator
     */
    function migrateValidator(address _validator) public {
        require(_validator != address(0), "Invalid validator address");
        require(validatorMigrationStatus[_validator] == false, "Validator already migrated");

        // Interact with Rocket Pool's migration tool to perform the migration
        bool success = IRocketPoolMigrationTool(rocketPoolMigrationTool).migrateValidator(_validator);
        require(success, "Migration failed");

        // Update the migration status and validator mapping
        validatorMigrationStatus[_validator] = true;
        address[] memory newValidators = IRocketPoolMigrationTool(rocketPoolMigrationTool).getNewValidators(_validator);
        validatorMapping[_validator] = newValidators;
    }

    /**
     * @dev Get the 8 ETH validators for a given 32 ETH validator
     * @param _validator Address of the 32 ETH validator
     * @return address[] Array of 8 ETH validator addresses
     */
    function getNewValidators(address _validator) public view returns (address[] memory) {
        return validatorMapping[_validator];
    }

    /**
     * @dev Update the Rocket Pool migration tool contract address
     * @param _newAddress New address of the Rocket Pool migration tool contract
     */
    function updateRocketPoolMigrationTool(address _newAddress) public onlyOwner {
        require(_newAddress != address(0), "Invalid Rocket Pool migration tool address");
        rocketPoolMigrationTool = _newAddress;
    }

    /**
     * @dev Update the Rocket Pool contract address
     * @param _newAddress New address of the Rocket Pool contract
     */
    function updateRocketPoolContract(address _newAddress) public onlyOwner {
        require(_newAddress != address(0), "Invalid Rocket Pool contract address");
        rocketPoolContract = _newAddress;
    }
}

// Interface for Rocket Pool migration tool contract
interface IRocketPoolMigrationTool {
    function migrateValidator(address _validator) external returns (bool);
    function getNewValidators(address _validator) external view returns (address[] memory);
}
```
