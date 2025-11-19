"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mantanetwork-network.github.io
Prompt: Generate an example of a smart contract that leverages Manta Network's secure infrastructure for a decentralized exchange.
Generated: DETERMINISTIC_a9bbe9a22fb896a9
Batch ID: 20250612_163135
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the Manta Network's secure infrastructure
interface IMantaNetwork {
    function deposit(address token, uint256 amount) external returns (bool);
    function withdraw(address token, uint256 amount) external returns (bool);
}

/**
 * @title DecentralizedExchange
 * @dev A smart contract for a simple decentralized exchange leveraging Manta Network.
 */
contract DecentralizedExchange is Ownable {
    using SafeMath for uint256;

    IMantaNetwork public mantaNetwork;

    // Event emitted when a trade is executed
    event TradeExecuted(address indexed seller, address indexed buyer, address indexed token, uint256 amount, uint256 price);

    // Mapping to store approved tokens
    mapping(address => bool) public approvedTokens;

    /**
     * @dev Constructor to set the Manta Network contract address.
     * @param _mantaNetwork Address of the Manta Network contract.
     */
    constructor(address _mantaNetwork) {
        mantaNetwork = IMantaNetwork(_mantaNetwork);
    }

    /**
     * @dev Approves a token for trading on the exchange.
     * @param token Address of the token to be approved.
     */
    function approveToken(address token) external onlyOwner {
        approvedTokens[token] = true;
    }

    /**
     * @dev Executes a trade on the decentralized exchange.
     * @param token Address of the ERC20 token.
     * @param amount Amount of tokens to be traded.
     * @param price Price per token in the transaction.
     */
    function executeTrade(address token, uint256 amount, uint256 price) external {
        require(approvedTokens[token], "Token not approved for trading");
        require(IERC20(token).balanceOf(msg.sender) >= amount, "Insufficient token balance");

        // Deposit tokens into Manta Network for secure handling
        require(IERC20(token).approve(address(mantaNetwork), amount), "Approval failed");
        require(mantaNetwork.deposit(token, amount), "Deposit to Manta Network failed");

        // Logic for handling the trade (e.g., updating state, transferring tokens)
        // For simplicity, we just emit an event here
        emit TradeExecuted(msg.sender, address(this), token, amount, price);
    }

    /**
     * @dev Withdraws tokens from the Manta Network.
     * @param token Address of the token to withdraw.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(mantaNetwork.withdraw(token, amount), "Withdrawal from Manta Network failed");
    }
}
```
