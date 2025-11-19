"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://btceftoken.pages.dev
Prompt: Provide an example of how to create a presale function in a smart contract for the Bitcoin ETF Token (BTCETF) that allows users to buy tokens using ETH or USDT.
Generated: DETERMINISTIC_33a12dcc7037ce43
Batch ID: 20250612_163848
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

// Importing OpenZeppelin's ERC20 contract for token functionality
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Define the BTCETF token contract inheriting from ERC20 and Ownable
contract BTCETF is ERC20, Ownable {
    // Presale settings
    uint256 public presalePrice; // Price per token in wei (for ETH)
    uint256 public totalSupplyPresale; // Total tokens available for presale
    uint256 public tokensSold; // Total tokens sold during the presale
    mapping(address => uint256) public contributions; // Track contributions of each address
    
    // Events for logging purposes
    event TokensPurchased(address indexed buyer, uint256 amount);
    
    // Constructor to initialize the token details and presale parameters
    constructor(uint256 _presalePrice, uint256 _totalSupplyPresale) ERC20("Bitcoin ETF Token", "BTCETF") {
        presalePrice = _presalePrice; // Set the presale price
        totalSupplyPresale = _totalSupplyPresale; // Set total supply for presale
        _mint(address(this), totalSupplyPresale); // Mint tokens to the contract address
    }

    // Function to purchase tokens during the presale using ETH
    function buyWithETH(uint256 _amount) external payable {
        require(msg.value == _amount * presalePrice, "Incorrect ETH amount sent");
        require(tokensSold + _amount <= totalSupplyPresale, "Not enough tokens available");
        
        tokensSold += _amount; // Update the total tokens sold
        contributions[msg.sender] += _amount; // Track tokens purchased by the buyer
        
        // Transfer the tokens to the buyer
        _transfer(address(this), msg.sender, _amount);
        
        emit TokensPurchased(msg.sender, _amount); // Emit purchase event
    }

    // Function to withdraw ETH from the contract (only callable by the owner)
    function withdrawETH() external onlyOwner {
        payable(owner()).transfer(address(this).balance);
    }

    // Function to buy tokens using USDT (assuming USDT is an ERC20 token)
    function buyWithUSDT(address _usdtContract, uint256 _amount) external {
        require(tokensSold + _amount <= totalSupplyPresale, "Not enough tokens available");

        // Transfer USDT from buyer to contract
        IERC20 usdt = IERC20(_usdtContract);
        require(usdt.transferFrom(msg.sender, address(this), _amount * presalePrice), "USDT transfer failed");
        
        tokensSold += _amount; // Update the total tokens sold
        contributions[msg.sender] += _amount; // Track tokens purchased by the buyer

        // Transfer the tokens to the buyer
        _transfer(address(this), msg.sender, _amount);
        
        emit TokensPurchased(msg.sender, _amount); // Emit purchase event
    }

    // Function to get the balance of tokens purchased by an address
    function getContribution(address _buyer) external view returns (uint256) {
        return contributions[_buyer];
    }
}

// Interface for the ERC20 token (USDT in this case)
interface IERC20 {
    function transferFrom(address sender, address recipient, uint256 amount) external returns (bool);
}
```
