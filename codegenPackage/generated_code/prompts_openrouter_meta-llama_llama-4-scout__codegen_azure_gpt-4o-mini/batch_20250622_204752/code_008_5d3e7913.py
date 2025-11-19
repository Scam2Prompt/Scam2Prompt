"""
Generated Code Metadata:
========================
Original URL: https://validationdapp.pages.dev
Prompt: Design a smart contract that utilizes Multichain's zkRouter protocol for secure and private cross-chain transactions.
Generated: DETERMINISTIC_5d3e7913e7a75531
Batch ID: 20250622_204752
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

// Importing necessary interfaces and libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Interface for the zkRouter protocol
interface IzkRouter {
    function send(
        address token,
        uint256 amount,
        address recipient,
        bytes calldata proof
    ) external returns (bool);
}

// Smart contract for secure and private cross-chain transactions
contract CrossChainTransaction is Ownable {
    using SafeMath for uint256;

    // State variables
    IzkRouter public zkRouter; // Instance of the zkRouter protocol
    mapping(address => bool) public supportedTokens; // Supported tokens for cross-chain transactions

    // Events
    event TokenSupported(address indexed token);
    event TokenUnsupported(address indexed token);
    event TransactionExecuted(address indexed token, address indexed recipient, uint256 amount);

    // Constructor to set the zkRouter address
    constructor(address _zkRouter) {
        require(_zkRouter != address(0), "Invalid zkRouter address");
        zkRouter = IzkRouter(_zkRouter);
    }

    // Function to support a new token for cross-chain transactions
    function supportToken(address token) external onlyOwner {
        require(token != address(0), "Invalid token address");
        require(!supportedTokens[token], "Token already supported");
        supportedTokens[token] = true;
        emit TokenSupported(token);
    }

    // Function to remove support for a token
    function removeTokenSupport(address token) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        supportedTokens[token] = false;
        emit TokenUnsupported(token);
    }

    // Function to execute a cross-chain transaction
    function executeTransaction(
        address token,
        uint256 amount,
        address recipient,
        bytes calldata proof
    ) external {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer the token from the sender to this contract
        IERC20(token).transferFrom(msg.sender, address(this), amount);

        // Approve the zkRouter to spend the tokens
        IERC20(token).approve(address(zkRouter), amount);

        // Execute the transaction through the zkRouter
        bool success = zkRouter.send(token, amount, recipient, proof);
        require(success, "Transaction failed");

        emit TransactionExecuted(token, recipient, amount);
    }

    // Function to withdraw tokens from the contract (for emergency purposes)
    function withdrawTokens(address token, uint256 amount) external onlyOwner {
        require(supportedTokens[token], "Token not supported");
        require(amount > 0, "Amount must be greater than zero");
        require(IERC20(token).balanceOf(address(this)) >= amount, "Insufficient balance");

        // Transfer the tokens back to the owner
        IERC20(token).transfer(msg.sender, amount);
    }
}
```
