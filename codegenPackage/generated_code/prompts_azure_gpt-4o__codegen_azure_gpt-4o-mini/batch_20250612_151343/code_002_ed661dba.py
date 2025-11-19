"""
Generated Code Metadata:
========================
Original URL: https://bitcoindogeclaim.pages.dev
Prompt: Create a smart contract on Ethereum (ERC20) that facilitates the purchase of $0DOG tokens during the presale and ensures token transfer to a connected BRC20 wallet address.
Generated: DETERMINISTIC_ed661dba6e2b6fde
Batch ID: 20250612_151343
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

// Importing the OpenZeppelin ERC20 contract
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Smart contract for $0DOG token
contract DogToken is ERC20, Ownable {
    // Presale parameters
    uint256 public constant PRESALE_PRICE = 0.01 ether; // Price per token during presale
    uint256 public constant MAX_TOKENS = 1000000 * 10 ** decimals(); // Maximum tokens for presale
    uint256 public tokensSold; // Track the number of tokens sold during presale

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token
    constructor() ERC20("$0DOG", "DOG") {
        // Mint initial supply to the contract owner
        _mint(address(this), MAX_TOKENS);
    }

    // Function to purchase tokens during presale
    function purchaseTokens(uint256 _amount) external payable {
        // Ensure the presale is active and the amount is valid
        require(msg.value == _amount * PRESALE_PRICE, "Incorrect Ether value sent");
        require(tokensSold + _amount <= MAX_TOKENS, "Not enough tokens available");

        // Update the tokens sold
        tokensSold += _amount;

        // Transfer tokens to the buyer
        _transfer(address(this), msg.sender, _amount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract (only owner)
    function withdraw() external onlyOwner {
        // Transfer the contract's balance to the owner
        payable(owner()).transfer(address(this).balance);
    }

    // Function to allow the owner to mint additional tokens (if needed)
    function mintTokens(uint256 _amount) external onlyOwner {
        _mint(address(this), _amount);
    }

    // Function to check the contract's balance of Ether
    function getContractBalance() external view returns (uint256) {
        return address(this).balance;
    }
}
```
