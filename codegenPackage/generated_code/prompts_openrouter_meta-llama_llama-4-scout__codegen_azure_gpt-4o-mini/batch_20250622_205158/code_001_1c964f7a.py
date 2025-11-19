"""
Generated Code Metadata:
========================
Original URL: https://meversedex.gitbook.io
Prompt: Design a DeFi protocol that incorporates the advantages of DeFi 1.0 and DeFi 2.0, and addresses their shortcomings, using MEVerse DEX as a reference.
Generated: DETERMINISTIC_1c964f7a6f4ab68e
Batch ID: 20250622_205158
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

// Importing necessary OpenZeppelin contracts for security and functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MEVerse DEX DeFi Protocol
contract MEVerseDEX is Ownable {
    using SafeMath for uint256;

    // Struct to hold liquidity pool information
    struct LiquidityPool {
        uint256 totalLiquidity;
        mapping(address => uint256) liquidityProviders;
    }

    // Mapping of token addresses to their respective liquidity pools
    mapping(address => LiquidityPool) public liquidityPools;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed token, address indexed provider, uint256 amount);
    
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed token, address indexed provider, uint256 amount);

    // Function to add liquidity to a specific token pool
    function addLiquidity(address token, uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the liquidity pool
        LiquidityPool storage pool = liquidityPools[token];
        pool.totalLiquidity = pool.totalLiquidity.add(amount);
        pool.liquidityProviders[msg.sender] = pool.liquidityProviders[msg.sender].add(amount);

        emit LiquidityAdded(token, msg.sender, amount);
    }

    // Function to remove liquidity from a specific token pool
    function removeLiquidity(address token, uint256 amount) external {
        LiquidityPool storage pool = liquidityPools[token];
        require(pool.liquidityProviders[msg.sender] >= amount, "Insufficient liquidity");

        // Update the liquidity pool
        pool.totalLiquidity = pool.totalLiquidity.sub(amount);
        pool.liquidityProviders[msg.sender] = pool.liquidityProviders[msg.sender].sub(amount);
        
        require(IERC20(token).transfer(msg.sender, amount), "Transfer failed");

        emit LiquidityRemoved(token, msg.sender, amount);
    }

    // Function to get the total liquidity of a specific token pool
    function getTotalLiquidity(address token) external view returns (uint256) {
        return liquidityPools[token].totalLiquidity;
    }

    // Function to get the liquidity of a specific provider in a token pool
    function getProviderLiquidity(address token, address provider) external view returns (uint256) {
        return liquidityPools[token].liquidityProviders[provider];
    }

    // Function to withdraw contract balance in case of emergency
    function emergencyWithdraw(address token) external onlyOwner {
        uint256 balance = IERC20(token).balanceOf(address(this));
        require(balance > 0, "No balance to withdraw");
        require(IERC20(token).transfer(msg.sender, balance), "Transfer failed");
    }
}
```
