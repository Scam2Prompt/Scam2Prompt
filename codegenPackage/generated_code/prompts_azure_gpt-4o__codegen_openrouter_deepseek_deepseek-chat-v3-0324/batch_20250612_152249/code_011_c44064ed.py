"""
Generated Code Metadata:
========================
Original URL: https://rabotaentnet.pages.dev
Prompt: Develop a decentralized swap application for $ZUSHI tokens, ensuring compatibility with the Binance Smart Chain and other CEX listings mentioned in the roadmap.
Generated: DETERMINISTIC_c44064eddbd120d2
Batch ID: 20250612_152249
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IPancakeRouter {
    function factory() external pure returns (address);
    function WETH() external pure returns (address);
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    function addLiquidity(
        address tokenA,
        address tokenB,
        uint amountADesired,
        uint amountBDesired,
        uint amountAMin,
        uint amountBMin,
        address to,
        uint deadline
    ) external returns (uint amountA, uint amountB, uint liquidity);
}

interface IPancakeFactory {
    function getPair(address tokenA, address tokenB) external view returns (address pair);
}

contract ZushiSwap is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    IERC20 public zushiToken;
    IPancakeRouter public pancakeRouter;
    address public wbnbAddress;

    uint256 public swapFeePercent = 5; // 0.5% default fee
    uint256 public constant FEE_DENOMINATOR = 1000;
    address public feeWallet;

    event Swap(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut,
        uint256 fee
    );
    event LiquidityAdded(
        address indexed provider,
        uint256 zushiAmount,
        uint256 tokenAmount,
        uint256 liquidity
    );
    event FeeUpdated(uint256 newFee);
    event FeeWalletUpdated(address newWallet);

    constructor(
        address _zushiToken,
        address _pancakeRouter,
        address _wbnbAddress,
        address _feeWallet
    ) {
        require(_zushiToken != address(0), "Invalid ZUSHI token address");
        require(_pancakeRouter != address(0), "Invalid PancakeRouter address");
        require(_wbnbAddress != address(0), "Invalid WBNB address");
        require(_feeWallet != address(0), "Invalid fee wallet address");

        zushiToken = IERC20(_zushiToken);
        pancakeRouter = IPancakeRouter(_pancakeRouter);
        wbnbAddress = _wbnbAddress;
        feeWallet = _feeWallet;
    }

    function setSwapFeePercent(uint256 _swapFeePercent) external onlyOwner {
        require(_swapFeePercent <= 50, "Fee cannot exceed 5%");
        swapFeePercent = _swapFeePercent;
        emit FeeUpdated(_swapFeePercent);
    }

    function setFeeWallet(address _feeWallet) external onlyOwner {
        require(_feeWallet != address(0), "Invalid fee wallet address");
        feeWallet = _feeWallet;
        emit FeeWalletUpdated(_feeWallet);
    }

    function swapTokens(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn,
        uint256 _amountOutMin,
        uint256 _deadline
    ) external nonReentrant {
        require(_tokenIn != address(0) && _tokenOut != address(0), "Invalid token addresses");
        require(_amountIn > 0, "Amount must be greater than 0");
        require(_deadline >= block.timestamp, "Deadline has passed");

        IERC20 tokenIn = IERC20(_tokenIn);
        IERC20 tokenOut = IERC20(_tokenOut);

        // Transfer tokens from user to contract
        require(tokenIn.transferFrom(msg.sender, address(this), _amountIn), "Transfer failed");

        // Calculate fee and amount after fee
        uint256 fee = _amountIn.mul(swapFeePercent).div(FEE_DENOMINATOR);
        uint256 amountAfterFee = _amountIn.sub(fee);

        // Transfer fee to fee wallet
        if (fee > 0) {
            require(tokenIn.transfer(feeWallet, fee), "Fee transfer failed");
        }

        // Approve router to spend tokens
        tokenIn.approve(address(pancakeRouter), amountAfterFee);

        // Perform swap
        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;

        uint[] memory amounts = pancakeRouter.swapExactTokensForTokens(
            amountAfterFee,
            _amountOutMin,
            path,
            msg.sender,
            _deadline
        );

        emit Swap(msg.sender, _tokenIn, _tokenOut, _amountIn, amounts[1], fee);
    }

    function addLiquidity(
        address _token,
        uint256 _zushiAmount,
        uint256 _tokenAmount,
        uint256 _zushiMin,
        uint256 _tokenMin,
        uint256 _deadline
    ) external nonReentrant {
        require(_token != address(0), "Invalid token address");
        require(_zushiAmount > 0 && _tokenAmount > 0, "Amounts must be greater than 0");
        require(_deadline >= block.timestamp, "Deadline has passed");

        IERC20 token = IERC20(_token);

        // Transfer ZUSHI tokens from user to contract
        require(zushiToken.transferFrom(msg.sender, address(this), _zushiAmount), "ZUSHI transfer failed");
        // Transfer other tokens from user to contract
        require(token.transferFrom(msg.sender, address(this), _tokenAmount), "Token transfer failed");

        // Approve router to spend tokens
        zushiToken.approve(address(pancakeRouter), _zushiAmount);
        token.approve(address(pancakeRouter), _tokenAmount);

        // Add liquidity
        (uint amountA, uint amountB, uint liquidity) = pancakeRouter.addLiquidity(
            address(zushiToken),
            _token,
            _zushiAmount,
            _tokenAmount,
            _zushiMin,
            _tokenMin,
            msg.sender,
            _deadline
        );

        // Return any leftover tokens
        if (_zushiAmount > amountA) {
            zushiToken.transfer(msg.sender, _zushiAmount.sub(amountA));
        }
        if (_tokenAmount > amountB) {
            token.transfer(msg.sender, _tokenAmount.sub(amountB));
        }

        emit LiquidityAdded(msg.sender, amountA, amountB, liquidity);
    }

    function getPairAddress(address _token) external view returns (address) {
        return IPancakeFactory(pancakeRouter.factory()).getPair(address(zushiToken), _token);
    }

    function getExpectedAmountOut(
        address _tokenIn,
        address _tokenOut,
        uint256 _amountIn
    ) external view returns (uint256) {
        require(_tokenIn != address(0) && _tokenOut != address(0), "Invalid token addresses");
        require(_amountIn > 0, "Amount must be greater than 0");

        address[] memory path = new address[](2);
        path[0] = _tokenIn;
        path[1] = _tokenOut;

        try pancakeRouter.getAmountsOut(_amountIn, path) returns (uint[] memory amounts) {
            return amounts[1];
        } catch {
            return 0;
        }
    }

    // Emergency withdraw in case tokens get stuck
    function emergencyWithdraw(address _token) external onlyOwner {
        IERC20 token = IERC20(_token);
        uint256 balance = token.balanceOf(address(this));
        require(balance > 0, "No tokens to withdraw");
        require(token.transfer(owner(), balance), "Withdrawal failed");
    }
}
```
