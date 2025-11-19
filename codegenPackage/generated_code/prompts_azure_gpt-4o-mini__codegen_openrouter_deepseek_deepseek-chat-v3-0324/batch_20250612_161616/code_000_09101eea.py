"""
Generated Code Metadata:
========================
Original URL: https://presale-jesse-9kw.pages.dev
Prompt: Generate a smart contract in Solidity for a presale event with a cap of 1000 BASE and a total supply of 100,000,000 JESSE tokens.
Generated: DETERMINISTIC_09101eea22e89c36
Batch ID: 20250612_161616
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

contract JessePresale is Ownable, ReentrancyGuard {
    IERC20 public jesseToken;
    uint256 public constant PRESALE_CAP = 1000 ether; // 1000 BASE
    uint256 public constant TOTAL_TOKENS = 100_000_000 ether; // 100,000,000 JESSE
    uint256 public constant TOKENS_PER_BASE = TOTAL_TOKENS / PRESALE_CAP;
    uint256 public totalRaised;
    uint256 public presaleEndTime;
    bool public presaleFinalized;

    mapping(address => uint256) public contributions;

    event Contributed(address indexed contributor, uint256 amount, uint256 tokens);
    event PresaleFinalized(uint256 totalRaised, uint256 tokensDistributed);
    event TokensClaimed(address indexed claimer, uint256 amount);

    constructor(address _jesseToken, uint256 _presaleDuration) {
        require(_jesseToken != address(0), "Invalid token address");
        jesseToken = IERC20(_jesseToken);
        presaleEndTime = block.timestamp + _presaleDuration;
    }

    function contribute() external payable nonReentrant {
        require(block.timestamp < presaleEndTime, "Presale has ended");
        require(!presaleFinalized, "Presale is finalized");
        require(msg.value > 0, "No BASE sent");
        require(totalRaised + msg.value <= PRESALE_CAP, "Presale cap reached");

        uint256 tokens = msg.value * TOKENS_PER_BASE;
        contributions[msg.sender] += tokens;
        totalRaised += msg.value;

        emit Contributed(msg.sender, msg.value, tokens);
    }

    function claimTokens() external nonReentrant {
        require(presaleFinalized, "Presale not finalized");
        require(contributions[msg.sender] > 0, "No tokens to claim");

        uint256 amount = contributions[msg.sender];
        contributions[msg.sender] = 0;

        require(
            jesseToken.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        emit TokensClaimed(msg.sender, amount);
    }

    function finalizePresale() external onlyOwner {
        require(block.timestamp >= presaleEndTime, "Presale not ended");
        require(!presaleFinalized, "Already finalized");

        presaleFinalized = true;

        // Transfer remaining tokens back to owner
        uint256 remainingTokens = TOTAL_TOKENS - (totalRaised * TOKENS_PER_BASE);
        if (remainingTokens > 0) {
            require(
                jesseToken.transfer(owner(), remainingTokens),
                "Remaining tokens transfer failed"
            );
        }

        emit PresaleFinalized(totalRaised, totalRaised * TOKENS_PER_BASE);
    }

    function withdrawBase() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        (bool success, ) = owner().call{value: address(this).balance}("");
        require(success, "Withdrawal failed");
    }

    function extendPresale(uint256 additionalTime) external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        presaleEndTime += additionalTime;
    }

    function emergencyWithdrawTokens() external onlyOwner {
        require(!presaleFinalized, "Presale already finalized");
        uint256 balance = jesseToken.balanceOf(address(this));
        require(jesseToken.transfer(owner(), balance), "Emergency transfer failed");
    }
}
```
