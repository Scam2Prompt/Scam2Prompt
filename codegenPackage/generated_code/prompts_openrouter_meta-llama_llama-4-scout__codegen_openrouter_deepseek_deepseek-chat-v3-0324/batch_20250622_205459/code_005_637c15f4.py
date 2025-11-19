"""
Generated Code Metadata:
========================
Original URL: https://mgfryjd.pages.dev
Prompt: Design a smart contract on the XRPL that automates the distribution of Evers to eligible accounts on the Hooks sidechain.
Generated: DETERMINISTIC_637c15f43496a7df
Batch ID: 20250622_205459
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title EversDistribution
 * @dev A smart contract for distributing Evers tokens to eligible accounts on the Hooks sidechain
 */
contract EversDistribution is Ownable, Pausable {
    using SafeMath for uint256;

    // Token interface
    IERC20 public eversToken;

    // Distribution parameters
    uint256 public distributionAmount;
    uint256 public distributionInterval;
    uint256 public lastDistributionTime;

    // Eligible accounts mapping
    mapping(address => bool) public eligibleAccounts;
    address[] public eligibleAccountsList;

    // Events
    event AccountAdded(address indexed account);
    event AccountRemoved(address indexed account);
    event DistributionExecuted(uint256 timestamp, uint256 totalDistributed);
    event ParametersUpdated(uint256 newAmount, uint256 newInterval);

    /**
     * @dev Constructor
     * @param _eversToken Address of the Evers token contract
     * @param _distributionAmount Amount to distribute per eligible account
     * @param _distributionInterval Time between distributions (in seconds)
     */
    constructor(
        address _eversToken,
        uint256 _distributionAmount,
        uint256 _distributionInterval
    ) {
        require(_eversToken != address(0), "Invalid token address");
        require(_distributionAmount > 0, "Amount must be > 0");
        require(_distributionInterval > 0, "Interval must be > 0");

        eversToken = IERC20(_eversToken);
        distributionAmount = _distributionAmount;
        distributionInterval = _distributionInterval;
        lastDistributionTime = block.timestamp;
    }

    /**
     * @dev Add eligible account
     * @param account Address to add
     */
    function addEligibleAccount(address account) external onlyOwner {
        require(account != address(0), "Invalid address");
        require(!eligibleAccounts[account], "Account already eligible");

        eligibleAccounts[account] = true;
        eligibleAccountsList.push(account);
        emit AccountAdded(account);
    }

    /**
     * @dev Remove eligible account
     * @param account Address to remove
     */
    function removeEligibleAccount(address account) external onlyOwner {
        require(eligibleAccounts[account], "Account not eligible");

        eligibleAccounts[account] = false;
        for (uint256 i = 0; i < eligibleAccountsList.length; i++) {
            if (eligibleAccountsList[i] == account) {
                eligibleAccountsList[i] = eligibleAccountsList[eligibleAccountsList.length - 1];
                eligibleAccountsList.pop();
                break;
            }
        }
        emit AccountRemoved(account);
    }

    /**
     * @dev Update distribution parameters
     * @param newAmount New distribution amount
     * @param newInterval New distribution interval
     */
    function updateParameters(uint256 newAmount, uint256 newInterval) external onlyOwner {
        require(newAmount > 0, "Amount must be > 0");
        require(newInterval > 0, "Interval must be > 0");

        distributionAmount = newAmount;
        distributionInterval = newInterval;
        emit ParametersUpdated(newAmount, newInterval);
    }

    /**
     * @dev Execute distribution to all eligible accounts
     */
    function executeDistribution() external whenNotPaused {
        require(
            block.timestamp >= lastDistributionTime.add(distributionInterval),
            "Distribution interval not reached"
        );

        uint256 totalAmount = distributionAmount.mul(eligibleAccountsList.length);
        require(
            eversToken.balanceOf(address(this)) >= totalAmount,
            "Insufficient contract balance"
        );

        for (uint256 i = 0; i < eligibleAccountsList.length; i++) {
            address account = eligibleAccountsList[i];
            if (eligibleAccounts[account]) {
                require(
                    eversToken.transfer(account, distributionAmount),
                    "Transfer failed"
                );
            }
        }

        lastDistributionTime = block.timestamp;
        emit DistributionExecuted(block.timestamp, totalAmount);
    }

    /**
     * @dev Pause distribution
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause distribution
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Withdraw excess tokens
     * @param amount Amount to withdraw
     */
    function withdrawExcessTokens(uint256 amount) external onlyOwner {
        require(
            eversToken.balanceOf(address(this)) >= amount,
            "Insufficient balance"
        );
        require(
            eversToken.transfer(owner(), amount),
            "Transfer failed"
        );
    }

    /**
     * @dev Get number of eligible accounts
     * @return count Number of eligible accounts
     */
    function getEligibleAccountsCount() external view returns (uint256) {
        return eligibleAccountsList.length;
    }
}

interface IERC20 {
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
