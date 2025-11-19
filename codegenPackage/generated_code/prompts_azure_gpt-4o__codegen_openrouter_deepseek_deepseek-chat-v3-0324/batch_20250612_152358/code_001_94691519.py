"""
Generated Code Metadata:
========================
Original URL: https://claimmogcoin.vercel.app
Prompt: Generate Solidity code for an ERC-20 token contract with features similar to $MOG, emphasizing tokenized cultural branding and community-driven growth.
Generated: DETERMINISTIC_946915198a2c7ff9
Batch ID: 20250612_152358
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

contract MogToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics
    uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant COMMUNITY_RESERVE = 600_000_000 * 10**18; // 60% for community
    uint256 public constant TEAM_RESERVE = 200_000_000 * 10**18; // 20% for team
    uint256 public constant MARKETING_RESERVE = 200_000_000 * 10**18; // 20% for marketing

    // Community governance
    address public communityWallet;
    address public marketingWallet;
    address public teamWallet;

    // Anti-whale measures
    uint256 public maxTransferAmount = 5_000_000 * 10**18; // 0.5% of total supply
    bool public antiWhaleEnabled = true;

    // Cultural branding
    string public culturalBrandURI;
    mapping(address => bool) public culturalBrandContributors;

    // Events
    event CulturalBrandUpdated(string newURI);
    event ContributorAdded(address contributor);
    event ContributorRemoved(address contributor);
    event AntiWhaleUpdated(bool status, uint256 maxAmount);

    constructor(
        address _communityWallet,
        address _marketingWallet,
        address _teamWallet
    ) ERC20("Mog Token", "MOG") {
        require(
            _communityWallet != address(0) &&
                _marketingWallet != address(0) &&
                _teamWallet != address(0),
            "Zero address not allowed"
        );

        communityWallet = _communityWallet;
        marketingWallet = _marketingWallet;
        teamWallet = _teamWallet;

        // Mint initial supply
        _mint(communityWallet, COMMUNITY_RESERVE);
        _mint(marketingWallet, MARKETING_RESERVE);
        _mint(teamWallet, TEAM_RESERVE);

        // Add initial contributors
        culturalBrandContributors[msg.sender] = true;
        culturalBrandContributors[_communityWallet] = true;
    }

    /**
     * @dev Override transfer to include anti-whale checks
     */
    function _transfer(
        address sender,
        address recipient,
        uint256 amount
    ) internal virtual override {
        if (antiWhaleEnabled && !isExcludedFromAntiWhale(sender)) {
            require(
                amount <= maxTransferAmount,
                "Transfer amount exceeds max limit"
            );
        }
        super._transfer(sender, recipient, amount);
    }

    /**
     * @dev Update cultural brand metadata URI (only by owner)
     */
    function updateCulturalBrandURI(string memory newURI) external onlyOwner {
        culturalBrandURI = newURI;
        emit CulturalBrandUpdated(newURI);
    }

    /**
     * @dev Add a cultural brand contributor (only by owner)
     */
    function addContributor(address contributor) external onlyOwner {
        require(contributor != address(0), "Zero address not allowed");
        culturalBrandContributors[contributor] = true;
        emit ContributorAdded(contributor);
    }

    /**
     * @dev Remove a cultural brand contributor (only by owner)
     */
    function removeContributor(address contributor) external onlyOwner {
        require(contributor != address(0), "Zero address not allowed");
        culturalBrandContributors[contributor] = false;
        emit ContributorRemoved(contributor);
    }

    /**
     * @dev Update anti-whale settings (only by owner)
     */
    function updateAntiWhale(bool enabled, uint256 maxAmount) external onlyOwner {
        antiWhaleEnabled = enabled;
        maxTransferAmount = maxAmount;
        emit AntiWhaleUpdated(enabled, maxAmount);
    }

    /**
     * @dev Check if address is excluded from anti-whale (team/community/marketing wallets)
     */
    function isExcludedFromAntiWhale(address account) public view returns (bool) {
        return account == owner() || 
               account == communityWallet || 
               account == marketingWallet || 
               account == teamWallet ||
               culturalBrandContributors[account];
    }

    /**
     * @dev Recover any ERC20 tokens sent to contract by mistake
     */
    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
