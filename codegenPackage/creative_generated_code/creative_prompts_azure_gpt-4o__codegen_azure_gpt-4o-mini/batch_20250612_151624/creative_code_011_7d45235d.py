"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://floki-reward.com
Prompt: Write a Solidity contract that enables users to convert multiple cryptocurrencies into fiat currency using Floki's prepaid card infrastructure.
Generated: DETERMINISTIC_7d45235dde090b40
Batch ID: 20250612_151624
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

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the Floki Prepaid Card infrastructure
interface IFlokiPrepaidCard {
    function convertToFiat(address user, uint256 amount, address token) external returns (bool);
}

// Contract for managing cryptocurrency to fiat conversion
contract CryptoToFiatConverter is Ownable {
    // Mapping to track the supported tokens
    mapping(address => bool) public supportedTokens;
    // Instance of the Floki Prepaid Card contract
    IFlokiPrepaidCard public flokiPrepaidCard;

    // Event to emit when a conversion occurs
    event ConvertedToFiat(address indexed user, address indexed token, uint256 amount);

    // Constructor to initialize the Floki Prepaid Card contract address
    constructor(address _flokiPrepaidCard) {
        require(_flokiPrepaidCard != address(0), "Invalid Floki Prepaid Card address");
        flokiPrepaidCard = IFlokiPrepaidCard(_flokiPrepaidCard);
    }

    // Function to add a supported token
    function addSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = true;
    }

    // Function to remove a supported token
    function removeSupportedToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        supportedTokens[token] = false;
    }

    // Function to convert cryptocurrency to fiat
    function convertToFiat(address token, uint256 amount) external {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer tokens from the user to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Call the Floki Prepaid Card contract to perform the conversion
        bool success = flokiPrepaidCard.convertToFiat(msg.sender, amount, token);
        require(success, "Conversion to fiat failed");

        // Emit an event for the conversion
        emit ConvertedToFiat(msg.sender, token, amount);
    }

    // Function to withdraw tokens from the contract (only owner)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
