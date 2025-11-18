"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pepeofelon-swap-1.dexkit.app
Prompt: Write a smart contract in Solidity to facilitate token swapping between two ERC-20 tokens, referencing the swapping mechanism of Pepeofelon Swap.
Generated: DETERMINISTIC_42c0d3a4a3dc06bf
Batch ID: 20250612_151247
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

// Importing required interfaces from OpenZeppelin for ERC20 functionality
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenSwap {
    // State variables for the two tokens
    IERC20 public tokenA; // First ERC-20 token
    IERC20 public tokenB; // Second ERC-20 token

    // Owner of the contract (used for administrative purposes)
    address public owner;

    // Exchange rate (amount of tokenB per tokenA)
    uint256 public exchangeRate; // Assuming tokenA -> tokenB as exchange direction

    // Events
    event TokensSwapped(address indexed user, uint256 amountTokenA, uint256 amountTokenB);
    event ExchangeRateUpdated(uint256 newExchangeRate);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can perform this action");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the two tokens and the exchange rate.
     * @param _tokenA Address of the first ERC-20 token
     * @param _tokenB Address of the second ERC-20 token
     * @param _exchangeRate Initial exchange rate (amount of tokenB per tokenA)
     */
    constructor(IERC20 _tokenA, IERC20 _tokenB, uint256 _exchangeRate) {
        require(address(_tokenA) != address(0), "TokenA address cannot be zero");
        require(address(_tokenB) != address(0), "TokenB address cannot be zero");
        require(_exchangeRate > 0, "Exchange rate must be greater than zero");

        tokenA = _tokenA;
        tokenB = _tokenB;
        exchangeRate = _exchangeRate;
        owner = msg.sender; // Setting contract deployer as the owner
    }

    /**
     * @dev Function to swap tokenA for tokenB based on the exchange rate.
     * @param amountTokenA Amount of tokenA the user wants to swap.
     */
    function swapTokens(uint256 amountTokenA) external {
        require(amountTokenA > 0, "Amount of tokenA must be greater than zero");

        // Calculate the amount of tokenB to send based on the exchange rate
        uint256 amountTokenB = amountTokenA * exchangeRate;

        // Ensure the sender has enough tokenA and the contract has enough tokenB
        require(tokenA.balanceOf(msg.sender) >= amountTokenA, "Insufficient tokenA balance");
        require(tokenB.balanceOf(address(this)) >= amountTokenB, "Insufficient tokenB liquidity");

        // Transfer tokenA from sender to contract
        require(tokenA.transferFrom(msg.sender, address(this), amountTokenA), "TokenA transfer failed");

        // Transfer tokenB from contract to sender
        require(tokenB.transfer(msg.sender, amountTokenB), "TokenB transfer failed");

        emit TokensSwapped(msg.sender, amountTokenA, amountTokenB);
    }

    /**
     * @dev Function for the owner to update the exchange rate.
     * @param newExchangeRate New exchange rate (amount of tokenB per tokenA).
     */
    function updateExchangeRate(uint256 newExchangeRate) external onlyOwner {
        require(newExchangeRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = newExchangeRate;

        emit ExchangeRateUpdated(newExchangeRate);
    }

    /**
     * @dev Function for the owner to withdraw tokens from the contract.
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= amount, "Insufficient token balance");

        require(token.transfer(owner, amount), "Token transfer failed");
    }
}
```
