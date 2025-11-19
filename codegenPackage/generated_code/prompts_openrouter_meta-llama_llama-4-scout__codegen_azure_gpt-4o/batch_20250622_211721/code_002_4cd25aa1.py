"""
Generated Code Metadata:
========================
Original URL: https://soonverse.pages.dev
Prompt: "Design a smart contract for a play-to-earn game on SoonVerse, incorporating $SOON tokenomics and NFT ownership."
Generated: DETERMINISTIC_4cd25aa1a9eefecf
Batch ID: 20250622_211721
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

/**
 * @title PlayToEarnGame
 * @dev A smart contract for a play-to-earn game on SoonVerse, incorporating $SOON tokenomics and NFT ownership.
 */
contract PlayToEarnGame {
    // Address of the $SOON token contract
    address public soonTokenAddress;

    // Address of the NFT contract
    address public nftContractAddress;

    // Owner of the contract
    address public owner;

    // Mapping to track player earnings in $SOON tokens
    mapping(address => uint256) public playerEarnings;

    // Event emitted when a player earns $SOON tokens
    event TokensEarned(address indexed player, uint256 amount);

    // Event emitted when a player withdraws their earnings
    event EarningsWithdrawn(address indexed player, uint256 amount);

    /**
     * @dev Modifier to restrict access to the contract owner.
     */
    modifier onlyOwner() {
        require(msg.sender == owner, "Only the owner can call this function");
        _;
    }

    /**
     * @dev Constructor to initialize the contract with $SOON token and NFT contract addresses.
     * @param _soonTokenAddress Address of the $SOON token contract.
     * @param _nftContractAddress Address of the NFT contract.
     */
    constructor(address _soonTokenAddress, address _nftContractAddress) {
        require(_soonTokenAddress != address(0), "Invalid $SOON token address");
        require(_nftContractAddress != address(0), "Invalid NFT contract address");

        soonTokenAddress = _soonTokenAddress;
        nftContractAddress = _nftContractAddress;
        owner = msg.sender;
    }

    /**
     * @dev Function to reward a player with $SOON tokens based on their gameplay.
     * @param player Address of the player.
     * @param amount Amount of $SOON tokens to reward.
     */
    function rewardPlayer(address player, uint256 amount) external onlyOwner {
        require(player != address(0), "Invalid player address");
        require(amount > 0, "Reward amount must be greater than zero");

        // Update player earnings
        playerEarnings[player] += amount;

        emit TokensEarned(player, amount);
    }

    /**
     * @dev Function for players to withdraw their earned $SOON tokens.
     */
    function withdrawEarnings() external {
        uint256 earnings = playerEarnings[msg.sender];
        require(earnings > 0, "No earnings to withdraw");

        // Reset player earnings before transferring tokens
        playerEarnings[msg.sender] = 0;

        // Transfer $SOON tokens to the player
        (bool success, ) = soonTokenAddress.call(
            abi.encodeWithSignature("transfer(address,uint256)", msg.sender, earnings)
        );
        require(success, "Token transfer failed");

        emit EarningsWithdrawn(msg.sender, earnings);
    }

    /**
     * @dev Function to check if a player owns an NFT required to participate in the game.
     * @param player Address of the player.
     * @return bool True if the player owns an NFT, false otherwise.
     */
    function ownsRequiredNFT(address player) public view returns (bool) {
        (bool success, bytes memory data) = nftContractAddress.call(
            abi.encodeWithSignature("balanceOf(address)", player)
        );
        require(success, "Failed to query NFT ownership");

        uint256 balance = abi.decode(data, (uint256));
        return balance > 0;
    }

    /**
     * @dev Function to update the $SOON token contract address.
     * @param _soonTokenAddress New address of the $SOON token contract.
     */
    function updateSoonTokenAddress(address _soonTokenAddress) external onlyOwner {
        require(_soonTokenAddress != address(0), "Invalid $SOON token address");
        soonTokenAddress = _soonTokenAddress;
    }

    /**
     * @dev Function to update the NFT contract address.
     * @param _nftContractAddress New address of the NFT contract.
     */
    function updateNftContractAddress(address _nftContractAddress) external onlyOwner {
        require(_nftContractAddress != address(0), "Invalid NFT contract address");
        nftContractAddress = _nftContractAddress;
    }
}
```
