"""
Generated Code Metadata:
========================
Original URL: https://sugarglidercoin.vercel.app
Prompt: Generate a smart contract code for an airdrop event similar to Sugar Glider's $SGDR drop on Solana.
Generated: DETERMINISTIC_b3c08bc9825e5f6a
Batch ID: 20250622_210802
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

/**
 * @title Airdrop Smart Contract
 * @dev This contract facilitates an airdrop event for distributing tokens to eligible recipients.
 */
contract Airdrop {
    // Address of the token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are successfully airdropped
    event TokensAirdropped(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address and set the owner.
     * @param _tokenAddress Address of the token contract to be used for the airdrop.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to airdrop tokens to multiple recipients.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function airdropTokens(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Call the token contract to transfer tokens
            (bool success, bytes memory data) = tokenAddress.call(
                abi.encodeWithSignature("transfer(address,uint256)", recipients[i], amounts[i])
            );

            require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");

            emit TokensAirdropped(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to update the token address (owner-only).
     * @param _newTokenAddress New token contract address.
     */
    function updateTokenAddress(address _newTokenAddress) external onlyOwner {
        require(_newTokenAddress != address(0), "Invalid token address");
        tokenAddress = _newTokenAddress;
    }

    /**
     * @dev Function to transfer ownership of the contract to a new owner.
     * @param _newOwner Address of the new owner.
     */
    function transferOwnership(address _newOwner) external onlyOwner {
        require(_newOwner != address(0), "Invalid new owner address");
        owner = _newOwner;
    }
}
```

This code is a production-ready smart contract for an airdrop event on Ethereum. It uses Solidity and follows best practices, including error handling, proper commenting, and modular design.
