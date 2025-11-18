"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mogcoins-xyz.pages.dev
Prompt: Generate Solidity code for interacting with the Mog Coin ($MOG) ERC-20 token contract, including functions to check balances, transfer tokens, and approve spending.
Generated: DETERMINISTIC_e4197a157bf40e38
Batch ID: 20250612_153526
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Contract to interact with the Mog Coin ($MOG) ERC-20 token
contract MogCoinInteraction is Ownable {
    // Address of the Mog Coin ERC-20 token contract
    address public mogCoinAddress;

    // Event emitted when tokens are transferred
    event TokensTransferred(address indexed from, address indexed to, uint256 amount);

    // Event emitted when approval is given for spending
    event ApprovalGiven(address indexed owner, address indexed spender, uint256 amount);

    // Constructor sets the Mog Coin contract address
    constructor(address _mogCoinAddress) {
        require(_mogCoinAddress != address(0), "Invalid token address");
        mogCoinAddress = _mogCoinAddress;
    }

    // Function to check the balance of a specific address
    function checkBalance(address _owner) external view returns (uint256) {
        require(_owner != address(0), "Invalid address");
        return IERC20(mogCoinAddress).balanceOf(_owner);
    }

    // Function to transfer tokens to another address
    function transferTokens(address _to, uint256 _amount) external {
        require(_to != address(0), "Invalid recipient address");
        require(_amount > 0, "Transfer amount must be greater than zero");
        
        // Call the transfer function on the Mog Coin contract
        bool success = IERC20(mogCoinAddress).transferFrom(msg.sender, _to, _amount);
        require(success, "Transfer failed");

        emit TokensTransferred(msg.sender, _to, _amount);
    }

    // Function to approve token spending by a spender
    function approveSpending(address _spender, uint256 _amount) external {
        require(_spender != address(0), "Invalid spender address");
        require(_amount > 0, "Approval amount must be greater than zero");

        // Call the approve function on the Mog Coin contract
        bool success = IERC20(mogCoinAddress).approve(_spender, _amount);
        require(success, "Approval failed");

        emit ApprovalGiven(msg.sender, _spender, _amount);
    }
}
```
