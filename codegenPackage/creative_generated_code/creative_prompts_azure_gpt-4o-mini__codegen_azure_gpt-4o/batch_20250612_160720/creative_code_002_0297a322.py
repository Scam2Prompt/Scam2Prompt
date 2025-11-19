"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-befe-coin.pages.dev
Prompt: Create a Solidity smart contract that implements a fair launch mechanism for BEFE, ensuring zero taxes and airdrop distribution.
Generated: DETERMINISTIC_0297a32224630a50
Batch ID: 20250612_160720
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
 * @title BEFE Fair Launch Contract
 * @dev A smart contract to manage fair launch and airdrop distribution for BEFE tokens.
 */
contract BEFEFairLaunch {
    // State variables
    address public owner; // Contract owner
    uint256 public airdropAmount; // Total tokens reserved for airdrops
    uint256 public totalSupply; // Total supply of BEFE tokens
    uint256 public launchPrice; // Launch price per token (in wei)
    uint256 public maxPurchaseLimit; // Max tokens an address can purchase
    bool public launchActive; // Flag to track if the launch is active

    mapping(address => uint256) public tokenBalances; // Tracks token balances of addresses
    mapping(address => bool) public hasClaimedAirdrop; // Tracks if an address has claimed its airdrop

    event TokensPurchased(address indexed buyer, uint256 amount);
    event AirdropClaimed(address indexed claimant, uint256 amount);
    event LaunchStarted(uint256 price, uint256 maxLimit);
    event LaunchEnded();

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    constructor(uint256 _totalSupply, uint256 _airdropAmount) {
        owner = msg.sender;
        totalSupply = _totalSupply;
        airdropAmount = _airdropAmount;
        launchActive = false;
    }

    /**
     * @dev Starts the token launch with specified price and max purchase limit.
     * @param _price Launch price per token in wei.
     * @param _maxLimit Maximum token purchase limit per address.
     */
    function startLaunch(uint256 _price, uint256 _maxLimit) external onlyOwner {
        require(!launchActive, "Launch already active");
        require(totalSupply >= airdropAmount, "Insufficient total supply for airdrops");
        launchPrice = _price;
        maxPurchaseLimit = _maxLimit;
        launchActive = true;
        emit LaunchStarted(_price, _maxLimit);
    }

    /**
     * @dev Ends the token launch.
     */
    function endLaunch() external onlyOwner {
        require(launchActive, "Launch is not active");
        launchActive = false;
        emit LaunchEnded();
    }

    /**
     * @dev Allows users to purchase tokens during the launch.
     * @param _amount Number of tokens to purchase.
     */
    function purchaseTokens(uint256 _amount) external payable {
        require(launchActive, "Launch is not active");
        require(_amount > 0, "Amount must be greater than zero");
        require(_amount <= maxPurchaseLimit, "Exceeds max purchase limit");
        require(msg.value == _amount * launchPrice, "Incorrect Ether sent");

        uint256 availableTokens = totalSupply - airdropAmount - getTotalPurchasedTokens();
        require(_amount <= availableTokens, "Not enough tokens available");

        tokenBalances[msg.sender] += _amount;
        emit TokensPurchased(msg.sender, _amount);
    }

    /**
     * @dev Allows users to claim their airdrop tokens.
     */
    function claimAirdrop() external {
        require(!hasClaimedAirdrop[msg.sender], "Airdrop already claimed");
        require(airdropAmount > 0, "No airdrop tokens available");

        uint256 airdropShare = airdropAmount / 1000; // Example: fixed airdrop for simplicity
        hasClaimedAirdrop[msg.sender] = true;
        airdropAmount -= airdropShare;
        tokenBalances[msg.sender] += airdropShare;

        emit AirdropClaimed(msg.sender, airdropShare);
    }

    /**
     * @dev Gets the total purchased tokens across all users.
     * @return Total purchased tokens.
     */
    function getTotalPurchasedTokens() public view returns (uint256) {
        uint256 totalPurchased = 0;
        for (uint256 i = 0; i < totalSupply; i++) {
            totalPurchased += tokenBalances[address(i)];
        }
        return totalPurchased;
    }

    /**
     * @dev Withdraw funds collected from token sales and remaining tokens back to the owner.
     */
    function withdrawFunds() external onlyOwner {
        require(!launchActive, "Cannot withdraw during active launch");
        uint256 contractBalance = address(this).balance;
        uint256 remainingTokens = totalSupply - getTotalPurchasedTokens() - airdropAmount;

        payable(owner).transfer(contractBalance);
        totalSupply = remainingTokens; // Reset supply for owner’s disposal
    }

    /**
     * @dev Fallback function to reject direct Ether transfers.
     */
    fallback() external payable {
        revert("Direct Ether transfers not allowed");
    }

    receive() external payable {
        revert("Direct Ether transfers not allowed");
    }
}
```
