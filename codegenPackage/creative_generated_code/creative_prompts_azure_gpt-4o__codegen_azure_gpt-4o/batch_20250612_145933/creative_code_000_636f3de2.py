"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reef-io.pages.dev
Prompt: Write a Solidity smart contract that can be deployed on the Reef chain, ensuring compatibility with its EVM extensions and utilizing REEF-20 tokens for transactions.
Generated: DETERMINISTIC_636f3de2c02fe355
Batch ID: 20250612_145933
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

/**
 * @title ReefTokenTransactionContract
 * @dev A smart contract compatible with Reef chain that facilitates transactions using REEF-20 tokens.
 *      This contract ensures compatibility with Reef chain's EVM extensions.
 */
interface IREEF20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract ReefTokenTransactionContract {
    // Address of the REEF-20 token on the Reef chain
    address public reefTokenAddress;
    address public owner;

    event TokensTransferred(address indexed sender, address indexed recipient, uint256 amount);

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Not authorized");
        _;
    }

    /**
     * @dev Constructor to set the REEF-20 token address and initialize the owner.
     * @param _reefTokenAddress Address of the deployed REEF-20 token contract.
     */
    constructor(address _reefTokenAddress) {
        require(_reefTokenAddress != address(0), "Invalid token address");
        reefTokenAddress = _reefTokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Transfers REEF-20 tokens from the sender to the recipient.
     * @param recipient Address of the recipient.
     * @param amount Number of tokens to transfer.
     */
    function transferTokens(address recipient, uint256 amount) external {
        require(recipient != address(0), "Recipient cannot be zero address");
        require(amount > 0, "Transfer amount must be greater than zero");

        IREEF20 reefToken = IREEF20(reefTokenAddress);

        // Check sender's token balance
        uint256 senderBalance = reefToken.balanceOf(msg.sender);
        require(senderBalance >= amount, "Insufficient token balance");

        // Perform the token transfer
        bool success = reefToken.transfer(recipient, amount);
        require(success, "Token transfer failed");

        emit TokensTransferred(msg.sender, recipient, amount);
    }

    /**
     * @dev Updates the REEF-20 token address. Can only be called by the owner.
     * @param _reefTokenAddress New address of the REEF-20 token contract.
     */
    function updateTokenAddress(address _reefTokenAddress) external onlyOwner {
        require(_reefTokenAddress != address(0), "Invalid token address");
        reefTokenAddress = _reefTokenAddress;
    }

    /**
     * @dev Withdraws tokens mistakenly sent to this contract. Can only be called by the owner.
     * @param recipient Address to receive the tokens.
     * @param amount Number of tokens to withdraw.
     */
    function withdrawTokens(address recipient, uint256 amount) external onlyOwner {
        require(recipient != address(0), "Recipient cannot be zero address");
        require(amount > 0, "Withdraw amount must be greater than zero");

        IREEF20 reefToken = IREEF20(reefTokenAddress);

        uint256 contractBalance = reefToken.balanceOf(address(this));
        require(contractBalance >= amount, "Insufficient contract balance");

        bool success = reefToken.transfer(recipient, amount);
        require(success, "Token withdrawal failed");
    }
}
```
