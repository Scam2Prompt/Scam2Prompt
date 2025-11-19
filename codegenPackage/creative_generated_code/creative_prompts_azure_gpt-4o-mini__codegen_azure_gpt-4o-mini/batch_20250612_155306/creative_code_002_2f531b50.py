"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://axondao.gitbook.io
Prompt: What are the steps to bridge AXGT between Ethereum and Arbitrum using smart contracts?
Generated: DETERMINISTIC_2f531b503f4b43df
Batch ID: 20250612_155306
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

// Import interfaces for ERC20 token standard and Ownable for access control
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Bridge contract to facilitate token transfer between Ethereum and Arbitrum
contract AXGTBridge is Ownable {
    // Events to emit on successful deposit and withdrawal
    event Deposited(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Token to be bridged
    IERC20 public axgtToken;

    // Mapping to track user balances
    mapping(address => uint256) public balances;

    // Constructor to initialize the token address
    constructor(address _axgtToken) {
        require(_axgtToken != address(0), "Invalid token address");
        axgtToken = IERC20(_axgtToken);
    }

    // Deposit AXGT tokens to the bridge
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer AXGT tokens from the user to the bridge contract
        axgtToken.transferFrom(msg.sender, address(this), amount);

        // Update the user's balance
        balances[msg.sender] += amount;

        // Emit deposit event
        emit Deposited(msg.sender, amount);
    }

    // Withdraw AXGT tokens from the bridge
    function withdraw(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        // Update the user's balance
        balances[msg.sender] -= amount;

        // Transfer AXGT tokens back to the user
        axgtToken.transfer(msg.sender, amount);

        // Emit withdrawal event
        emit Withdrawn(msg.sender, amount);
    }

    // Allow the owner to withdraw tokens from the bridge contract
    function ownerWithdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(axgtToken.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        axgtToken.transfer(owner(), amount);
    }
    
    // Function to check contract's AXGT balance (for owner)
    function contractBalance() external view onlyOwner returns (uint256) {
        return axgtToken.balanceOf(address(this));
    }
}
```
