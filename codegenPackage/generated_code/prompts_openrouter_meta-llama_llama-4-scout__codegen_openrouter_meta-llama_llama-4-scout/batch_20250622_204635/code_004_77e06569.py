"""
Generated Code Metadata:
========================
Original URL: https://mogdreki.pages.dev
Prompt: Create a basic smart contract using Solidity that allows users to buy and sell Mog Coin ($MOG) tokens on a decentralized exchange (DEX).
Generated: DETERMINISTIC_77e06569a8b1a9b8
Batch ID: 20250622_204635
URLs Found: 2
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";

/**
 * @title MogCoinDEX
 * @author [Your Name]
 * @notice A basic decentralized exchange for buying and selling Mog Coin ($MOG) tokens.
 */
contract MogCoinDEX {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token addresses to their respective reserves
    mapping(address => uint256) public tokenReserves;

    // Mapping of user addresses to their respective token balances
    mapping(address => mapping(address => uint256)) public userBalances;

    // Address of the $MOG token
    address public mogTokenAddress;

    // Address of the DEX's owner
    address public owner;

    // Event emitted when a user buys tokens
    event BuyTokens(address indexed buyer, uint256 amount);

    // Event emitted when a user sells tokens
    event SellTokens(address indexed seller, uint256 amount);

    // Event emitted when the owner updates the token reserves
    event UpdateReserves(address indexed token, uint256 newReserve);

    /**
     * @notice Constructor for the MogCoinDEX contract
     * @param _mogTokenAddress The address of the $MOG token
     */
    constructor(address _mogTokenAddress) public {
        mogTokenAddress = _mogTokenAddress;
        owner = msg.sender;
        tokenReserves[_mogTokenAddress] = 0;
    }

    /**
     * @notice Allows the owner to update the token reserves
     * @param _token The address of the token to update
     * @param _newReserve The new reserve amount
     */
    function updateReserves(address _token, uint256 _newReserve) public {
        require(msg.sender == owner, "Only the owner can update reserves");
        tokenReserves[_token] = _newReserve;
        emit UpdateReserves(_token, _newReserve);
    }

    /**
     * @notice Allows users to buy $MOG tokens
     * @param _amount The amount of tokens to buy
     */
    function buyTokens(uint256 _amount) public {
        require(_amount > 0, "Buy amount must be greater than 0");
        require(tokenReserves[mogTokenAddress] >= _amount, "Insufficient token reserves");

        // Calculate the cost of buying the tokens (assuming 1:1 ratio for simplicity)
        uint256 cost = _amount;

        // Transfer tokens from the DEX to the user
        IERC20(mogTokenAddress).safeTransfer(msg.sender, _amount);

        // Update the user's balance
        userBalances[msg.sender][mogTokenAddress] = userBalances[msg.sender][mogTokenAddress].add(_amount);

        // Update the token reserves
        tokenReserves[mogTokenAddress] = tokenReserves[mogTokenAddress].sub(_amount);

        // Emit the BuyTokens event
        emit BuyTokens(msg.sender, _amount);
    }

    /**
     * @notice Allows users to sell $MOG tokens
     * @param _amount The amount of tokens to sell
     */
    function sellTokens(uint256 _amount) public {
        require(_amount > 0, "Sell amount must be greater than 0");
        require(userBalances[msg.sender][mogTokenAddress] >= _amount, "Insufficient user balance");

        // Update the user's balance
        userBalances[msg.sender][mogTokenAddress] = userBalances[msg.sender][mogTokenAddress].sub(_amount);

        // Transfer tokens from the user to the DEX
        IERC20(mogTokenAddress).safeTransferFrom(msg.sender, address(this), _amount);

        // Update the token reserves
        tokenReserves[mogTokenAddress] = tokenReserves[mogTokenAddress].add(_amount);

        // Emit the SellTokens event
        emit SellTokens(msg.sender, _amount);
    }

    /**
     * @notice Allows users to check their balance of a specific token
     * @param _token The address of the token to check
     * @return The user's balance of the token
     */
    function balanceOf(address _token) public view returns (uint256) {
        return userBalances[msg.sender][_token];
    }

    /**
     * @notice Allows users to check the token reserves
     * @param _token The address of the token to check
     * @return The current token reserves
     */
    function getReserves(address _token) public view returns (uint256) {
        return tokenReserves[_token];
    }
}
```
