"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bafybeigknes33h76f7skpeenkp5p5s74x65rjrgymqbdmpd2i3kufhzxqe.ipfs.dweb.link
Prompt: Write a function in Solidity to distribute airdropped tokens named "$SLOTH" to multiple wallet addresses based on predefined criteria.
Generated: DETERMINISTIC_76cd4c9fb7f7629e
Batch ID: 20250612_152240
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
 * @title SlothTokenAirdrop
 * @dev Contract to distribute $SLOTH tokens to multiple wallet addresses.
 */
contract SlothTokenAirdrop {
    IERC20 public slothToken; // Interface for the $SLOTH token
    address public owner; // Owner of the contract

    // Events
    event AirdropCompleted(address indexed recipient, uint256 amount);
    event OwnershipTransferred(address indexed oldOwner, address indexed newOwner);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with $SLOTH token address.
     * @param _tokenAddress Address of the $SLOTH token contract.
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        slothToken = IERC20(_tokenAddress);
        owner = msg.sender;
    }

    /**
     * @dev Function to distribute tokens to multiple addresses based on predefined criteria.
     * @param recipients List of wallet addresses to receive the airdrop.
     * @param amounts List of token amounts corresponding to each recipient.
     */
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");
        require(recipients.length > 0, "No recipients provided");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Invalid recipient address");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Transfer $SLOTH tokens to the recipient
            require(slothToken.transfer(recipients[i], amounts[i]), "Token transfer failed");
            
            // Emit event for successful airdrop
            emit AirdropCompleted(recipients[i], amounts[i]);
        }
    }

    /**
     * @dev Function to transfer ownership of the contract.
     * @param newOwner Address of the new owner.
     */
    function transferOwnership(address newOwner) external onlyOwner {
        require(newOwner != address(0), "New owner cannot be the zero address");
        emit OwnershipTransferred(owner, newOwner);
        owner = newOwner;
    }

    /**
     * @dev Function to withdraw tokens from the contract in case of accidental deposit.
     * @param amount Amount of tokens to withdraw.
     */
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        require(slothToken.transfer(owner, amount), "Token withdrawal failed");
    }
}

/**
 * @dev Minimal IERC20 interface for token interactions.
 */
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
}
```
