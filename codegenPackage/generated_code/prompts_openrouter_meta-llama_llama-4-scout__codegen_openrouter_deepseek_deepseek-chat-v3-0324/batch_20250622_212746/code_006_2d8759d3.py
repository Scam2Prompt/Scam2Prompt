"""
Generated Code Metadata:
========================
Original URL: https://claim-mindofpepe-allocations.pages.dev
Prompt: Write a Solidity contract for the MIND of Pepe token, defining its tokenomics, including the allocation of tokens for exchanges, AI agent development, marketing, rewards, and community staking.
Generated: DETERMINISTIC_2d8759d3d6d7e880
Batch ID: 20250622_212746
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Snapshot.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract MindOfPepe is ERC20, ERC20Burnable, ERC20Snapshot, Ownable, Pausable {
    // Token allocation percentages
    uint256 public constant EXCHANGES_ALLOCATION = 30;
    uint256 public constant AI_DEVELOPMENT_ALLOCATION = 20;
    uint256 public constant MARKETING_ALLOCATION = 15;
    uint256 public constant REWARDS_ALLOCATION = 20;
    uint256 public constant COMMUNITY_STAKING_ALLOCATION = 15;

    // Allocation addresses
    address public exchangesWallet;
    address public aiDevelopmentWallet;
    address public marketingWallet;
    address public rewardsWallet;
    address public communityStakingWallet;

    // Total supply: 1 trillion tokens with 18 decimals
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000_000 * 10**18;

    // Track minted allocations
    bool private exchangesMinted;
    bool private aiDevelopmentMinted;
    bool private marketingMinted;
    bool private rewardsMinted;
    bool private communityStakingMinted;

    constructor(
        address _exchangesWallet,
        address _aiDevelopmentWallet,
        address _marketingWallet,
        address _rewardsWallet,
        address _communityStakingWallet
    ) ERC20("MIND of Pepe", "MIND") {
        require(
            _exchangesWallet != address(0) &&
            _aiDevelopmentWallet != address(0) &&
            _marketingWallet != address(0) &&
            _rewardsWallet != address(0) &&
            _communityStakingWallet != address(0),
            "Invalid wallet address"
        );

        exchangesWallet = _exchangesWallet;
        aiDevelopmentWallet = _aiDevelopmentWallet;
        marketingWallet = _marketingWallet;
        rewardsWallet = _rewardsWallet;
        communityStakingWallet = _communityStakingWallet;
    }

    /**
     * @dev Mint initial token allocations according to tokenomics
     */
    function mintAllocations() external onlyOwner {
        require(!exchangesMinted, "Exchanges allocation already minted");
        _mint(exchangesWallet, (TOTAL_SUPPLY * EXCHANGES_ALLOCATION) / 100);
        exchangesMinted = true;

        require(!aiDevelopmentMinted, "AI Development allocation already minted");
        _mint(aiDevelopmentWallet, (TOTAL_SUPPLY * AI_DEVELOPMENT_ALLOCATION) / 100);
        aiDevelopmentMinted = true;

        require(!marketingMinted, "Marketing allocation already minted");
        _mint(marketingWallet, (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100);
        marketingMinted = true;

        require(!rewardsMinted, "Rewards allocation already minted");
        _mint(rewardsWallet, (TOTAL_SUPPLY * REWARDS_ALLOCATION) / 100);
        rewardsMinted = true;

        require(!communityStakingMinted, "Community Staking allocation already minted");
        _mint(communityStakingWallet, (TOTAL_SUPPLY * COMMUNITY_STAKING_ALLOCATION) / 100);
        communityStakingMinted = true;
    }

    /**
     * @dev Create a new snapshot
     */
    function snapshot() public onlyOwner {
        _snapshot();
    }

    /**
     * @dev Pause token transfers
     */
    function pause() public onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() public onlyOwner {
        _unpause();
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override(ERC20, ERC20Snapshot) whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }

    /**
     * @dev Update exchanges wallet address
     */
    function setExchangesWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        exchangesWallet = _newWallet;
    }

    /**
     * @dev Update AI development wallet address
     */
    function setAiDevelopmentWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        aiDevelopmentWallet = _newWallet;
    }

    /**
     * @dev Update marketing wallet address
     */
    function setMarketingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        marketingWallet = _newWallet;
    }

    /**
     * @dev Update rewards wallet address
     */
    function setRewardsWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        rewardsWallet = _newWallet;
    }

    /**
     * @dev Update community staking wallet address
     */
    function setCommunityStakingWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Invalid address");
        communityStakingWallet = _newWallet;
    }
}
```
