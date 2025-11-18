"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://app-basemafia-com.pages.dev
Prompt: Write a Solidity contract for a liquidity provision functionality that aligns with the Base Mafia roadmap for Phase 1 development.
Generated: DETERMINISTIC_893ed6e11cff2a6d
Batch ID: 20250612_145924
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

// Import necessary OpenZeppelin contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title LiquidityProvision
 * @dev A contract to provide liquidity functionality
 * aligned with the Base Mafia roadmap for Phase 1 development.
 */
contract LiquidityProvision is Ownable {
    using SafeERC20 for IERC20;

    // Event emitted when liquidity is added
    event LiquidityAdded(address indexed provider, uint256 amountA, uint256 amountB);
    
    // Event emitted when liquidity is removed
    event LiquidityRemoved(address indexed provider, uint256 amountA, uint256 amountB);

    // Liquidity Pool Tokens
    IERC20 public tokenA;
    IERC20 public tokenB;

    // Structure to hold provider liquidity details
    struct Liquidity {
        uint256 amountA;
        uint256 amountB;
    }

    // Mapping to track liquidity provided by each address
    mapping(address => Liquidity) public liquidityProviders;

    /**
     * @dev Constructor to set the tokens for liquidity provision.
     * @param _tokenA Address of the first token (ERC20)
     * @param _tokenB Address of the second token (ERC20)
     */
    constructor(address _tokenA, address _tokenB) {
        require(_tokenA != address(0), "TokenA address cannot be zero");
        require(_tokenB != address(0), "TokenB address cannot be zero");

        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
    }

    /**
     * @dev Allows users to add liquidity to the pool.
     * @param _amountA Amount of token A to provide
     * @param _amountB Amount of token B to provide
     */
    function addLiquidity(uint256 _amountA, uint256 _amountB) external {
        require(_amountA > 0 && _amountB > 0, "Amounts must be greater than zero");

        // Transfer tokens from the user to the contract
        tokenA.safeTransferFrom(msg.sender, address(this), _amountA);
        tokenB.safeTransferFrom(msg.sender, address(this), _amountB);

        // Update liquidity provider's balance
        liquidityProviders[msg.sender].amountA += _amountA;
        liquidityProviders[msg.sender].amountB += _amountB;

        emit LiquidityAdded(msg.sender, _amountA, _amountB);
    }

    /**
     * @dev Allows users to remove liquidity from the pool.
     * @param _amountA Amount of token A to withdraw
     * @param _amountB Amount of token B to withdraw
     */
    function removeLiquidity(uint256 _amountA, uint256 _amountB) external {
        require(_amountA > 0 && _amountB > 0, "Amounts must be greater than zero");
        require(liquidityProviders[msg.sender].amountA >= _amountA, "Insufficient token A liquidity");
        require(liquidityProviders[msg.sender].amountB >= _amountB, "Insufficient token B liquidity");

        // Update liquidity provider's balance
        liquidityProviders[msg.sender].amountA -= _amountA;
        liquidityProviders[msg.sender].amountB -= _amountB;

        // Transfer tokens back to the user
        tokenA.safeTransfer(msg.sender, _amountA);
        tokenB.safeTransfer(msg.sender, _amountB);

        emit LiquidityRemoved(msg.sender, _amountA, _amountB);
    }

    /**
     * @dev Function to retrieve the liquidity details for a provider.
     * @param _provider Address of the liquidity provider
     * @return amountA Amount of token A provided
     * @return amountB Amount of token B provided
     */
    function getLiquidityDetails(address _provider) external view returns (uint256 amountA, uint256 amountB) {
        return (liquidityProviders[_provider].amountA, liquidityProviders[_provider].amountB);
    }
}
```
