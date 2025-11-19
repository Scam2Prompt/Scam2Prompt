"""
Generated Code Metadata:
========================
Original URL: https://simoncat.pages.dev
Prompt: Generate a smart contract code in Solidity for a token with a similar tokenomics structure to Simon's Cat, including a 30% presale allocation for investors and a 10% allocation for the foundation.
Generated: DETERMINISTIC_78e8a2d06db77432
Batch ID: 20250622_211317
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

/**
 * @title SimonCatToken
 * @dev ERC20 token with presale and foundation allocations similar to Simon's Cat tokenomics
 */
contract SimonCatToken is ERC20, Ownable {
    using SafeMath for uint256;

    // Token distribution percentages
    uint256 public constant PRESALE_ALLOCATION = 30; // 30% for presale investors
    uint256 public constant FOUNDATION_ALLOCATION = 10; // 10% for foundation
    uint256 public constant REMAINING_ALLOCATION = 60; // 60% remaining allocation

    // Addresses for allocations
    address public presaleWallet;
    address public foundationWallet;

    // Total supply
    uint256 private constant TOTAL_SUPPLY = 1_000_000_000 * 10**18; // 1 billion tokens

    // Track if allocations have been distributed
    bool private presaleAllocated = false;
    bool private foundationAllocated = false;

    /**
     * @dev Constructor that initializes the token and allocates initial supplies
     * @param _presaleWallet Address of the presale investors wallet
     * @param _foundationWallet Address of the foundation wallet
     */
    constructor(
        address _presaleWallet,
        address _foundationWallet
    ) ERC20("SimonCatToken", "SCT") {
        require(
            _presaleWallet != address(0),
            "Presale wallet cannot be zero address"
        );
        require(
            _foundationWallet != address(0),
            "Foundation wallet cannot be zero address"
        );

        presaleWallet = _presaleWallet;
        foundationWallet = _foundationWallet;

        // Mint remaining allocation to contract owner
        uint256 remainingTokens = TOTAL_SUPPLY.mul(REMAINING_ALLOCATION).div(100);
        _mint(owner(), remainingTokens);
    }

    /**
     * @dev Allocate presale tokens to presale wallet
     */
    function allocatePresale() external onlyOwner {
        require(!presaleAllocated, "Presale tokens already allocated");
        
        uint256 presaleTokens = TOTAL_SUPPLY.mul(PRESALE_ALLOCATION).div(100);
        _mint(presaleWallet, presaleTokens);
        presaleAllocated = true;
    }

    /**
     * @dev Allocate foundation tokens to foundation wallet
     */
    function allocateFoundation() external onlyOwner {
        require(!foundationAllocated, "Foundation tokens already allocated");
        
        uint256 foundationTokens = TOTAL_SUPPLY.mul(FOUNDATION_ALLOCATION).div(100);
        _mint(foundationWallet, foundationTokens);
        foundationAllocated = true;
    }

    /**
     * @dev Change presale wallet address
     * @param _newPresaleWallet New presale wallet address
     */
    function changePresaleWallet(address _newPresaleWallet) external onlyOwner {
        require(
            _newPresaleWallet != address(0),
            "New presale wallet cannot be zero address"
        );
        presaleWallet = _newPresaleWallet;
    }

    /**
     * @dev Change foundation wallet address
     * @param _newFoundationWallet New foundation wallet address
     */
    function changeFoundationWallet(address _newFoundationWallet) external onlyOwner {
        require(
            _newFoundationWallet != address(0),
            "New foundation wallet cannot be zero address"
        );
        foundationWallet = _newFoundationWallet;
    }

    /**
     * @dev Override to prevent transfers until presale and foundation allocations are done
     */
    function _beforeTokenTransfer(
        address from,
        address to,
        uint256 amount
    ) internal virtual override {
        super._beforeTokenTransfer(from, to, amount);

        // Allow minting and initial allocations
        if (from == address(0) || to == address(0)) {
            return;
        }

        require(
            presaleAllocated && foundationAllocated,
            "Token transfers not allowed until allocations are complete"
        );
    }
}
```
