"""
Generated Code Metadata:
========================
Original URL: https://seedify-fundnft-project.pages.dev
Prompt: "Generate a smart contract code for an NFT launchpad that includes staking $SFUND and $SNFTS for early access to project tokens and NFTs, with functionalities for team mint, lottery phases, and FCFS allocation."
Generated: DETERMINISTIC_f6a3d559a342684d
Batch ID: 20250622_210502
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
import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTLaunchpad is ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of users to their staked amounts
    mapping (address => uint256) public sfundStakers;
    mapping (address => uint256) public snftsStakers;

    // Mapping of users to their claimed tokens and NFTs
    mapping (address => bool) public hasClaimed;

    // Mapping of project tokens
    mapping (address => bool) public projectTokens;

    // Mapping of NFTs
    mapping (address => bool) public nftContracts;

    // Team wallet address
    address public teamWallet;

    // SFUND and SNFTS token addresses
    address public sfundToken;
    address public snftsToken;

    // Lottery phases
    uint256 public lotteryPhases;
    uint256 public currentLotteryPhase;

    // FCFS allocation
    uint256 public fcfsAllocation;

    // Mapping of users to their lottery tickets
    mapping (address => uint256) public lotteryTickets;

    // Event emitted when a user stakes SFUND
    event StakedSfund(address indexed user, uint256 amount);

    // Event emitted when a user stakes SNFTS
    event StakedSnfts(address indexed user, uint256 amount);

    // Event emitted when a user claims tokens and NFTs
    event Claimed(address indexed user, uint256 tokens, uint256 nft);

    // Event emitted when team mints tokens and NFTs
    event TeamMint(address indexed user, uint256 tokens, uint256 nft);

    constructor(
        address _teamWallet,
        address _sfundToken,
        address _snftsToken
    ) public {
        teamWallet = _teamWallet;
        sfundToken = _sfundToken;
        snftsToken = _snftsToken;
        lotteryPhases = 3;
        currentLotteryPhase = 1;
        fcfsAllocation = 1000;
    }

    // Function to stake SFUND
    function stakeSfund(uint256 _amount) public {
        require(ERC20(sfundToken).transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        sfundStakers[msg.sender] = sfundStakers[msg.sender].add(_amount);
        emit StakedSfund(msg.sender, _amount);
    }

    // Function to stake SNFTS
    function stakeSnfts(uint256 _amount) public {
        require(ERC20(snftsToken).transferFrom(msg.sender, address(this), _amount), "Transfer failed");
        snftsStakers[msg.sender] = snftsStakers[msg.sender].add(_amount);
        emit StakedSnfts(msg.sender, _amount);
    }

    // Function to claim tokens and NFTs
    function claim() public {
        require(!hasClaimed[msg.sender], "Already claimed");
        require(sfundStakers[msg.sender] > 0 || snftsStakers[msg.sender] > 0, "No stake");

        uint256 tokens = calculateTokens(msg.sender);
        uint256 nft = calculateNFT(msg.sender);

        hasClaimed[msg.sender] = true;

        // Transfer tokens and NFTs to user
        require(ERC20(projectTokens[address(this)]).transfer(msg.sender, tokens), "Transfer failed");
        require(ERC721(nftContracts[address(this)]).safeTransferFrom(address(this), msg.sender, nft), "Transfer failed");

        emit Claimed(msg.sender, tokens, nft);
    }

    // Function to calculate tokens
    function calculateTokens(address _user) internal view returns (uint256) {
        // Implement token calculation logic here
        return 0;
    }

    // Function to calculate NFTs
    function calculateNFT(address _user) internal view returns (uint256) {
        // Implement NFT calculation logic here
        return 0;
    }

    // Function for team to mint tokens and NFTs
    function teamMint(address _user, uint256 _tokens, uint256 _nft) public {
        require(msg.sender == teamWallet, "Only team can mint");

        // Mint tokens and NFTs
        projectTokens[address(this)] = true;
        nftContracts[address(this)] = true;

        emit TeamMint(_user, _tokens, _nft);
    }

    // Function to participate in lottery
    function participateInLottery() public {
        require(lotteryTickets[msg.sender] == 0, "Already participated");

        // Generate lottery ticket
        lotteryTickets[msg.sender] = uint256(keccak256(abi.encodePacked(msg.sender))) % 100;

        // Check if user won
        if (lotteryTickets[msg.sender] < fcfsAllocation) {
            // Grant access to project tokens and NFTs
            hasClaimed[msg.sender] = false;
        }
    }

    // Function to progress lottery phase
    function progressLotteryPhase() public {
        require(msg.sender == teamWallet, "Only team can progress phase");
        require(currentLotteryPhase < lotteryPhases, "Already completed all phases");

        currentLotteryPhase++;

        // Update FCFS allocation
        fcfsAllocation = fcfsAllocation.sub(10);
    }

    // Function to get user's staked amounts
    function getStakedAmounts(address _user) public view returns (uint256, uint256) {
        return (sfundStakers[_user], snftsStakers[_user]);
    }
}
```
