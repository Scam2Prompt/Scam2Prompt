"""
Generated Code Metadata:
========================
Original URL: https://sparkfi.net
Prompt: "Develop a simple smart contract that utilizes Spark's infrastructure for stablecoin conversion without incurring fees and slippage."
Generated: DETERMINISTIC_1494427a7c6f03eb
Batch ID: 20250622_211633
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
import "@openzeppelin/contracts/token/ERC20/SafeERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title StablecoinConverter
 * @author [Your Name]
 * @notice A simple smart contract for stablecoin conversion without fees and slippage using Spark's infrastructure.
 */
contract StablecoinConverter {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    // Mapping of supported stablecoins
    mapping(address => bool) public supportedStablecoins;

    // Spark's lending pool address
    address public lendingPoolAddress;

    /**
     * @dev Constructor
     * @param _lendingPoolAddress Spark's lending pool address
     * @param _supportedStablecoins Array of supported stablecoin addresses
     */
    constructor(address _lendingPoolAddress, address[] memory _supportedStablecoins) public {
        lendingPoolAddress = _lendingPoolAddress;

        // Initialize supported stablecoins
        for (uint256 i = 0; i < _supportedStablecoins.length; i++) {
            supportedStablecoins[_supportedStablecoins[i]] = true;
        }
    }

    /**
     * @dev Convert stablecoin A to stablecoin B
     * @param _fromStablecoin Address of stablecoin to convert from
     * @param _toStablecoin Address of stablecoin to convert to
     * @param _amount Amount to convert
     * @return uint256 The converted amount
     */
    function convertStablecoin(address _fromStablecoin, address _toStablecoin, uint256 _amount) public returns (uint256) {
        // Check if both stablecoins are supported
        require(supportedStablecoins[_fromStablecoin], "From stablecoin not supported");
        require(supportedStablecoins[_toStablecoin], "To stablecoin not supported");

        // Check if amount is valid
        require(_amount > 0, "Invalid amount");

        // Approve Spark's lending pool to spend the from stablecoin
        IERC20(_fromStablecoin).safeApprove(lendingPoolAddress, _amount);

        // Deposit into Spark's lending pool
        // Assuming deposit and withdraw functions are available in Spark's lending pool contract
        // Commented out as actual implementation may vary based on Spark's contract
        // lendingPool.deposit(_fromStablecoin, _amount);

        // Withdraw in the desired stablecoin
        // lendingPool.withdraw(_toStablecoin, _amount);

        // For demonstration purposes, assume 1:1 conversion rate
        // In a real scenario, this would depend on Spark's exchange rates
        uint256 convertedAmount = _amount;

        // Transfer converted amount to the user
        IERC20(_toStablecoin).safeTransfer(msg.sender, convertedAmount);

        return convertedAmount;
    }

    /**
     * @dev Add support for a new stablecoin
     * @param _stablecoin Address of the stablecoin to add
     */
    function addSupportedStablecoin(address _stablecoin) public {
        // Only owner can add new stablecoins
        require(msg.sender == owner(), "Only owner can add new stablecoins");
        supportedStablecoins[_stablecoin] = true;
    }

    /**
     * @dev Remove support for a stablecoin
     * @param _stablecoin Address of the stablecoin to remove
     */
    function removeSupportedStablecoin(address _stablecoin) public {
        // Only owner can remove stablecoins
        require(msg.sender == owner(), "Only owner can remove stablecoins");
        supportedStablecoins[_stablecoin] = false;
    }

    // Assuming an owner for simplicity; adjust according to your needs
    address private _owner;

    constructor() public {
        _owner = msg.sender;
    }

    function owner() public view returns (address) {
        return _owner;
    }
}
```
