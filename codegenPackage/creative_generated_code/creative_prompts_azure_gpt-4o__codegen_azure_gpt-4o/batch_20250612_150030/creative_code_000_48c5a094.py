"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eth-usdc.xyz
Prompt: Write a smart contract in Solidity that facilitates the exchange of ETH for USDC using a decentralized finance protocol.
Generated: DETERMINISTIC_48c5a09461afafce
Batch ID: 20250612_150030
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.17;

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function swapExactETHForTokens(
        uint256 amountOutMin,
        address[] calldata path,
        address to,
        uint256 deadline
    ) external payable returns (uint256[] memory amounts);
}

contract ETHToUSDCExchange {
    // Address of the Uniswap V2 Router on the Ethereum mainnet
    address private constant UNISWAP_V2_ROUTER = 0xE592427A0AEce92De3Edee1F18E0157C05861564;

    // Address of the USDC token on Ethereum (ERC20 token)
    address private constant USDC_TOKEN = 0xA0b86991c6218b36c1d19D4a2e9Eb0CE3606eb48;

    IUniswapV2Router private uniswapRouter;

    event TokensSwapped(address indexed user, uint256 ethAmount, uint256 usdcAmount);

    constructor() {
        // Initialize the Uniswap Router interface
        uniswapRouter = IUniswapV2Router(UNISWAP_V2_ROUTER);
    }

    /**
     * @notice This function accepts ETH and swaps it for USDC
     * @param amountOutMin The minimum amount of USDC expected to receive (slippage tolerance)
     * @param deadline The deadline timestamp by which the swap must occur
     */
    function swapETHForUSDC(uint256 amountOutMin, uint256 deadline) external payable {
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Build the token swap path (ETH -> USDC)
        address[] memory path = new address[](2);
        path[0] = uniswapRouter.WETH(); // Wrapped ETH address
        path[1] = USDC_TOKEN;

        // Execute the swap
        uint256[] memory amounts = uniswapRouter.swapExactETHForTokens{value: msg.value}(
            amountOutMin,             // Minimum amount of USDC to receive
            path,                     // Token path
            msg.sender,               // Recipient of USDC
            deadline                  // Deadline
        );

        // Emit an event to record the swap
        emit TokensSwapped(msg.sender, msg.value, amounts[1]);
    }

    /**
     * @notice Fallback function to receive ETH
     */
    receive() external payable {}

    /**
     * @notice Allows the contract owner to withdraw any accidentally sent ETH
     */
    function withdrawETH() external {
        // Transfer any remaining ETH in contract to the owner
        payable(msg.sender).transfer(address(this).balance);
    }
}
```
