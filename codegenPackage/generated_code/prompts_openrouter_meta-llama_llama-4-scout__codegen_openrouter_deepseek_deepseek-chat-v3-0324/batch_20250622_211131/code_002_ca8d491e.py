"""
Generated Code Metadata:
========================
Original URL: https://kabosu-bsc.pages.dev
Prompt: Develop a simple smart contract in Solidity to facilitate the swapping of Kabosu Tokens on a decentralized exchange (DEX), as mentioned in the project's roadmap.
Generated: DETERMINISTIC_ca8d491eea4570d7
Batch ID: 20250622_211131
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title KabosuTokenSwap
 * @dev A smart contract for swapping Kabosu Tokens on a decentralized exchange (DEX)
 * with features for pausing, ownership control, and reentrancy protection.
 */
contract KabosuTokenSwap is Ownable, ReentrancyGuard {
    IERC20 public kabosuToken;
    IERC20 public pairedToken;
    uint256 public exchangeRate;
    bool public isPaused;

    event TokensSwapped(
        address indexed user,
        uint256 kabosuAmount,
        uint256 pairedTokenAmount
    );
    event ExchangeRateUpdated(uint256 newRate);
    event ContractPaused(bool isPaused);

    /**
     * @dev Initializes the contract with the Kabosu Token, paired token addresses, and initial exchange rate.
     * @param _kabosuToken Address of the Kabosu Token contract
     * @param _pairedToken Address of the token to swap with Kabosu
     * @param _initialExchangeRate Initial exchange rate (amount of pairedToken per Kabosu Token)
     */
    constructor(
        address _kabosuToken,
        address _pairedToken,
        uint256 _initialExchangeRate
    ) {
        require(_kabosuToken != address(0), "Kabosu token address cannot be zero");
        require(_pairedToken != address(0), "Paired token address cannot be zero");
        require(_initialExchangeRate > 0, "Exchange rate must be greater than zero");

        kabosuToken = IERC20(_kabosuToken);
        pairedToken = IERC20(_pairedToken);
        exchangeRate = _initialExchangeRate;
        isPaused = false;
    }

    /**
     * @dev Swaps Kabosu Tokens for the paired token at the current exchange rate.
     * @param _kabosuAmount Amount of Kabosu Tokens to swap
     */
    function swapTokens(uint256 _kabosuAmount) external nonReentrant {
        require(!isPaused, "Contract is paused");
        require(_kabosuAmount > 0, "Amount must be greater than zero");

        uint256 pairedTokenAmount = _kabosuAmount * exchangeRate;
        require(
            pairedToken.balanceOf(address(this)) >= pairedTokenAmount,
            "Insufficient paired token balance"
        );

        require(
            kabosuToken.transferFrom(msg.sender, address(this), _kabosuAmount),
            "Kabosu token transfer failed"
        );
        require(
            pairedToken.transfer(msg.sender, pairedTokenAmount),
            "Paired token transfer failed"
        );

        emit TokensSwapped(msg.sender, _kabosuAmount, pairedTokenAmount);
    }

    /**
     * @dev Updates the exchange rate for the token swap.
     * @param _newRate New exchange rate (amount of pairedToken per Kabosu Token)
     */
    function updateExchangeRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Exchange rate must be greater than zero");
        exchangeRate = _newRate;
        emit ExchangeRateUpdated(_newRate);
    }

    /**
     * @dev Pauses or unpauses the token swapping functionality.
     * @param _paused Boolean indicating whether to pause or unpause
     */
    function setPaused(bool _paused) external onlyOwner {
        isPaused = _paused;
        emit ContractPaused(_paused);
    }

    /**
     * @dev Withdraws any ERC20 tokens from the contract. Only callable by owner.
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function withdrawTokens(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(0), "Token address cannot be zero");
        require(_amount > 0, "Amount must be greater than zero");
        IERC20 token = IERC20(_token);
        require(
            token.transfer(msg.sender, _amount),
            "Token transfer failed"
        );
    }
}
```
