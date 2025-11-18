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

// Importing the interface for the ERC20 token standard
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ETHLock {
    // State variables
    address public owner;
    address public recipient;
    uint256 public releaseTime;
    uint256 public amountETH;
    IERC20 public usdcToken;

    // Events
    event EthLocked(address indexed owner, uint256 amount, uint256 releaseTime);
    event UsdcReleased(address indexed recipient, uint256 amount);
    event EthWithdrawn(address indexed owner, uint256 amount);

    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not the contract owner");
        _;
    }

    modifier onlyRecipient() {
        require(msg.sender == recipient, "Not the specified recipient");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _usdcToken, address _recipient, uint256 _releaseTime) {
        require(_usdcToken != address(0), "Invalid USDC token address");
        require(_recipient != address(0), "Invalid recipient address");
        require(_releaseTime > block.timestamp, "Release time must be in the future");

        owner = msg.sender;
        usdcToken = IERC20(_usdcToken);
        recipient = _recipient;
        releaseTime = _releaseTime;
    }

    // Function to lock ETH
    function lockETH() external payable onlyOwner {
        require(msg.value > 0, "Must send ETH to lock");
        amountETH += msg.value;
        emit EthLocked(owner, msg.value, releaseTime);
    }

    // Function to release USDC to the recipient after the specified time
    function releaseUSDC(uint256 _amount) external onlyRecipient {
        require(block.timestamp >= releaseTime, "Release time not reached");
        require(usdcToken.balanceOf(address(this)) >= _amount, "Insufficient USDC balance in contract");

        // Transfer USDC to the recipient
        usdcToken.transfer(recipient, _amount);
        emit UsdcReleased(recipient, _amount);
    }

    // Function to withdraw locked ETH before release time (only for owner)
    function withdrawETH() external onlyOwner {
        require(block.timestamp < releaseTime, "Cannot withdraw after release time");
        
        uint256 amountToWithdraw = amountETH;
        amountETH = 0; // Reset amount before transfer to prevent reentrancy
        payable(owner).transfer(amountToWithdraw);
        emit EthWithdrawn(owner, amountToWithdraw);
    }

    // Fallback function to receive ETH
    receive() external payable {
        lockETH();
    }
}
```
