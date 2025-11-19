"""
Generated Code Metadata:
========================
Original URL: https://tenderize.xyz
Prompt: Generate code to implement a token burn mechanism for deflationary purposes, similar to Tenderize's approach of burning tokens from platform fees.
Generated: DETERMINISTIC_19131e4acf444a80
Batch ID: 20250612_145913
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
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title TokenBurner
 * @dev A contract that handles burning tokens from collected fees for deflationary purposes
 */
contract TokenBurner is Ownable, Pausable {
    using SafeERC20 for IERC20;

    // The token to be burned
    IERC20 public immutable burnToken;

    // Address where tokens are collected before burning
    address public feeCollector;

    // Minimum token balance required before burning can occur
    uint256 public minBurnThreshold;

    // Event emitted when tokens are burned
    event TokensBurned(uint256 amount);
    event FeeCollectorUpdated(address newCollector);
    event MinBurnThresholdUpdated(uint256 newThreshold);

    /**
     * @dev Initializes the contract with the token to burn and initial parameters
     * @param _burnToken Address of the ERC20 token to burn
     * @param _feeCollector Address where fees are collected
     * @param _minBurnThreshold Minimum token balance required for burning
     */
    constructor(
        address _burnToken,
        address _feeCollector,
        uint256 _minBurnThreshold
    ) {
        require(_burnToken != address(0), "TokenBurner: invalid token address");
        require(_feeCollector != address(0), "TokenBurner: invalid collector address");

        burnToken = IERC20(_burnToken);
        feeCollector = _feeCollector;
        minBurnThreshold = _minBurnThreshold;
    }

    /**
     * @dev Burns all available tokens in the fee collector address
     */
    function burnTokens() external whenNotPaused {
        uint256 balance = burnToken.balanceOf(feeCollector);
        require(balance >= minBurnThreshold, "TokenBurner: insufficient balance to burn");

        // Transfer tokens from collector to this contract first
        burnToken.safeTransferFrom(feeCollector, address(this), balance);

        // Burn the tokens by sending to address(0)
        burnToken.safeTransfer(address(0), balance);

        emit TokensBurned(balance);
    }

    /**
     * @dev Updates the fee collector address
     * @param _newCollector New fee collector address
     */
    function updateFeeCollector(address _newCollector) external onlyOwner {
        require(_newCollector != address(0), "TokenBurner: invalid collector address");
        feeCollector = _newCollector;
        emit FeeCollectorUpdated(_newCollector);
    }

    /**
     * @dev Updates the minimum burn threshold
     * @param _newThreshold New minimum threshold for burning
     */
    function updateMinBurnThreshold(uint256 _newThreshold) external onlyOwner {
        minBurnThreshold = _newThreshold;
        emit MinBurnThresholdUpdated(_newThreshold);
    }

    /**
     * @dev Pauses the burning functionality
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpauses the burning functionality
     */
    function unpause() external onlyOwner {
        _unpause();
    }
}
```
