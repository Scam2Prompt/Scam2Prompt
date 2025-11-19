"""
Generated Code Metadata:
========================
Original URL: https://futureswap.pages.dev
Prompt: Develop a simple smart contract in Solidity to facilitate low-slippage stablecoin swaps on a blockchain platform like Ethereum, inspired by the Future Swap use case.
Generated: DETERMINISTIC_79b6d024e79bf744
Batch ID: 20250622_210655
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
 * @title StablecoinSwapper
 * @author [Your Name]
 * @notice A simple smart contract to facilitate low-slippage stablecoin swaps.
 */
contract StablecoinSwapper {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public reserves;

    // Mapping of token addresses to their respective token balances in the contract
    mapping(address => uint256) public tokenBalances;

    // List of supported tokens
    address[] public supportedTokens;

    // Fee for swaps (in bps)
    uint256 public fee;

    /**
     * @notice Event emitted when a swap occurs
     * @param fromToken Address of the token being swapped from
     * @param toToken Address of the token being swapped to
     * @param amount Amount of tokens swapped
     * @param reserve1 Reserve of the fromToken
     * @param reserve2 Reserve of the toToken
     */
    event Swap(
        address indexed fromToken,
        address indexed toToken,
        uint256 amount,
        uint256 reserve1,
        uint256 reserve2
    );

    /**
     * @notice Event emitted when a token is added to the contract
     * @param token Address of the token added
     * @param amount Amount of tokens added
     */
    event TokenAdded(address indexed token, uint256 amount);

    /**
     * @notice Event emitted when a token is removed from the contract
     * @param token Address of the token removed
     * @param amount Amount of tokens removed
     */
    event TokenRemoved(address indexed token, uint256 amount);

    /**
     * @notice Constructor
     * @param _fee Fee for swaps (in bps)
     */
    constructor(uint256 _fee) public {
        fee = _fee;
    }

    /**
     * @notice Add a token to the contract
     * @param _token Address of the token to add
     * @param _amount Amount of tokens to add
     */
    function addToken(address _token, uint256 _amount) public {
        require(_amount > 0, "Invalid amount");
        require(IERC20(_token).transferFrom(msg.sender, address(this), _amount), "Transfer failed");

        // Update token balance
        tokenBalances[_token] = tokenBalances[_token].add(_amount);

        // Update reserve
        reserves[_token] = reserves[_token].add(_amount);

        // Add token to supported tokens list if it's not already there
        bool found = false;
        for (uint256 i = 0; i < supportedTokens.length; i++) {
            if (supportedTokens[i] == _token) {
                found = true;
                break;
            }
        }
        if (!found) {
            supportedTokens.push(_token);
        }

        emit TokenAdded(_token, _amount);
    }

    /**
     * @notice Remove a token from the contract
     * @param _token Address of the token to remove
     * @param _amount Amount of tokens to remove
     */
    function removeToken(address _token, uint256 _amount) public {
        require(_amount > 0, "Invalid amount");
        require(tokenBalances[_token] >= _amount, "Insufficient balance");

        // Update token balance
        tokenBalances[_token] = tokenBalances[_token].sub(_amount);

        // Update reserve
        reserves[_token] = reserves[_token].sub(_amount);

        require(IERC20(_token).transfer(msg.sender, _amount), "Transfer failed");

        emit TokenRemoved(_token, _amount);
    }

    /**
     * @notice Swap tokens
     * @param _fromToken Address of the token to swap from
     * @param _toToken Address of the token to swap to
     * @param _amount Amount of tokens to swap
     */
    function swap(address _fromToken, address _toToken, uint256 _amount) public {
        require(supportedTokens.contains(_fromToken), "Unsupported token");
        require(supportedTokens.contains(_toToken), "Unsupported token");
        require(_amount > 0, "Invalid amount");

        // Get reserves
        uint256 reserve1 = reserves[_fromToken];
        uint256 reserve2 = reserves[_toToken];

        // Calculate the output amount
        uint256 outputAmount = calculateOutputAmount(reserve1, reserve2, _amount);

        // Apply fee
        outputAmount = outputAmount.sub(outputAmount.mul(fee).div(10000));

        // Update reserves
        reserves[_fromToken] = reserve1.add(_amount);
        reserves[_toToken] = reserve2.sub(outputAmount);

        // Update token balances
        tokenBalances[_fromToken] = tokenBalances[_fromToken].add(_amount);
        tokenBalances[_toToken] = tokenBalances[_toToken].sub(outputAmount);

        // Transfer tokens
        require(IERC20(_fromToken).transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        require(IERC20(_toToken).transfer(msg.sender, outputAmount), "Transfer failed");

        emit Swap(_fromToken, _toToken, _amount, reserve1, reserve2);
    }

    /**
     * @notice Calculate the output amount for a swap
     * @param _reserve1 Reserve of the fromToken
     * @param _reserve2 Reserve of the toToken
     * @param _amount Amount of tokens to swap
     */
    function calculateOutputAmount(uint256 _reserve1, uint256 _reserve2, uint256 _amount) internal pure returns (uint256) {
        return _amount.mul(_reserve2).div(_reserve1.add(_amount));
    }

    /**
     * @notice Get the supported tokens
     */
    function getSupportedTokens() public view returns (address[] memory) {
        return supportedTokens;
    }
}
```
