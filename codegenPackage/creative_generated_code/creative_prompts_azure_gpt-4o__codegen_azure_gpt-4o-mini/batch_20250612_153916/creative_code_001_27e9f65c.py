"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://spark.fishersclubs.com
Prompt: Generate Solidity code for a smart contract that integrates SparkLend to supply and borrow assets like ETH, wstETH, and cbBTC, while adhering to Spark's audited security standards.
Generated: DETERMINISTIC_27e9f65c0c621492
Batch ID: 20250612_153916
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

// Import necessary interfaces from OpenZeppelin and SparkLend
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the SparkLend protocol
interface ISparkLend {
    function supply(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repay(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

// Smart contract to interact with SparkLend
contract SparkLendIntegration is ReentrancyGuard, Ownable {
    // Instance of SparkLend protocol
    ISparkLend public sparkLend;

    // Events to log actions
    event Supplied(address indexed asset, uint256 amount);
    event Borrowed(address indexed asset, uint256 amount);
    event Repaid(address indexed asset, uint256 amount);
    event Withdrawn(address indexed asset, uint256 amount);

    // Constructor to set the SparkLend address
    constructor(address _sparkLendAddress) {
        require(_sparkLendAddress != address(0), "Invalid address for SparkLend");
        sparkLend = ISparkLend(_sparkLendAddress);
    }

    // Function to supply assets to SparkLend
    function supplyAsset(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(sparkLend), amount);
        
        sparkLend.supply(asset, amount);
        
        emit Supplied(asset, amount);
    }

    // Function to borrow assets from SparkLend
    function borrowAsset(address asset, uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        sparkLend.borrow(asset, amount);
        
        emit Borrowed(asset, amount);
    }

    // Function to repay borrowed assets
    function repayAsset(address asset, uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        IERC20(asset).approve(address(sparkLend), amount);
        
        sparkLend.repay(asset, amount);
        
        emit Repaid(asset, amount);
    }

    // Function to withdraw supplied assets
    function withdrawAsset(address asset, uint256 amount) external nonReentrant onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        sparkLend.withdraw(asset, amount);
        IERC20(asset).transfer(msg.sender, amount);
        
        emit Withdrawn(asset, amount);
    }

    // Function to set new SparkLend address (only for the owner)
    function setSparkLendAddress(address _sparkLendAddress) external onlyOwner {
        require(_sparkLendAddress != address(0), "Invalid address for SparkLend");
        sparkLend = ISparkLend(_sparkLendAddress);
    }
}
```
