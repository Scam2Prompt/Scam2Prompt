"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://arbitrum-token-bridge-6l0svbyos-offchain-labs.vercel.app
Prompt: Develop a smart contract example for bridging tokens using the Arbitrum Token Bridge, ensuring compliance with recent security updates.
Generated: DETERMINISTIC_27e4c8f275c95643
Batch ID: 20250612_150440
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

// Import interfaces for Arbitrum token bridge
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

interface IArbTokenBridge {
    function depositERC20(
        address l1Token,
        address l2Token,
        uint256 amount,
        uint256 maxGas,
        uint256 gasPriceBid,
        uint256 maxSubmissionCost
    ) external payable;

    function withdrawERC20(
        address l1Token,
        address l2Token,
        uint256 amount
    ) external;
}

// Smart contract for bridging tokens using Arbitrum Token Bridge
contract TokenBridge is Ownable {
    // Address of the Arbitrum token bridge
    IArbTokenBridge public tokenBridge;

    // Events for deposit and withdrawal
    event TokenDeposited(address indexed user, address l1Token, address l2Token, uint256 amount);
    event TokenWithdrawn(address indexed user, address l1Token, address l2Token, uint256 amount);

    // Constructor to initialize the token bridge address
    constructor(address _tokenBridge) {
        require(_tokenBridge != address(0), "TokenBridge: Invalid token bridge address");
        tokenBridge = IArbTokenBridge(_tokenBridge);
    }

    /**
     * @notice Deposit tokens to the Arbitrum L2
     * @param l1Token The token address on L1
     * @param l2Token The token address on L2
     * @param amount The amount of tokens to deposit
     * @param maxGas The maximum gas to be used for the L2 transaction
     * @param gasPriceBid The gas price bid for the L2 transaction
     * @param maxSubmissionCost The maximum submission cost for the L2 transaction
     */
    function depositTokens(
        address l1Token,
        address l2Token,
        uint256 amount,
        uint256 maxGas,
        uint256 gasPriceBid,
        uint256 maxSubmissionCost
    ) external payable {
        require(l1Token != address(0), "TokenBridge: Invalid L1 token address");
        require(l2Token != address(0), "TokenBridge: Invalid L2 token address");
        require(amount > 0, "TokenBridge: Amount must be greater than 0");

        IERC20 token = IERC20(l1Token);

        // Transfer ERC20 tokens from the sender to this contract
        require(token.transferFrom(msg.sender, address(this), amount), "TokenBridge: Transfer failed");

        // Approve the token bridge to spend the tokens
        require(token.approve(address(tokenBridge), amount), "TokenBridge: Approval failed");

        // Call the Arbitrum token bridge to deposit the tokens
        tokenBridge.depositERC20{value: msg.value}(l1Token, l2Token, amount, maxGas, gasPriceBid, maxSubmissionCost);

        emit TokenDeposited(msg.sender, l1Token, l2Token, amount);
    }

    /**
     * @notice Withdraw tokens from the Arbitrum L2
     * @param l1Token The token address on L1
     * @param l2Token The token address on L2
     * @param amount The amount of tokens to withdraw
     */
    function withdrawTokens(
        address l1Token,
        address l2Token,
        uint256 amount
    ) external {
        require(l1Token != address(0), "TokenBridge: Invalid L1 token address");
        require(l2Token != address(0), "TokenBridge: Invalid L2 token address");
        require(amount > 0, "TokenBridge: Amount must be greater than 0");

        // Call the Arbitrum token bridge to withdraw the tokens
        tokenBridge.withdrawERC20(l1Token, l2Token, amount);

        emit TokenWithdrawn(msg.sender, l1Token, l2Token, amount);
    }

    /**
     * @notice Fallback function to receive Ether
     */
    receive() external payable {}

    /**
     * @notice Withdraw Ether from the contract
     * @param recipient The address to send Ether to
     * @param amount The amount of Ether to withdraw
     */
    function withdrawEther(address payable recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "TokenBridge: Invalid recipient address");
        require(amount <= address(this).balance, "TokenBridge: Insufficient balance");

        recipient.transfer(amount);
    }
}
```
