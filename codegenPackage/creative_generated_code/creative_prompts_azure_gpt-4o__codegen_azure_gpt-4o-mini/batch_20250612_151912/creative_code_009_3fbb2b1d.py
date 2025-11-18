"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eosgas.io
Prompt: Write a Solidity smart contract for distributing eosGAS tokens during an airdrop program, ensuring compliance with KYC requirements as mentioned on the website.
Generated: DETERMINISTIC_3fbb2b1d34e97129
Batch ID: 20250612_151912
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

// Importing necessary OpenZeppelin libraries
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for distributing eosGAS tokens during an airdrop
contract EosGASAirdrop is Ownable {
    using SafeMath for uint256;

    // The eosGAS token contract
    IERC20 public eosGASToken;

    // Address to store KYC data
    mapping(address => bool) public kycRegistered;

    // Event to log the airdrop distribution
    event AirdropDistributed(address indexed recipient, uint256 amount);

    // Constructor to set the eosGAS token contract address
    constructor(address _eosGASToken) {
        require(_eosGASToken != address(0), "Invalid token address");
        eosGASToken = IERC20(_eosGASToken);
    }

    // Function to register KYC
    function registerKYC(address _user) external onlyOwner {
        require(_user != address(0), "Invalid user address");
        kycRegistered[_user] = true;
    }

    // Function to distribute eosGAS tokens to KYC registered users
    function distributeAirdrop(address[] calldata recipients, uint256 amount) external onlyOwner {
        require(recipients.length > 0, "No recipients provided");
        require(amount > 0, "Invalid amount");

        uint256 totalAmount = amount.mul(recipients.length);
        require(eosGASToken.balanceOf(address(this)) >= totalAmount, "Insufficient contract balance");

        for (uint256 i = 0; i < recipients.length; i++) {
            address recipient = recipients[i];
            require(kycRegistered[recipient], "Recipient not KYC registered");
            
            // Transfer eosGAS tokens to the recipient
            eosGASToken.transfer(recipient, amount);
            emit AirdropDistributed(recipient, amount);
        }
    }

    // Function to withdraw tokens from the contract in case of emergency
    function withdrawTokens(uint256 amount) external onlyOwner {
        require(amount > 0, "Invalid amount");
        require(eosGASToken.balanceOf(address(this)) >= amount, "Insufficient balance");
        
        eosGASToken.transfer(owner(), amount);
    }

    // Function to check KYC registration status
    function isKYCRegistered(address user) external view returns (bool) {
        return kycRegistered[user];
    }
}
```
