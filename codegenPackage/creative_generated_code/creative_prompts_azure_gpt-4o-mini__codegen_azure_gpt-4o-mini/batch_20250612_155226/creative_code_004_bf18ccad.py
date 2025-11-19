"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbidoge.pages.dev
Prompt: What are the steps to deploy a meme token on the Arbitrum Layer 2 network, similar to Arbidoge, including liquidity management?
Generated: DETERMINISTIC_bf18ccadd96aa3b6
Batch ID: 20250612_155226
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

// Importing necessary OpenZeppelin contracts for ERC20 token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// MemeToken contract definition
contract MemeToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Event emitted when liquidity is added
    event LiquidityAdded(uint256 tokenAmount, uint256 ethAmount);

    // Constructor to initialize the token with name and symbol
    constructor() ERC20("MemeToken", "MEME") {
        // Mint an initial supply of tokens to the deployer
        _mint(msg.sender, 1000000 * (10 ** decimals())); // Mint 1 million tokens
    }

    // Function to add liquidity to a liquidity pool
    // Only callable by the owner of the token
    function addLiquidity(uint256 tokenAmount) external payable onlyOwner {
        require(tokenAmount > 0, "Token amount must be greater than zero");
        require(msg.value > 0, "ETH amount must be greater than zero");

        // Transfer the specified amount of tokens to the contract
        _transfer(msg.sender, address(this), tokenAmount);

        // Emit an event for liquidity addition
        emit LiquidityAdded(tokenAmount, msg.value);
    }

    // Function to withdraw ETH from the contract
    // Only callable by the owner
    function withdrawETH() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No ETH available for withdrawal");

        // Send the balance to the owner
        payable(msg.sender).transfer(balance);
    }

    // Function to withdraw tokens from the contract
    // Only callable by the owner
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Token amount must be greater than zero");
        require(balanceOf(address(this)) >= amount, "Insufficient token balance");

        // Transfer tokens to the owner
        _transfer(address(this), msg.sender, amount);
    }
}

// Interface for the Uniswap V2 Router
interface IUniswapV2Router {
    function addLiquidityETH(
        address token,
        uint256 tokenAmount,
        uint256 minTokenAmount,
        uint256 minETHAmount,
        address to,
        uint256 deadline
    ) external payable returns (uint256 amountToken, uint256 amountETH, uint256 liquidity);
}

// Deploying the MemeToken and adding liquidity function
contract MemeTokenDeployer {
    address public memeTokenAddress;
    IUniswapV2Router public uniswapRouter;

    // Constructor to initialize the Uniswap router address
    constructor(address _router) {
        uniswapRouter = IUniswapV2Router(_router);
    }

    // Function to deploy the MemeToken and add liquidity
    function deployAndAddLiquidity() external payable {
        // Deploy the token
        MemeToken memeToken = new MemeToken();
        memeTokenAddress = address(memeToken);

        // Approve the token for the router
        memeToken.approve(address(uniswapRouter), type(uint256).max);

        // Add liquidity to the Uniswap pool
        uniswapRouter.addLiquidityETH{value: msg.value}(
            memeTokenAddress,
            memeToken.balanceOf(address(memeToken)),
            0, // Accept any amount of tokens
            0, // Accept any amount of ETH
            msg.sender,
            block.timestamp
        );
    }

    // Fallback function to receive ETH
    receive() external payable {}
}
```
