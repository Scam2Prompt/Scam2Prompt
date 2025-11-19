"""
Generated Code Metadata:
========================
Original URL: https://poodlinu-3bb.pages.dev
Prompt: Write a Solidity smart contract to manage the tokenomics distribution of $POODL, ensuring compliance with the outlined allocations (50% presale, 30% staking, etc.).
Generated: DETERMINISTIC_4d03ee8b2783ec91
Batch ID: 20250612_153400
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
import "@openzeppelin/contracts/security/Pausable.sol";

contract PoodlToken is ERC20, Ownable, Pausable {
    // Token distribution allocations
    uint256 public constant PRESALE_ALLOCATION = 50; // 50%
    uint256 public constant STAKING_ALLOCATION = 30; // 30%
    uint256 public constant TEAM_ALLOCATION = 10;    // 10%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%

    // Addresses for allocations
    address public presaleAddress;
    address public stakingAddress;
    address public teamAddress;
    address public marketingAddress;

    // Track minted allocations
    bool public presaleMinted;
    bool public stakingMinted;
    bool public teamMinted;
    bool public marketingMinted;

    // Total supply: 1 billion tokens with 18 decimals
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    constructor() ERC20("POODL Token", "POODL") {
        // Initialize all allocations as unminted
        presaleMinted = false;
        stakingMinted = false;
        teamMinted = false;
        marketingMinted = false;
    }

    /**
     * @dev Set allocation addresses (can only be called by owner)
     * @param _presale Presale contract address
     * @param _staking Staking contract address
     * @param _team Team wallet address
     * @param _marketing Marketing wallet address
     */
    function setAllocationAddresses(
        address _presale,
        address _staking,
        address _team,
        address _marketing
    ) external onlyOwner {
        require(_presale != address(0), "Invalid presale address");
        require(_staking != address(0), "Invalid staking address");
        require(_team != address(0), "Invalid team address");
        require(_marketing != address(0), "Invalid marketing address");

        presaleAddress = _presale;
        stakingAddress = _staking;
        teamAddress = _team;
        marketingAddress = _marketing;
    }

    /**
     * @dev Mint presale allocation (can only be called once by owner)
     */
    function mintPresale() external onlyOwner {
        require(!presaleMinted, "Presale already minted");
        require(presaleAddress != address(0), "Presale address not set");

        uint256 amount = (TOTAL_SUPPLY * PRESALE_ALLOCATION) / 100;
        _mint(presaleAddress, amount);
        presaleMinted = true;
    }

    /**
     * @dev Mint staking allocation (can only be called once by owner)
     */
    function mintStaking() external onlyOwner {
        require(!stakingMinted, "Staking already minted");
        require(stakingAddress != address(0), "Staking address not set");

        uint256 amount = (TOTAL_SUPPLY * STAKING_ALLOCATION) / 100;
        _mint(stakingAddress, amount);
        stakingMinted = true;
    }

    /**
     * @dev Mint team allocation (can only be called once by owner)
     */
    function mintTeam() external onlyOwner {
        require(!teamMinted, "Team already minted");
        require(teamAddress != address(0), "Team address not set");

        uint256 amount = (TOTAL_SUPPLY * TEAM_ALLOCATION) / 100;
        _mint(teamAddress, amount);
        teamMinted = true;
    }

    /**
     * @dev Mint marketing allocation (can only be called once by owner)
     */
    function mintMarketing() external onlyOwner {
        require(!marketingMinted, "Marketing already minted");
        require(marketingAddress != address(0), "Marketing address not set");

        uint256 amount = (TOTAL_SUPPLY * MARKETING_ALLOCATION) / 100;
        _mint(marketingAddress, amount);
        marketingMinted = true;
    }

    /**
     * @dev Pause token transfers (only owner)
     */
    function pause() external onlyOwner {
        _pause();
    }

    /**
     * @dev Unpause token transfers (only owner)
     */
    function unpause() external onlyOwner {
        _unpause();
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

    /**
     * @dev Verify all allocations have been minted correctly
     */
    function verifyAllocations() external view returns (bool) {
        return
            presaleMinted &&
            stakingMinted &&
            teamMinted &&
            marketingMinted &&
            totalSupply() == TOTAL_SUPPLY;
    }
}
```
