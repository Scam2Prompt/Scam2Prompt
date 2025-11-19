"""
Generated Code Metadata:
========================
Original URL: https://presale-astraworld.pages.dev
Prompt: Generate a smart contract code in Solidity for a token sale platform that allows users to buy tokens at a discounted price before the public launch, similar to the $RVV token presale.
Generated: DETERMINISTIC_14ec5e14ec7b614b
Batch ID: 20250622_204752
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

// Importing OpenZeppelin's ERC20 token implementation
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Token contract
contract MyToken is ERC20, Ownable {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}

// Token Sale contract
contract TokenSale is Ownable {
    using SafeMath for uint256;

    // The token being sold
    MyToken public token;

    // Address where funds are collected
    address payable public wallet;

    // How many tokens a buyer gets per wei
    uint256 public rate;

    // Amount of wei raised
    uint256 public weiRaised;

    // Sale parameters
    uint256 public openingTime;
    uint256 public closingTime;
    bool public isFinalized = false;

    // Events
    event TokensPurchased(address indexed purchaser, address indexed beneficiary, uint256 value, uint256 amount);

    // Modifier to check if the sale is open
    modifier onlyWhileOpen {
        require(block.timestamp >= openingTime && block.timestamp <= closingTime, "TokenSale: Sale is not open");
        _;
    }

    // Constructor to initialize the token sale
    constructor(uint256 _rate, address payable _wallet, MyToken _token, uint256 _openingTime, uint256 _closingTime) {
        require(_rate > 0, "TokenSale: Rate is 0");
        require(_wallet != address(0), "TokenSale: Wallet is the zero address");
        require(address(_token) != address(0), "TokenSale: Token is the zero address");
        require(_openingTime >= block.timestamp, "TokenSale: Opening time is before current time");
        require(_closingTime > _openingTime, "TokenSale: Closing time is before opening time");

        rate = _rate;
        wallet = _wallet;
        token = _token;
        openingTime = _openingTime;
        closingTime = _closingTime;
    }

    // Fallback function to buy tokens
    receive() external payable {
        buyTokens(msg.sender);
    }

    // Function to buy tokens
    function buyTokens(address beneficiary) public payable onlyWhileOpen {
        uint256 weiAmount = msg.value;
        require(beneficiary != address(0), "TokenSale: Beneficiary is the zero address");
        require(weiAmount != 0, "TokenSale: Wei amount is 0");

        // Calculate token amount to be created
        uint256 tokens = weiAmount.mul(rate);

        // Update state
        weiRaised = weiRaised.add(weiAmount);

        // Transfer tokens to the beneficiary
        token.transfer(beneficiary, tokens);

        // Emit an event
        emit TokensPurchased(msg.sender, beneficiary, weiAmount, tokens);

        // Forward funds to the wallet
        wallet.transfer(msg.value);
    }

    // Function to finalize the sale
    function finalize() public onlyOwner {
        require(!isFinalized, "TokenSale: Sale is already finalized");
        require(block.timestamp > closingTime, "TokenSale: Sale is not yet closed");

        isFinalized = true;
    }

    // Function to withdraw unsold tokens
    function withdrawUnsoldTokens() public onlyOwner {
        require(isFinalized, "TokenSale: Sale is not finalized");
        uint256 unsoldTokens = token.balanceOf(address(this));
        token.transfer(owner(), unsoldTokens);
    }
}
```
