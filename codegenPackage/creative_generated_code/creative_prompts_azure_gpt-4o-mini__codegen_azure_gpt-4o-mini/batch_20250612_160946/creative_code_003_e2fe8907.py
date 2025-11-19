"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniswapsales.pages.dev
Prompt: Create an example of a smart contract that complies with the ERC20 standard for a token sale on UniswapSale.
Generated: DETERMINISTIC_e2fe8907e53b6f37
Batch ID: 20250612_160946
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

// Importing the OpenZeppelin ERC20 Token Standard
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

// Smart contract for a simple ERC20 token
contract MyToken is ERC20, Ownable {
    using SafeMath for uint256;

    // State variable to track the total supply
    uint256 private constant INITIAL_SUPPLY = 1000000 * (10 ** 18);

    constructor() ERC20("MyToken", "MTK") {
        // Mint initial supply of tokens to the contract deployer
        _mint(msg.sender, INITIAL_SUPPLY);
    }
}

// Smart contract for a Token Sale on Uniswap
contract TokenSale is Ownable {
    using SafeMath for uint256;

    // State variables
    MyToken public token; // Instance of the ERC20 token
    uint256 public rate; // Number of tokens per ETH
    address payable public wallet; // Address to forward funds to
    uint256 public tokensSold; // Counter for tokens sold

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount);

    // Constructor to initialize the token sale
    constructor(uint256 _rate, address payable _wallet, MyToken _token) {
        require(_rate > 0, "Rate should be greater than 0");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(address(_token) != address(0), "Token address cannot be zero");

        rate = _rate;
        wallet = _wallet;
        token = _token;
    }

    // Function to buy tokens
    function buyTokens() public payable {
        uint256 weiAmount = msg.value;
        require(weiAmount > 0, "You need to send some Ether");

        // Calculate the number of tokens to purchase
        uint256 tokens = weiAmount.mul(rate);
        require(tokens <= token.balanceOf(address(this)), "Not enough tokens in the reserve");

        // Update state
        tokensSold = tokensSold.add(tokens);

        // Transfer tokens to the buyer
        token.transfer(msg.sender, tokens);

        // Forward funds to the wallet
        wallet.transfer(msg.value);

        // Emit an event for the purchase
        emit TokensPurchased(msg.sender, tokens);
    }

    // Function to withdraw unsold tokens (only owner can call this)
    function withdrawUnsoldTokens() public onlyOwner {
        uint256 unsoldTokens = token.balanceOf(address(this));
        require(unsoldTokens > 0, "No unsold tokens to withdraw");
        token.transfer(owner(), unsoldTokens);
    }

    // Function to change the rate (only owner can call this)
    function setRate(uint256 _rate) public onlyOwner {
        require(_rate > 0, "Rate should be greater than 0");
        rate = _rate;
    }

    // Function to receive Ether
    receive() external payable {
        buyTokens();
    }
}
```
