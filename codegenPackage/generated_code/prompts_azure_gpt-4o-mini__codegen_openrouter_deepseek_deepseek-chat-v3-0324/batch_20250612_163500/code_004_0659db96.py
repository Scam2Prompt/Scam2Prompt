"""
Generated Code Metadata:
========================
Original URL: https://wienerdog-is.pages.dev
Prompt: Provide an example of a Solidity contract that could be used to manage the presale and token distribution for WienerAI, incorporating the tokenomics outlined in the whitepaper.
Generated: DETERMINISTIC_0659db960ea42f00
Batch ID: 20250612_163500
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title WienerAIToken
 * @dev ERC20 token contract for WienerAI with presale functionality
 */
contract WienerAIToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant MAX_SUPPLY = 69_000_000_000 * 10**18; // 69 billion tokens
    uint256 public constant PRESALE_SUPPLY = 13_800_000_000 * 10**18; // 20% of total supply
    uint256 public constant TEAM_SUPPLY = 13_800_000_000 * 10**18; // 20% of total supply
    uint256 public constant ECOSYSTEM_SUPPLY = 41_400_000_000 * **18; // 60% of total supply

    uint256 public presaleStartTime;
    uint256 public presaleEndTime;
    uint256 public presaleRate; // Tokens per ETH
    uint256 public presaleMinContribution;
    uint256 public presaleMaxContribution;
    uint256 public presaleTokensSold;
    bool public presaleFinalized;

    address public teamWallet;
    address public ecosystemWallet;

    mapping(address => uint256) public contributions;

    event PresaleContribution(address indexed contributor, uint256 amount, uint256 tokens);
    event PresaleFinalized(uint256 tokensSold, uint256 ethRaised);
    event TokensClaimed(address indexed claimer, uint256 amount);

    /**
     * @dev Constructor
     * @param _presaleRate Tokens per ETH during presale
     * @param _presaleMinContribution Minimum ETH contribution
     * @param _presaleMaxContribution Maximum ETH contribution per address
     * @param _presaleDuration Duration of presale in seconds
     * @param _teamWallet Address for team allocation
     * @param _ecosystemWallet Address for ecosystem allocation
     */
    constructor(
        uint256 _presaleRate,
        uint256 _presaleMinContribution,
        uint256 _presaleMaxContribution,
        uint256 _presaleDuration,
        address _teamWallet,
        address _ecosystemWallet
    ) ERC20("WienerAI", "WAI") {
        require(_teamWallet != address(0), "Invalid team wallet");
        require(_ecosystemWallet != address(0), "Invalid ecosystem wallet");

        presaleRate = _presaleRate;
        presaleMinContribution = _presaleMinContribution;
        presaleMaxContribution = _presaleMaxContribution;
        presaleStartTime = block.timestamp;
        presaleEndTime = block.timestamp + _presaleDuration;
        teamWallet = _teamWallet;
        ecosystemWallet = _ecosystemWallet;

        // Mint ecosystem and team tokens (vesting should be handled separately)
        _mint(ecosystemWallet, ECOSYSTEM_SUPPLY);
        _mint(address(this), TEAM_SUPPLY); // Team tokens locked in contract
    }

    /**
     * @dev Participate in presale
     */
    function contributeToPresale() external payable nonReentrant {
        require(block.timestamp >= presaleStartTime && block.timestamp <= presaleEndTime, "Presale not active");
        require(msg.value >= presaleMinContribution, "Contribution too low");
        require(contributions[msg.sender] + msg.value <= presaleMaxContribution, "Exceeds max contribution");
        require(presaleTokensSold < PRESALE_SUPPLY, "Presale supply exhausted");

        uint256 tokens = msg.value * presaleRate;
        require(presaleTokensSold + tokens <= PRESALE_SUPPLY, "Not enough tokens remaining");

        contributions[msg.sender] += msg.value;
        presaleTokensSold += tokens;
        _mint(msg.sender, tokens);

        emit PresaleContribution(msg.sender, msg.value, tokens);
    }

    /**
     * @dev Finalize presale and distribute remaining tokens
     */
    function finalizePresale() external onlyOwner {
        require(block.timestamp > presaleEndTime || presaleTokensSold >= PRESALE_SUPPLY, "Presale not ended");
        require(!presaleFinalized, "Presale already finalized");

        presaleFinalized = true;

        // Burn unsold presale tokens
        uint256 unsoldTokens = PRESALE_SUPPLY - presaleTokensSold;
        if (unsoldTokens > 0) {
            _burn(address(this), unsoldTokens);
        }

        emit PresaleFinalized(presaleTokensSold, address(this).balance);
    }

    /**
     * @dev Withdraw collected ETH
     */
    function withdrawETH() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        payable(owner()).transfer(address(this).balance);
    }

    /**
     * @dev Release team tokens (to be called after vesting period)
     */
    function releaseTeamTokens() external onlyOwner {
        require(presaleFinalized, "Presale not finalized");
        require(block.timestamp >= presaleEndTime + 365 days, "Vesting period not ended");

        _transfer(address(this), teamWallet, TEAM_SUPPLY);
    }

    /**
     * @dev Get remaining presale time
     */
    function getPresaleTimeRemaining() external view returns (uint256) {
        if (block.timestamp >= presaleEndTime) {
            return 0;
        }
        return presaleEndTime - block.timestamp;
    }

    /**
     * @dev Get user's claimable tokens
     */
    function getClaimableTokens(address user) external view returns (uint256) {
        return balanceOf(user);
    }
}
```
