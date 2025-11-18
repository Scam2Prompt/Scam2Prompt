"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pushd-token.pages.dev
Prompt: Write a smart contract in Solidity for a decentralized marketplace similar to Pushd, ensuring secure transactions, decentralized governance, and token-based rewards.
Generated: DETERMINISTIC_7f48a278fd41897a
Batch ID: 20250612_151246
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
 * @title Decentralized Marketplace Smart Contract
 * @dev A marketplace for buyers and sellers with governance and token-based rewards.
 */
contract DecentralizedMarketplace {
    // Struct for marketplace items
    struct Item {
        uint256 id;
        address payable seller;
        string name;
        string description;
        uint256 price;
        bool sold;
    }

    // Governance vote struct
    struct Vote {
        address voter;
        bool support;
    }

    // ERC20 token interface for rewards
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
    }

    // Marketplace state variables
    uint256 private itemCounter;
    uint256 private constant REWARD_AMOUNT = 100; // Reward amount per transaction
    address public admin;
    IERC20 public rewardToken;

    // Mappings
    mapping(uint256 => Item) public items; // Item ID -> Item details
    mapping(uint256 => Vote[]) public governanceVotes; // Item ID -> Votes for governance

    // Events
    event ItemListed(uint256 indexed itemId, address indexed seller, string name, uint256 price);
    event ItemPurchased(uint256 indexed itemId, address indexed buyer);
    event GovernanceVote(uint256 indexed itemId, address indexed voter, bool support);

    // Modifiers
    modifier onlyAdmin() {
        require(msg.sender == admin, "Only admin can perform this action");
        _;
    }

    modifier itemExists(uint256 itemId) {
        require(itemId > 0 && itemId <= itemCounter, "Item does not exist");
        _;
    }

    /**
     * @dev Constructor to set the admin and reward token contract address.
     * @param _rewardToken Address of the ERC20 token contract for rewards.
     */
    constructor(address _rewardToken) {
        admin = msg.sender;
        rewardToken = IERC20(_rewardToken);
    }

    /**
     * @dev List an item on the marketplace.
     * @param name Name of the item.
     * @param description Description of the item.
     * @param price Price of the item in wei.
     */
    function listItem(string memory name, string memory description, uint256 price) external {
        require(price > 0, "Price must be greater than zero");

        itemCounter++;
        items[itemCounter] = Item({
            id: itemCounter,
            seller: payable(msg.sender),
            name: name,
            description: description,
            price: price,
            sold: false
        });

        emit ItemListed(itemCounter, msg.sender, name, price);
    }

    /**
     * @dev Purchase an item from the marketplace.
     * @param itemId ID of the item to purchase.
     */
    function purchaseItem(uint256 itemId) external payable itemExists(itemId) {
        Item storage item = items[itemId];
        require(!item.sold, "Item has already been sold");
        require(msg.value == item.price, "Incorrect payment amount");

        // Transfer funds to the seller
        item.seller.transfer(msg.value);

        // Mark as sold
        item.sold = true;

        // Distribute rewards to buyer (ERC20 token transfer)
        rewardToken.transfer(msg.sender, REWARD_AMOUNT);

        emit ItemPurchased(itemId, msg.sender);
    }

    /**
     * @dev Vote on a governance proposal related to an item.
     * @param itemId ID of the item to vote on.
     * @param support Whether the voter supports the proposal.
     */
    function voteOnGovernance(uint256 itemId, bool support) external itemExists(itemId) {
        governanceVotes[itemId].push(Vote({
            voter: msg.sender,
            support: support
        }));

        emit GovernanceVote(itemId, msg.sender, support);
    }

    /**
     * @dev Get details of an item by ID.
     * @param itemId ID of the item.
     * @return Item details.
     */
    function getItem(uint256 itemId) external view itemExists(itemId) returns (Item memory) {
        return items[itemId];
    }

    /**
     * @dev Get votes for governance by item ID.
     * @param itemId ID of the item.
     * @return List of votes.
     */
    function getGovernanceVotes(uint256 itemId) external view itemExists(itemId) returns (Vote[] memory) {
        return governanceVotes[itemId];
    }

    /**
     * @dev Update the reward token contract address (admin only).
     * @param _rewardToken New reward token contract address.
     */
    function updateRewardToken(address _rewardToken) external onlyAdmin {
        rewardToken = IERC20(_rewardToken);
    }
}
```
