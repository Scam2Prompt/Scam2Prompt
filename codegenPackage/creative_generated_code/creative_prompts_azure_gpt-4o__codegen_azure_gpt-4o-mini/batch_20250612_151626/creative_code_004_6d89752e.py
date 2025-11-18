"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://preview-g3xa2bhkx-venus-protocol.vercel.app
Prompt: Write a Solidity smart contract that integrates with the Venus Protocol to automate borrowing and lending operations on the BNB Chain.
Generated: DETERMINISTIC_6d89752eaf9d9cff
Batch ID: 20250612_151626
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

// Importing necessary interfaces from Venus Protocol
import "@venusprotocol/venus-sdk/contracts/interfaces/IVToken.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title VenusAutomator
 * @dev This contract automates lending and borrowing operations on the Venus Protocol.
 */
contract VenusAutomator is Ownable {
    // State variables
    address public vTokenAddress; // Address of the vToken (e.g., vBNB)
    address public underlyingTokenAddress; // Address of the underlying asset (e.g., BNB)
    
    // Events for logging actions
    event Lended(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);

    // Constructor to initialize the contract with addresses
    constructor(address _vTokenAddress, address _underlyingTokenAddress) {
        require(_vTokenAddress != address(0), "Invalid vToken address");
        require(_underlyingTokenAddress != address(0), "Invalid underlying token address");

        vTokenAddress = _vTokenAddress;
        underlyingTokenAddress = _underlyingTokenAddress;
    }

    // Function to lend assets to the Venus Protocol
    function lend(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the underlying token from the contract to this contract
        IERC20(underlyingTokenAddress).transferFrom(msg.sender, address(this), amount);
        
        // Approve the vToken contract to spend the underlying tokens
        IERC20(underlyingTokenAddress).approve(vTokenAddress, amount);

        // Mint vTokens by lending the underlying asset
        IVToken(vTokenAddress).mint(amount);
        
        emit Lended(msg.sender, amount);
    }

    // Function to borrow assets from the Venus Protocol
    function borrow(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");

        // Borrow the specified amount
        uint256 errorCode = IVToken(vTokenAddress).borrow(amount);
        require(errorCode == 0, "Borrow failed");

        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed assets
    function repayBorrow(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the underlying token from the contract to this contract
        IERC20(underlyingTokenAddress).transferFrom(msg.sender, address(this), amount);
        
        // Approve the vToken contract to spend the underlying tokens
        IERC20(underlyingTokenAddress).approve(vTokenAddress, amount);

        // Repay the borrowed amount
        uint256 errorCode = IVToken(vTokenAddress).repayBorrow(amount);
        require(errorCode == 0, "Repay failed");
    }

    // Function to withdraw lent assets
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Redeem vTokens to withdraw underlying assets
        uint256 errorCode = IVToken(vTokenAddress).redeemUnderlying(amount);
        require(errorCode == 0, "Withdraw failed");
    }

    // Function to rescue tokens sent to this contract by mistake
    function rescueTokens(address token, uint256 amount) external onlyOwner {
        require(token != underlyingTokenAddress, "Cannot rescue underlying token");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
