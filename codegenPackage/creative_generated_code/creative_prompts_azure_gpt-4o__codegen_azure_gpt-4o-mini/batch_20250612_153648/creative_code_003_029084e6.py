"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-merlinstartercom.pages.dev
Prompt: Write a smart contract on MerlinChain that automates token swaps for $MP across multiple pools ($BTC, $M-BTC, $VOYA, $HUHU) based on predefined price thresholds.
Generated: DETERMINISTIC_029084e6698e28ae
Batch ID: 20250612_153648
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

// Import interfaces for token and pool contracts
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract TokenSwap {
    // State variables
    address public owner;
    IERC20 public mpToken;        // $MP token contract
    address public btcPool;       // Pool contract for $BTC
    address public mbtcPool;      // Pool contract for $M-BTC
    address public voyaPool;      // Pool contract for $VOYA
    address public huhuPool;      // Pool contract for $HUHU

    // Price thresholds for triggering swaps
    uint256 public btcThreshold;
    uint256 public mbtcThreshold;
    uint256 public voyaThreshold;
    uint256 public huhuThreshold;

    // Events
    event TokensSwapped(address indexed pool, uint256 amountIn, uint256 amountOut);

    // Modifier to restrict functions to only the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        address _mpToken,
        address _btcPool,
        address _mbtcPool,
        address _voyaPool,
        address _huhuPool,
        uint256 _btcThreshold,
        uint256 _mbtcThreshold,
        uint256 _voyaThreshold,
        uint256 _huhuThreshold
    ) {
        owner = msg.sender;
        mpToken = IERC20(_mpToken);
        btcPool = _btcPool;
        mbtcPool = _mbtcPool;
        voyaPool = _voyaPool;
        huhuPool = _huhuPool;

        btcThreshold = _btcThreshold;
        mbtcThreshold = _mbtcThreshold;
        voyaThreshold = _voyaThreshold;
        huhuThreshold = _huhuThreshold;
    }

    // Function to swap tokens based on price thresholds
    function swapTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(mpToken.balanceOf(address(this)) >= amount, "Insufficient $MP balance");

        // Check price conditions and execute swaps
        uint256 currentPrice = getCurrentPrice(); // Implement this as per your price feed integration

        if (currentPrice > btcThreshold) {
            // Swap $MP for $BTC
            _swap(mpToken, btcPool, amount);
        } else if (currentPrice > mbtcThreshold) {
            // Swap $MP for $M-BTC
            _swap(mpToken, mbtcPool, amount);
        } else if (currentPrice > voyaThreshold) {
            // Swap $MP for $VOYA
            _swap(mpToken, voyaPool, amount);
        } else if (currentPrice > huhuThreshold) {
            // Swap $MP for $HUHU
            _swap(mpToken, huhuPool, amount);
        }
    }

    // Internal function to handle the swap logic
    function _swap(IERC20 tokenIn, address pool, uint256 amount) internal {
        // Transfer $MP tokens to the swap pool
        require(tokenIn.transfer(pool, amount), "Token transfer failed");

        // Call the pool contract's swap function (assumes a swap function exists)
        // This function should be defined in your pool contract
        // (bool success, ) = pool.call(abi.encodeWithSignature("swap(address,uint256)", address(tokenIn), amount));
        // require(success, "Swap failed");

        emit TokensSwapped(pool, amount, amount); // Placeholder for actual amounts
    }

    // Function to set new thresholds (restricted to owner)
    function setThresholds(uint256 _btcThreshold, uint256 _mbtcThreshold, uint256 _voyaThreshold, uint256 _huhuThreshold) external onlyOwner {
        btcThreshold = _btcThreshold;
        mbtcThreshold = _mbtcThreshold;
        voyaThreshold = _voyaThreshold;
        huhuThreshold = _huhuThreshold;
    }

    // Fallback function to receive ETH (if needed)
    receive() external payable {}

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(IERC20 token, uint256 amount) external onlyOwner {
        require(token.balanceOf(address(this)) >= amount, "Insufficient balance");
        require(token.transfer(msg.sender, amount), "Transfer failed");
    }

    // Placeholder for getting current price
    function getCurrentPrice() internal view returns (uint256) {
        // Implement price fetching logic here (e.g., using Chainlink or another oracle)
        return 0; // Replace with actual price fetching
    }
}
```
