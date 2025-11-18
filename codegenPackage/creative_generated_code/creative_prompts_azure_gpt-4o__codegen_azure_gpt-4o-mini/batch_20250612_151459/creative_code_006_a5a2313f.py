"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://blickchainloginn-usa.godaddysites.com
Prompt: Create a smart contract in Solidity that facilitates secure cryptocurrency purchases, specifically for Bitcoin and Ethereum.
Generated: DETERMINISTIC_a5a2313f4894cc6f
Batch ID: 20250612_151459
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

// Importing ERC20 interface for token interactions
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

// Smart contract for facilitating secure cryptocurrency purchases
contract CryptoPurchase {
    // Event to log purchases
    event Purchase(address indexed buyer, uint256 amount, string currency);

    // Address of the accepted ERC20 tokens (Bitcoin and Ethereum in this context)
    address public bitcoinToken;
    address public ethereumToken;

    // Constructor to set the addresses of the tokens
    constructor(address _bitcoinToken, address _ethereumToken) {
        require(_bitcoinToken != address(0), "Invalid Bitcoin token address");
        require(_ethereumToken != address(0), "Invalid Ethereum token address");
        
        bitcoinToken = _bitcoinToken;
        ethereumToken = _ethereumToken;
    }

    // Function to purchase Bitcoin
    function purchaseBitcoin(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer Bitcoin tokens from buyer to contract
        IERC20(bitcoinToken).transferFrom(msg.sender, address(this), amount);

        // Emit purchase event
        emit Purchase(msg.sender, amount, "Bitcoin");
    }

    // Function to purchase Ethereum
    function purchaseEthereum(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");

        // Transfer Ethereum tokens from buyer to contract
        IERC20(ethereumToken).transferFrom(msg.sender, address(this), amount);

        // Emit purchase event
        emit Purchase(msg.sender, amount, "Ethereum");
    }

    // Function to withdraw tokens from the contract
    function withdrawTokens(address tokenAddress, uint256 amount) external {
        // Only allow the owner to withdraw tokens
        require(msg.sender == owner(), "Only the owner can withdraw tokens");
        require(amount > 0, "Amount must be greater than zero");

        // Transfer specified token amount to the owner
        IERC20(tokenAddress).transfer(msg.sender, amount);
    }

    // Fallback function to receive Ether payments, if needed
    receive() external payable {
        // Logic for receiving Ether can be implemented here if necessary
    }
    
    // Modifier to restrict access to the owner of the contract
    modifier onlyOwner() {
        require(msg.sender == owner(), "Caller is not the owner");
        _;
    }

    // Function to get the owner of the contract
    function owner() public view returns (address) {
        return address(this); // Set to contract address for demonstration; modify as needed
    }
}
```
