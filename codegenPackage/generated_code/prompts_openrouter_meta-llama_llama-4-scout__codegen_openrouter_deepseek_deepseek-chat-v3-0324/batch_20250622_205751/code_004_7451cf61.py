"""
Generated Code Metadata:
========================
Original URL: https://kjbsdakjb.pages.dev
Prompt: Create a simple smart contract using Solidity that interacts with ZeroLend's protocol to borrow or lend assets on zkSync.
Generated: DETERMINISTIC_7451cf61c8ce9923
Batch ID: 20250622_205751
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
import "@openzeppelin/contracts/utils/Address.sol";

interface IZeroLend {
    function deposit(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
}

contract ZeroLendInteraction is Ownable {
    using Address for address;

    IZeroLend public zeroLend;
    
    event Deposited(address indexed asset, uint256 amount);
    event Withdrawn(address indexed asset, uint256 amount);
    event Borrowed(address indexed asset, uint256 amount);
    event Repaid(address indexed asset, uint256 amount);

    constructor(address _zeroLendAddress) {
        require(_zeroLendAddress != address(0), "Invalid ZeroLend address");
        zeroLend = IZeroLend(_zeroLendAddress);
    }

    function setZeroLendAddress(address _zeroLendAddress) external onlyOwner {
        require(_zeroLendAddress != address(0), "Invalid ZeroLend address");
        zeroLend = IZeroLend(_zeroLendAddress);
    }

    function deposit(address asset, uint256 amount) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(asset);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        token.transferFrom(msg.sender, address(this), amount);
        token.approve(address(zeroLend), amount);
        zeroLend.deposit(asset, amount);

        emit Deposited(asset, amount);
    }

    function withdraw(address asset, uint256 amount) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");

        zeroLend.withdraw(asset, amount);
        
        IERC20 token = IERC20(asset);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Insufficient contract balance");
        
        token.transfer(msg.sender, amount);

        emit Withdrawn(asset, amount);
    }

    function borrow(address asset, uint256 amount) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");

        zeroLend.borrow(asset, amount);
        
        IERC20 token = IERC20(asset);
        uint256 balance = token.balanceOf(address(this));
        require(balance >= amount, "Borrow failed");
        
        token.transfer(msg.sender, amount);

        emit Borrowed(asset, amount);
    }

    function repay(address asset, uint256 amount) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        require(amount > 0, "Amount must be greater than 0");

        IERC20 token = IERC20(asset);
        require(token.balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        token.transferFrom(msg.sender, address(this), amount);
        token.approve(address(zeroLend), amount);
        zeroLend.repay(asset, amount);

        emit Repaid(asset, amount);
    }

    function emergencyWithdraw(address asset) external onlyOwner {
        require(asset != address(0), "Invalid asset address");
        
        IERC20 token = IERC20(asset);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        
        token.transfer(msg.sender, balance);
    }
}
```
