"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeunchained-dashboard.pages.dev
Prompt: Write a Solidity contract to implement liquidity pool functionality for $PEPU tokens, ensuring compatibility with decentralized exchanges as outlined in Pepe Unchained tokenomics.
Generated: DETERMINISTIC_45694d9d4885f956
Batch ID: 20250612_153447
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// A contract to implement a liquidity pool for $PEPU tokens.
contract PepuLiquidityPool is Ownable {
    using SafeMath for uint256;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amountPEPU, uint256 amountETH);
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed provider, uint256 amountPEPU, uint256 amountETH);

    // Address of the $PEPU token contract
    IERC20 public pepuToken;

    // Mapping to track liquidity providers and their balances
    mapping(address => uint256) public liquidityBalances;

    // Constructor to initialize the contract with the $PEPU token address
    constructor(address _pepuTokenAddress) {
        require(_pepuTokenAddress != address(0), "Zero address provided");
        pepuToken = IERC20(_pepuTokenAddress);
    }

    // Function to add liquidity to the pool
    function addLiquidity(uint256 _amountPEPU) external payable {
        require(_amountPEPU > 0, "Amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Transfer $PEPU tokens from liquidity provider to this contract
        require(pepuToken.transferFrom(msg.sender, address(this), _amountPEPU), "Transfer failed");

        // Update the liquidity balance of the provider
        liquidityBalances[msg.sender] = liquidityBalances[msg.sender].add(_amountPEPU);

        // Emit the liquidity added event
        emit LiquidityAdded(msg.sender, _amountPEPU, msg.value);
    }

    // Function to remove liquidity from the pool
    function removeLiquidity(uint256 _amountPEPU) external {
        require(_amountPEPU > 0, "Amount must be greater than zero");
        require(liquidityBalances[msg.sender] >= _amountPEPU, "Insufficient liquidity balance");

        // Calculate the corresponding ETH amount to transfer back
        uint256 ethAmount = address(this).balance.mul(_amountPEPU).div(totalLiquidity());

        // Update the liquidity balance of the provider
        liquidityBalances[msg.sender] = liquidityBalances[msg.sender].sub(_amountPEPU);

        // Transfer $PEPU tokens back to the provider
        require(pepuToken.transfer(msg.sender, _amountPEPU), "Transfer failed");

        // Transfer ETH back to the provider
        payable(msg.sender).transfer(ethAmount);

        // Emit the liquidity removed event
        emit LiquidityRemoved(msg.sender, _amountPEPU, ethAmount);
    }

    // Function to view total liquidity in the pool
    function totalLiquidity() public view returns (uint256) {
        return pepuToken.balanceOf(address(this));
    }

    // Function to withdraw any ERC20 tokens sent to the contract by mistake
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Zero address provided");
        IERC20 token = IERC20(_tokenAddress);
        require(token.transfer(msg.sender, _amount), "Token transfer failed");
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdrawETH(uint256 _amount) external onlyOwner {
        require(address(this).balance >= _amount, "Insufficient ETH balance");
        payable(msg.sender).transfer(_amount);
    }
    
    // Fallback function to receive ETH
    receive() external payable {}
}
```
