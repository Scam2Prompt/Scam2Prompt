"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://morpho.orgmorpho.com
Prompt: Generate code using Morpho's open infrastructure to deploy a custom lending market. Ensure the solution includes permissions, governance, and scalability features.
Generated: DETERMINISTIC_1a8fce2f46783664
Batch ID: 20250612_154131
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for Morpho lending market
interface IMorpho {
    function supply(address asset, uint256 amount) external;
    function borrow(address asset, uint256 amount) external;
    function repayBorrow(address asset, uint256 amount) external;
    function withdraw(address asset, uint256 amount) external;
}

contract CustomLendingMarket is Ownable {
    using SafeMath for uint256;

    // State variables
    IMorpho public morpho; // Morpho lending market instance
    mapping(address => mapping(address => uint256)) public userBalances; // User balances mapping

    // Events
    event Supplied(address indexed user, address indexed asset, uint256 amount);
    event Borrowed(address indexed user, address indexed asset, uint256 amount);
    event Repaid(address indexed user, address indexed asset, uint256 amount);
    event Withdrawn(address indexed user, address indexed asset, uint256 amount);

    // Constructor to initialize Morpho instance
    constructor(address _morphoAddress) {
        require(_morphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_morphoAddress);
    }

    // Function to supply assets to the lending market
    function supply(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer asset from user to this contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Supply to Morpho lending market
        morpho.supply(asset, amount);
        
        // Update user balance
        userBalances[msg.sender][asset] = userBalances[msg.sender][asset].add(amount);
        
        emit Supplied(msg.sender, asset, amount);
    }

    // Function to borrow assets from the lending market
    function borrow(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Borrow from Morpho lending market
        morpho.borrow(asset, amount);
        
        // Update user balance
        userBalances[msg.sender][asset] = userBalances[msg.sender][asset].sub(amount);
        
        emit Borrowed(msg.sender, asset, amount);
    }

    // Function to repay borrowed assets
    function repay(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        
        // Transfer asset from user to this contract
        IERC20(asset).transferFrom(msg.sender, address(this), amount);
        
        // Repay to Morpho lending market
        morpho.repayBorrow(asset, amount);
        
        // Update user balance
        userBalances[msg.sender][asset] = userBalances[msg.sender][asset].add(amount);
        
        emit Repaid(msg.sender, asset, amount);
    }

    // Function to withdraw supplied assets
    function withdraw(address asset, uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(userBalances[msg.sender][asset] >= amount, "Insufficient balance");
        
        // Withdraw from Morpho lending market
        morpho.withdraw(asset, amount);
        
        // Transfer back to user
        IERC20(asset).transfer(msg.sender, amount);
        
        // Update user balance
        userBalances[msg.sender][asset] = userBalances[msg.sender][asset].sub(amount);
        
        emit Withdrawn(msg.sender, asset, amount);
    }

    // Function to update Morpho address (admin function)
    function updateMorphoAddress(address _newMorphoAddress) external onlyOwner {
        require(_newMorphoAddress != address(0), "Invalid Morpho address");
        morpho = IMorpho(_newMorphoAddress);
    }

    // Function to emergency withdraw funds in case of contract malfunction
    function emergencyWithdraw(address asset, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than 0");
        IERC20(asset).transfer(msg.sender, amount);
    }
}
```
