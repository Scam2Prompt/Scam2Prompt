"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sourcecopy.pages.dev
Prompt: Write a Solidity contract that interacts with the WETH contract at address `0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2` and the Uniswap V2 router at address `0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D`, as shown in the Oneinch Slippage Bot example.
Generated: DETERMINISTIC_9d5e1d6bfa9dcad4
Batch ID: 20250612_151347
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

/**
 * @title WETHInteractionAndUniswapBot
 * @dev A Solidity contract that interacts with the WETH contract and Uniswap V2 Router
 */
interface IWETH {
    function deposit() external payable;
    function withdraw(uint256 wad) external;
    function transfer(address to, uint256 value) external returns (bool);
}

interface IUniswapV2Router {
    function swapExactTokensForTokens(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
    
    function swapExactETHForTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable returns (uint[] memory amounts);
    
    function swapExactTokensForETH(
        uint amountIn,
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external returns (uint[] memory amounts);
}

contract WETHInteractionAndUniswapBot {
    // Address of the WETH contract
    address public immutable WETH_ADDRESS = 0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2;
    
    // Address of the Uniswap V2 Router
    address public immutable UNISWAP_V2_ROUTER = 0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D;

    IWETH private immutable weth;
    IUniswapV2Router private immutable router;

    /**
     * @dev Constructor that initializes the WETH and Uniswap Router interfaces.
     */
    constructor() {
        weth = IWETH(WETH_ADDRESS);
        router = IUniswapV2Router(UNISWAP_V2_ROUTER);
    }

    /**
     * @dev Deposit ETH and wrap it into WETH.
     */
    function depositETHToWETH() external payable {
        require(msg.value > 0, "Must send ETH to deposit");
        weth.deposit{value: msg.value}();
    }

    /**
     * @dev Withdraw WETH and unwrap it into ETH.
     * @param amount The amount of WETH to unwrap into ETH.
     */
    function withdrawWETHToETH(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        weth.withdraw(amount);
    }

    /**
     * @dev Swap WETH for tokens using Uniswap V2.
     * @param amountIn Amount of WETH to swap.
     * @param amountOutMin Minimum output amount of tokens.
     * @param path Token swap path (e.g., WETH -> Token).
     * @param deadline Transaction deadline (block timestamp).
     */
    function swapWETHForTokens(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(path[0] == WETH_ADDRESS, "Path must start with WETH");
        
        // Approve the Uniswap router to spend WETH
        weth.transfer(address(this), amountIn);
        
        // Perform the swap on Uniswap
        router.swapExactTokensForTokens(amountIn, amountOutMin, path, msg.sender, deadline);
    }

    /**
     * @dev Swap ETH for tokens using Uniswap V2.
     * @param amountOutMin Minimum output amount of tokens.
     * @param path Token swap path (e.g., ETH -> Token).
     * @param deadline Transaction deadline (block timestamp).
     */
    function swapETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external payable {
        require(msg.value > 0, "Must send ETH to swap");
        require(path[0] == WETH_ADDRESS, "Path must start with WETH");
        
        // Perform the swap on Uniswap
        router.swapExactETHForTokens{value: msg.value}(amountOutMin, path, msg.sender, deadline);
    }

    /**
     * @dev Swap tokens for ETH using Uniswap V2.
     * @param amountIn Amount of tokens to swap.
     * @param amountOutMin Minimum output amount of ETH.
     * @param path Token swap path (e.g., Token -> ETH).
     * @param deadline Transaction deadline (block timestamp).
     */
    function swapTokensForETH(
        uint256 amountIn,
        uint256 amountOutMin,
        address[] calldata path,
        uint256 deadline
    ) external {
        require(amountIn > 0, "Amount in must be greater than zero");
        require(path[path.length - 1] == WETH_ADDRESS, "Path must end with WETH");
        
        // Perform the swap on Uniswap
        router.swapExactTokensForETH(amountIn, amountOutMin, path, msg.sender, deadline);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {
        // Accept ETH deposits
    }

    /**
     * @dev Withdraw accidentally sent ETH or ERC20 tokens.
     * @param token Address of the token to withdraw (use address(0) for ETH).
     * @param to Address to send the funds to.
     * @param amount Amount of funds to withdraw.
     */
    function withdrawFunds(address token, address to, uint256 amount) external {
        require(to != address(0), "Invalid recipient address");
        require(amount > 0, "Amount must be greater than zero");
        
        if (token == address(0)) {
            // Withdraw ETH
            payable(to).transfer(amount);
        } else {
            // Withdraw ERC20 tokens
            IERC20(token).transfer(to, amount);
        }
    }
}

interface IERC20 {
    function transfer(address to, uint256 value) external returns (bool);
}
```
