"""
Generated Code Metadata:
========================
Original URL: https://lido-hi.github.io
Prompt: Explain how Lido Finance's oracle contract works and provide a high-level overview of its role in tracking validator balances on the Ethereum Beacon Chain.
Generated: DETERMINISTIC_7959c6ba712eb83e
Batch ID: 20250622_211156
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
 * @title Lido Oracle Contract
 * @dev This contract is a simplified representation of how Lido Finance's oracle works.
 * It tracks validator balances on the Ethereum Beacon Chain and updates the total staked ETH.
 * Note: This is a high-level overview and not the actual implementation used by Lido Finance.
 */
contract LidoOracle {
    // State variables
    uint256 public totalStakedETH; // Total ETH staked across all validators
    address public owner; // Owner of the contract (typically the Lido DAO or a trusted entity)
    mapping(address => bool) public trustedReporters; // List of trusted reporters (oracles)

    // Events
    event ValidatorBalanceUpdated(uint256 newTotalStakedETH);
    event ReporterAdded(address reporter);
    event ReporterRemoved(address reporter);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    modifier onlyTrustedReporter() {
        require(trustedReporters[msg.sender], "Caller is not a trusted reporter");
        _;
    }

    /**
     * @dev Constructor to initialize the contract.
     * @param _owner Address of the contract owner.
     */
    constructor(address _owner) {
        require(_owner != address(0), "Owner address cannot be zero");
        owner = _owner;
    }

    /**
     * @dev Adds a trusted reporter (oracle) to the contract.
     * @param _reporter Address of the reporter to be added.
     */
    function addReporter(address _reporter) external onlyOwner {
        require(_reporter != address(0), "Reporter address cannot be zero");
        trustedReporters[_reporter] = true;
        emit ReporterAdded(_reporter);
    }

    /**
     * @dev Removes a trusted reporter (oracle) from the contract.
     * @param _reporter Address of the reporter to be removed.
     */
    function removeReporter(address _reporter) external onlyOwner {
        require(trustedReporters[_reporter], "Reporter is not trusted");
        trustedReporters[_reporter] = false;
        emit ReporterRemoved(_reporter);
    }

    /**
     * @dev Updates the total staked ETH based on validator balances reported by a trusted oracle.
     * @param _newTotalStakedETH The new total staked ETH value.
     */
    function updateValidatorBalances(uint256 _newTotalStakedETH) external onlyTrustedReporter {
        require(_newTotalStakedETH >= 0, "Staked ETH cannot be negative");
        totalStakedETH = _newTotalStakedETH;
        emit ValidatorBalanceUpdated(_newTotalStakedETH);
    }

    /**
     * @dev Allows the owner to transfer ownership of the contract.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "New owner address cannot be zero");
        owner = _newOwner;
    }
}
```
