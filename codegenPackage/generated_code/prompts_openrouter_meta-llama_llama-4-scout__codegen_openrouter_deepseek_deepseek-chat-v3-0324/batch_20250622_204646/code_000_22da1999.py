"""
Generated Code Metadata:
========================
Original URL: https://bnbfour-meme.pages.dev
Prompt: Generate a simple smart contract in Solidity for a token sale platform similar to the one described for $FOUR on the Four website.
Generated: DETERMINISTIC_22da19994aaabe4b
Batch ID: 20250622_204646
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

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract FourTokenSale is Ownable {
    using SafeMath for uint256;

    // Token being sold
    ERC20 public token;

    // Sale parameters
    uint256 public rate; // tokens per ETH
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public saleEndTime;

    // Whitelist functionality
    mapping(address => bool) public whitelist;

    // Track investor contributions
    mapping(address => uint256) public contributions;

    // Events
    event TokensPurchased(address indexed purchaser, uint256 value, uint256 amount);
    event WhitelistUpdated(address indexed account, bool isWhitelisted);
    event SaleExtended(uint256 newEndTime);
    event SaleFinalized(uint256 totalRaised);

    /**
     * @dev Constructor
     * @param _token Address of the token being sold
     * @param _rate Number of tokens per ETH
     * @param _minPurchase Minimum ETH purchase amount
     * @param _maxPurchase Maximum ETH purchase amount per address
     * @param _hardCap Maximum ETH to be raised
     * @param _saleDuration Duration of the sale in seconds
     */
    constructor(
        ERC20 _token,
        uint256 _rate,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _hardCap,
        uint256 _saleDuration
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_rate > 0, "Rate cannot be zero");
        require(_minPurchase > 0, "Min purchase cannot be zero");
        require(_maxPurchase > _minPurchase, "Max purchase must be greater than min");
        require(_hardCap > 0, "Hard cap cannot be zero");

        token = _token;
        rate = _rate;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        hardCap = _hardCap;
        saleEndTime = block.timestamp.add(_saleDuration);
    }

    /**
     * @dev Fallback function to buy tokens
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Buy tokens with ETH
     */
    function buyTokens() public payable {
        require(block.timestamp <= saleEndTime, "Sale has ended");
        require(whitelist[msg.sender], "Address not whitelisted");
        require(msg.value >= minPurchase, "Amount below minimum purchase");
        require(contributions[msg.sender].add(msg.value) <= maxPurchase, "Exceeds max purchase limit");
        require(totalRaised.add(msg.value) <= hardCap, "Hard cap reached");

        uint256 tokens = msg.value.mul(rate);
        require(token.balanceOf(address(this)) >= tokens, "Insufficient token balance");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalRaised = totalRaised.add(msg.value);

        token.transfer(msg.sender, tokens);
        emit TokensPurchased(msg.sender, msg.value, tokens);
    }

    /**
     * @dev Add address to whitelist
     * @param _address Address to add
     */
    function addToWhitelist(address _address) external onlyOwner {
        whitelist[_address] = true;
        emit WhitelistUpdated(_address, true);
    }

    /**
     * @dev Add multiple addresses to whitelist
     * @param _addresses Array of addresses to add
     */
    function addManyToWhitelist(address[] calldata _addresses) external onlyOwner {
        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_addresses[i]] = true;
            emit WhitelistUpdated(_addresses[i], true);
        }
    }

    /**
     * @dev Remove address from whitelist
     * @param _address Address to remove
     */
    function removeFromWhitelist(address _address) external onlyOwner {
        whitelist[_address] = false;
        emit WhitelistUpdated(_address, false);
    }

    /**
     * @dev Extend sale duration
     * @param _newEndTime New end time (timestamp)
     */
    function extendSale(uint256 _newEndTime) external onlyOwner {
        require(_newEndTime > saleEndTime, "New end time must be after current end time");
        saleEndTime = _newEndTime;
        emit SaleExtended(_newEndTime);
    }

    /**
     * @dev Withdraw ETH raised
     */
    function withdraw() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale has not ended");
        payable(owner()).transfer(address(this).balance);
        emit SaleFinalized(totalRaised);
    }

    /**
     * @dev Withdraw unsold tokens
     */
    function withdrawUnsoldTokens() external onlyOwner {
        require(block.timestamp > saleEndTime, "Sale has not ended");
        uint256 unsold = token.balanceOf(address(this));
        token.transfer(owner(), unsold);
    }
}
```
