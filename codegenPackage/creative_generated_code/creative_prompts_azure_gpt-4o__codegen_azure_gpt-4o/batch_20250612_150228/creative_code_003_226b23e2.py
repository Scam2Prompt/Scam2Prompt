"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeiaoulkqm54mkpjy5t7idjlc2wxddyj7a4cpdrpi4reejwkd4gphke.ipfs.dweb.link
Prompt: Create a smart contract snippet in Solidity for listing $Gou tokens on Uniswap, ensuring compatibility with Ethereum wallets like MetaMask.
Generated: DETERMINISTIC_226b23e2d1f33afe
Batch ID: 20250612_150228
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

// Interface for Uniswap's Router
interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint amountTokenDesired,
        uint amountTokenMin,
        uint amountETHMin,
        address to,
        uint deadline
    )
        external
        payable
        returns (
            uint amountToken,
            uint amountETH,
            uint liquidity
        );
}

// Interface for ERC20 token
interface IERC20 {
    function approve(address spender, uint256 amount) external returns (bool);
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}

contract GouTokenListing {
    address public immutable gouToken; // Address of the $Gou token
    address public immutable uniswapRouter; // Address of the Uniswap V2 Router

    // Address of the contract deployer
    address public owner;

    // Event emitted when liquidity is successfully added
    event LiquidityAdded(uint amountToken, uint amountETH, uint liquidity);

    // Modifier to restrict access to the contract owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not contract owner");
        _;
    }

    // Constructor to initialize the contract
    constructor(address _gouToken, address _uniswapRouter) {
        gouToken = _gouToken;
        uniswapRouter = _uniswapRouter;
        owner = msg.sender; // Set the deployer as the owner
    }

    /**
     * @dev Adds liquidity to Uniswap using $Gou tokens and ETH.
     * @param _tokenAmount Desired amount of $Gou tokens to add to liquidity.
     * @param _ethAmount Desired amount of ETH to add to liquidity.
     * @param _tokenMin Minimum amount of $Gou tokens expected to be added to liquidity.
     * @param _ethMin Minimum amount of ETH expected to be added to liquidity.
     */
    function addLiquidity(
        uint256 _tokenAmount,
        uint256 _ethAmount,
        uint256 _tokenMin,
        uint256 _ethMin
    ) external payable onlyOwner {
        require(msg.value >= _ethAmount, "Insufficient ETH sent");

        // Transfer $Gou tokens from the owner to this contract
        IERC20(gouToken).transferFrom(msg.sender, address(this), _tokenAmount);

        // Approve Uniswap Router to spend $Gou tokens
        require(
            IERC20(gouToken).approve(uniswapRouter, _tokenAmount),
            "Token approval failed"
        );

        // Call Uniswap's addLiquidityETH function
        (uint amountToken, uint amountETH, uint liquidity) = IUniswapV2Router(
            uniswapRouter
        ).addLiquidityETH{value: _ethAmount}(
            gouToken,
            _tokenAmount,
            _tokenMin,
            _ethMin,
            msg.sender,
            block.timestamp + 300 // Deadline set to 5 minutes from now
        );

        // Emit event for successful liquidity addition
        emit LiquidityAdded(amountToken, amountETH, liquidity);
    }

    /**
     * @dev Fallback function to accept ETH deposits.
     */
    receive() external payable {}

    /**
     * @dev Withdraw any accidentally sent ETH to the contract.
     */
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Withdraw any accidentally sent $Gou tokens to the contract.
     */
    function withdrawTokens() external onlyOwner {
        uint256 tokenBalance = IERC20(gouToken).balanceOf(address(this));
        require(tokenBalance > 0, "No tokens to withdraw");
        require(
            IERC20(gouToken).transfer(owner, tokenBalance),
            "Token transfer failed"
        );
    }
}
```
