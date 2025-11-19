"""
Generated Code Metadata:
========================
Original URL: https://bafybeig2qxervlifeg5gur3hrsbgo6hrco4esjxaz2r6nixoqkc6nhhjbe.ipfs.dweb.link
Prompt: Develop a decentralized application (dApp) that integrates Pencils Protocol's low-slippage, low-gas swaps, lending, and borrowing features on the Scroll platform.
Generated: DETERMINISTIC_e68e5527063fba54
Batch ID: 20250612_150228
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

interface IPencilsRouter {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function getAmountsOut(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts);
}

interface IPencilsLending {
    function deposit(address token, uint amount) external;
    function withdraw(address token, uint amount) external;
    function borrow(address token, uint amount) external;
    function repay(address token, uint amount) external;
    function getBorrowRate(address token) external view returns (uint);
    function getSupplyRate(address token) external view returns (uint);
}

contract PencilsScrollIntegration is Ownable, ReentrancyGuard {
    IPencilsRouter public immutable pencilsRouter;
    IPencilsLending public immutable pencilsLending;
    
    event SwapExecuted(
        address indexed user,
        address[] path,
        uint amountIn,
        uint amountOut
    );
    
    event DepositMade(
        address indexed user,
        address token,
        uint amount
    );
    
    event WithdrawalMade(
        address indexed user,
        address token,
        uint amount
    );
    
    event BorrowExecuted(
        address indexed user,
        address token,
        uint amount
    );
    
    event RepaymentMade(
        address indexed user,
        address token,
        uint amount
    );

    constructor(address _router, address _lending) {
        require(_router != address(0), "Invalid router address");
        require(_lending != address(0), "Invalid lending address");
        
        pencilsRouter = IPencilsRouter(_router);
        pencilsLending = IPencilsLending(_lending);
    }

    /**
     * @dev Execute a token swap with minimal slippage
     * @param amountIn Amount of input tokens to swap
     * @param amountOutMin Minimum amount of output tokens expected
     * @param path Array of token addresses representing swap path
     * @param deadline Deadline for the swap transaction
     */
    function executeSwap(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        uint deadline
    ) external nonReentrant {
        require(amountIn > 0, "Amount must be greater than 0");
        require(path.length >= 2, "Invalid path");
        require(deadline >= block.timestamp, "Expired deadline");
        
        IERC20 inputToken = IERC20(path[0]);
        require(inputToken.transferFrom(msg.sender, address(this), amountIn), "Transfer failed");
        require(inputToken.approve(address(pencilsRouter), amountIn), "Approval failed");
        
        uint[] memory amounts = pencilsRouter.swapExactTokensForTokens(
            amountIn,
            amountOutMin,
            path,
            msg.sender,
            deadline
        );
        
        emit SwapExecuted(msg.sender, path, amountIn, amounts[amounts.length - 1]);
    }

    /**
     * @dev Get estimated output amount for a swap
     * @param amountIn Amount of input tokens
     * @param path Array of token addresses representing swap path
     * @return amounts Array of amounts at each step of the path
     */
    function getSwapEstimate(uint amountIn, address[] calldata path) external view returns (uint[] memory amounts) {
        require(amountIn > 0, "Amount must be greater than 0");
        require(path.length >= 2, "Invalid path");
        
        amounts = pencilsRouter.getAmountsOut(amountIn, path);
        return amounts;
    }

    /**
     * @dev Deposit tokens into the lending protocol
     * @param token Address of the token to deposit
     * @param amount Amount of tokens to deposit
     */
    function deposit(address token, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        IERC20(token).approve(address(pencilsLending), amount);
        
        pencilsLending.deposit(token, amount);
        emit DepositMade(msg.sender, token, amount);
    }

    /**
     * @dev Withdraw tokens from the lending protocol
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function withdraw(address token, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        pencilsLending.withdraw(token, amount);
        IERC20(token).transfer(msg.sender, amount);
        
        emit WithdrawalMade(msg.sender, token, amount);
    }

    /**
     * @dev Borrow tokens from the lending protocol
     * @param token Address of the token to borrow
     * @param amount Amount of tokens to borrow
     */
    function borrow(address token, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        pencilsLending.borrow(token, amount);
        IERC20(token).transfer(msg.sender, amount);
        
        emit BorrowExecuted(msg.sender, token, amount);
    }

    /**
     * @dev Repay borrowed tokens to the lending protocol
     * @param token Address of the token to repay
     * @param amount Amount of tokens to repay
     */
    function repay(address token, uint amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        
        IERC20(token).transferFrom(msg.sender, address(this), amount);
        IERC20(token).approve(address(pencilsLending), amount);
        
        pencilsLending.repay(token, amount);
        emit RepaymentMade(msg.sender, token, amount);
    }

    /**
     * @dev Get current borrow rate for a token
     * @param token Address of the token
     * @return Current borrow rate
     */
    function getBorrowRate(address token) external view returns (uint) {
        return pencilsLending.getBorrowRate(token);
    }

    /**
     * @dev Get current supply rate for a token
     * @param token Address of the token
     * @return Current supply rate
     */
    function getSupplyRate(address token) external view returns (uint) {
        return pencilsLending.getSupplyRate(token);
    }

    /**
     * @dev Emergency function to recover ERC20 tokens sent by mistake
     * @param token Address of the token to recover
     * @param amount Amount to recover
     */
    function recoverERC20(address token, uint amount) external onlyOwner {
        IERC20(token).transfer(owner(), amount);
    }
}
```
