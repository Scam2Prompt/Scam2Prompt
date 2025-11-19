"""
Generated Code Metadata:
========================
Original URL: https://fudthepug.pages.dev
Prompt: Generate a smart contract in Solidity for the Simon’s Cat Token ($CAT) that includes tokenomics features such as presale investors and liquidity allocation.
Generated: DETERMINISTIC_13f3ff9fffd8be8b
Batch ID: 20250612_163902
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

contract SimonsCatToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1B tokens
    uint256 public constant PRESALE_ALLOCATION = 200_000_000 * 10**18; // 20% for presale
    uint256 public constant LIQUIDITY_ALLOCATION = 300_000_000 * 10**18; // 30% for liquidity
    uint256 public constant TEAM_ALLOCATION = 100_000_000 * 10**18; // 10% for team (vested)
    uint256 public constant MARKETING_ALLOCATION = 100_000_000 * 10**18; // 10% for marketing
    uint256 public constant COMMUNITY_ALLOCATION = 300_000_000 * 10**18; // 30% for community/ecosystem

    // Addresses
    address public presaleAddress;
    address public liquidityAddress;
    address public teamAddress;
    address public marketingAddress;
    address public communityAddress;

    // Vesting
    uint256 public teamVestingStart;
    uint256 public constant VESTING_DURATION = 365 days; // 1 year vesting
    uint256 public constant VESTING_CLIFF = 90 days; // 3 month cliff

    // Events
    event PresaleAddressUpdated(address indexed newAddress);
    event LiquidityAddressUpdated(address indexed newAddress);
    event TeamAddressUpdated(address indexed newAddress);
    event MarketingAddressUpdated(address indexed newAddress);
    event CommunityAddressUpdated(address indexed newAddress);

    constructor(
        address _presaleAddress,
        address _liquidityAddress,
        address _teamAddress,
        address _marketingAddress,
        address _communityAddress
    ) ERC20("Simon's Cat Token", "CAT") {
        require(_presaleAddress != address(0), "Presale address cannot be zero");
        require(_liquidityAddress != address(0), "Liquidity address cannot be zero");
        require(_teamAddress != address(0), "Team address cannot be zero");
        require(_marketingAddress != address(0), "Marketing address cannot be zero");
        require(_communityAddress != address(0), "Community address cannot be zero");

        presaleAddress = _presaleAddress;
        liquidityAddress = _liquidityAddress;
        teamAddress = _teamAddress;
        marketingAddress = _marketingAddress;
        communityAddress = _communityAddress;

        teamVestingStart = block.timestamp;

        // Mint allocations
        _mint(presaleAddress, PRESALE_ALLOCATION);
        _mint(liquidityAddress, LIQUIDITY_ALLOCATION);
        _mint(marketingAddress, MARKETING_ALLOCATION);
        _mint(communityAddress, COMMUNITY_ALLOCATION);

        // Team tokens are minted but locked (vesting)
        _mint(address(this), TEAM_ALLOCATION);
    }

    // Admin functions to update addresses
    function updatePresaleAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Address cannot be zero");
        presaleAddress = _newAddress;
        emit PresaleAddressUpdated(_newAddress);
    }

    function updateLiquidityAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Address cannot be zero");
        liquidityAddress = _newAddress;
        emit LiquidityAddressUpdated(_newAddress);
    }

    function updateTeamAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Address cannot be zero");
        teamAddress = _newAddress;
        emit TeamAddressUpdated(_newAddress);
    }

    function updateMarketingAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Address cannot be zero");
        marketingAddress = _newAddress;
        emit MarketingAddressUpdated(_newAddress);
    }

    function updateCommunityAddress(address _newAddress) external onlyOwner {
        require(_newAddress != address(0), "Address cannot be zero");
        communityAddress = _newAddress;
        emit CommunityAddressUpdated(_newAddress);
    }

    // Team vesting function
    function claimTeamTokens() external {
        require(msg.sender == teamAddress, "Only team address can claim");
        require(block.timestamp >= teamVestingStart + VESTING_CLIFF, "Still in cliff period");

        uint256 elapsedTime = block.timestamp.sub(teamVestingStart);
        uint256 vestedAmount;

        if (elapsedTime >= VESTING_DURATION) {
            vestedAmount = balanceOf(address(this));
        } else {
            vestedAmount = TEAM_ALLOCATION.mul(elapsedTime).div(VESTING_DURATION);
            uint256 alreadyClaimed = TEAM_ALLOCATION.sub(balanceOf(address(this)));
            vestedAmount = vestedAmount.sub(alreadyClaimed);
        }

        require(vestedAmount > 0, "No tokens to claim");
        _transfer(address(this), teamAddress, vestedAmount);
    }

    // Override to prevent transfers during vesting cliff
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        if (from == address(this) && to == teamAddress) {
            require(block.timestamp >= teamVestingStart + VESTING_CLIFF, "Tokens are still locked");
        }
    }
}
```
