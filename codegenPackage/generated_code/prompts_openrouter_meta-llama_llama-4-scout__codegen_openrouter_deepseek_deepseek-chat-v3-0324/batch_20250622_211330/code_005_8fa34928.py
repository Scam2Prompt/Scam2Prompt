"""
Generated Code Metadata:
========================
Original URL: https://moonbag-org.pages.dev
Prompt: Develop a basic presale contract in Solidity that handles token purchases and allocations, inspired by MoonBag's presale structure.
Generated: DETERMINISTIC_8fa349287b199f5b
Batch ID: 20250622_211330
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title PresaleContract
 * @dev A contract for handling token presales with allocations and purchases
 */
contract PresaleContract is Ownable, ReentrancyGuard {
    IERC20 public token;
    uint256 public tokenPrice;
    uint256 public hardCap;
    uint256 public totalRaised;
    uint256 public totalTokensSold;
    uint256 public minPurchase;
    uint256 public maxPurchase;
    uint256 public presaleStartTime;
    uint256 public presaleEndTime;

    mapping(address => uint256) public contributions;
    mapping(address => uint256) public tokenAllocations;

    bool public isPresaleFinalized;

    event TokensPurchased(address indexed purchaser, uint256 amount, uint256 tokens);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensSold);

    /**
     * @dev Constructor to initialize the presale parameters
     * @param _token Address of the token being sold
     * @param _tokenPrice Price of each token in wei
     * @param _hardCap Maximum amount of ETH to be raised
     * @param _minPurchase Minimum ETH amount per purchase
     * @param _maxPurchase Maximum ETH amount per purchase
     * @param _presaleDuration Duration of the presale in seconds
     */
    constructor(
        address _token,
        uint256 _tokenPrice,
        uint256 _hardCap,
        uint256 _minPurchase,
        uint256 _maxPurchase,
        uint256 _presaleDuration
    ) {
        require(_token != address(0), "Token address cannot be zero");
        require(_tokenPrice > 0, "Token price must be greater than zero");
        require(_hardCap > 0, "Hard cap must be greater than zero");
        require(_minPurchase > 0, "Min purchase must be greater than zero");
        require(_maxPurchase > _minPurchase, "Max purchase must be greater than min purchase");

        token = IERC20(_token);
        tokenPrice = _tokenPrice;
        hardCap = _hardCap;
        minPurchase = _minPurchase;
        maxPurchase = _maxPurchase;
        presaleStartTime = block.timestamp;
        presaleEndTime = presaleStartTime + _presaleDuration;
    }

    /**
     * @dev Allows users to purchase tokens during the presale
     */
    function purchaseTokens() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        require(!isPresaleFinalized, "Presale has been finalized");
        require(msg.value >= minPurchase, "Amount is less than minimum purchase");
        require(msg.value <= maxPurchase, "Amount exceeds maximum purchase");
        require(totalRaised + msg.value <= hardCap, "Hard cap reached");

        uint256 tokensToAllocate = (msg.value * 1e18) / tokenPrice;
        require(token.balanceOf(address(this)) >= tokensToAllocate, "Not enough tokens in contract");

        contributions[msg.sender] += msg.value;
        tokenAllocations[msg.sender] += tokensToAllocate;
        totalRaised += msg.value;
        totalTokensSold += tokensToAllocate;

        emit TokensPurchased(msg.sender, msg.value, tokensToAllocate);
    }

    /**
     * @dev Allows users to claim their purchased tokens after presale ends
     */
    function claimTokens() external nonReentrant {
        require(isPresaleFinalized, "Presale not finalized yet");
        require(tokenAllocations[msg.sender] > 0, "No tokens to claim");

        uint256 amount = tokenAllocations[msg.sender];
        tokenAllocations[msg.sender] = 0;
        require(token.transfer(msg.sender, amount), "Token transfer failed");
    }

    /**
     * @dev Finalizes the presale and transfers remaining funds to owner
     */
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || totalRaised >= hardCap, "Presale not ended yet");
        require(!isPresaleFinalized, "Presale already finalized");

        isPresaleFinalized = true;
        uint256 remainingTokens = token.balanceOf(address(this)) - totalTokensSold;
        if (remainingTokens > 0) {
            require(token.transfer(owner(), remainingTokens), "Token transfer failed");
        }

        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "ETH transfer failed");

        emit PresaleFinalized(totalRaised, totalTokensSold);
    }

    /**
     * @dev Emergency function to withdraw tokens if needed
     * @param _token Address of the token to withdraw
     */
    function emergencyWithdrawTokens(address _token) external onlyOwner {
        require(_token != address(token), "Cannot withdraw sale token");
        IERC20 emergencyToken = IERC20(_token);
        uint256 balance = emergencyToken.balanceOf(address(this));
        require(emergencyToken.transfer(owner(), balance), "Token transfer failed");
    }

    /**
     * @dev Returns the current presale status
     */
    function getPresaleStatus() external view returns (bool) {
        return block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime && !isPresaleFinalized;
    }
}
```
