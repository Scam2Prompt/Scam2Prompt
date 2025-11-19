"""
Generated Code Metadata:
========================
Original URL: https://automation-feat-front-3795-display-log-tr-chainlinklabs.vercel.app
Prompt: Provide a code example for detecting a wallet and triggering Chainlink Automation to execute a function on Ethereum Goerli.
Generated: DETERMINISTIC_d2e41ee1412a10e1
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
pragma solidity ^0.8.7;

// Import Chainlink Automation interfaces
import "@chainlink/contracts/src/v0.8/automation/interfaces/AutomationCompatibleInterface.sol";

/**
 * @title WalletMonitor
 * @dev A contract that monitors a wallet balance and triggers Chainlink Automation
 * when the balance falls below a threshold.
 */
contract WalletMonitor is AutomationCompatibleInterface {
    // The wallet address to monitor
    address public immutable walletToMonitor;
    // The minimum balance threshold (in wei)
    uint256 public immutable minBalanceThreshold;
    // The target contract to call when balance is low
    address public immutable targetContract;
    // The function selector to call on the target contract
    bytes4 public immutable targetFunctionSelector;

    /**
     * @dev Constructor to initialize the monitor parameters
     * @param _walletToMonitor The wallet address to monitor
     * @param _minBalanceThreshold The minimum balance threshold in wei
     * @param _targetContract The contract to call when balance is low
     * @param _targetFunctionSelector The function selector to call
     */
    constructor(
        address _walletToMonitor,
        uint256 _minBalanceThreshold,
        address _targetContract,
        bytes4 _targetFunctionSelector
    ) {
        walletToMonitor = _walletToMonitor;
        minBalanceThreshold = _minBalanceThreshold;
        targetContract = _targetContract;
        targetFunctionSelector = _targetFunctionSelector;
    }

    /**
     * @dev Checks if the wallet balance is below threshold
     * @return upkeepNeeded Boolean indicating if upkeep is needed
     * @return performData Additional data for the upkeep (not used here)
     */
    function checkUpkeep(
        bytes calldata /* checkData */
    )
        external
        view
        override
        returns (bool upkeepNeeded, bytes memory performData)
    {
        uint256 currentBalance = walletToMonitor.balance;
        upkeepNeeded = currentBalance < minBalanceThreshold;
        performData = ""; // No additional data needed
        return (upkeepNeeded, performData);
    }

    /**
     * @dev Executes the target function when balance is low
     * @param /* performData */ Additional data (not used here)
     */
    function performUpkeep(bytes calldata /* performData */) external override {
        // Verify the balance is still below threshold
        uint256 currentBalance = walletToMonitor.balance;
        require(currentBalance < minBalanceThreshold, "Balance above threshold");

        // Call the target function
        (bool success, ) = targetContract.call(
            abi.encodeWithSelector(targetFunctionSelector)
        );
        require(success, "Target call failed");
    }
}
```

```javascript
// This is a sample Hardhat task to register the upkeep with Chainlink Automation
// Should be run after deploying the WalletMonitor contract

const { ethers } = require("hardhat");
const { LinkToken } = require("@chainlink/contracts/tests/test-helpers");

async function registerUpkeep() {
  // Get contract factories
  const WalletMonitor = await ethers.getContractFactory("WalletMonitor");
  const linkToken = await ethers.getContractAt(
    LinkToken.abi,
    "0x326C977E6efc84E512bB9C30f76E30c160eD06FB" // Goerli LINK token
  );
  const automationRegistry = await ethers.getContractAt(
    "KeeperRegistry",
    "0xE16Df59B887e3Caa439E0b29B42bA2e7976FD8b2" // Goerli registry
  );

  // Deploy WalletMonitor
  const walletMonitor = await WalletMonitor.deploy(
    "0xWalletAddressToMonitor", // Replace with actual wallet
    ethers.utils.parseEther("0.1"), // 0.1 ETH threshold
    "0xTargetContractAddress", // Replace with target contract
    "0xabcdef12" // Replace with function selector
  );
  await walletMonitor.deployed();

  // Approve LINK for registration
  const registrationTx = await linkToken.approve(
    automationRegistry.address,
    ethers.utils.parseEther("5.0") // 5 LINK registration fee
  );
  await registrationTx.wait();

  // Register the upkeep
  const registerTx = await automationRegistry.registerUpkeep(
    walletMonitor.address, // Upkeep target
    200000, // Gas limit
    "0x", // Admin address
    "0x", // Check data
    ethers.utils.parseEther("5.0"), // 5 LINK funding amount
    0, // Source (0 for off-chain)
    "WalletMonitor Upkeep" // Descriptive name
  );
  await registerTx.wait();

  console.log("Upkeep registered successfully");
}

registerUpkeep().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
```
