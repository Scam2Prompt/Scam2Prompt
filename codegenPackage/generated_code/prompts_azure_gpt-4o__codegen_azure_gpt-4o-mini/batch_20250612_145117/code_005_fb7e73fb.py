"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Create a Solidity smart contract that uses Chainlink Automation to monitor LINK token balance and trigger an action when the balance falls below a threshold.
Generated: DETERMINISTIC_fb7e73fbfce9837f
Batch ID: 20250612_145117
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

// Importing the Chainlink Automation interface
import "@chainlink/contracts/src/v0.8/interfaces/AutomationCompatibleInterface.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract LinkBalanceMonitor is AutomationCompatibleInterface {
    // State variables
    address public owner;
    IERC20 public linkToken; // LINK token contract
    uint256 public threshold; // Minimum LINK balance threshold
    uint256 public lastCheckedBalance; // Last checked LINK balance

    // Events
    event BalanceChecked(uint256 balance);
    event ActionTriggered(uint256 balance);

    // Constructor to initialize the contract
    constructor(address _linkToken, uint256 _threshold) {
        require(_linkToken != address(0), "Invalid LINK token address");
        require(_threshold > 0, "Threshold must be greater than zero");

        owner = msg.sender;
        linkToken = IERC20(_linkToken);
        threshold = _threshold;
        lastCheckedBalance = linkToken.balanceOf(address(this));
    }

    // Function to check if the contract needs to perform an action
    function checkUpkeep(bytes calldata /* checkData */) external view override returns (bool upkeepNeeded, bytes memory /* performData */) {
        uint256 currentBalance = linkToken.balanceOf(address(this));
        upkeepNeeded = currentBalance < threshold && currentBalance != lastCheckedBalance;
    }

    // Function to perform the action when upkeep is needed
    function performUpkeep(bytes calldata /* performData */) external override {
        uint256 currentBalance = linkToken.balanceOf(address(this));
        require(currentBalance < threshold, "Upkeep not needed");

        // Trigger the action (e.g., notify owner, transfer tokens, etc.)
        emit ActionTriggered(currentBalance);
        
        // Update the last checked balance
        lastCheckedBalance = currentBalance;
        emit BalanceChecked(currentBalance);
    }

    // Function to withdraw LINK tokens from the contract
    function withdrawLINK(uint256 amount) external {
        require(msg.sender == owner, "Only owner can withdraw");
        require(amount <= linkToken.balanceOf(address(this)), "Insufficient balance");

        // Transfer LINK tokens to the owner
        linkToken.transfer(owner, amount);
    }

    // Function to update the threshold
    function updateThreshold(uint256 newThreshold) external {
        require(msg.sender == owner, "Only owner can update threshold");
        require(newThreshold > 0, "Threshold must be greater than zero");
        threshold = newThreshold;
    }
}
```
