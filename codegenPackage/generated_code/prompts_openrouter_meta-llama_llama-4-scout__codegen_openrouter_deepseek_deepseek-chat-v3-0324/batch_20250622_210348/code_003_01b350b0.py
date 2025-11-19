"""
Generated Code Metadata:
========================
Original URL: https://integratedconnections.pages.dev
Prompt: "Design a library for wallet validation and safety tools, including unusual wallet distribution alerts and deployer wallet warnings, using the EVM protocol."
Generated: DETERMINISTIC_01b350b08187394f
Batch ID: 20250622_210348
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
 * @title WalletSafetyTools
 * @dev A library for wallet validation and safety tools on EVM-compatible chains
 */
library WalletSafetyTools {
    // Thresholds for unusual activity detection
    uint256 public constant UNUSUAL_TX_COUNT_THRESHOLD = 100;
    uint256 public constant UNUSUAL_VALUE_THRESHOLD = 100 ether;
    uint256 public constant RECENT_TIME_WINDOW = 1 days;
    
    /**
     * @dev Struct to hold wallet activity data
     */
    struct WalletActivity {
        uint256 transactionCount;
        uint256 totalValue;
        uint256 lastActiveTimestamp;
        address[] interactedWallets;
    }
    
    /**
     * @dev Emitted when unusual wallet activity is detected
     */
    event UnusualActivityDetected(address indexed wallet, string reason);
    
    /**
     * @dev Emitted when a deployer wallet is detected
     */
    event DeployerWalletDetected(address indexed wallet);
    
    /**
     * @dev Validates if a wallet address is valid (not zero address and proper format)
     * @param _wallet The wallet address to validate
     */
    function validateWallet(address _wallet) internal pure returns (bool) {
        return _wallet != address(0);
    }
    
    /**
     * @dev Checks for unusual wallet activity patterns
     * @param activity The wallet's activity data
     */
    function checkUnusualActivity(WalletActivity memory activity) internal view {
        if (activity.transactionCount > UNUSUAL_TX_COUNT_THRESHOLD) {
            emit UnusualActivityDetected(msg.sender, "High transaction count");
        }
        
        if (activity.totalValue > UNUSUAL_VALUE_THRESHOLD) {
            emit UnusualActivityDetected(msg.sender, "High value transferred");
        }
        
        if (block.timestamp - activity.lastActiveTimestamp < RECENT_TIME_WINDOW) {
            emit UnusualActivityDetected(msg.sender, "High frequency activity");
        }
    }
    
    /**
     * @dev Checks if a wallet is a contract deployer (has created contracts)
     * @param _wallet The wallet address to check
     */
    function checkDeployerWallet(address _wallet) internal view {
        uint256 size;
        assembly {
            size := extcodesize(_wallet)
        }
        
        if (size > 0) {
            emit DeployerWalletDetected(_wallet);
        }
    }
    
    /**
     * @dev Checks for wallet clustering (multiple wallets interacting with same addresses)
     * @param activity1 First wallet's activity data
     * @param activity2 Second wallet's activity data
     * @return overlapCount Number of overlapping interacted wallets
     */
    function checkWalletClustering(
        WalletActivity memory activity1,
        WalletActivity memory activity2
    ) internal pure returns (uint256 overlapCount) {
        for (uint256 i = 0; i < activity1.interactedWallets.length; i++) {
            for (uint256 j = 0; j < activity2.interactedWallets.length; j++) {
                if (activity1.interactedWallets[i] == activity2.interactedWallets[j]) {
                    overlapCount++;
                    break;
                }
            }
        }
        return overlapCount;
    }
    
    /**
     * @dev Checks if a wallet is a known exchange address
     * @param _wallet The wallet address to check
     * @param knownExchangeAddresses List of known exchange addresses
     */
    function checkExchangeWallet(
        address _wallet,
        address[] memory knownExchangeAddresses
    ) internal pure returns (bool) {
        for (uint256 i = 0; i < knownExchangeAddresses.length; i++) {
            if (_wallet == knownExchangeAddresses[i]) {
                return true;
            }
        }
        return false;
    }
}
```
