"""
Generated Code Metadata:
========================
Original URL: https://usdswap.org
Prompt: "Generate a smart contract in Solidity for a basic token swap on the Ethereum network involving a USD pegged stablecoin."
Generated: DETERMINISTIC_6b1a4cb72ca02948
Batch ID: 20250622_205306
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
    IERC20 public tokenA; // Stablecoin (e.g., USDC)
    IERC20 public tokenB; // Other token to swap with
    uint256 public rate;  // Exchange rate (tokenA per tokenB)

    event Swap(
        address indexed user,
        uint256 amountA,
        uint256 amountB,
        uint256 timestamp
    );

    constructor(
        address _tokenA,
        address _tokenB,
        uint256 _rate
    ) {
        require(_tokenA != address(0), "TokenA address cannot be zero");
        require(_tokenB != address(0), "TokenB address cannot be zero");
        require(_rate > 0, "Rate must be greater than zero");

        tokenA = IERC20(_tokenA);
        tokenB = IERC20(_tokenB);
        rate = _rate;
    }

    function swapAToB(uint256 amountA) external nonReentrant {
        require(amountA > 0, "Amount must be greater than zero");

        uint256 amountB = (amountA * 1e18) / rate;
        require(
            tokenB.balanceOf(address(this)) >= amountB,
            "Insufficient tokenB liquidity"
        );

        require(
            tokenA.transferFrom(msg.sender, address(this), amountA),
            "TokenA transfer failed"
        );
        require(
            tokenB.transfer(msg.sender, amountB),
            "TokenB transfer failed"
        );

        emit Swap(msg.sender, amountA, amountB, block.timestamp);
    }

    function swapBToA(uint256 amountB) external nonReentrant {
        require(amountB > 0, "Amount must be greater than zero");

        uint256 amountA = (amountB * rate) / 1e18;
        require(
            tokenA.balanceOf(address(this)) >= amountA,
            "Insufficient tokenA liquidity"
        );

        require(
            tokenB.transferFrom(msg.sender, address(this), amountB),
            "TokenB transfer failed"
        );
        require(
            tokenA.transfer(msg.sender, amountA),
            "TokenA transfer failed"
        );

        emit Swap(msg.sender, amountA, amountB, block.timestamp);
    }

    function updateRate(uint256 newRate) external onlyOwner {
        require(newRate > 0, "Rate must be greater than zero");
        rate = newRate;
    }

    function withdrawTokenA(uint256 amount) external onlyOwner {
        require(
            tokenA.transfer(msg.sender, amount),
            "TokenA withdrawal failed"
        );
    }

    function withdrawTokenB(uint256 amount) external onlyOwner {
        require(
            tokenB.transfer(msg.sender, amount),
            "TokenB withdrawal failed"
        );
    }

    function getTokenABalance() external view returns (uint256) {
        return tokenA.balanceOf(address(this));
    }

    function getTokenBBalance() external view returns (uint256) {
        return tokenB.balanceOf(address(this));
    }
}
```
