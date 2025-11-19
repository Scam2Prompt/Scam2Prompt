"""
Generated Code Metadata:
========================
Original URL: https://godcandle404-en.web.app
Prompt: Design an ERC721 NFT contract that provides holders with a 37.77% MEV revenue share, similar to God Candle's OG NFT.
Generated: DETERMINISTIC_238ed1886fdf478b
Batch ID: 20250622_205709
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

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract MEVRevenueShareNFT is ERC721, Ownable, ReentrancyGuard {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    uint256 public constant MAX_SUPPLY = 777;
    uint256 public constant REVENUE_SHARE_PERCENT = 3777; // 37.77% in basis points
    uint256 public constant BASIS_POINTS = 10000;
    
    address public revenueToken;
    uint256 public totalRevenueDistributed;
    mapping(uint256 => uint256) public lastClaimedAt;
    mapping(uint256 => uint256) public accumulatedRevenuePerToken;

    event RevenueDeposited(address indexed depositor, uint256 amount);
    event RevenueClaimed(address indexed claimant, uint256 tokenId, uint256 amount);

    constructor(
        string memory name,
        string memory symbol,
        address _revenueToken
    ) ERC721(name, symbol) {
        revenueToken = _revenueToken;
    }

    function safeMint(address to) external onlyOwner {
        require(_tokenIdCounter.current() < MAX_SUPPLY, "Max supply reached");
        _tokenIdCounter.increment();
        uint256 tokenId = _tokenIdCounter.current();
        _safeMint(to, tokenId);
    }

    function depositRevenue(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(totalSupply() > 0, "No tokens minted yet");

        IERC20 token = IERC20(revenueToken);
        require(token.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        uint256 perTokenShare = (amount * REVENUE_SHARE_PERCENT) / (totalSupply() * BASIS_POINTS);
        accumulatedRevenuePerToken[_tokenIdCounter.current()] += perTokenShare;
        totalRevenueDistributed += amount;

        emit RevenueDeposited(msg.sender, amount);
    }

    function claimRevenue(uint256 tokenId) external nonReentrant {
        require(ownerOf(tokenId) == msg.sender, "Not token owner");
        
        uint256 claimable = getClaimableRevenue(tokenId);
        require(claimable > 0, "No revenue to claim");

        lastClaimedAt[tokenId] = _tokenIdCounter.current();
        
        IERC20 token = IERC20(revenueToken);
        require(token.transfer(msg.sender, claimable), "Transfer failed");

        emit RevenueClaimed(msg.sender, tokenId, claimable);
    }

    function getClaimableRevenue(uint256 tokenId) public view returns (uint256) {
        if (_tokenIdCounter.current() <= lastClaimedAt[tokenId]) {
            return 0;
        }
        return accumulatedRevenuePerToken[_tokenIdCounter.current()] - accumulatedRevenuePerToken[lastClaimedAt[tokenId]];
    }

    function totalSupply() public view returns (uint256) {
        return _tokenIdCounter.current();
    }

    function withdrawExcessFunds(address recipient) external onlyOwner {
        IERC20 token = IERC20(revenueToken);
        uint256 balance = token.balanceOf(address(this));
        uint256 reserved = totalRevenueDistributed * REVENUE_SHARE_PERCENT / BASIS_POINTS;
        require(balance > reserved, "No excess funds");

        uint256 excess = balance - reserved;
        require(token.transfer(recipient, excess), "Transfer failed");
    }
}
```
