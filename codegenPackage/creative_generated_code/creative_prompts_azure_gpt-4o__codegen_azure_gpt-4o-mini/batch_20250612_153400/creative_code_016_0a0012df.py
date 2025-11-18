"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://etfswap-ai.pages.dev
Prompt: Write a Solidity contract to enable swapping cryptocurrency with commodity ETFs (e.g., gold, silver, oil) on the ETFSwap platform.
Generated: DETERMINISTIC_0a0012dfdc2bf40c
Batch ID: 20250612_153400
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// ETFSwap contract to facilitate swapping between cryptocurrencies and commodity ETFs
contract ETFSwap is Ownable {
    // Define an interface for the ETF tokens
    struct ETF {
        address tokenAddress; // Address of the ETF token
        string name;          // Name of the ETF
        uint256 exchangeRate; // Conversion rate relative to cryptocurrency (scaled by 1e18 for precision)
    }

    // Mapping to store registered ETFs
    mapping(string => ETF) public etfs;

    // Event emitted after a successful swap
    event SwapExecuted(address indexed user, string etfName, uint256 cryptoAmount, uint256 etfAmount);

    // Modifier to check if the ETF exists
    modifier etfExists(string memory etfName) {
        require(etfs[etfName].tokenAddress != address(0), "ETF does not exist");
        _;
    }

    // Function to register a new ETF
    function registerETF(string memory etfName, address tokenAddress, uint256 exchangeRate) external onlyOwner {
        require(etfs[etfName].tokenAddress == address(0), "ETF already registered");
        require(exchangeRate > 0, "Exchange rate must be greater than zero");

        etfs[etfName] = ETF({
            tokenAddress: tokenAddress,
            name: etfName,
            exchangeRate: exchangeRate
        });
    }

    // Function to swap cryptocurrency for ETFs
    function swapForETF(string memory etfName, uint256 cryptoAmount) external etfExists(etfName) {
        ETF storage etf = etfs[etfName];

        // Calculate the amount of ETF tokens to be swapped
        uint256 etfAmount = (cryptoAmount * etf.exchangeRate) / 1e18;

        // Transfer the cryptocurrency from the user to the contract
        require(IERC20(msg.sender).transferFrom(msg.sender, address(this), cryptoAmount), "Crypto transfer failed");

        // Transfer the ETF tokens from the contract to the user
        require(IERC20(etf.tokenAddress).transfer(msg.sender, etfAmount), "ETF transfer failed");

        // Emit the SwapExecuted event
        emit SwapExecuted(msg.sender, etfName, cryptoAmount, etfAmount);
    }

    // Function to withdraw cryptocurrency from the contract (only owner)
    function withdrawCrypto(address tokenAddress, uint256 amount) external onlyOwner {
        require(IERC20(tokenAddress).transfer(msg.sender, amount), "Withdraw failed");
    }

    // Function to withdraw ETFs from the contract (only owner)
    function withdrawETF(string memory etfName, uint256 amount) external onlyOwner etfExists(etfName) {
        require(IERC20(etfs[etfName].tokenAddress).transfer(msg.sender, amount), "Withdraw failed");
    }
}
```
