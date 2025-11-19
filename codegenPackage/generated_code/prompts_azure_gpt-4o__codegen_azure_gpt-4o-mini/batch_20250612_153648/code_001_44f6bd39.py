"""
Generated Code Metadata:
========================
Original URL: https://paseceoooveceee.pages.dev
Prompt: Create a smart contract in Solidity for managing the pre-sale of the Portal gaming coin, including features like token distribution and wallet connection.
Generated: DETERMINISTIC_44f6bd39b21f18b5
Batch ID: 20250612_153648
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

// Importing OpenZeppelin's ERC20 and Ownable contracts for token functionality and ownership management
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// PortalCoin is the ERC20 token for the Portal gaming coin
contract PortalCoin is ERC20, Ownable {
    // Constructor to initialize the token with a name and symbol
    constructor() ERC20("PortalCoin", "PORTAL") {
        // Mint initial supply to the contract owner
        _mint(msg.sender, 1000000 * 10 ** decimals()); // 1 million tokens
    }
}

// Presale contract to manage the pre-sale of PortalCoin
contract PortalPresale is Ownable {
    // Instance of the PortalCoin token
    PortalCoin public token;

    // Presale parameters
    uint256 public presalePrice; // Price per token in wei
    uint256 public tokensSold; // Total tokens sold during the presale
    uint256 public maxTokens; // Maximum tokens available for sale
    bool public presaleActive; // Status of the presale

    // Event to log token purchases
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the presale contract with the token and parameters
    constructor(PortalCoin _token, uint256 _presalePrice, uint256 _maxTokens) {
        token = _token;
        presalePrice = _presalePrice;
        maxTokens = _maxTokens;
        presaleActive = false; // Presale is initially inactive
    }

    // Modifier to check if presale is active
    modifier whenPresaleActive() {
        require(presaleActive, "Presale is not active");
        _;
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        presaleActive = true;
    }

    // Function to stop the presale
    function stopPresale() external onlyOwner {
        presaleActive = false;
    }

    // Function to purchase tokens during the presale
    function buyTokens(uint256 _amount) external payable whenPresaleActive {
        require(msg.value == _amount * presalePrice, "Incorrect Ether value sent");
        require(tokensSold + _amount <= maxTokens, "Not enough tokens available");

        // Update the total tokens sold
        tokensSold += _amount;

        // Transfer tokens to the buyer
        token.transfer(msg.sender, _amount);

        // Emit the purchase event
        emit TokensPurchased(msg.sender, _amount);
    }

    // Function to withdraw Ether from the contract
    function withdraw() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to set a new presale price
    function setPresalePrice(uint256 _newPrice) external onlyOwner {
        presalePrice = _newPrice;
    }

    // Function to set a new maximum token limit
    function setMaxTokens(uint256 _newMax) external onlyOwner {
        maxTokens = _newMax;
    }

    // Fallback function to prevent accidental Ether transfers
    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
