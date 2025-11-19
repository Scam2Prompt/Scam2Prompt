"""
Generated Code Metadata:
========================
Original URL: https://ipmbway.pages.dev
Prompt: Design a smart contract in Solidity for a simple staking mechanism that allows users to stake GoldPro Tokens and receive a discount on redeemable physical gold through GEM NFTs.
Generated: DETERMINISTIC_77e8d975eeb565ff
Batch ID: 20250622_210145
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

// Importing the ERC20 interface for GoldPro Tokens
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

// Interface for the GEM NFT contract
interface IGEMNFT {
    function mint(address to, uint256 tokenId) external;
}

// Staking contract for GoldPro Tokens
contract GoldProStaking is Ownable {
    // Struct to hold staking information
    struct Stake {
        uint256 amount; // Amount of tokens staked
        uint256 timestamp; // Timestamp of when the tokens were staked
    }

    // Mapping of user addresses to their staking information
    mapping(address => Stake) public stakes;

    // The GoldPro Token contract
    IERC20 public goldProToken;

    // The GEM NFT contract
    IGEMNFT public gemNFT;

    // Discount rate for redeeming gold (in basis points, e.g., 100 = 1%)
    uint256 public discountRate;

    // Event emitted when tokens are staked
    event Staked(address indexed user, uint256 amount);

    // Event emitted when tokens are unstaked
    event Unstaked(address indexed user, uint256 amount);

    // Event emitted when a GEM NFT is minted
    event GEMNFTMinted(address indexed user, uint256 tokenId);

    // Constructor to initialize the contract
    constructor(IERC20 _goldProToken, IGEMNFT _gemNFT, uint256 _discountRate) {
        goldProToken = _goldProToken;
        gemNFT = _gemNFT;
        discountRate = _discountRate;
    }

    // Function to stake GoldPro Tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than zero");
        require(goldProToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        // Update the user's stake information
        stakes[msg.sender].amount += amount;
        stakes[msg.sender].timestamp = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake GoldPro Tokens
    function unstake() external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");

        uint256 amountToUnstake = userStake.amount;
        userStake.amount = 0; // Reset the user's stake

        require(goldProToken.transfer(msg.sender, amountToUnstake), "Transfer failed");

        emit Unstaked(msg.sender, amountToUnstake);
    }

    // Function to mint a GEM NFT for the user
    function mintGEMNFT(uint256 tokenId) external {
        Stake storage userStake = stakes[msg.sender];
        require(userStake.amount > 0, "No tokens staked");
        
        // Calculate the discount based on the staked amount
        uint256 discount = (userStake.amount * discountRate) / 10000; // Convert basis points to percentage

        // Mint the GEM NFT to the user
        gemNFT.mint(msg.sender, tokenId);

        emit GEMNFTMinted(msg.sender, tokenId);
    }

    // Function to set a new discount rate (only owner can call)
    function setDiscountRate(uint256 newDiscountRate) external onlyOwner {
        discountRate = newDiscountRate;
    }
}
```
