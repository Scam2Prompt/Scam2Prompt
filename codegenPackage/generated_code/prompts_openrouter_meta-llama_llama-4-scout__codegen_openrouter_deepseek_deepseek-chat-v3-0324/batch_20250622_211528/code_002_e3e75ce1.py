"""
Generated Code Metadata:
========================
Original URL: https://bridgetensor.org
Prompt: Generate a Solidity smart contract code snippet for handling TAO token bridging to Ethereum Mainnet, including the logic for deducting fees (0.0012 TAO for bridging back to Finney).
Generated: DETERMINISTIC_e3e75ce1f88be2bb
Batch ID: 20250622_211528
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title TAOBridge
 * @dev A smart contract for handling TAO token bridging between Ethereum Mainnet and Finney
 * Includes fee deduction logic for bridging back to Finney (0.0012 TAO fee)
 */
contract TAOBridge is Ownable, ReentrancyGuard {
    IERC20 public taoToken;
    uint256 public constant BRIDGE_FEE = 0.0012 ether; // 0.0012 TAO fee (assuming TAO uses 18 decimals)
    address public feeCollector;

    event BridgedToFinney(address indexed user, uint256 amount, uint256 fee);
    event BridgedToMainnet(address indexed user, uint256 amount);
    event FeeCollectorUpdated(address newFeeCollector);

    /**
     * @dev Constructor initializes the contract with TAO token address and fee collector
     * @param _taoToken Address of the TAO ERC20 token
     * @param _feeCollector Address where bridging fees will be sent
     */
    constructor(address _taoToken, address _feeCollector) {
        require(_taoToken != address(0), "TAO token address cannot be zero");
        require(_feeCollector != address(0), "Fee collector address cannot be zero");
        
        taoToken = IERC20(_taoToken);
        feeCollector = _feeCollector;
    }

    /**
     * @dev Bridges TAO tokens to Finney (with fee deduction)
     * @param amount Amount of TAO tokens to bridge
     */
    function bridgeToFinney(uint256 amount) external nonReentrant {
        require(amount > BRIDGE_FEE, "Amount must be greater than bridge fee");
        
        uint256 amountAfterFee = amount - BRIDGE_FEE;
        
        // Transfer fee to fee collector
        require(
            taoToken.transferFrom(msg.sender, feeCollector, BRIDGE_FEE),
            "Fee transfer failed"
        );
        
        // Transfer remaining amount to bridge contract
        require(
            taoToken.transferFrom(msg.sender, address(this), amountAfterFee),
            "Token transfer failed"
        );
        
        emit BridgedToFinney(msg.sender, amountAfterFee, BRIDGE_FEE);
    }

    /**
     * @dev Bridges TAO tokens back to Ethereum Mainnet (no fee)
     * @param amount Amount of TAO tokens to bridge back
     */
    function bridgeToMainnet(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer tokens back to user
        require(
            taoToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );
        
        emit BridgedToMainnet(msg.sender, amount);
    }

    /**
     * @dev Updates the fee collector address (owner only)
     * @param newFeeCollector New address to receive bridging fees
     */
    function updateFeeCollector(address newFeeCollector) external onlyOwner {
        require(newFeeCollector != address(0), "Fee collector address cannot be zero");
        feeCollector = newFeeCollector;
        emit FeeCollectorUpdated(newFeeCollector);
    }

    /**
     * @dev Emergency withdraw function for stuck tokens (owner only)
     * @param tokenAddress Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Emergency withdraw failed"
        );
    }
}
```
