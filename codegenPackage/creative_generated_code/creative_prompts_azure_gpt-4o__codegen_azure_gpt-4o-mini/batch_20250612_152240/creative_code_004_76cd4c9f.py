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

// Interface for the ERC20 token standard
interface IERC20 {
    function transfer(address recipient, uint256 amount) external returns (bool);
    function balanceOf(address account) external view returns (uint256);
}

contract SlothAirdrop {
    IERC20 public slothToken; // Instance of the $SLOTH token
    address public owner; // Owner of the contract

    // Event emitted when tokens are airdropped
    event Airdrop(address indexed recipient, uint256 amount);

    // Constructor to initialize the contract with the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Token address cannot be zero");
        slothToken = IERC20(_tokenAddress);
        owner = msg.sender; // Set the contract deployer as the owner
    }

    // Modifier to restrict function to the owner
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    // Function to distribute airdropped tokens
    // @param recipients: Array of wallet addresses to receive tokens
    // @param amounts: Array of amounts corresponding to each recipient
    function distributeAirdrop(address[] calldata recipients, uint256[] calldata amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts length mismatch");

        for (uint256 i = 0; i < recipients.length; i++) {
            require(recipients[i] != address(0), "Recipient address cannot be zero");
            require(amounts[i] > 0, "Amount must be greater than zero");

            // Check if the contract has enough balance to perform the transfer
            uint256 balance = slothToken.balanceOf(address(this));
            require(balance >= amounts[i], "Insufficient contract balance");

            // Transfer tokens to the recipient
            bool success = slothToken.transfer(recipients[i], amounts[i]);
            require(success, "Transfer failed");

            // Emit an event for the airdrop
            emit Airdrop(recipients[i], amounts[i]);
        }
    }

    // Function to withdraw any remaining tokens from the contract
    // Only the owner can call this function
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Amount must be greater than zero");
        uint256 balance = slothToken.balanceOf(address(this));
        require(balance >= amount, "Insufficient contract balance");

        bool success = slothToken.transfer(owner, amount);
        require(success, "Withdrawal failed");
    }
}
```
