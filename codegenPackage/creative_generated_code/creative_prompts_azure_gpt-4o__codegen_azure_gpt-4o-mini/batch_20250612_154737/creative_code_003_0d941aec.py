"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://venus-page.vercel.app
Prompt: Create a smart contract in Solidity that integrates with Venus Protocol to automate lending and borrowing operations for a specific BEP-20 asset.
Generated: DETERMINISTIC_0d941aec74a2174b
Batch ID: 20250612_154737
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

// Importing required interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IVenus {
    function mint(address asset, uint amount) external returns (uint);
    function redeem(address asset, uint amount) external returns (uint);
    function borrow(address asset, uint amount) external returns (uint);
    function repayBorrow(address asset, uint amount) external returns (uint);
}

contract VenusLending is Ownable {
    IVenus public venus;

    // Event declarations for logging
    event Minted(address indexed asset, uint amount);
    event Redeemed(address indexed asset, uint amount);
    event Borrowed(address indexed asset, uint amount);
    event Repaid(address indexed asset, uint amount);

    // Constructor to set the Venus Protocol contract address
    constructor(address _venus) {
        require(_venus != address(0), "Invalid Venus address");
        venus = IVenus(_venus);
    }

    // Function to mint a specific BEP-20 asset
    function mint(address asset, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        require(IERC20(asset).approve(address(venus), amount), "Approval failed");

        uint result = venus.mint(asset, amount);
        require(result == 0, "Minting failed");

        emit Minted(asset, amount);
    }

    // Function to redeem a specific BEP-20 asset
    function redeem(address asset, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        uint result = venus.redeem(asset, amount);
        require(result == 0, "Redeeming failed");

        emit Redeemed(asset, amount);
    }

    // Function to borrow a specific BEP-20 asset
    function borrow(address asset, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        uint result = venus.borrow(asset, amount);
        require(result == 0, "Borrowing failed");

        emit Borrowed(asset, amount);
    }

    // Function to repay a borrowed specific BEP-20 asset
    function repayBorrow(address asset, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        require(IERC20(asset).approve(address(venus), amount), "Approval failed");

        uint result = venus.repayBorrow(asset, amount);
        require(result == 0, "Repaying failed");

        emit Repaid(asset, amount);
    }

    // Function to withdraw specific BEP-20 assets from the contract
    function withdraw(address asset, uint amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(asset).transfer(msg.sender, amount);
    }
}
```
