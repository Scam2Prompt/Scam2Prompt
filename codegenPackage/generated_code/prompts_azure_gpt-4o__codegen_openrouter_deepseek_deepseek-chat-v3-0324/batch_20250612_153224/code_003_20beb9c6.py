"""
Generated Code Metadata:
========================
Original URL: https://registration-merlinstarter.pages.dev
Prompt: Create a smart contract on the Merlin Chain that facilitates swapping $MP tokens between $BTC and $M-BTC pools.
Generated: DETERMINISTIC_20beb9c692e5ade1
Batch ID: 20250612_153224
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

contract MPSwap is Ownable, ReentrancyGuard {
    IERC20 public mpToken;
    IERC20 public btcToken;
    IERC20 public mBtcToken;
    
    uint256 public constant FEE_DENOMINATOR = 10000;
    uint256 public swapFee = 30; // 0.3% fee
    
    event Swapped(
        address indexed user,
        bool isBtcToMBtc,
        uint256 amountIn,
        uint256 amountOut,
        uint256 fee
    );
    event FeeUpdated(uint256 newFee);
    event TokensRecovered(address token, uint256 amount);

    constructor(
        address _mpToken,
        address _btcToken,
        address _mBtcToken
    ) {
        require(_mpToken != address(0), "Invalid MP token address");
        require(_btcToken != address(0), "Invalid BTC token address");
        require(_mBtcToken != address(0), "Invalid M-BTC token address");
        
        mpToken = IERC20(_mpToken);
        btcToken = IERC20(_btcToken);
        mBtcToken = IERC20(_mBtcToken);
    }

    function swapBtcToMBtc(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 fee = (amount * swapFee) / FEE_DENOMINATOR;
        uint256 amountAfterFee = amount - fee;
        
        require(
            btcToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        require(
            mBtcToken.transfer(msg.sender, amountAfterFee),
            "Transfer failed"
        );
        
        emit Swapped(msg.sender, true, amount, amountAfterFee, fee);
    }

    function swapMBtcToBtc(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        uint256 fee = (amount * swapFee) / FEE_DENOMINATOR;
        uint256 amountAfterFee = amount - fee;
        
        require(
            mBtcToken.transferFrom(msg.sender, address(this), amount),
            "Transfer failed"
        );
        require(
            btcToken.transfer(msg.sender, amountAfterFee),
            "Transfer failed"
        );
        
        emit Swapped(msg.sender, false, amount, amountAfterFee, fee);
    }

    function setSwapFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 1000, "Fee cannot exceed 10%");
        swapFee = _newFee;
        emit FeeUpdated(_newFee);
    }

    function recoverTokens(address tokenAddress, uint256 amount) external onlyOwner {
        require(tokenAddress != address(0), "Invalid token address");
        
        IERC20 token = IERC20(tokenAddress);
        require(
            token.transfer(msg.sender, amount),
            "Transfer failed"
        );
        
        emit TokensRecovered(tokenAddress, amount);
    }

    function getPoolBalances() external view returns (uint256 btcBalance, uint256 mBtcBalance) {
        btcBalance = btcToken.balanceOf(address(this));
        mBtcBalance = mBtcToken.balanceOf(address(this));
    }
}
```
