"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://7-brett-com.pages.dev
Prompt: Develop a Solidity function to distribute token allocations (85% LP, 10% treasury, 5% CEX wallet) upon deployment, inspired by the Brett token.
Generated: DETERMINISTIC_1f9c232be9c50b43
Batch ID: 20250612_153517
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

// Import ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title BrettToken
 * @dev A simple ERC20 Token with allocations for liquidity pool (LP), treasury, and CEX wallet.
 */
contract BrettToken is ERC20, Ownable {
    // Define allocation percentages
    uint256 public constant LP_ALLOCATION = 85;
    uint256 public constant TREASURY_ALLOCATION = 10;
    uint256 public constant CEX_WALLET_ALLOCATION = 5;

    // Define addresses for allocations
    address public liquidityPool;
    address public treasury;
    address public cexWallet;

    // Total supply of tokens
    uint256 public totalSupplyTokens;

    // Event to log token distribution
    event TokenDistributed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor that sets the name and symbol of the token,
     * distributes the tokens according to the specified allocation.
     * @param _liquidityPool Address for liquidity pool
     * @param _treasury Address for treasury
     * @param _cexWallet Address for centralized exchange wallet
     * @param _totalSupply Total supply of the token
     */
    constructor(address _liquidityPool, address _treasury, address _cexWallet, uint256 _totalSupply) 
        ERC20("BrettToken", "BRETT") 
    {
        require(_liquidityPool != address(0), "Invalid liquidity pool address");
        require(_treasury != address(0), "Invalid treasury address");
        require(_cexWallet != address(0), "Invalid CEX wallet address");
        
        liquidityPool = _liquidityPool;
        treasury = _treasury;
        cexWallet = _cexWallet;
        totalSupplyTokens = _totalSupply;

        // Mint total supply tokens
        _mint(address(this), totalSupplyTokens);
        
        // Calculate allocations
        uint256 lpTokens = (totalSupplyTokens * LP_ALLOCATION) / 100;
        uint256 treasuryTokens = (totalSupplyTokens * TREASURY_ALLOCATION) / 100;
        uint256 cexTokens = (totalSupplyTokens * CEX_WALLET_ALLOCATION) / 100;

        // Distribute tokens
        _distributeTokens(liquidityPool, lpTokens);
        _distributeTokens(treasury, treasuryTokens);
        _distributeTokens(cexWallet, cexTokens);
    }

    /**
     * @dev Internal function to distribute tokens.
     * @param recipient Address of the recipient
     * @param amount Amount of tokens to distribute
     */
    function _distributeTokens(address recipient, uint256 amount) internal {
        require(recipient != address(0), "Recipient address cannot be the zero address");
        require(amount > 0, "Amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient balance for distribution");

        // Transfer tokens to the recipient
        _transfer(address(this), recipient, amount);
        emit TokenDistributed(recipient, amount);
    }

    /**
     * @dev Allow the owner to withdraw any tokens sent to the contract by mistake.
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(owner(), amount);
    }
}
```
