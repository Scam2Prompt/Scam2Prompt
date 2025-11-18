"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.zkfinance.org
Prompt: Write a smart contract for supplying assets to zkFinance to earn yield and use them as collateral, ensuring compatibility with zkSync's zero-knowledge technology.
Generated: DETERMINISTIC_32bf81dc19185bbb
Batch ID: 20250612_153547
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

// Interface for the zkFinance protocol
interface IzkFinance {
    function supplyAsset(address asset, uint256 amount) external;
    function withdrawAsset(address asset, uint256 amount) external;
    function getYield(address asset) external view returns (uint256);
}

contract ZkFinanceYieldCollateral is Ownable, ReentrancyGuard {
    // State variables
    IzkFinance public zkFinance; // Instance of the zkFinance protocol
    mapping(address => uint256) public collateral; // User collateral mapping

    // Events for logging actions
    event AssetSupplied(address indexed user, address indexed asset, uint256 amount);
    event AssetWithdrawn(address indexed user, address indexed asset, uint256 amount);
    event YieldClaimed(address indexed user, address indexed asset, uint256 yieldAmount);

    // Constructor to set the zkFinance contract address
    constructor(address _zkFinanceAddress) {
        require(_zkFinanceAddress != address(0), "Invalid zkFinance address");
        zkFinance = IzkFinance(_zkFinanceAddress);
    }

    // Function to supply assets to zkFinance for earning yield
    function supplyAsset(address asset, uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(asset).balanceOf(msg.sender) >= amount, "Insufficient balance");

        // Transfer asset from user to contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);

        // Approve zkFinance to spend the asset
        IERC20(asset).approve(address(zkFinance), amount);

        // Supply the asset to zkFinance
        zkFinance.supplyAsset(asset, amount);

        // Update collateral balance
        collateral[msg.sender] += amount;

        emit AssetSupplied(msg.sender, asset, amount);
    }

    // Function to withdraw assets from zkFinance
    function withdrawAsset(address asset, uint256 amount) external nonReentrant {
        require(collateral[msg.sender] >= amount, "Insufficient collateral");

        // Withdraw asset from zkFinance
        zkFinance.withdrawAsset(asset, amount);

        // Transfer asset back to the user
        IERC20(asset).transfer(msg.sender, amount);
        
        // Update collateral balance
        collateral[msg.sender] -= amount;

        emit AssetWithdrawn(msg.sender, asset, amount);
    }

    // Function to claim yield earned on the supplied asset
    function claimYield(address asset) external nonReentrant {
        uint256 yieldAmount = zkFinance.getYield(asset);
        require(yieldAmount > 0, "No yield available to claim");

        // Transfer yield to the user
        IERC20(asset).transfer(msg.sender, yieldAmount);

        emit YieldClaimed(msg.sender, asset, yieldAmount);
    }
}
```
