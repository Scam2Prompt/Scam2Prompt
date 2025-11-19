"""
Generated Code Metadata:
========================
Original URL: https://sun-swap.github.io
Prompt: Write a smart contract that incorporates SunSwap's eco-friendly initiatives while enabling users to perform token swaps and liquidity provision.
Generated: DETERMINISTIC_196d540d6d3150f1
Batch ID: 20250612_142640
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
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title SunSwap Contract
 * @author [Your Name]
 * @notice This contract enables users to perform token swaps and liquidity provision
 *         while incorporating eco-friendly initiatives.
 */
contract SunSwap {
    using SafeMath for uint256;

    // Mapping of token addresses to their respective reserves
    mapping(address => mapping(address => uint256)) public reserves;

    // Mapping of token addresses to their respective liquidity providers
    mapping(address => mapping(address => mapping(address => uint256))) public liquidityProviders;

    // Mapping of eco-friendly initiative participants
    mapping(address => bool) public ecoInitiativeParticipants;

    // Event emitted when a token swap occurs
    event TokenSwap(address indexed tokenIn, address indexed tokenOut, uint256 amountIn, uint256 amountOut);

    // Event emitted when liquidity is provided
    event LiquidityProvided(address indexed token, address indexed provider, uint256 amount);

    // Event emitted when eco-friendly initiative participant is added
    event EcoInitiativeParticipantAdded(address indexed participant);

    /**
     * @notice Constructor function
     */
    constructor() public {}

    /**
     * @notice Adds a token reserve
     * @param tokenIn Address of token to add reserve for
     * @param tokenOut Address of token to add reserve for
     * @param reserveIn Initial reserve amount for tokenIn
     * @param reserveOut Initial reserve amount for tokenOut
     */
    function addReserve(address tokenIn, address tokenOut, uint256 reserveIn, uint256 reserveOut) public onlyOwner {
        require(reserveIn > 0 && reserveOut > 0, "Reserves must be greater than 0");
        reserves[tokenIn][tokenOut] = reserveIn;
        reserves[tokenOut][tokenIn] = reserveOut;
    }

    /**
     * @notice Performs a token swap
     * @param tokenIn Address of token to swap from
     * @param tokenOut Address of token to swap to
     * @param amountIn Amount of tokenIn to swap
     * @return amountOut Amount of tokenOut received
     */
    function swap(address tokenIn, address tokenOut, uint256 amountIn) public returns (uint256 amountOut) {
        require(amountIn > 0, "Amount in must be greater than 0");
        require(reserves[tokenIn][tokenOut] > 0, "Reserve not available");

        uint256 reserveIn = reserves[tokenIn][tokenOut];
        uint256 reserveOut = reserves[tokenOut][tokenIn];

        // Calculate the amount out using the constant product market maker formula
        amountOut = amountIn.mul(reserveOut).div(reserveIn);

        // Update reserves
        reserves[tokenIn][tokenOut] = reserveIn.add(amountIn);
        reserves[tokenOut][tokenIn] = reserveOut.sub(amountOut);

        // Emit event
        emit TokenSwap(tokenIn, tokenOut, amountIn, amountOut);

        return amountOut;
    }

    /**
     * @notice Provides liquidity for a token pair
     * @param token Address of token to provide liquidity for
     * @param provider Address of liquidity provider
     * @param amount Amount of liquidity to provide
     */
    function provideLiquidity(address token, address provider, uint256 amount) public {
        require(amount > 0, "Amount must be greater than 0");

        // Update liquidity provider mapping
        liquidityProviders[token][provider][token] = liquidityProviders[token][provider][token].add(amount);

        // Emit event
        emit LiquidityProvided(token, provider, amount);
    }

    /**
     * @notice Adds an eco-friendly initiative participant
     * @param participant Address of participant to add
     */
    function addEcoInitiativeParticipant(address participant) public onlyOwner {
        ecoInitiativeParticipants[participant] = true;

        // Emit event
        emit EcoInitiativeParticipantAdded(participant);
    }

    /**
     * @notice Checks if an address is an eco-friendly initiative participant
     * @param participant Address to check
     * @return bool True if participant is an eco-friendly initiative participant, false otherwise
     */
    function isEcoInitiativeParticipant(address participant) public view returns (bool) {
        return ecoInitiativeParticipants[participant];
    }

    /**
     * @notice Transfers tokens from this contract to a user
     * @param token Address of token to transfer
     * @param to Address of user to transfer to
     * @param amount Amount of tokens to transfer
     */
    function transferTokens(address token, address to, uint256 amount) public onlyOwner {
        IERC20(token).transfer(to, amount);
    }
}
```
