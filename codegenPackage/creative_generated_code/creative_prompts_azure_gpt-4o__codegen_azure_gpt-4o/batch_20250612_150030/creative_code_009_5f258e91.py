"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Generate a Solidity contract that locks ETH and releases USDC to a recipient after a specified time period.
Generated: DETERMINISTIC_5f258e919899a0d6
Batch ID: 20250612_150030
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
 * @title ETHLocker
 * @dev Locks ETH and releases USDC to a recipient after a specified time period.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ETHLocker {
    // Address of the USDC token contract
    IERC20 public usdcToken;

    // Address of the recipient to receive USDC
    address public recipient;

    // Timestamp when the USDC can be released
    uint256 public unlockTime;

    // Tracks if USDC has been released
    bool public isReleased;

    // Event emitted when ETH is locked
    event ETHLocked(address indexed sender, uint256 amount);

    // Event emitted when USDC is released
    event USDCReleased(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize contract parameters.
     * @param _usdcToken Address of the USDC token contract.
     * @param _recipient Address of the recipient to receive USDC.
     * @param _unlockTime Timestamp when USDC can be released.
     */
    constructor(IERC20 _usdcToken, address _recipient, uint256 _unlockTime) {
        require(_recipient != address(0), "Recipient address cannot be zero");
        require(_unlockTime > block.timestamp, "Unlock time must be in the future");

        usdcToken = _usdcToken;
        recipient = _recipient;
        unlockTime = _unlockTime;
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {
        require(msg.value > 0, "Deposit amount must be greater than zero");
        emit ETHLocked(msg.sender, msg.value);
    }

    /**
     * @dev Function to release USDC to the recipient after unlock time.
     */
    function releaseUSDC(uint256 usdcAmount) external {
        require(block.timestamp >= unlockTime, "Cannot release USDC before unlock time");
        require(!isReleased, "USDC has already been released");
        require(usdcToken.balanceOf(address(this)) >= usdcAmount, "Insufficient USDC balance in contract");

        // Mark USDC as released
        isReleased = true;

        // Transfer USDC to the recipient
        require(usdcToken.transfer(recipient, usdcAmount), "USDC transfer failed");

        emit USDCReleased(recipient, usdcAmount);
    }

    /**
     * @dev Function to view contract's ETH balance.
     * @return Contract's ETH balance.
     */
    function getETHBalance() external view returns (uint256) {
        return address(this).balance;
    }

    /**
     * @dev Function to view contract's USDC balance.
     * @return Contract's USDC balance.
     */
    function getUSDCBalance() external view returns (uint256) {
        return usdcToken.balanceOf(address(this));
    }
}
```
