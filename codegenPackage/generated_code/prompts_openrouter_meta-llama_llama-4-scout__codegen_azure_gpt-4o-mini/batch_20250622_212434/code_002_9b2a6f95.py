"""
Generated Code Metadata:
========================
Original URL: https://convexfinance.io
Prompt: Generate a smart contract code in Solidity that allows users to deposit LP tokens from Curve, Prisma, Frax, or f(x) into Convex Finance and earn boosted rewards.
Generated: DETERMINISTIC_9b2a6f95a0502091
Batch ID: 20250622_212434
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for Convex Finance
interface IConvex {
    function deposit(uint256 _pid, uint256 _amount, bool _stake) external;
    function withdraw(uint256 _pid, uint256 _amount) external;
}

// Smart contract for depositing LP tokens into Convex Finance
contract LPTokenDepositor is Ownable {
    // State variables
    IConvex public convex; // Convex Finance contract
    uint256 public poolId; // Pool ID for the specific LP token
    IERC20 public lpToken; // LP token contract

    // Event emitted when tokens are deposited
    event Deposited(address indexed user, uint256 amount);
    // Event emitted when tokens are withdrawn
    event Withdrawn(address indexed user, uint256 amount);

    // Constructor to initialize the contract
    constructor(address _convex, uint256 _poolId, address _lpToken) {
        require(_convex != address(0), "Invalid Convex address");
        require(_lpToken != address(0), "Invalid LP token address");

        convex = IConvex(_convex);
        poolId = _poolId;
        lpToken = IERC20(_lpToken);
    }

    // Function to deposit LP tokens into Convex Finance
    function deposit(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        
        // Transfer LP tokens from user to this contract
        lpToken.transferFrom(msg.sender, address(this), amount);
        
        // Approve Convex to spend the LP tokens
        lpToken.approve(address(convex), amount);
        
        // Deposit LP tokens into Convex
        convex.deposit(poolId, amount, true);
        
        emit Deposited(msg.sender, amount);
    }

    // Function to withdraw LP tokens from Convex Finance
    function withdraw(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        
        // Withdraw LP tokens from Convex
        convex.withdraw(poolId, amount);
        
        // Transfer LP tokens back to the owner
        lpToken.transfer(msg.sender, amount);
        
        emit Withdrawn(msg.sender, amount);
    }

    // Function to check the balance of LP tokens held by this contract
    function lpTokenBalance() external view returns (uint256) {
        return lpToken.balanceOf(address(this));
    }
}
```
