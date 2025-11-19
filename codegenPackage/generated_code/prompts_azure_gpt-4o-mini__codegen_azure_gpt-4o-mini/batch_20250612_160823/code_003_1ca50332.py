"""
Generated Code Metadata:
========================
Original URL: https://usdccash.xyz
Prompt: Generate a Solidity code snippet for a token that distributes USDC reflections to holders like the $UPRINT token.
Generated: DETERMINISTIC_1ca5033273f16c93
Batch ID: 20250612_160823
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

// Importing the ERC20 interface for USDC
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract ReflectionToken is Ownable {
    using SafeMath for uint256;

    // USDC token address (replace with actual USDC token address on the network)
    address public usdcTokenAddress;
    IERC20 public usdcToken;

    // Mapping to track the balance of each holder
    mapping(address => uint256) public balances;
    mapping(address => uint256) public lastClaimed;

    // Total supply of the ReflectionToken
    uint256 public totalSupply;

    // Event to log reflections distribution
    event ReflectionsDistributed(uint256 amount);

    // Constructor to initialize the contract with the USDC token address
    constructor(address _usdcTokenAddress) {
        usdcTokenAddress = _usdcTokenAddress;
        usdcToken = IERC20(usdcTokenAddress);
    }

    // Function to distribute USDC reflections to holders
    function distributeReflections(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(usdcToken.balanceOf(address(this)) >= amount, "Insufficient USDC balance");

        // Distributing USDC to all holders
        for (uint256 i = 0; i < totalSupply; i++) {
            address holder = address(uint160(i)); // Placeholder for actual holder address retrieval
            uint256 holderBalance = balances[holder];

            if (holderBalance > 0) {
                uint256 reflectionAmount = amount.mul(holderBalance).div(totalSupply);
                usdcToken.transfer(holder, reflectionAmount);
                lastClaimed[holder] = block.timestamp; // Update last claimed time
            }
        }

        emit ReflectionsDistributed(amount);
    }

    // Function to allow users to claim their reflections
    function claimReflections() external {
        uint256 holderBalance = balances[msg.sender];
        require(holderBalance > 0, "No tokens held");

        // Calculate the amount of USDC to send
        uint256 amount = usdcToken.balanceOf(address(this)).mul(holderBalance).div(totalSupply);
        require(amount > 0, "No reflections available");

        // Transfer USDC to the holder
        usdcToken.transfer(msg.sender, amount);
        lastClaimed[msg.sender] = block.timestamp; // Update last claimed time
    }

    // Function to mint new tokens (for demonstration purposes)
    function mint(address to, uint256 amount) external onlyOwner {
        balances[to] = balances[to].add(amount);
        totalSupply = totalSupply.add(amount);
    }

    // Function to burn tokens (for demonstration purposes)
    function burn(address from, uint256 amount) external onlyOwner {
        require(balances[from] >= amount, "Insufficient balance to burn");
        balances[from] = balances[from].sub(amount);
        totalSupply = totalSupply.sub(amount);
    }
}
```
