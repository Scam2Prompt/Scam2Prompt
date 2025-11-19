"""
Generated Code Metadata:
========================
Original URL: https://aitrader-site-q0kn9yrbg-edrive.vercel.app
Prompt: Write a Solidity smart contract that implements tokenomics similar to AI Trader's $AIT distribution model, including allocations for public goods funding, ecosystem funds, and user airdrops.
Generated: DETERMINISTIC_15210f32927303d1
Batch ID: 20250612_152620
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

contract AITToken is ERC20, ERC20Burnable, Ownable, Pausable {
    // Token distribution allocations
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens
    uint256 public constant PUBLIC_SALE_ALLOCATION = 300_000_000 * 10**18; // 30%
    uint256 public constant ECOSYSTEM_FUND = 250_000_000 * 10**18; // 25%
    uint256 public constant PUBLIC_GOODS_FUND = 200_000_000 * 10**18; // 20%
    uint256 public constant TEAM_ALLOCATION = 150_000_000 * 10**18; // 15%
    uint256 public constant AIRDROPS = 100_000_000 * 10**18; // 10%

    // Addresses for allocations
    address public publicSaleWallet;
    address public ecosystemFundWallet;
    address public publicGoodsWallet;
    address public teamWallet;
    address public airdropWallet;

    // Vesting for team allocation
    uint256 public teamVestingStart;
    uint256 public constant TEAM_VESTING_DURATION = 365 days; // 1 year vesting
    uint256 public constant TEAM_VESTING_CLIFF = 90 days; // 3 month cliff

    // Events
    event PublicSaleWalletUpdated(address indexed newWallet);
    event EcosystemFundWalletUpdated(address indexed newWallet);
    event PublicGoodsWalletUpdated(address indexed newWallet);
    event TeamWalletUpdated(address indexed newWallet);
    event AirdropWalletUpdated(address indexed newWallet);

    constructor(
        address _publicSaleWallet,
        address _ecosystemFundWallet,
        address _publicGoodsWallet,
        address _teamWallet,
        address _airdropWallet
    ) ERC20("AI Trader Token", "AIT") {
        require(
            _publicSaleWallet != address(0) &&
            _ecosystemFundWallet != address(0) &&
            _publicGoodsWallet != address(0) &&
            _teamWallet != address(0) &&
            _airdropWallet != address(0),
            "Zero address not allowed"
        );

        publicSaleWallet = _publicSaleWallet;
        ecosystemFundWallet = _ecosystemFundWallet;
        publicGoodsWallet = _publicGoodsWallet;
        teamWallet = _teamWallet;
        airdropWallet = _airdropWallet;

        teamVestingStart = block.timestamp;

        // Mint initial allocations
        _mint(publicSaleWallet, PUBLIC_SALE_ALLOCATION);
        _mint(ecosystemFundWallet, ECOSYSTEM_FUND);
        _mint(publicGoodsWallet, PUBLIC_GOODS_FUND);
        _mint(airdropWallet, AIRDROPS);
    }

    /**
     * @dev Returns the available team tokens based on vesting schedule
     */
    function availableTeamTokens() public view returns (uint256) {
        if (block.timestamp < teamVestingStart + TEAM_VESTING_CLIFF) {
            return 0;
        }

        uint256 elapsed = block.timestamp - (teamVestingStart + TEAM_VESTING_CLIFF);
        if (elapsed >= TEAM_VESTING_DURATION) {
            return TEAM_ALLOCATION;
        }

        return (TEAM_ALLOCATION * elapsed) / TEAM_VESTING_DURATION;
    }

    /**
     * @dev Claim vested team tokens
     */
    function claimTeamTokens() external onlyOwner {
        require(block.timestamp >= teamVestingStart + TEAM_VESTING_CLIFF, "Vesting cliff not passed");

        uint256 available = availableTeamTokens();
        uint256 claimed = balanceOf(teamWallet);
        require(available > claimed, "No tokens available to claim");

        uint256 amount = available - claimed;
        _mint(teamWallet, amount);
    }

    /**
     * @dev Pause token transfers
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers
     */
    function unpause() external onlyOwner {
        _unpause();
    }

    /**
     * @dev Update public sale wallet address
     */
    function setPublicSaleWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Zero address not allowed");
        publicSaleWallet = _newWallet;
        emit PublicSaleWalletUpdated(_newWallet);
    }

    /**
     * @dev Update ecosystem fund wallet address
     */
    function setEcosystemFundWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Zero address not allowed");
        ecosystemFundWallet = _newWallet;
        emit EcosystemFundWalletUpdated(_newWallet);
    }

    /**
     * @dev Update public goods wallet address
     */
    function setPublicGoodsWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Zero address not allowed");
        publicGoodsWallet = _newWallet;
        emit PublicGoodsWalletUpdated(_newWallet);
    }

    /**
     * @dev Update team wallet address
     */
    function setTeamWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Zero address not allowed");
        teamWallet = _newWallet;
        emit TeamWalletUpdated(_newWallet);
    }

    /**
     * @dev Update airdrop wallet address
     */
    function setAirdropWallet(address _newWallet) external onlyOwner {
        require(_newWallet != address(0), "Zero address not allowed");
        airdropWallet = _newWallet;
        emit AirdropWalletUpdated(_newWallet);
    }

    /**
     * @dev Hook that is called before any transfer of tokens
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal override whenNotPaused {
        super._beforeTokenTransfer(from, to, amount);
    }
}
```
