"""
Generated Code Metadata:
========================
Original URL: https://casinotg.pages.dev
Prompt: Create a smart contract in Solidity for implementing TG.Casino's buy-back mechanism for `$TGC` tokens as described in the roadmap.
Generated: DETERMINISTIC_46c2d7eb5f1f7e0f
Batch ID: 20250612_150435
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/token/ERC20/SafeERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/math/SafeMath.sol";
import "https://github.com/OpenZeppelin/openzeppelin-solidity/contracts/ownership/Ownable.sol";

/**
 * @title TG.Casino Buy-Back Mechanism Smart Contract
 * @author [Your Name]
 * @notice This contract implements the buy-back mechanism for $TGC tokens as described in the TG.Casino roadmap.
 */
contract TGCasinoBuyBack {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Mapping of token addresses to their respective buy-back configurations
    mapping(address => BuyBackConfig) public buyBackConfigs;

    // Mapping of transaction hashes to their respective buy-back details
    mapping(bytes32 => BuyBackDetails) public buyBackDetails;

    // Event emitted when a buy-back transaction is executed
    event BuyBackExecuted(address indexed token, uint256 amount, uint256 burnedAmount);

    // Event emitted when a buy-back configuration is updated
    event BuyBackConfigUpdated(address indexed token, uint256 burnPercentage, address burnAddress);

    // Struct to represent a buy-back configuration
    struct BuyBackConfig {
        uint256 burnPercentage; // Percentage of tokens to burn
        address burnAddress; // Address to burn tokens
    }

    // Struct to represent a buy-back transaction
    struct BuyBackDetails {
        address token; // Address of the token being bought back
        uint256 amount; // Amount of tokens bought back
        uint256 burnedAmount; // Amount of tokens burned
    }

    // Address of the $TGC token
    address public constant TGC_TOKEN_ADDRESS = 0x...; // Replace with actual TGC token address

    // Address of the buy-back wallet
    address public constant BUY_BACK_WALLET = 0x...; // Replace with actual buy-back wallet address

    /**
     * @notice Initializes the contract with the $TGC token address and buy-back wallet address
     */
    constructor() public {
        // Initialize buy-back configuration for $TGC token
        buyBackConfigs[TGC_TOKEN_ADDRESS] = BuyBackConfig(10, 0x0000000000000000000000000000000000000000);
    }

    /**
     * @notice Updates the buy-back configuration for a given token
     * @param token Address of the token to update
     * @param burnPercentage New burn percentage
     * @param burnAddress New burn address
     */
    function updateBuyBackConfig(address token, uint256 burnPercentage, address burnAddress) public onlyOwner {
        buyBackConfigs[token] = BuyBackConfig(burnPercentage, burnAddress);
        emit BuyBackConfigUpdated(token, burnPercentage, burnAddress);
    }

    /**
     * @notice Executes a buy-back transaction for a given token
     * @param token Address of the token to buy back
     * @param amount Amount of tokens to buy back
     */
    function executeBuyBack(address token, uint256 amount) public {
        require(msg.sender == BUY_BACK_WALLET, "Only the buy-back wallet can execute buy-back transactions");

        // Get the buy-back configuration for the given token
        BuyBackConfig memory config = buyBackConfigs[token];

        // Calculate the amount of tokens to burn
        uint256 burnedAmount = amount.mul(config.burnPercentage).div(100);

        // Transfer tokens to the burn address
        IERC20(token).safeTransfer(config.burnAddress, burnedAmount);

        // Update the buy-back details
        bytes32 txHash = keccak256(abi.encodePacked(token, amount, burnedAmount));
        buyBackDetails[txHash] = BuyBackDetails(token, amount, burnedAmount);

        // Emit the buy-back executed event
        emit BuyBackExecuted(token, amount, burnedAmount);
    }

    /**
     * @notice Burns tokens on behalf of the contract
     * @param token Address of the token to burn
     * @param amount Amount of tokens to burn
     */
    function burnTokens(address token, uint256 amount) internal {
        // Transfer tokens to the zero address (effectively burning them)
        IERC20(token).safeTransfer(address(0), amount);
    }

    /**
     * @notice Getter function for the buy-back configuration of a given token
     * @param token Address of the token to retrieve the configuration for
     * @return BuyBackConfig The buy-back configuration for the given token
     */
    function getBuyBackConfig(address token) public view returns (BuyBackConfig memory) {
        return buyBackConfigs[token];
    }

    /**
     * @notice Getter function for the buy-back details of a given transaction
     * @param txHash Hash of the transaction to retrieve the details for
     * @return BuyBackDetails The buy-back details for the given transaction
     */
    function getBuyBackDetails(bytes32 txHash) public view returns (BuyBackDetails memory) {
        return buyBackDetails[txHash];
    }
}
```
