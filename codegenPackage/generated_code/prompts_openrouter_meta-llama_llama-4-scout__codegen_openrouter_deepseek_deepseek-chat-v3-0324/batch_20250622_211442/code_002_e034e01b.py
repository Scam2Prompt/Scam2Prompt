"""
Generated Code Metadata:
========================
Original URL: https://ondo-finance.pages.dev
Prompt: "Generate a smart contract code for converting between OUSG and rOUSG token versions on the Ethereum network."
Generated: DETERMINISTIC_e034e01b1f857daf
Batch ID: 20250622_211442
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title OUSG-rOUSG Converter
 * @dev Smart contract for converting between OUSG and rOUSG token versions
 * Features:
 * - Convert OUSG to rOUSG
 * - Convert rOUSG back to OUSG
 * - Admin functions for managing conversion rates and pausing
 * - Reentrancy protection
 * - Proper access control
 */
contract OUSGConverter is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    // Token contracts
    IERC20 public immutable ousgToken;
    IERC20 public immutable rousgToken;

    // Conversion rate (with decimals)
    uint256 public conversionRate;
    uint256 public constant RATE_DECIMALS = 1e18;

    // Contract state
    bool public isActive;

    // Events
    event ConvertedToROUSG(address indexed user, uint256 ousgAmount, uint256 rousgAmount);
    event ConvertedToOUSG(address indexed user, uint256 rousgAmount, uint256 ousgAmount);
    event ConversionRateUpdated(uint256 newRate);
    contract is not active");
        _;
    }

    /**
     * @dev Constructor
     * @param _ousg Address of OUSG token contract
     * @param _rousg Address of rOUSG token contract
     * @param _initialRate Initial conversion rate (1 OUSG = X rOUSG)
     */
    constructor(
        address _ousg,
        address _rousg,
        uint256 _initialRate
    ) {
        require(_ousg != address(0), "OUSG address cannot be zero");
        require(_rousg != address(0), "rOUSG address cannot be zero");
        require(_initialRate > 0, "Conversion rate must be positive");

        ousgToken = IERC20(_ousg);
        rousgToken = IERC20(_rousg);
        conversionRate = _initialRate;
        isActive = true;
    }

    /**
     * @dev Convert OUSG to rOUSG
     * @param amount Amount of OUSG to convert
     */
    function convertToROUSG(uint256 amount) external nonReentrant whenActive {
        require(amount > 0, "Amount must be positive");

        // Calculate rOUSG amount
        uint256 rousgAmount = (amount * conversionRate) / RATE_DECIMALS;
        require(rousgAmount > 0, "Resulting rOUSG amount too small");

        // Transfer OUSG from user
        ousgToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer rOUSG to user
        rousgToken.safeTransfer(msg.sender, rousgAmount);

        emit ConvertedToROUSG(msg.sender, amount, rousgAmount);
    }

    /**
     * @dev Convert rOUSG back to OUSG
     * @param amount Amount of rOUSG to convert
     */
    function convertToOUSG(uint256 amount) external nonReentrant whenActive {
        require(amount > 0, "Amount must be positive");

        // Calculate OUSG amount
        uint256 ousgAmount = (amount * RATE_DECIMALS) / conversionRate;
        require(ousgAmount > 0, "Resulting OUSG amount too small");

        // Transfer rOUSG from user
        rousgToken.safeTransferFrom(msg.sender, address(this), amount);

        // Transfer OUSG to user
        ousgToken.safeTransfer(msg.sender, ousgAmount);

        emit ConvertedToOUSG(msg.sender, amount, ousgAmount);
    }

    /**
     * @dev Update conversion rate (admin only)
     * @param newRate New conversion rate (1 OUSG = X rOUSG)
     */
    function updateConversionRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Conversion rate must be positive");
        conversionRate = newRate;
        emit ConversionRateUpdated(newRate);
    }

    /**
     * @dev Toggle contract activity (admin only)
     * @param active New state (true = active, false = paused)
     */
    function setActive(bool active) external onlyOwner {
        isActive = active;
        emit ContractActiveStateChanged(active);
    }

    /**
     * @dev Emergency withdraw tokens (admin only)
     * @param token Address of token to withdraw
     * @param amount Amount to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Token address cannot be zero");
        IERC20(token).safeTransfer(owner(), amount);
        emit EmergencyWithdraw(token, amount);
    }
}
```
