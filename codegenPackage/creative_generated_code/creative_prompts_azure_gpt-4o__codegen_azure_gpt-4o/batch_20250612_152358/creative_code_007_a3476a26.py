"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://milady-dfk.pages.dev
Prompt: Generate a Solidity contract for a token sale mechanism that includes stepped raises and fixed-price pools, similar to the Milady Cult presale structure.
Generated: DETERMINISTIC_a3476a2614ba538b
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title TokenSale
 * @dev A token sale contract with stepped raises and fixed-price pools.
 */
contract TokenSale {
    // Token interface
    IERC20 public token;

    // Address of the wallet where funds are collected
    address public wallet;

    // Total tokens allocated for sale
    uint256 public totalTokensForSale;

    // Current sale phase
    uint256 public currentPhase;

    // Mapping to store phase details
    mapping(uint256 => Phase) public phases;

    // Structure for phase details
    struct Phase {
        uint256 tokensAvailable;    // Tokens available for the phase
        uint256 pricePerToken;      // Price per token in Wei
        bool isActive;              // Indicates if the phase is active
    }

    // Events
    event TokensPurchased(address indexed buyer, uint256 amount, uint256 phase);
    event PhaseActivated(uint256 phase);

    // Modifiers
    modifier onlyActivePhase(uint256 phase) {
        require(phases[phase].isActive, "Phase is not active");
        _;
    }

    modifier validPhase(uint256 phase) {
        require(phase >= 1 && phase <= currentPhase, "Invalid phase");
        _;
    }

    /**
     * @dev Constructor initializes the contract with token address, wallet, and total tokens for sale.
     * @param _token Address of the ERC20 token being sold.
     * @param _wallet Address where funds will be collected.
     * @param _totalTokensForSale Total tokens allocated for sale.
     */
    constructor(
        IERC20 _token,
        address _wallet,
        uint256 _totalTokensForSale
    ) {
        require(address(_token) != address(0), "Token address cannot be zero");
        require(_wallet != address(0), "Wallet address cannot be zero");
        require(_totalTokensForSale > 0, "Total tokens must be greater than zero");

        token = _token;
        wallet = _wallet;
        totalTokensForSale = _totalTokensForSale;
    }

    /**
     * @dev Adds a new phase to the sale.
     * @param tokensAvailable Number of tokens available for the phase.
     * @param pricePerToken Price per token in Wei.
     */
    function addPhase(uint256 tokensAvailable, uint256 pricePerToken) external {
        require(tokensAvailable > 0, "Tokens must be greater than zero");
        require(pricePerToken > 0, "Price must be greater than zero");
        require(
            tokensAvailable <= totalTokensForSale,
            "Exceeds total tokens for sale"
        );

        currentPhase++;
        phases[currentPhase] = Phase({
            tokensAvailable: tokensAvailable,
            pricePerToken: pricePerToken,
            isActive: false // Initially inactive
        });
        totalTokensForSale -= tokensAvailable;
    }

    /**
     * @dev Activates a specific phase.
     * @param phase Phase number to activate.
     */
    function activatePhase(uint256 phase) external validPhase(phase) {
        require(!phases[phase].isActive, "Phase is already active");
        phases[phase].isActive = true;
        emit PhaseActivated(phase);
    }

    /**
     * @dev Allows users to purchase tokens in an active phase.
     * @param phase Phase number to purchase tokens from.
     * @param amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 phase, uint256 amount)
        external
        payable
        onlyActivePhase(phase)
    {
        Phase storage current = phases[phase];

        require(amount > 0, "Amount must be greater than zero");
        require(amount <= current.tokensAvailable, "Not enough tokens available");
        require(
            msg.value == amount * current.pricePerToken,
            "Incorrect Ether sent"
        );

        // Transfer tokens to the buyer
        require(
            token.transfer(msg.sender, amount),
            "Token transfer failed"
        );

        // Update tokens available in the phase
        current.tokensAvailable -= amount;

        // Transfer Ether to the wallet
        (bool success, ) = wallet.call{value: msg.value}("");
        require(success, "Ether transfer failed");

        emit TokensPurchased(msg.sender, amount, phase);
    }

    /**
     * @dev Fallback function to prevent accidental Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfer not allowed");
    }

    /**
     * @dev Receives Ether if sent directly to the contract address.
     */
    receive() external payable {
        revert("Direct Ether transfer not allowed");
    }
}

// Interface for ERC20 token
interface IERC20 {
    function transfer(address recipient, uint256 amount)
        external
        returns (bool);
}
```
