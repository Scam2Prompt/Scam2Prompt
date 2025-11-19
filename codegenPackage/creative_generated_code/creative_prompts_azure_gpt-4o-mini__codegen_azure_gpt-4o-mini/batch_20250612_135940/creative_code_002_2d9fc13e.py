"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://freeairdropcrypto.com
Prompt: Provide a code example for a smart contract that facilitates the distribution of tokens for the DEFLECT Protocol airdrop.
Generated: DETERMINISTIC_2d9fc13e2f0dc7d6
Batch ID: 20250612_135940
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

// Import the ERC20 interface
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title DeflectAirdrop
 * @dev Smart contract for distributing tokens for the DEFLECT Protocol airdrop
 */
contract DeflectAirdrop is Ownable {
    using SafeMath for uint256;

    // Token to be airdropped
    IERC20 public token;

    // Mapping to track which addresses have received tokens
    mapping(address => bool) public hasClaimed;

    // Event emitted when tokens are airdropped
    event AirdropClaimed(address indexed recipient, uint256 amount);

    /**
     * @dev Constructor to initialize the token contract
     * @param _tokenAddress The address of the token to be distributed
     */
    constructor(address _tokenAddress) {
        require(_tokenAddress != address(0), "Invalid token address");
        token = IERC20(_tokenAddress);
    }

    /**
     * @dev Function to airdrop tokens to a list of addresses
     * @param recipients Array of addresses to receive tokens
     * @param amounts Array of amounts corresponding to each recipient
     */
    function airdropTokens(address[] memory recipients, uint256[] memory amounts) external onlyOwner {
        require(recipients.length == amounts.length, "Recipients and amounts must match");
        
        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            uint256 amount = amounts[i];

            // Check if the recipient has already claimed tokens
            require(!hasClaimed[recipient], "Recipient has already claimed tokens");
            require(amount > 0, "Amount must be greater than zero");
            require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

            // Mark as claimed
            hasClaimed[recipient] = true;

            // Transfer tokens to recipient
            token.transfer(recipient, amount);

            // Emit airdrop event
            emit AirdropClaimed(recipient, amount);
        }
    }

    /**
     * @dev Function to withdraw remaining tokens in the contract
     * @param to Address to withdraw tokens to
     * @param amount Amount of tokens to withdraw
     */
    function withdrawTokens(address to, uint256 amount) external onlyOwner {
        require(to != address(0), "Invalid withdrawal address");
        require(token.balanceOf(address(this)) >= amount, "Insufficient contract balance");

        // Transfer tokens to owner
        token.transfer(to, amount);
    }

    /**
     * @dev Function to check the balance of the contract
     * @return Balance of the contract in the token
     */
    function contractBalance() external view returns (uint256) {
        return token.balanceOf(address(this));
    }
}
```
