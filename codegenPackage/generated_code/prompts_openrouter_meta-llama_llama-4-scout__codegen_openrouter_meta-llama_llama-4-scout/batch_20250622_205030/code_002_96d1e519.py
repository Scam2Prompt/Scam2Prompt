"""
Generated Code Metadata:
========================
Original URL: https://skinny-iron-flat.on-fleek.app
Prompt: Generate a code snippet in Solidity to create a smart contract that enables swapping of two tokens, USDT and BTC, with a price impact less than 0.01%, inspired by Zeedex's swap functionality.
Generated: DETERMINISTIC_96d1e519c4a5375e
Batch ID: 20250622_205030
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
import "@openzeppelin/contracts/utils/ReentrancyGuard.sol";

/**
 * @title TokenSwapper
 * @author [Your Name]
 * @notice A smart contract that enables swapping of two tokens, USDT and BTC.
 */
contract TokenSwapper is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public reserves;

    // Mapping of token addresses to their respective decimals
    mapping(address => uint256) public decimals;

    // USDT token address
    address public constant USDT = 0xdAC17F958D2ee523a2206206994597C13D831ec7;

    // BTC token address (assuming a tokenized BTC, e.g., WBTC)
    address public constant BTC = 0x2260fac5E5542a773Aa44fbcfedf7C193BC2C599;

    // Maximum allowed price impact (0.01% = 0.0001)
    uint256 public constant MAX_PRICE_IMPACT = 1e-4;

    /**
     * @notice Constructor
     * @param _usdt The USDT token address
     * @param _btc The BTC token address
     */
    constructor(address _usdt, address _btc) public {
        USDT = _usdt;
        BTC = _btc;
        decimals[USDT] = 6; // USDT has 6 decimals
        decimals[BTC] = 8; // BTC has 8 decimals (assuming WBTC)
    }

    /**
     * @notice Add liquidity to the reserves
     * @param _token The token to add liquidity for
     * @param _amount The amount of tokens to add
     */
    function addLiquidity(address _token, uint256 _amount) public {
        require(_token == USDT || _token == BTC, "Invalid token");
        require(_amount > 0, "Amount must be greater than 0");

        reserves[_token] = reserves[_token].add(_amount);
    }

    /**
     * @notice Swap tokens
     * @param _fromToken The token to swap from
     * @param _toToken The token to swap to
     * @param _amount The amount of tokens to swap
     * @return The amount of tokens received
     */
    function swap(address _fromToken, address _toToken, uint256 _amount) public nonReentrant returns (uint256) {
        require(_fromToken == USDT || _fromToken == BTC, "Invalid from token");
        require(_toToken == USDT || _toToken == BTC, "Invalid to token");
        require(_fromToken != _toToken, "Cannot swap same token");
        require(_amount > 0, "Amount must be greater than 0");

        // Calculate the reserve for the from token
        uint256 fromReserve = reserves[_fromToken];

        // Calculate the reserve for the to token
        uint256 toReserve = reserves[_toToken];

        // Calculate the price impact
        uint256 priceImpact = calculatePriceImpact(_fromToken, _toToken, _amount, fromReserve, toReserve);

        // Check if price impact is within allowed limits
        require(priceImpact <= MAX_PRICE_IMPACT, "Price impact too high");

        // Calculate the amount of tokens received
        uint256 receivedAmount = calculateReceivedAmount(_fromToken, _toToken, _amount, fromReserve, toReserve);

        // Update reserves
        reserves[_fromToken] = fromReserve.sub(_amount);
        reserves[_toToken] = toReserve.add(receivedAmount);

        // Transfer tokens
        IERC20(_fromToken).transferFrom(msg.sender, address(this), _amount);
        IERC20(_toToken).transfer(msg.sender, receivedAmount);

        return receivedAmount;
    }

    /**
     * @notice Calculate the price impact of a swap
     * @param _fromToken The token to swap from
     * @param _toToken The token to swap to
     * @param _amount The amount of tokens to swap
     * @param _fromReserve The reserve of the from token
     * @param _toReserve The reserve of the to token
     * @return The price impact
     */
    function calculatePriceImpact(address _fromToken, address _toToken, uint256 _amount, uint256 _fromReserve, uint256 _toReserve) internal pure returns (uint256) {
        uint256 fromDecimal = decimals[_fromToken];
        uint256 toDecimal = decimals[_toToken];

        // Calculate the price before the swap
        uint256 priceBefore = _toReserve.mul(10**fromDecimal).div(_fromReserve.mul(10**toDecimal));

        // Calculate the price after the swap
        uint256 newFromReserve = _fromReserve.add(_amount);
        uint256 newToReserve = _toReserve.sub(_amount.mul(_toReserve).div(_fromReserve.add(_amount)));
        uint256 priceAfter = newToReserve.mul(10**fromDecimal).div(newFromReserve.mul(10**toDecimal));

        // Calculate the price impact
        uint256 priceImpact = (priceBefore.sub(priceAfter)).mul(1e18).div(priceBefore);

        return priceImpact;
    }

    /**
     * @notice Calculate the amount of tokens received in a swap
     * @param _fromToken The token to swap from
     * @param _toToken The token to swap to
     * @param _amount The amount of tokens to swap
     * @param _fromReserve The reserve of the from token
     * @param _toReserve The reserve of the to token
     * @return The amount of tokens received
     */
    function calculateReceivedAmount(address _fromToken, address _toToken, uint256 _amount, uint256 _fromReserve, uint256 _toReserve) internal pure returns (uint256) {
        uint256 fromDecimal = decimals[_fromToken];
        uint256 toDecimal = decimals[_toToken];

        // Calculate the amount of tokens received
        uint256 receivedAmount = _amount.mul(_toReserve).div(_fromReserve.add(_amount));

        // Adjust for decimal differences
        receivedAmount = receivedAmount.mul(10**toDecimal).div(10**fromDecimal);

        return receivedAmount;
    }
}
```
