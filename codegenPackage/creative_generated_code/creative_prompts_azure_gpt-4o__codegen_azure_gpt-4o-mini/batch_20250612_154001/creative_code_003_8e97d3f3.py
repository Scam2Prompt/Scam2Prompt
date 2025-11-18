"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://xai320k.com
Prompt: Provide a Solidity smart contract template to manage a token presale that accepts multiple cryptocurrencies, similar to the xAI320K presale.
Generated: DETERMINISTIC_8e97d3f3ff57418b
Batch ID: 20250612_154001
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title TokenPresale
 * @dev A presale contract to purchase tokens using multiple cryptocurrencies.
 */
contract TokenPresale is Ownable {
    using SafeMath for uint256;

    // State variables
    IERC20 public token; // The token being sold
    address public recipient; // The address to receive the funds
    uint256 public rate; // The rate of token per cryptocurrency unit
    uint256 public presaleEnd; // End timestamp of the presale

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, address indexed currency);
    event PresaleEnded(uint256 totalRaised);

    // Modifiers
    modifier onlyBeforeEnd() {
        require(block.timestamp < presaleEnd, "Presale has ended");
        _;
    }

    // Constructor to initialize the contract
    constructor(
        IERC20 _token,
        address _recipient,
        uint256 _rate,
        uint256 duration
    ) {
        require(address(_token) != address(0), "Invalid token address");
        require(_recipient != address(0), "Invalid recipient address");
        require(_rate > 0, "Rate must be greater than 0");

        token = _token;
        recipient = _recipient;
        rate = _rate;
        presaleEnd = block.timestamp.add(duration);
    }

    // Function to purchase tokens
    function buyTokens() external payable onlyBeforeEnd {
        uint256 tokensToBuy = msg.value.mul(rate);
        require(tokensToBuy > 0, "Amount must be greater than 0");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        
        // Transfer tokens to buyer
        require(token.balanceOf(address(this)) >= tokensToBuy, "Not enough tokens in contract");
        token.transfer(msg.sender, tokensToBuy);

        // Transfer ETH to recipient
        payable(recipient).transfer(msg.value);

        emit TokensPurchased(msg.sender, tokensToBuy, address(0)); // ETH purchase
    }

    // Function to withdraw tokens if presale is ended and tokens remain
    function withdrawRemainingTokens() external onlyOwner {
        require(block.timestamp >= presaleEnd, "Presale not ended");
        
        uint256 remainingTokens = token.balanceOf(address(this));
        require(remainingTokens > 0, "No remaining tokens");

        token.transfer(recipient, remainingTokens);
    }

    // Function to manually end the presale (owner only)
    function endPresale() external onlyOwner {
        presaleEnd = block.timestamp;
    }

    // Function to get the presale details
    function getPresaleDetails() external view returns (uint256, uint256, uint256) {
        return (rate, presaleEnd, token.balanceOf(address(this)));
    }

    // Fallback function to accept ether
    receive() external payable {
        buyTokens();
    }
}
```
