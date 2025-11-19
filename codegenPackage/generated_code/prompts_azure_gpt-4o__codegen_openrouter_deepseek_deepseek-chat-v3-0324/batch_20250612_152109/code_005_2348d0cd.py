"""
Generated Code Metadata:
========================
Original URL: https://anyinumult.pages.dev
Prompt: Develop a decentralized application (DApp) that allows users to lock $AI tokens for a specified term and receive soulbound receipt tokens. Include features for calculating multipliers based on lock duration.
Generated: DETERMINISTIC_2348d0cdf042149d
Batch ID: 20250612_152109
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
import "@openzeppelin/contracts/utils/Counters.sol";

contract AITokenLocker is ERC721, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    IERC20 public aiToken;
    uint256 public constant MIN_LOCK_DURATION = 30 days;
    uint256 public constant MAX_LOCK_DURATION = 365 days;

    struct Lock {
        uint256 amount;
        uint256 unlockTime;
        uint256 lockTime;
        uint256 multiplier;
    }

    mapping(uint256 => Lock) public locks;
    mapping(address => uint256[]) public userLocks;

    event TokensLocked(
        address indexed user,
        uint256 indexed tokenId,
        uint256 amount,
        uint256 unlockTime,
        uint256 multiplier
    );
    event TokensUnlocked(
        address indexed user,
        uint256 indexed tokenId,
        uint256 amount
    );

    constructor(address _aiToken) ERC721("AI Lock Receipt", "AILR") {
        require(_aiToken != address(0), "Invalid token address");
        aiToken = IERC20(_aiToken);
    }

    function lockTokens(uint256 amount, uint256 duration) external {
        require(amount > 0, "Amount must be greater than 0");
        require(
            duration >= MIN_LOCK_DURATION && duration <= MAX_LOCK_DURATION,
            "Invalid lock duration"
        );

        uint256 multiplier = calculateMultiplier(duration);
        uint256 unlockTime = block.timestamp + duration;

        require(
            aiToken.transferFrom(msg.sender, address(this), amount),
            "Token transfer failed"
        );

        uint256 tokenId = _tokenIdCounter.current();
        _tokenIdCounter.increment();
        _safeMint(msg.sender, tokenId);

        locks[tokenId] = Lock({
            amount: amount,
            unlockTime: unlockTime,
            lockTime: block.timestamp,
            multiplier: multiplier
        });

        userLocks[msg.sender].push(tokenId);

        emit TokensLocked(
            msg.sender,
            tokenId,
            amount,
            unlockTime,
            multiplier
        );
    }

    function unlockTokens(uint256 tokenId) external {
        require(ownerOf(tokenId) == msg.sender, "Not the owner");
        Lock storage lock = locks[tokenId];
        require(block.timestamp >= lock.unlockTime, "Lock period not ended");

        uint256 amount = lock.amount;
        delete locks[tokenId];
        _burn(tokenId);

        require(aiToken.transfer(msg.sender, amount), "Token transfer failed");

        emit TokensUnlocked(msg.sender, tokenId, amount);
    }

    function calculateMultiplier(uint256 duration) public pure returns (uint256) {
        uint256 baseMultiplier = 1 * 10**18; // 1x in 18 decimals
        uint256 additionalMultiplier = (duration - MIN_LOCK_DURATION) * 10**18 / (MAX_LOCK_DURATION - MIN_LOCK_DURATION);
        return baseMultiplier + additionalMultiplier;
    }

    function getUserLocks(address user) external view returns (uint256[] memory) {
        return userLocks[user];
    }

    function getLockDetails(uint256 tokenId) external view returns (Lock memory) {
        return locks[tokenId];
    }

    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 tokenId
    ) internal override {
        require(from == address(0) || to == address(0), "Soulbound: Transfers not allowed");
        super._beforeTokenTransfer(from, to, tokenId);
    }
}
```
