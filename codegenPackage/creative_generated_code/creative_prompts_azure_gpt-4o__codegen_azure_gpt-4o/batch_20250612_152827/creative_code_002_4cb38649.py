"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://gameswap-org.web.app
Prompt: Implement a DeFi-powered smart order routing system for trading gaming NFTs on a decentralized exchange, using GameSwap's approach with ERC20 tokens and stablecoins.
Generated: DETERMINISTIC_4cb38649cd71136d
Batch ID: 20250612_152827
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Certainly. Below is the clean, production-ready Solidity code implementing the requested functionality.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Importing OpenZeppelin's ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Interface for GameSwap's decentralized exchange
interface IGameSwap {
    function swapTokens(
        address tokenIn,
        address tokenOut,
        uint256 amountIn,
        uint256 amountOutMin,
        address to
    ) external returns (uint256);

    function getSwapRate(address tokenIn, address tokenOut, uint256 amountIn) external view returns (uint256);
}

contract NFTOrderRouting {
    // Owner of the contract
    address public owner;

    // Address of the GameSwap decentralized exchange
    IGameSwap public gameSwap;

    // Events for logging key activities
    event TokensSwapped(
        address indexed user,
        address indexed tokenIn,
        address indexed tokenOut,
        uint256 amountIn,
        uint256 amountOut
    );
    event StablecoinPurchased(
        address indexed user,
        uint256 stablecoinAmount,
        uint256 nftPrice
    );

    // Modifiers for access control
    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract
     * @param _gameSwap Address of the GameSwap DEX contract
     */
    constructor(address _gameSwap) {
        require(_gameSwap != address(0), "Invalid GameSwap address");
        owner = msg.sender;
        gameSwap = IGameSwap(_gameSwap);
    }

    /**
     * @dev Transfers the ownership of the contract to another address
     * @param newOwner Address of the new owner
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be zero address");
        owner = newOwner;
    }

    /**
     * @dev Function to swap ERC20 tokens for stablecoins (e.g., USDC/USDT) to purchase NFTs
     * @param tokenIn Address of the token the user wants to swap (e.g., gaming ERC20 token)
     * @param stablecoin Address of the stablecoin (e.g., USDC/USDT)
     * @param amountIn Amount of tokenIn to swap
     * @param nftPrice Price of the gaming NFT in stablecoins
     */
    function routeOrderForNFT(
        address tokenIn,
        address stablecoin,
        uint256 amountIn,
        uint256 nftPrice
    ) external {
        require(tokenIn != address(0), "Invalid tokenIn address");
        require(stablecoin != address(0), "Invalid stablecoin address");
        require(amountIn > 0, "AmountIn must be greater than zero");
        require(nftPrice > 0, "NFT price must be greater than zero");

        // Transfer tokenIn from user to this contract
        IERC20(tokenIn).transferFrom(msg.sender, address(this), amountIn);

        // Approve GameSwap to spend the tokenIn
        IERC20(tokenIn).approve(address(gameSwap), amountIn);

        // Get the minimum output amount for the swap
        uint256 stablecoinAmountOut = gameSwap.getSwapRate(tokenIn, stablecoin, amountIn);
        require(stablecoinAmountOut >= nftPrice, "Insufficient stablecoin amount for NFT purchase");

        // Perform the token swap
        uint256 swappedStablecoinAmount = gameSwap.swapTokens(
            tokenIn,
            stablecoin,
            amountIn,
            nftPrice,
            msg.sender
        );

        // Emit events for logging
        emit TokensSwapped(msg.sender, tokenIn, stablecoin, amountIn, swappedStablecoinAmount);
        emit StablecoinPurchased(msg.sender, swappedStablecoinAmount, nftPrice);
    }

    /**
     * @dev Emergency withdrawal function for the contract owner
     * @param token Address of the token to withdraw
     * @param amount Amount of tokens to withdraw
     */
    function emergencyWithdraw(address token, uint256 amount) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the specified amount of tokens to the owner
        IERC20(token).transfer(owner, amount);
    }
}
```

### Key Notes:
1. Make sure to replace `IGameSwap` with the actual GameSwap interface if available.
2. Use appropriate library imports for deployment (e.g., OpenZeppelin for ERC20).
3. Ensure the GameSwap DEX smart contract is deployed and its address is correctly passed during deployment.
