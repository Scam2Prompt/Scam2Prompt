"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tenon-restore.pages.dev
Prompt: Create a smart contract that integrates the DeFi Protocol's "Whitelist/Presale" feature for token sales, including validation and metadata restoration.
Generated: DETERMINISTIC_a17fc24bc6f5d84a
Batch ID: 20250612_153526
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
 * @title WhitelistPresale
 * @dev A smart contract for managing a token presale with a whitelist feature.
 * Users can participate in the presale only if they're whitelisted, and metadata restoration is supported.
 */
contract WhitelistPresale {
    // Address of the owner/admin of the contract
    address public owner;

    // Mapping to track whitelisted addresses
    mapping(address => bool) public whitelist;

    // Token sale metadata structure
    struct Metadata {
        string tokenName;
        string tokenSymbol;
        uint256 tokenPrice;
        uint256 presaleSupply;
        uint256 presaleStart;
        uint256 presaleEnd;
    }

    // Metadata for the presale
    Metadata public presaleMetadata;

    // Mapping to track contributions
    mapping(address => uint256) public contributions;

    // Event emitted when a user participates in the presale
    event PresaleContribution(address indexed user, uint256 amount);

    // Event emitted when the whitelist is updated
    event WhitelistUpdated(address indexed account, bool status);

    // Event emitted when metadata is restored
    event MetadataRestored(string tokenName, string tokenSymbol, uint256 tokenPrice);

    // Modifier to enforce ownership
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the contract owner can perform this action");
        _;
    }

    // Modifier to check if the presale is active
    modifier presaleActive() {
        require(
            block.timestamp >= presaleMetadata.presaleStart && block.timestamp <= presaleMetadata.presaleEnd,
            "Presale is not active"
        );
        _;
    }

    /**
     * @dev Constructor that initializes the contract with presale metadata and sets the owner.
     * @param _tokenName Name of the token being sold in the presale.
     * @param _tokenSymbol Symbol of the token being sold in the presale.
     * @param _tokenPrice Price of the token in wei.
     * @param _presaleSupply Total supply for the presale.
     * @param _presaleStart Start time of the presale (timestamp).
     * @param _presaleEnd End time of the presale (timestamp).
     */
    constructor(
        string memory _tokenName,
        string memory _tokenSymbol,
        uint256 _tokenPrice,
        uint256 _presaleSupply,
        uint256 _presaleStart,
        uint256 _presaleEnd
    ) {
        owner = msg.sender;
        presaleMetadata = Metadata({
            tokenName: _tokenName,
            tokenSymbol: _tokenSymbol,
            tokenPrice: _tokenPrice,
            presaleSupply: _presaleSupply,
            presaleStart: _presaleStart,
            presaleEnd: _presaleEnd
        });
    }

    /**
     * @dev Function to update whitelist status for an account.
     * @param _account Address of the account to update.
     * @param _status True to whitelist, false to remove from whitelist.
     */
    function updateWhitelist(address _account, bool _status) external onlyOwner {
        whitelist[_account] = _status;
        emit WhitelistUpdated(_account, _status);
    }

    /**
     * @dev Function to allow users to participate in the presale.
     */
    function participatePresale() external payable presaleActive {
        require(whitelist[msg.sender], "You are not whitelisted");
        require(msg.value > 0, "Must send some ETH to participate");
        uint256 tokens = msg.value / presaleMetadata.tokenPrice;
        require(
            presaleMetadata.presaleSupply >= tokens,
            "Not enough tokens left in presale supply"
        );

        // Update contributions and presale supply
        contributions[msg.sender] += tokens;
        presaleMetadata.presaleSupply -= tokens;

        emit PresaleContribution(msg.sender, tokens);
    }

    /**
     * @dev Function to restore token sale metadata. Only callable by the owner.
     * @param _tokenName Name of the token being sold in the presale.
     * @param _tokenSymbol Symbol of the token being sold in the presale.
     * @param _tokenPrice Price of the token in wei.
     */
    function restoreMetadata(
        string memory _tokenName,
        string memory _tokenSymbol,
        uint256 _tokenPrice
    ) external onlyOwner {
        presaleMetadata.tokenName = _tokenName;
        presaleMetadata.tokenSymbol = _tokenSymbol;
        presaleMetadata.tokenPrice = _tokenPrice;

        emit MetadataRestored(_tokenName, _tokenSymbol, _tokenPrice);
    }

    /**
     * @dev Function to withdraw collected funds. Only callable by the owner.
     */
    function withdrawFunds() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No funds to withdraw");
        payable(owner).transfer(balance);
    }

    /**
     * @dev Function to retrieve the remaining presale supply.
     * @return Remaining presale supply.
     */
    function getRemainingSupply() external view returns (uint256) {
        return presaleMetadata.presaleSupply;
    }

    /**
     * @dev Fallback function to prevent accidental ETH transfers to the contract.
     */
    fallback() external payable {
        revert("ETH transfers are not allowed");
    }

    /**
     * @dev Receive function to prevent accidental ETH transfers to the contract.
     */
    receive() external payable {
        revert("ETH transfers are not allowed");
    }
}
```
