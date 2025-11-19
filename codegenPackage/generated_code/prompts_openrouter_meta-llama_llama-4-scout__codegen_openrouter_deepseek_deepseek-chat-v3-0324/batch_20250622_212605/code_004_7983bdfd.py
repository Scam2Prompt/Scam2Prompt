"""
Generated Code Metadata:
========================
Original URL: https://unisocks.fi
Prompt: Design a basic smart contract for managing the sale, purchase, and redemption of digital assets for physical goods, inspired by the Unisocks platform.
Generated: DETERMINISTIC_7983bdfd9b45d931
Batch ID: 20250622_212605
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
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract DigitalAssetForPhysicalGoods is ERC721, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 1000;
    uint256 public constant REDEMPTION_PERIOD = 30 days;
    uint256 public constant PRICE = 0.1 ether;
    
    uint256 public totalSupply;
    uint256 public redemptionStartTime;
    bool public redemptionActive;
    
    mapping(uint256 => bool) public redeemedTokens;
    mapping(address => uint256) public purchaseCount;
    
    event Purchased(address indexed buyer, uint256 tokenId);
    event Redeemed(address indexed redeemer, uint256 tokenId);
    event RedemptionStarted();
    event FundsWithdrawn(address indexed owner, uint256 amount);
    
    constructor() ERC721("DigitalAssetForPhysicalGoods", "DAPG") {
        redemptionActive = false;
    }
    
    function purchase(uint256 quantity) external payable nonReentrant {
        require(quantity > 0, "Quantity must be greater than 0");
        require(totalSupply + quantity <= MAX_SUPPLY, "Exceeds max supply");
        require(msg.value >= PRICE * quantity, "Insufficient payment");
        
        for (uint256 i = 0; i < quantity; i++) {
            uint256 tokenId = totalSupply + 1;
            _safeMint(msg.sender, tokenId);
            purchaseCount[msg.sender]++;
            totalSupply++;
            emit Purchased(msg.sender, tokenId);
        }
    }
    
    function redeem(uint256 tokenId) external nonReentrant {
        require(redemptionActive, "Redemption not active");
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        require(!redeemedTokens[tokenId], "Token already redeemed");
        require(block.timestamp <= redemptionStartTime + REDEMPTION_PERIOD, "Redemption period ended");
        
        redeemedTokens[tokenId] = true;
        _burn(tokenId);
        emit Redeemed(msg.sender, tokenId);
    }
    
    function startRedemption() external onlyOwner {
        require(!redemptionActive, "Redemption already active");
        redemptionActive = true;
        redemptionStartTime = block.timestamp;
        emit RedemptionStarted();
    }
    
    function withdrawFunds() external onlyOwner nonReentrant {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        
        (bool success, ) = owner().call{value: balance}("");
        require(success, "Withdrawal failed");
        emit FundsWithdrawn(owner(), balance);
    }
    
    function supportsInterface(bytes4 interfaceId) public view override(ERC721) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
```
