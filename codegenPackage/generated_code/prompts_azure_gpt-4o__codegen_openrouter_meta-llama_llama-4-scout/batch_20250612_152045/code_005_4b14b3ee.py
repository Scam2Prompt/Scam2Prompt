"""
Generated Code Metadata:
========================
Original URL: https://quickwasp.godaddysites.com
Prompt: Develop a Solidity implementation of a fee mechanism for a DEX, where 0.30% of each transaction is added to the reserves and later distributed to liquidity providers when they withdraw their shares.
Generated: DETERMINISTIC_4b14b3ee039fbe97
Batch ID: 20250612_152045
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/math/SafeMath.sol";

/**
 * @title Fee Mechanism for DEX
 * @author [Your Name]
 * @notice This contract implements a fee mechanism for a DEX, where 0.30% of each transaction is added to the reserves and later distributed to liquidity providers when they withdraw their shares.
 */
contract DexFeeMechanism {
    using SafeMath for uint256;

    // Mapping of liquidity providers and their shares
    mapping (address => uint256) public liquidityProviders;

    // Total reserves
    uint256 public totalReserves;

    // Total liquidity
    uint256 public totalLiquidity;

    // Fee percentage (0.30%)
    uint256 public constant FEE_PERCENTAGE = 30;

    // Fee denominator
    uint256 public constant FEE_DENOMINATOR = 10000;

    // ERC20 token
    IERC20 public token;

    /**
     * @notice Constructor
     * @param _token ERC20 token address
     */
    constructor(address _token) public {
        require(_token != address(0), "Token address cannot be zero");
        token = IERC20(_token);
    }

    /**
     * @notice Add liquidity
     * @param _amount Amount of tokens to add
     */
    function addLiquidity(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than zero");
        require(token.transferFrom(msg.sender, address(this), _amount), "Token transfer failed");

        uint256 liquidity = _amount;
        if (totalLiquidity > 0) {
            liquidity = _amount.mul(totalLiquidity).div(totalReserves);
        }

        liquidityProviders[msg.sender] = liquidityProviders[msg.sender].add(liquidity);
        totalLiquidity = totalLiquidity.add(liquidity);
        totalReserves = totalReserves.add(_amount);
    }

    /**
     * @notice Remove liquidity
     * @param _amount Amount of liquidity to remove
     */
    function removeLiquidity(uint256 _amount) public {
        require(_amount > 0, "Amount must be greater than zero");
        require(liquidityProviders[msg.sender] >= _amount, "Insufficient liquidity");

        uint256 reserves = _amount.mul(totalReserves).div(totalLiquidity);
        uint256 fee = reserves.mul(FEE_PERCENTAGE).div(FEE_DENOMINATOR);
        uint256 amount = reserves.sub(fee);

        liquidityProviders[msg.sender] = liquidityProviders[msg.sender].sub(_amount);
        totalLiquidity = totalLiquidity.sub(_amount);
        totalReserves = totalReserves.sub(reserves);

        require(token.transfer(msg.sender, amount), "Token transfer failed");
        if (fee > 0) {
            totalReserves = totalReserves.add(fee);
        }
    }

    /**
     * @notice Distribute reserves to liquidity providers
     */
    function distributeReserves() public {
        uint256 reserves = totalReserves;
        totalReserves = 0;

        for (address provider in liquidityProviders) {
            uint256 share = liquidityProviders[provider].mul(reserves).div(totalLiquidity);
            require(token.transfer(provider, share), "Token transfer failed");
        }
    }
}
```
