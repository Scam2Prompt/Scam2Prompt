"""
Generated Code Metadata:
========================
Original URL: https://cowonbasenets.pages.dev
Prompt: Create a Solidity function that checks if liquidity for the $COW token has been burned, referencing the unique features of the token.
Generated: DETERMINISTIC_798e9e547762d9b1
Batch ID: 20250612_145619
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

/**
 * @title CowTokenLiquidityChecker
 * @author [Your Name]
 * @notice Checks if liquidity for the $COW token has been burned.
 */
contract CowTokenLiquidityChecker {
    // Mapping of liquidity pool addresses to their respective burned status
    mapping(address => bool) public liquidityPools;

    // Address of the $COW token contract
    address public immutable cowTokenAddress;

    /**
     * @param _cowTokenAddress Address of the $COW token contract
     */
    constructor(address _cowTokenAddress) {
        require(_cowTokenAddress != address(0), "CowTokenLiquidityChecker: Invalid $COW token address");
        cowTokenAddress = _cowTokenAddress;
    }

    /**
     * @notice Checks if liquidity for the $COW token has been burned in a given pool
     * @param _liquidityPoolAddress Address of the liquidity pool
     * @return bool True if liquidity has been burned, false otherwise
     */
    function isLiquidityBurned(address _liquidityPoolAddress) public view returns (bool) {
        // Check if the provided liquidity pool address is valid
        require(_liquidityPoolAddress != address(0), "CowTokenLiquidityChecker: Invalid liquidity pool address");

        // Check if the liquidity pool has been marked as burned
        return liquidityPools[_liquidityPoolAddress];
    }

    /**
     * @notice Marks a liquidity pool as burned
     * @param _liquidityPoolAddress Address of the liquidity pool
     * @param _burned True if the liquidity has been burned, false otherwise
     */
    function setLiquidityBurned(address _liquidityPoolAddress, bool _burned) public {
        // Check if the provided liquidity pool address is valid
        require(_liquidityPoolAddress != address(0), "CowTokenLiquidityChecker: Invalid liquidity pool address");

        // Only the $COW token contract or this contract can update the burned status
        require(msg.sender == cowTokenAddress || msg.sender == address(this), "CowTokenLiquidityChecker: Unauthorized");

        // Update the burned status of the liquidity pool
        liquidityPools[_liquidityPoolAddress] = _burned;
    }

    /**
     * @notice Burns liquidity for the $COW token in a given pool
     * @param _liquidityPoolAddress Address of the liquidity pool
     */
    function burnLiquidity(address _liquidityPoolAddress) public {
        // Check if the provided liquidity pool address is valid
        require(_liquidityPoolAddress != address(0), "CowTokenLiquidityChecker: Invalid liquidity pool address");

        // Only the $COW token contract can burn liquidity
        require(msg.sender == cowTokenAddress, "CowTokenLiquidityChecker: Unauthorized");

        // Mark the liquidity pool as burned
        liquidityPools[_liquidityPoolAddress] = true;

        // Call the liquidity pool's burn function (assuming it's a standard ERC20 pool)
        IERC20(_liquidityPoolAddress).burn(IERC20(_liquidityPoolAddress).balanceOf(address(this)));
    }
}
```
