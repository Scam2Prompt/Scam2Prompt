"""
Generated Code Metadata:
========================
Original URL: https://hehe-com.pages.dev
Prompt: Generate a Solidity contract for the $HEHE airdrop, ensuring that 666 recipients are randomly selected and rewarded with tokens.
Generated: DETERMINISTIC_0a31c5792fbce780
Batch ID: 20250612_153517
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
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract HEHEAirdrop is Ownable {
    using SafeMath for uint256;

    IERC20 public heheToken;
    uint256 public constant RECIPIENT_COUNT = 666;
    uint256 public constant TOKENS_PER_RECIPIENT = 666 * 10**18; // 666 tokens with 18 decimals
    uint256 public airdropEndBlock;
    bool public airdropCompleted;
    mapping(address => bool) public hasReceivedAirdrop;
    address[] public recipients;

    event AirdropDistributed(address indexed recipient, uint256 amount);
    event AirdropCompleted(uint256 totalRecipients);

    constructor(address _heheToken, uint256 _airdropDurationBlocks) {
        require(_heheToken != address(0), "Invalid token address");
        heheToken = IERC20(_heheToken);
        airdropEndBlock = block.number.add(_airdropDurationBlocks);
    }

    function registerForAirdrop() external {
        require(block.number <= airdropEndBlock, "Airdrop registration closed");
        require(!hasReceivedAirdrop[msg.sender], "Already registered");
        require(recipients.length < RECIPIENT_COUNT, "Airdrop full");

        hasReceivedAirdrop[msg.sender] = true;
        recipients.push(msg.sender);
    }

    function distributeAirdrop() external onlyOwner {
        require(block.number > airdropEndBlock, "Airdrop not ended");
        require(!airdropCompleted, "Airdrop already completed");
        require(recipients.length == RECIPIENT_COUNT, "Not enough recipients");

        uint256 totalTokens = TOKENS_PER_RECIPIENT.mul(RECIPIENT_COUNT);
        require(
            heheToken.balanceOf(address(this)) >= totalTokens,
            "Insufficient token balance"
        );

        // Fisher-Yates shuffle algorithm
        for (uint256 i = recipients.length - 1; i > 0; i--) {
            uint256 j = uint256(
                keccak256(abi.encodePacked(block.timestamp, block.difficulty, i))
            ) % (i + 1);
            (recipients[i], recipients[j]) = (recipients[j], recipients[i]);
        }

        for (uint256 i = 0; i < recipients.length; i++) {
            heheToken.transfer(recipients[i], TOKENS_PER_RECIPIENT);
            emit AirdropDistributed(recipients[i], TOKENS_PER_RECIPIENT);
        }

        airdropCompleted = true;
        emit AirdropCompleted(RECIPIENT_COUNT);
    }

    function withdrawRemainingTokens() external onlyOwner {
        require(airdropCompleted, "Airdrop not completed");
        uint256 remainingBalance = heheToken.balanceOf(address(this));
        heheToken.transfer(owner(), remainingBalance);
    }

    function extendAirdrop(uint256 _additionalBlocks) external onlyOwner {
        require(block.number <= airdropEndBlock, "Airdrop already ended");
        airdropEndBlock = airdropEndBlock.add(_additionalBlocks);
    }
}
```
