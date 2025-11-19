"""
Generated Code Metadata:
========================
Original URL: https://yieldeth.org
Prompt: Generate a Solidity contract for WrappedPool functionality that liquifies yieldETH and creates staked ETH liquid tokens, ensuring compatibility with DeFi applications.
Generated: DETERMINISTIC_5b23c037869450b4
Batch ID: 20250612_150644
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// WrappedPool contract for liquifying yieldETH and creating staked ETH liquid tokens
contract WrappedPool is Ownable {
    using SafeERC20 for IERC20;

    // State variables
    IERC20 public yieldETH; // The yield-bearing ETH token
    IERC20 public stakedETH; // The staked ETH liquid token
    uint256 public totalSupply; // Total supply of staked ETH tokens
    mapping(address => uint256) public balanceOf; // User balances

    // Events
    event Liquified(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    // Constructor to initialize the contract with yieldETH and stakedETH addresses
    constructor(IERC20 _yieldETH, IERC20 _stakedETH) {
        yieldETH = _yieldETH;
        stakedETH = _stakedETH;
    }

    // Function to liquify yieldETH and mint stakedETH tokens
    function liquify(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(yieldETH.balanceOf(msg.sender) >= amount, "Insufficient yieldETH balance");

        // Transfer yieldETH from user to this contract
        yieldETH.safeTransferFrom(msg.sender, address(this), amount);

        // Mint stakedETH tokens to the user
        balanceOf[msg.sender] += amount;
        totalSupply += amount;
        stakedETH.safeTransfer(msg.sender, amount);

        emit Liquified(msg.sender, amount);
    }

    // Function to unstake stakedETH and return yieldETH
    function unstake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf[msg.sender] >= amount, "Insufficient stakedETH balance");

        // Burn stakedETH tokens from the user
        balanceOf[msg.sender] -= amount;
        totalSupply -= amount;

        // Transfer yieldETH back to the user
        yieldETH.safeTransfer(msg.sender, amount);

        emit Unstaked(msg.sender, amount);
    }

    // Function to get the total balance of yieldETH held by the contract
    function getYieldETHBalance() external view returns (uint256) {
        return yieldETH.balanceOf(address(this));
    }

    // Function to withdraw any ERC20 tokens accidentally sent to the contract
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        token.safeTransfer(msg.sender, amount);
    }
}
```
