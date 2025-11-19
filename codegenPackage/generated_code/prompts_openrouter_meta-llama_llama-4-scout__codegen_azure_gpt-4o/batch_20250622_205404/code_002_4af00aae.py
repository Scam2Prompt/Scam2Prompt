"""
Generated Code Metadata:
========================
Original URL: https://claim-simoncat.pages.dev
Prompt: Generate a smart contract code snippet in Solidity for a token airdrop similar to the one described for $FLOKI holders and Simon's Cat Token.
Generated: DETERMINISTIC_4af00aaebad56bd0
Batch ID: 20250622_205404
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
 * @title TokenAirdrop
 * @dev A smart contract for distributing tokens to eligible holders.
 */
contract TokenAirdrop {
    // Address of the token contract
    address public tokenAddress;

    // Owner of the contract
    address public owner;

    // Event emitted when tokens are airdropped
    event AirdropExecuted(address indexed recipient, uint256 amount);

    // Modifier to restrict access to owner-only functions
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with the token address.
     * @param _tokenAddress Address of the token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to execute the airdrop.
     * @param recipients Array of recipient addresses.
     * @param amounts Array of token amounts corresponding to each recipient.
     */
    function executeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Invalid token amount");

            // Transfer tokens to the recipient
            (bool success, bytes memory data) = tokenAddress.call(
                abi.encodeWithSignature("transfer(address,uint256)", recipients[i], amounts[i])
            );

            require(success && (data.length == 0 || abi.decode(data, (bool))), "Token transfer failed");

            emit AirdropExecuted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to update the token address.
     * @param _tokenAddress New token address.
     */
    function updateTokenAddress(address _tokenAddress) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        tokenAddress = _tokenAddress;
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "Invalid new owner address");
        owner = newOwner;
    }
}
```
