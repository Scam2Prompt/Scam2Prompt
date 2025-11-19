"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ktest-296.pages.dev
Prompt: Explain how to implement a presale mechanism for a cryptocurrency token, referencing a cap of 5,000 ETH and a total supply of 100,000,000 KSI.
Generated: DETERMINISTIC_9a18d0d6a65d24d6
Batch ID: 20250612_161617
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

// Import OpenZeppelin contracts for safety and security
import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract KSIPresale is Ownable {
    using SafeMath for uint256;

    // Define state variables
    uint256 public constant TOTAL_SUPPLY = 100000000 * 10**18; // Total supply of 100 million KSI with 18 decimals
    uint256 public constant ETH_CAP = 5000 ether; // Presale cap of 5,000 ETH
    uint256 public tokensSold; // Total tokens sold during presale
    uint256 public tokenPrice; // Price of KSI in ETH
    bool public presaleActive; // Status of the presale
    ERC20 public ksiToken; // KSI token contract reference

    // Event to log token purchase
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 cost);

    // Constructor to initialize the KSI token and presale parameters
    constructor(ERC20 _ksiToken, uint256 _tokenPrice) {
        require(_ksiToken != ERC20(address(0)), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than zero");

        ksiToken = _ksiToken;
        tokenPrice = _tokenPrice;
        presaleActive = false; // Presale is initially inactive
    }

    // Function to start the presale
    function startPresale() external onlyOwner {
        require(!presaleActive, "Presale already active");
        presaleActive = true;
    }

    // Function to end the presale
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale not active");
        presaleActive = false;
    }

    // Function to purchase tokens during the presale
    function purchaseTokens(uint256 _amount) external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value == _amount.mul(tokenPrice), "Incorrect ETH amount sent");
        require(tokensSold.add(_amount) <= TOTAL_SUPPLY, "Not enough tokens left");
        require(address(this).balance <= ETH_CAP, "ETH cap reached");

        // Update state variables
        tokensSold = tokensSold.add(_amount);

        // Transfer KSI tokens to the buyer
        require(ksiToken.transfer(msg.sender, _amount), "Token transfer failed");

        // Emit event for the purchase
        emit TokensPurchased(msg.sender, _amount, msg.value);
    }

    // Function to withdraw ETH from the contract to the owner
    function withdraw() external onlyOwner {
        require(address(this).balance > 0, "No ETH to withdraw");
        payable(owner()).transfer(address(this).balance);
    }

    // Function to withdraw unsold tokens after presale ends
    function withdrawUnsoldTokens() external onlyOwner {
        require(!presaleActive, "Cannot withdraw tokens while presale is active");
        uint256 unsoldTokens = TOTAL_SUPPLY.sub(tokensSold);
        require(unsoldTokens > 0, "No unsold tokens to withdraw");

        // Transfer unsold tokens back to the owner
        require(ksiToken.transfer(owner(), unsoldTokens), "Token transfer failed");
    }
}
```
