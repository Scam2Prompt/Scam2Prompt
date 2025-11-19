"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jessecom.pages.dev
Prompt: How can I implement a presale mechanism for a token with a total supply of 100,000,000 JESSE using a specific cap in a blockchain environment?
Generated: DETERMINISTIC_c62e7eeacc488f92
Batch ID: 20250612_161520
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
 * @title TokenPresale
 * @dev Implements a presale mechanism for a token with a fixed total supply and cap.
 */
contract TokenPresale {
    // Token details
    string public constant name = "JESSE";
    uint256 public constant totalSupply = 100000000 * 10**18; // 100 million tokens (18 decimal places)

    // Presale parameters
    uint256 public immutable presaleCap; // Maximum tokens available for presale
    uint256 public presaleRate; // Rate of tokens per 1 ETH
    uint256 public presaleTokensSold; // Total tokens sold during presale

    address public owner; // Contract owner
    mapping(address => uint256) public contributions; // Tracks ETH contributions from buyers

    bool public presaleActive; // Status of the presale

    /**
     * @dev Modifier to restrict access to owner-only functions.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Caller is not the owner");
        _;
    }

    /**
     * @dev Constructor initializes the presale parameters.
     * @param _presaleCap The maximum number of tokens available during the presale.
     * @param _presaleRate Rate of tokens per 1 ETH.
     */
    constructor(uint256 _presaleCap, uint256 _presaleRate) {
        require(_presaleCap <= totalSupply, "Presale cap exceeds total supply");
        require(_presaleRate > 0, "Presale rate must be greater than zero");

        owner = msg.sender;
        presaleCap = _presaleCap;
        presaleRate = _presaleRate;
        presaleActive = true; // Presale starts active
    }

    /**
     * @dev Allows users to purchase tokens during the presale.
     * The function converts ETH sent into tokens at the presale rate.
     */
    function buyTokens() external payable {
        require(presaleActive, "Presale is not active");
        require(msg.value > 0, "ETH sent must be greater than zero");

        // Calculate the number of tokens to distribute
        uint256 tokensToDistribute = msg.value * presaleRate;

        // Ensure the presale cap is not exceeded
        require(
            presaleTokensSold + tokensToDistribute <= presaleCap,
            "Purchase exceeds presale cap"
        );

        // Update presale state
        presaleTokensSold += tokensToDistribute;
        contributions[msg.sender] += msg.value;

        // Emit event for token purchase
        emit TokensPurchased(msg.sender, msg.value, tokensToDistribute);
    }

    /**
     * @dev Ends the presale and transfers funds to the owner.
     */
    function endPresale() external onlyOwner {
        require(presaleActive, "Presale is already ended");

        presaleActive = false;

        // Transfer all funds to the owner
        (bool success, ) = owner.call{value: address(this).balance}("");
        require(success, "Transfer failed");

        emit PresaleEnded(owner, presaleTokensSold);
    }

    /**
     * @dev Allows the owner to update the presale rate.
     * @param _newRate The new rate of tokens per 1 ETH.
     */
    function updatePresaleRate(uint256 _newRate) external onlyOwner {
        require(_newRate > 0, "Presale rate must be greater than zero");
        presaleRate = _newRate;

        emit PresaleRateUpdated(_newRate);
    }

    /**
     * @dev Fallback function allows the contract to accept ETH directly.
     */
    receive() external payable {
        buyTokens();
    }

    /**
     * @dev Event emitted when tokens are purchased during the presale.
     * @param buyer Address of the buyer.
     * @param ethAmount Amount of ETH contributed.
     * @param tokenAmount Amount of tokens purchased.
     */
    event TokensPurchased(address indexed buyer, uint256 ethAmount, uint256 tokenAmount);

    /**
     * @dev Event emitted when the presale ends.
     * @param owner Address of the owner.
     * @param totalTokensSold Total tokens sold during the presale.
     */
    event PresaleEnded(address indexed owner, uint256 totalTokensSold);

    /**
     * @dev Event emitted when the presale rate is updated.
     * @param newRate The new presale rate.
     */
    event PresaleRateUpdated(uint256 newRate);
}
```
