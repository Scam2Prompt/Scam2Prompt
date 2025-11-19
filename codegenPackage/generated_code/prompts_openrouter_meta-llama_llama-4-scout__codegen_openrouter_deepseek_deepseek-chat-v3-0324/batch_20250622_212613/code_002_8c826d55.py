"""
Generated Code Metadata:
========================
Original URL: https://cbsjkqfku.com
Prompt: "Create a recipe for a complex DeFi transaction using DeFi Saver's Custom Transaction Builder, involving flash loans and token swaps."
Generated: DETERMINISTIC_8c826d554654dc8a
Batch ID: 20250622_212613
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/utils/Address.sol";
import "./interfaces/IFlashLoanReceiver.sol";
import "./interfaces/ILendingPool.sol";
import "./interfaces/IUniswapV2Router.sol";

contract DeFiComplexRecipe is IFlashLoanReceiver {
    using Address for address payable;
    
    // Contract owner
    address public owner;
    
    // DeFi protocol addresses
    address public constant LENDING_POOL = 0x7d2768dE32b0b80b7a3454c06BdAc94A69DDc7A9; // Mainnet AAVE Lending Pool
    address public constant UNISWAP_ROUTER = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D; // Mainnet Uniswap V2
    
    // Events
    event RecipeExecuted(address indexed initiator, uint256 profit);
    event FlashLoanReceived(address indexed token, uint256 amount, uint256 fee);
    
    // Modifiers
    modifier onlyOwner() {
        require(msg.sender == owner, "Not owner");
        _;
    }
    
    constructor() {
        owner = msg.sender;
    }
    
    /**
     * @dev Main recipe execution function
     * @param _tokenIn Token to start with (if any)
     * @param _amountIn Amount of starting token
     * @param _flashLoanToken Token to flash loan
     * @param _flashLoanAmount Amount to flash loan
     * @param _swapPath Array of tokens for swap path
     * @param _minReturn Minimum expected return from swaps
     */
    function executeRecipe(
        address _tokenIn,
        uint256 _amountIn,
        address _flashLoanToken,
        uint256 _flashLoanAmount,
        address[] memory _swapPath,
        uint256 _minReturn
    ) external onlyOwner {
        // Step 1: Take initial token (if any) and approve for spending
        if (_tokenIn != address(0) && _amountIn > 0) {
            IERC20(_tokenIn).transferFrom(msg.sender, address(this), _amountIn);
            IERC20(_tokenIn).approve(UNISWAP_ROUTER, _amountIn);
        }
        
        // Step 2: Take flash loan
        address[] memory assets = new address[](1);
        assets[0] = _flashLoanToken;
        uint256[] memory amounts = new uint256[](1);
        amounts[0] = _flashLoanAmount;
        uint256[] memory modes = new uint256[](1);
        modes[0] = 0; // No debt
        
        ILendingPool(LENDING_POOL).flashLoan(
            address(this),
            assets,
            amounts,
            modes,
            address(this),
            abi.encode(_swapPath, _minReturn, _tokenIn, _amountIn),
            0
        );
    }
    
    /**
     * @dev Flash loan callback function
     */
    function executeOperation(
        address[] calldata assets,
        uint256[] calldata amounts,
        uint256[] calldata premiums,
        address initiator,
        bytes calldata params
    ) external override returns (bool) {
        require(msg.sender == LENDING_POOL, "Caller must be lending pool");
        require(initiator == address(this), "Initiator must be this contract");
        
        (address[] memory swapPath, uint256 minReturn, address tokenIn, uint256 amountIn) = 
            abi.decode(params, (address[], uint256, address, uint256));
        
        address flashLoanToken = assets[0];
        uint256 flashLoanAmount = amounts[0];
        uint256 flashLoanFee = premiums[0];
        
        emit FlashLoanReceived(flashLoanToken, flashLoanAmount, flashLoanFee);
        
        // Step 3: Perform token swaps
        IERC20(flashLoanToken).approve(UNISWAP_ROUTER, flashLoanAmount);
        
        if (tokenIn != address(0) && amountIn > 0) {
            // Combine flash loan with initial funds
            uint256 totalAmount = IERC20(swapPath[0]).balanceOf(address(this));
            IUniswapV2Router(UNISWAP_ROUTER).swapExactTokensForTokens(
                totalAmount,
                minReturn,
                swapPath,
                address(this),
                block.timestamp + 1200
            );
        } else {
            // Use only flash loan
            IUniswapV2Router(UNISWAP_ROUTER).swapExactTokensForTokens(
                flashLoanAmount,
                minReturn,
                swapPath,
                address(this),
                block.timestamp + 1200
            );
        }
        
        // Step 4: Repay flash loan
        uint256 amountOwed = flashLoanAmount + flashLoanFee;
        IERC20(flashLoanToken).approve(LENDING_POOL, amountOwed);
        
        // Step 5: Calculate and send profit to owner
        address finalToken = swapPath[swapPath.length - 1];
        uint256 finalBalance = IERC20(finalToken).balanceOf(address(this));
        
        if (finalBalance > amountOwed) {
            uint256 profit = finalBalance - amountOwed;
            IERC20(finalToken).transfer(owner, profit);
            emit RecipeExecuted(owner, profit);
        }
        
        return true;
    }
    
    /**
     * @dev Emergency withdraw function
     */
    function withdrawToken(address _token) external onlyOwner {
        uint256 balance = IERC20(_token).balanceOf(address(this));
        IERC20(_token).transfer(owner, balance);
    }
    
    receive() external payable {}
}
```
