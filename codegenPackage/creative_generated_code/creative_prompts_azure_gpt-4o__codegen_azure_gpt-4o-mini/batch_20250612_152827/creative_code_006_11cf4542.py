"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pulsechain-app.pages.dev
Prompt: Write a Solidity contract that locks ETH on Ethereum and issues "ETH from Ethereum" on PulseChain at a 1:1 ratio.
Generated: DETERMINISTIC_11cf4542039da3e8
Batch ID: 20250612_152827
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

interface IERC20 {
    function totalSupply() external view returns (uint256);
    function balanceOf(address account) external view returns (uint256);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);
}

contract ETHLock {
    // Address of the PulseChain token contract
    address public pulseChainToken;
    // Mapping to track locked ETH balance for each user
    mapping(address => uint256) public lockedETH;

    // Event emitted when ETH is locked
    event ETHLocked(address indexed user, uint256 amount);
    // Event emitted when ETH is unlocked
    event ETHUnlocked(address indexed user, uint256 amount);
    // Event emitted when ETH is issued on PulseChain
    event ETHIssuedOnPulseChain(address indexed user, uint256 amount);

    constructor(address _pulseChainToken) {
        require(_pulseChainToken != address(0), "Invalid PulseChain token address");
        pulseChainToken = _pulseChainToken;
    }

    // Function to lock ETH in the contract
    function lockETH() external payable {
        require(msg.value > 0, "Must send ETH to lock");
        lockedETH[msg.sender] += msg.value;
        emit ETHLocked(msg.sender, msg.value);
    }

    // Function to issue "ETH from Ethereum" on PulseChain
    function issueOnPulseChain(uint256 amount) external {
        require(lockedETH[msg.sender] >= amount, "Insufficient locked ETH");

        // Deduct the amount from the user's locked balance
        lockedETH[msg.sender] -= amount;

        // Transfer the issued tokens from the contract to the user
        IERC20(pulseChainToken).transfer(msg.sender, amount);
        emit ETHIssuedOnPulseChain(msg.sender, amount);
    }

    // Function to unlock ETH and withdraw it back to the user
    function unlockETH(uint256 amount) external {
        require(lockedETH[msg.sender] >= amount, "Insufficient locked ETH");

        // Deduct the amount from the user's locked balance
        lockedETH[msg.sender] -= amount;

        // Transfer the ETH back to the user
        (bool success, ) = msg.sender.call{value: amount}("");
        require(success, "ETH transfer failed");

        emit ETHUnlocked(msg.sender, amount);
    }

    // Function to get the locked ETH balance of a user
    function getLockedETHBalance(address user) external view returns (uint256) {
        return lockedETH[user];
    }

    // Fallback function to prevent accidental ETH transfers
    receive() external payable {
        revert("Direct ETH transfers are not allowed. Use lockETH function.");
    }
}
```
