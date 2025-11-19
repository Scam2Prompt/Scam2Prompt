"""
Generated Code Metadata:
========================
Original URL: https://shibaswap.us.com
Prompt: Develop a decentralized trading platform similar to ShibaSwap, incorporating features like governance, NFT marketplace, and yield farming.
Generated: DETERMINISTIC_47332434a994499e
Batch ID: 20250622_212702
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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/IERC721Enumerable.sol";

contract ShibaSwap is ReentrancyGuard, Ownable {
    using SafeMath for uint256;
    using SafeERC20 for IERC20;

    // Token details
    IERC20 public shibaToken;
    uint256 public totalStaked;
    uint256 public rewardRate;
    uint256 public lastUpdateTime;
    uint256 public rewardPerTokenStored;

    // Governance
    struct Proposal {
        uint256 id;
        address proposer;
        uint256 startTime;
        uint256 endTime;
        uint256 forVotes;
        uint256 againstVotes;
        bool executed;
        string description;
    }

    Proposal[] public proposals;
    mapping(address => uint256) public voteLock;
    mapping(uint256 => mapping(address => bool)) public hasVoted;

    // NFT Marketplace
    struct NFTListing {
        address seller;
        address nftContract;
        uint256 tokenId;
        uint256 price;
        bool isActive;
    }

    NFTListing[] public nftListings;
    mapping(address => mapping(uint256 => uint256)) public nftListingIndex;

    // Yield Farming
    struct PoolInfo {
        IERC20 lpToken;
        uint256 allocPoint;
        uint256 lastRewardBlock;
        uint256 accShibaPerShare;
    }

    PoolInfo[] public poolInfo;
    mapping(uint256 => mapping(address => uint256)) public userInfo;
    uint256 public totalAllocPoint = 0;
    uint256 public shibaPerBlock;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Withdrawn(address indexed user, uint256 amount);
    event RewardPaid(address indexed user, uint256 reward);
    event ProposalCreated(uint256 indexed proposalId, address indexed proposer);
    event Voted(uint256 indexed proposalId, address indexed voter, bool support);
    event ProposalExecuted(uint256 indexed proposalId);
    event NFTListed(uint256 indexed listingId, address indexed seller, address nftContract, uint256 tokenId, uint256 price);
    event NFTSold(uint256 indexed listingId, address indexed buyer, address nftContract, uint256 tokenId, uint256 price);
    event Deposit(address indexed user, uint256 indexed pid, uint256 amount);
    event Withdraw(address indexed user, uint256 indexed pid, uint256 amount);
    event EmergencyWithdraw(address indexed user, uint256 indexed pid, uint256 amount);

    constructor(IERC20 _shibaToken, uint256 _shibaPerBlock) {
        shibaToken = _shibaToken;
        shibaPerBlock = _shibaPerBlock;
    }

    // Staking functions
    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0");
        updateReward(msg.sender);
        totalStaked = totalStaked.add(amount);
        shibaToken.safeTransferFrom(msg.sender, address(this), amount);
        emit Staked(msg.sender, amount);
    }

    function withdraw(uint256 amount) public nonReentrant {
        require(amount > 0, "Cannot withdraw 0");
        updateReward(msg.sender);
        totalStaked = totalStaked.sub(amount);
        shibaToken.safeTransfer(msg.sender, amount);
        emit Withdrawn(msg.sender, amount);
    }

    function exit() external {
        withdraw(balanceOf(msg.sender));
        getReward();
    }

    function getReward() public nonReentrant {
        updateReward(msg.sender);
        uint256 reward = earned(msg.sender);
        if (reward > 0) {
            rewards[msg.sender] = 0;
            shibaToken.safeTransfer(msg.sender, reward);
            emit RewardPaid(msg.sender, reward);
        }
    }

    function balanceOf(address account) public view returns (uint256) {
        return balances[account];
    }

    function earned(address account) public view returns (uint256) {
        return balances[account].mul(rewardPerToken().sub(userRewardPerTokenPaid[account])).div(1e18).add(rewards[account]);
    }

    function rewardPerToken() public view returns (uint256) {
        if (totalStaked == 0) {
            return rewardPerTokenStored;
        }
        return rewardPerTokenStored.add(
            lastTimeRewardApplicable().sub(lastUpdateTime).mul(rewardRate).mul(1e18).div(totalStaked)
        );
    }

    function lastTimeRewardApplicable() public view returns (uint256) {
        return block.timestamp;
    }

    function updateReward(address account) internal {
        rewardPerTokenStored = rewardPerToken();
        lastUpdateTime = lastTimeRewardApplicable();
        if (account != address(0)) {
            rewards[account] = earned(account);
            userRewardPerTokenPaid[account] = rewardPerTokenStored;
        }
    }

    // Governance functions
    function createProposal(string memory description) external returns (uint256) {
        uint256 proposalId = proposals.length;
        proposals.push(Proposal({
            id: proposalId,
            proposer: msg.sender,
            startTime: block.timestamp,
            endTime: block.timestamp + 3 days,
            forVotes: 0,
            againstVotes: 0,
            executed: false,
            description: description
        }));
        emit ProposalCreated(proposalId, msg.sender);
        return proposalId;
    }

    function vote(uint256 proposalId, bool support) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp >= proposal.startTime && block.timestamp <= proposal.endTime, "Voting period closed");
        require(!hasVoted[proposalId][msg.sender], "Already voted");
        require(shibaToken.balanceOf(msg.sender) > 0, "No voting power");

        hasVoted[proposalId][msg.sender] = true;
        voteLock[msg.sender] = proposal.endTime;

        if (support) {
            proposal.forVotes = proposal.forVotes.add(shibaToken.balanceOf(msg.sender));
        } else {
            proposal.againstVotes = proposal.againstVotes.add(shibaToken.balanceOf(msg.sender));
        }

        emit Voted(proposalId, msg.sender, support);
    }

    function executeProposal(uint256 proposalId) external {
        Proposal storage proposal = proposals[proposalId];
        require(block.timestamp > proposal.endTime, "Voting period not ended");
        require(!proposal.executed, "Proposal already executed");
        require(proposal.forVotes > proposal.againstVotes, "Proposal not passed");

        proposal.executed = true;
        emit ProposalExecuted(proposalId);
    }

    // NFT Marketplace functions
    function listNFT(address nftContract, uint256 tokenId, uint256 price) external {
        IERC721(nftContract).transferFrom(msg.sender, address(this), tokenId);
        uint256 listingId = nftListings.length;
        nftListings.push(NFTListing({
            seller: msg.sender,
            nftContract: nftContract,
            tokenId: tokenId,
            price: price,
            isActive: true
        }));
        nftListingIndex[nftContract][tokenId] = listingId;
        emit NFTListed(listingId, msg.sender, nftContract, tokenId, price);
    }

    function buyNFT(uint256 listingId) external payable {
        NFTListing storage listing = nftListings[listingId];
        require(listing.isActive, "Listing not active");
        require(msg.value >= listing.price, "Insufficient funds");

        listing.isActive = false;
        payable(listing.seller).transfer(listing.price);
        IERC721(listing.nftContract).transferFrom(address(this), msg.sender, listing.tokenId);

        emit NFTSold(listingId, msg.sender, listing.nftContract, listing.tokenId, listing.price);
    }

    function cancelListing(uint256 listingId) external {
        NFTListing storage listing = nftListings[listingId];
        require(listing.seller == msg.sender, "Not seller");
        require(listing.isActive, "Listing not active");

        listing.isActive = false;
        IERC721(listing.nftContract).transferFrom(address(this), msg.sender, listing.tokenId);
    }

    // Yield Farming functions
    function addPool(uint256 _allocPoint, IERC20 _
