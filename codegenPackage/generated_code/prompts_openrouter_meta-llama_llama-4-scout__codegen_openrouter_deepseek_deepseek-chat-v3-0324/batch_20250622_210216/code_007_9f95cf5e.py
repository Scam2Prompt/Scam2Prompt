"""
Generated Code Metadata:
========================
Original URL: https://diamond-7n0.pages.dev
Prompt: Develop a basic smart contract in Solidity that allows users to swap Diamond Coin with other cryptocurrencies on the Ethereum blockchain.
Generated: DETERMINISTIC_9f95cf5e871d5add
Batch ID: 20250622_210216
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

contract DiamondCoinSwap is Ownable, ReentrancyGuard {
    IERC20 public diamondCoin;
    mapping(address => bool) public supportedTokens;
    mapping(address => uint256) public exchangeRates; // Rate is tokens per 1 Diamond Coin

    event TokenSwapped(
        address indexed user,
        address indexed fromToken,
        address indexed toToken,
        uint256 amountIn,
        uint256 amountOut
    );
    event TokenSupported(address token, uint256 exchangeRate);
    event TokenUnsupported(address token);
    event ExchangeRateUpdated(address token, uint256 newRate);

    constructor(address _diamondCoin) {
        require(_diamondCoin != address(0), "Invalid Diamond Coin address");
        diamondCoin = IERC20(_diamondCoin);
    }

    function addSupportedToken(address _token, uint256 _exchangeRate) external onlyOwner {
        require(_token != address(0), "Invalid token address");
        require(_exchangeRate > 0, "Exchange rate must be positive");
        supportedTokens[_token] = true;
        exchangeRates[_token] = _exchangeRate;
        emit TokenSupported(_token, _exchangeRate);
    }

    function removeSupportedToken(address _token) external onlyOwner {
        require(supportedTokens[_token], "Token not supported");
        supportedTokens[_token] = false;
        exchangeRates[_token] = 0;
        emit TokenUnsupported(_token);
    }

    function updateExchangeRate(address _token, uint256 _newRate) external onlyOwner {
        require(supportedTokens[_token], "Token not supported");
        require(_newRate > 0, "Exchange rate must be positive");
        exchangeRates[_token] = _newRate;
        emit ExchangeRateUpdated(_token, _newRate);
    }

    function swapDiamondToToken(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Amount must be positive");

        uint256 tokenAmount = _amount * exchangeRates[_token];
        require(
            IERC20(_token).balanceOf(address(this)) >= tokenAmount,
            "Insufficient contract balance"
        );

        diamondCoin.transferFrom(msg.sender, address(this), _amount);
        IERC20(_token).transfer(msg.sender, tokenAmount);

        emit TokenSwapped(msg.sender, address(diamondCoin), _token, _amount, tokenAmount);
    }

    function swapTokenToDiamond(address _token, uint256 _amount) external nonReentrant {
        require(supportedTokens[_token], "Token not supported");
        require(_amount > 0, "Amount must be positive");

        uint256 diamondAmount = _amount / exchangeRates[_token];
        require(
            diamondCoin.balanceOf(address(this)) >= diamondAmount,
            "Insufficient Diamond Coin balance"
        );

        IERC20(_token).transferFrom(msg.sender, address(this), _amount);
        diamondCoin.transfer(msg.sender, diamondAmount);

        emit TokenSwapped(msg.sender, _token, address(diamondCoin), _amount, diamondAmount);
    }

    function withdrawToken(address _token, uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be positive");
        IERC20 token = IERC20(_token);
        require(
            token.balanceOf(address(this)) >= _amount,
            "Insufficient contract balance"
        );
        token.transfer(owner(), _amount);
    }

    function withdrawDiamond(uint256 _amount) external onlyOwner {
        require(_amount > 0, "Amount must be positive");
        require(
            diamondCoin.balanceOf(address(this)) >= _amount,
            "Insufficient Diamond Coin balance"
        );
        diamondCoin.transfer(owner(), _amount);
    }
}
```
