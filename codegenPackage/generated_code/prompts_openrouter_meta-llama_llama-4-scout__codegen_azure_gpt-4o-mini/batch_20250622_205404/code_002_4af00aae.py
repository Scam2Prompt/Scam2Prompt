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

// Importing the ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Airdrop contract for distributing tokens to eligible holders
contract TokenAirdrop is Ownable {
    // The token to be airdropped
    IERC20 public token;

    // Mapping to track if an address has already claimed their airdrop
    mapping(address => bool) public hasClaimed;

    // Event to log successful airdrop claims
    event AirdropClaimed(address indexed recipient, uint256 amount);

    // Constructor to set the token address
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    // Function to airdrop tokens to a list of addresses
    function airdropTokens(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Amount must be greater than zero");
        require(token.balanceOf(address(this)) >= recipients.length * amount, "Insufficient contract balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            // Ensure the recipient has not claimed their tokens yet
            require(!hasClaimed[recipient], "Recipient has already claimed");

            // Mark the recipient as having claimed
            hasClaimed[recipient] = true;

            // Transfer the tokens to the recipient
            token.transfer(recipient, amount);
            emit AirdropClaimed(recipient, amount);
        }
    }

    // Function to withdraw any tokens accidentally sent to the contract
    function withdrawTokens(address _tokenAddress, uint256 _amount) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        IERC20(_tokenAddress).transfer(msg.sender, _amount);
    }

    // Function to check the contract's token balance
    function contractTokenBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
