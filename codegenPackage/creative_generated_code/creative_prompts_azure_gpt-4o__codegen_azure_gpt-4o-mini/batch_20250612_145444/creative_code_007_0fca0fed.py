"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://safe-app.morpho.dev
Prompt: Develop a smart contract that interacts with Morpho's V2 platform to automate lending and borrowing processes.
Generated: DETERMINISTIC_0fca0fed7941976b
Batch ID: 20250612_145444
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

// Import the Morpho's V2 interface
import "@morpho.xyz/morpho-core/contracts/interfaces/IMorpho.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract to automate lending and borrowing on Morpho's V2 platform
contract MorphoLending is Ownable {
    // State variables
    IMorpho public morpho;                  // Morpho's core contract
    IERC20 public collateralToken;           // Token used for collateral
    IERC20 public debtToken;                 // Token borrowed

    // Events
    event Lent(address indexed user, uint256 amount);
    event Borrowed(address indexed user, uint256 amount);
    event Repaid(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to set Morpho's core contract and the tokens
    constructor(address _morpho, address _collateralToken, address _debtToken) {
        morpho = IMorpho(_morpho);
        collateralToken = IERC20(_collateralToken);
        debtToken = IERC20(_debtToken);
    }

    // Function to lend collateral
    function lend(uint256 amount) external {
        require(amount > 0, "Amount should be greater than zero");

        // Transfer collateral from user to contract
        collateralToken.transferFrom(msg.sender, address(this), amount);

        // Approve Morpho to use the collateral
        collateralToken.approve(address(morpho), amount);

        // Lend the collateral to Morpho
        morpho.supply(address(collateralToken), amount);
        
        emit Lent(msg.sender, amount);
    }

    // Function to borrow assets
    function borrow(uint256 amount) external {
        require(amount > 0, "Amount should be greater than zero");

        // Borrow the specified amount of the debt token
        morpho.borrow(address(debtToken), amount);
        
        // Transfer the borrowed tokens to the user
        debtToken.transfer(msg.sender, amount);
        
        emit Borrowed(msg.sender, amount);
    }

    // Function to repay borrowed assets
    function repay(uint256 amount) external {
        require(amount > 0, "Amount should be greater than zero");

        // Transfer the repayment amount from the user to the contract
        debtToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve Morpho to use the repayment amount
        debtToken.approve(address(morpho), amount);

        // Repay the borrowed amount to Morpho
        morpho.repay(address(debtToken), amount);
        
        emit Repaid(msg.sender, amount);
    }

    // Function to withdraw collateral after repayment
    function withdrawCollateral(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount should be greater than zero");

        // Withdraw collateral from Morpho
        morpho.withdraw(address(collateralToken), amount);
        
        // Transfer the collateral back to the owner
        collateralToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of collateral tokens
    function collateralBalance() external view returns (uint256) {
        return collateralToken.balanceOf(address(this));
    }

    // Function to check the balance of debt tokens
    function debtBalance() external view returns (uint256) {
        return debtToken.balanceOf(address(this));
    }
}
```
