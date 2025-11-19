"""
Generated Code Metadata:
========================
Original URL: https://memeskombat.pages.dev
Prompt: Generate a smart contract code in Solidity for a token presale system, similar to the one used in Meme Kombat, with a 50% token supply allocated for presale.
Generated: DETERMINISTIC_bd4584ddb9f2ea90
Batch ID: 20250622_205955
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract PresaleToken is ERC20, Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant PRESALE_SUPPLY = TOTAL_SUPPLY.div(2); // 50% of total supply
    uint256 public constant PRESALE_RATE = 1000; // 1 ETH = 1000 tokens
    uint256 public constant MIN_CONTRIBUTION = 0.1 ether;
    uint256 public constant MAX_CONTRIBUTION = 10 ether;

    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public totalContributed;
    uint256 public totalPresaleTokensSold;

    bool public presaleFinalized;
    bool public tokensClaimable;

    mapping(address => uint256) public contributions;
    mapping(address => bool) public claimedTokens;

    event TokensPurchased(address indexed buyer, uint256 amount);
    event TokensClaimed(address indexed recipient, uint256 amount);
    event PresaleFinalized(uint256 totalRaised, uint256 totalTokensSold);

    constructor(
        uint256 _presaleStartTime,
        uint256 _presaleDuration
    ) ERC20("Presale Token", "PRESALE") {
        require(_presaleStartTime > block.timestamp, "Start time must be in the future");
        require(_presaleDuration > 0, "Duration must be positive");

        presaleStartTime = _presaleStartTime;
        presaleEndTime = _presaleStartTime.add(_presaleDuration);

        _mint(address(this), PRESALE_SUPPLY);
    }

    modifier whenPresaleActive() {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale is not active");
        _;
    }

    modifier whenPresaleEnded() {
        require(block.timestamp > presaleEndTime, "Presale has not ended");
        _;
    }

    function contribute() external payable nonReentrant whenPresaleActive {
        require(msg.value >= MIN_CONTRIBUTION, "Contribution too low");
        require(msg.value <= MAX_CONTRIBUTION, "Contribution too high");
        require(totalContributed.add(msg.value) <= getPresaleCap(), "Presale cap reached");

        uint256 tokens = msg.value.mul(PRESALE_RATE);
        require(totalPresaleTokensSold.add(tokens) <= PRESALE_SUPPLY, "Not enough tokens left");

        contributions[msg.sender] = contributions[msg.sender].add(msg.value);
        totalContributed = totalContributed.add(msg.value);
        totalPresaleTokensSold = totalPresaleTokensSold.add(tokens);

        emit TokensPurchased(msg.sender, tokens);
    }

    function claimTokens() external nonReentrant whenPresaleEnded {
        require(tokensClaimable, "Tokens are not yet claimable");
        require(!claimedTokens[msg.sender], "Tokens already claimed");
        require(contributions[msg.sender] > 0, "No contribution");

        uint256 tokenAmount = contributions[msg.sender].mul(PRESALE_RATE);
        claimedTokens[msg.sender] = true;

        _transfer(address(this), msg.sender, tokenAmount);
        emit TokensClaimed(msg.sender, tokenAmount);
    }

    function finalizePresale() external onlyOwner whenPresaleEnded {
        require(!presaleFinalized, "Presale already finalized");
        
        presaleFinalized = true;
        tokensClaimable = true;

        // Burn unsold tokens
        uint256 unsoldTokens = PRESALE_SUPPLY.sub(totalPresaleTokensSold);
        if (unsoldTokens > 0) {
            _burn(address(this), unsoldTokens);
        }

        emit PresaleFinalized(totalContributed, totalPresaleTokensSold);
    }

    function withdrawFunds() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        payable(owner()).transfer(address(this).balance);
    }

    function getPresaleCap() public pure returns (uint256) {
        return PRESALE_SUPPLY.div(PRESALE_RATE);
    }

    function getTokensLeft() public view returns (uint256) {
        return PRESALE_SUPPLY.sub(totalPresaleTokensSold);
    }

    function getContribution(address contributor) external view returns (uint256) {
        return contributions[contributor];
    }

    function getClaimableTokens(address contributor) external view returns (uint256) {
        if (claimedTokens[contributor] || contributions[contributor] == 0) {
            return 0;
        }
        return contributions[contributor].mul(PRESALE_RATE);
    }
}
```
