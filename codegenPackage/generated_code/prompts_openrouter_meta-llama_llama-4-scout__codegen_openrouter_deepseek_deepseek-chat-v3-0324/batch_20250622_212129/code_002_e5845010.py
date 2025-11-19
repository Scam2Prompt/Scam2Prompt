"""
Generated Code Metadata:
========================
Original URL: https://buttholecoin.dev
Prompt: Generate a simple smart contract in Solidity for a token swap feature similar to the one mentioned on the Butthole Coin website.
Generated: DETERMINISTIC_e58450109652db49
Batch ID: 20250622_212129
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

contract TokenSwap is Ownable, ReentrancyGuard {
    IERC20 public immutable tokenFrom;
    IERC20 public immutable tokenTo;
    uint256 public swapRate; // Amount of tokenTo per tokenFrom (multiplied by 1e18 for precision)
    bool public swapEnabled;

    event Swap(
        address indexed user,
        uint256 amountFrom,
        uint256 amountTo
    );
    event SwapRateUpdated(uint256 newRate);
    event SwapToggled(bool enabled);

    constructor(
        address _tokenFrom,
        address _tokenTo,
        uint256 _swapRate
    ) {
        require(_tokenFrom != address(0), "TokenFrom cannot be zero address");
        require(_tokenTo != address(0), "TokenTo cannot be zero address");
        require(_swapRate > 0, "Swap rate must be positive");

        tokenFrom = IERC20(_tokenFrom);
        tokenTo = IERC20(_tokenTo);
        swapRate = _swapRate;
        swapEnabled = true;
    }

    function swap(uint256 amountFrom) external nonReentrant {
        require(swapEnabled, "Swap is currently disabled");
        require(amountFrom > 0, "Amount must be positive");

        uint256 amountTo = (amountFrom * swapRate) / 1e18;
        require(
            tokenTo.balanceOf(address(this)) >= amountTo,
            "Insufficient contract balance"
        );

        // Transfer tokens from user
        require(
            tokenFrom.transferFrom(msg.sender, address(this), amountFrom),
            "TransferFrom failed"
        );

        // Transfer tokens to user
        require(
            tokenTo.transfer(msg.sender, amountTo),
            "Transfer failed"
        );

        emit Swap(msg.sender, amountFrom, amountTo);
    }

    function updateSwapRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Swap rate must be positive");
        swapRate = newRate;
        emit SwapRateUpdated(newRate);
    }

    function toggleSwap(bool enabled) external onlyOwner {
        swapEnabled = enabled;
        emit SwapToggled(enabled);
    }

    function withdrawTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Token address cannot be zero");
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Withdrawal failed"
        );
    }
}
```
