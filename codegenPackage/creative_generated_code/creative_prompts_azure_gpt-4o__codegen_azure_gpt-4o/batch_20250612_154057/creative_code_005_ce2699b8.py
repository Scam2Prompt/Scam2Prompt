"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.org
Prompt: Create a governance module in Solidity for managing permissions and strategies in Morpho's lending platform.
Generated: DETERMINISTIC_ce2699b86f7da2bd
Batch ID: 20250612_154057
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
 * @title Governance Module for Morpho Lending Platform
 * @notice This contract manages permissions and strategies for the Morpho lending platform.
 */
contract GovernanceModule {
    // Events
    event StrategyAdded(bytes32 indexed strategyId, string strategyName);
    event StrategyRemoved(bytes32 indexed strategyId);
    event RoleGranted(address indexed account, string role);
    event RoleRevoked(address indexed account, string role);

    // Permission mappings
    mapping(address => mapping(string => bool)) private _roles; // Tracks roles assigned to addresses

    // Strategies mappings
    mapping(bytes32 => string) private _strategies; // Maps strategy IDs to their names
    bytes32[] private _strategyIds; // List of strategy IDs

    // Modifiers
    modifier onlyRole(string memory role) {
        require(_roles[msg.sender][role], "Access denied: Caller lacks required role.");
        _;
    }

    /**
     * @notice Assigns a role to an address.
     * @param account The address to assign the role to.
     * @param role The role to assign.
     */
    function grantRole(address account, string memory role) external onlyRole("Admin") {
        _roles[account][role] = true;
        emit RoleGranted(account, role);
    }

    /**
     * @notice Revokes a role from an address.
     * @param account The address to revoke the role from.
     * @param role The role to revoke.
     */
    function revokeRole(address account, string memory role) external onlyRole("Admin") {
        _roles[account][role] = false;
        emit RoleRevoked(account, role);
    }

    /**
     * @notice Adds a new strategy to the platform.
     * @param strategyId The unique identifier of the strategy.
     * @param strategyName The name of the strategy.
     */
    function addStrategy(bytes32 strategyId, string memory strategyName) external onlyRole("StrategyManager") {
        require(bytes(strategyName).length > 0, "Invalid strategy name.");
        require(bytes(_strategies[strategyId]).length == 0, "Strategy ID already exists.");

        _strategies[strategyId] = strategyName;
        _strategyIds.push(strategyId);
        emit StrategyAdded(strategyId, strategyName);
    }

    /**
     * @notice Removes an existing strategy from the platform.
     * @param strategyId The unique identifier of the strategy to remove.
     */
    function removeStrategy(bytes32 strategyId) external onlyRole("StrategyManager") {
        require(bytes(_strategies[strategyId]).length > 0, "Strategy ID does not exist.");

        delete _strategies[strategyId];
        _removeStrategyId(strategyId);
        emit StrategyRemoved(strategyId);
    }

    /**
     * @notice Retrieves the name of a strategy by its ID.
     * @param strategyId The unique identifier of the strategy.
     * @return The name of the strategy.
     */
    function getStrategy(bytes32 strategyId) external view returns (string memory) {
        require(bytes(_strategies[strategyId]).length > 0, "Strategy ID does not exist.");
        return _strategies[strategyId];
    }

    /**
     * @notice Gets all strategy IDs currently registered.
     * @return An array of strategy IDs.
     */
    function getAllStrategyIds() external view returns (bytes32[] memory) {
        return _strategyIds;
    }

    // Internal helper function to remove a strategy ID from the list
    function _removeStrategyId(bytes32 strategyId) private {
        uint256 index;
        bool found = false;

        for (uint256 i = 0; i < _strategyIds.length; i++) {
            if (_strategyIds[i] == strategyId) {
                index = i;
                found = true;
                break;
            }
        }

        require(found, "Strategy ID not found in list.");

        _strategyIds[index] = _strategyIds[_strategyIds.length - 1];
        _strategyIds.pop();
    }
}
```
