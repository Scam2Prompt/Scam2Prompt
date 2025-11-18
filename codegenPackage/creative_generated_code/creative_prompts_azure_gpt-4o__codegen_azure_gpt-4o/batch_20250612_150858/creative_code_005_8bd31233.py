"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cowswap-finance.medium.com
Prompt: Develop a smart contract that supports fair token launches, inspired by CowSwap's "Fair Sales" concept.
Generated: DETERMINISTIC_8bd312333bf812a1
Batch ID: 20250612_150858
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

/**
 * @title FairTokenLaunch
 * @dev A smart contract inspired by CowSwap's "Fair Sales" concept for fair token launches.
 */
contract FairTokenLaunch {
    // Token details
    address public immutable tokenAddress;
    uint256 public immutable tokenAmount; // Amount of tokens to sell
    uint256 public immutable saleStart;  // Start time of the sale (Unix timestamp)
    uint256 public immutable saleDuration; // Duration of the sale

    // Sale state
    uint256 public totalCommittedETH = 0; // Total ETH committed by buyers
    mapping(address => uint256) public commitments; // ETH committed per buyer
    bool public finalized = false; // Whether the sale has been finalized

    // Events
    event CommitmentMade(address indexed buyer, uint256 amount);
    event SaleFinalized(uint256 totalETHRaised, uint256 tokenPrice);

    // Constructor to initialize the contract
    constructor(
        address _tokenAddress,
        uint256 _tokenAmount,
        uint256 _saleStart,
        uint256 _saleDuration
    ) {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenAmount > 0, "Token amount must be positive");
        require(_saleDuration > 0, "Sale duration must be positive");

        tokenAddress = _tokenAddress;
        tokenAmount = _tokenAmount;
        saleStart = _saleStart;
        saleDuration = _saleDuration;
    }

    /**
     * @dev Function to commit ETH to the sale during the active sale period.
     */
    function commitETH() external payable {
        require(block.timestamp >= saleStart, "Sale has not started yet");
        require(block.timestamp <= saleStart + saleDuration, "Sale has ended");
        require(msg.value > 0, "Commitment amount must be positive");

        commitments[msg.sender] += msg.value;
        totalCommittedETH += msg.value;

        emit CommitmentMade(msg.sender, msg.value);
    }

    /**
     * @dev Finalize the sale, distributing tokens proportionally to commitments.
     * Callable only after the sale has ended.
     */
    function finalizeSale() external {
        require(block.timestamp > saleStart + saleDuration, "Sale has not ended yet");
        require(!finalized, "Sale already finalized");

        finalized = true;

        uint256 tokenPrice = totalCommittedETH > 0 ? totalCommittedETH / tokenAmount : 0;

        emit SaleFinalized(totalCommittedETH, tokenPrice);

        // Distribute tokens to participants based on their commitments
        for (uint256 i = 0; i < _participants.length; i++) {
            address participant = _participants[i];
            uint256 ethContribution = commitments[participant];
            if (ethContribution > 0) {
                uinttype
