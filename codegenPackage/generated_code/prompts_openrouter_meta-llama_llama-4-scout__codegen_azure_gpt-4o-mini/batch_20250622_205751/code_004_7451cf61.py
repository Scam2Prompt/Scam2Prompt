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

// Importing the necessary interfaces from the ZeroLend protocol
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the ZeroLend protocol
interface IZeroLend {
    function lend(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

// Smart contract for interacting with ZeroLend's protocol
contract ZeroLendManager is Ownable {
    IZeroLend public zeroLend;

    // Event declarations for logging actions
    event Lend(address indexed asset, uint256 amount);
    event Borrow(address indexed asset, uint256 amount);
    event Repay(address indexed asset, uint256 amount);
    event Withdraw(address indexed asset, uint256 amount);

    // Constructor to set the ZeroLend protocol address
    constructor(address _zeroLendAddress) {
        require(_zeroLendAddress != address(0), "Invalid ZeroLend address");
        zeroLend = IZeroLend(_zeroLendAddress);
    }

    // Function to lend assets to ZeroLend
    function lendAsset(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the asset from the owner to this contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Approve the ZeroLend contract to spend the asset
        IERC20(asset).approve(address(zeroLend), amount);
        
        // Lend the asset to ZeroLend
        zeroLend.lend(asset, amount);
        
        emit Lend(asset, amount);
    }

    // Function to borrow assets from ZeroLend
    function borrowAsset(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Borrow the asset from ZeroLend
        zeroLend.borrow(asset, amount);
        
        emit Borrow(asset, amount);
    }

    // Function to repay borrowed assets to ZeroLend
    function repayAsset(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer the asset from the owner to this contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Approve the ZeroLend contract to spend the asset
        IERC20(asset).approve(address(zeroLend), amount);
        
        // Repay the borrowed asset to ZeroLend
        zeroLend.repay(asset, amount);
        
        emit Repay(asset, amount);
    }

    // Function to withdraw lent assets from ZeroLend
    function withdrawAsset(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw the asset from ZeroLend
        zeroLend.withdraw(asset, amount);
        
        // Transfer the asset back to the owner
        IERC20(asset).transfer(msg.sender, amount);
        
        emit Withdraw(asset, amount);
    }
}
```
