"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://moonbag-claiming.pages.dev
Prompt: Create a Solidity function for a "BuyBack & Burn" event that uses a specified amount of funds to purchase tokens and remove them from circulation, following MoonBag's scarcity-driven value model.
Generated: DETERMINISTIC_acb62d0c1feefda2
Batch ID: 20250612_145625
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

// Import necessary interfaces for interacting with tokens
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
    function approve(address spender, uint256 amount) external returns (bool);
}

interface IUniswapV2Router {
    function swapExactETHForTokensSupportingFeeOnTransferTokens(
        uint amountOutMin,
        address[] calldata path,
        address to,
        uint deadline
    ) external payable;
}

contract BuyBackAndBurn {
    address public immutable token; // Address of the token to buy back and burn
    address public immutable uniswapRouter; // Address of the Uniswap V2 router contract
    address public owner; // Contract owner address

    event BuyBackAndBurnExecuted(uint256 ethSpent, uint256 tokensBurned);

    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    constructor(address _token, address _uniswapRouter) {
        require(_token != address(0), "Invalid token address");
        require(_uniswapRouter != address(0), "Invalid router address");
        token = _token;
        uniswapRouter = _uniswapRouter;
        owner = msg.sender;
    }

    // Function to execute the buyback and burn
    function buyBackAndBurn(uint256 minTokensOut) external payable onlyOwner {
        require(msg.value > 0, "No ETH sent for buyback");

        // Define the Uniswap trading pair path (ETH -> Token)
        address[] memory path = new address[](2);
        path[0] = address(0); // WETH address, usually replaced with a wrapped ETH token
        path[1] = token;

        uint256 initialTokenBalance = IERC20(token).balanceOf(address(this));

        // Execute the token purchase (swap ETH for tokens)
        IUniswapV2Router(uniswapRouter).swapExactETHForTokensSupportingFeeOnTransferTokens{value: msg.value}(
            minTokensOut,
            path,
            address(this),
            block.timestamp
        );

        uint256 tokensPurchased = IERC20(token).balanceOf(address(this)) - initialTokenBalance;
        require(tokensPurchased >= minTokensOut, "Insufficient tokens purchased");

        // Burn the tokens by transferring them to a burn address (e.g., 0x000...dEaD)
        address burnAddress = 0x000000000000000000000000000000000000dEaD;
        require(IERC20(token).transfer(burnAddress, tokensPurchased), "Token burn failed");

        emit BuyBackAndBurnExecuted(msg.value, tokensPurchased);
    }

    // Allow withdrawal of ETH in case of emergencies
    function emergencyWithdrawETH() external onlyOwner {
        payable(owner).transfer(address(this).balance);
    }

    // Allow the owner to withdraw any ERC20 tokens mistakenly sent to the contract
    function emergencyWithdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != token, "Cannot withdraw buyback token");
        IERC20(_tokenAddress).transfer(owner, _amount);
    }

    // Fallback function to accept ETH sent directly to the contract
    receive() external payable {}
}
```
