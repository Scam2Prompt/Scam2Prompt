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

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract NFTLaunchpad is Ownable {
    using SafeMath for uint256;

    // Token interfaces
    IERC20 public sfundToken;
    IERC20 public snftsToken;
    IERC721 public nftToken;

    // Staking structure
    struct Staker {
        uint256 amountStaked;
        uint256 lastStakeTime;
    }

    mapping(address => Staker) public stakers;

    // Lottery phase structure
    struct LotteryPhase {
        uint256 startTime;
        uint256 endTime;
        uint256 totalTickets;
        mapping(address => uint256) tickets;
    }

    LotteryPhase[] public lotteryPhases;

    // Events
    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event LotteryEntered(address indexed user, uint256 phaseIndex, uint256 tickets);
    event TeamMinted(address indexed teamAddress, uint256 amount);

    // Constructor to initialize tokens
    constructor(address _sfundToken, address _snftsToken, address _nftToken) {
        sfundToken = IERC20(_sfundToken);
        snftsToken = IERC20(_snftsToken);
        nftToken = IERC721(_nftToken);
    }

    // Function to stake SFUND tokens
    function stake(uint256 amount) external {
        require(amount > 0, "Amount must be greater than 0");
        require(sfundToken.transferFrom(msg.sender, address(this), amount), "Transfer failed");

        Staker storage staker = stakers[msg.sender];
        staker.amountStaked = staker.amountStaked.add(amount);
        staker.lastStakeTime = block.timestamp;

        emit Staked(msg.sender, amount);
    }

    // Function to unstake SFUND tokens
    function unstake(uint256 amount) external {
        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked >= amount, "Insufficient staked amount");

        staker.amountStaked = staker.amountStaked.sub(amount);
        require(sfundToken.transfer(msg.sender, amount), "Transfer failed");

        emit Unstaked(msg.sender, amount);
    }

    // Function to create a new lottery phase
    function createLotteryPhase(uint256 duration) external onlyOwner {
        LotteryPhase storage newPhase = lotteryPhases.push();
        newPhase.startTime = block.timestamp;
        newPhase.endTime = block.timestamp.add(duration);
        newPhase.totalTickets = 0;
    }

    // Function to enter the lottery
    function enterLottery(uint256 phaseIndex, uint256 tickets) external {
        require(phaseIndex < lotteryPhases.length, "Invalid phase index");
        LotteryPhase storage phase = lotteryPhases[phaseIndex];
        require(block.timestamp >= phase.startTime && block.timestamp <= phase.endTime, "Lottery phase not active");

        Staker storage staker = stakers[msg.sender];
        require(staker.amountStaked > 0, "Must stake to enter lottery");

        phase.tickets[msg.sender] = phase.tickets[msg.sender].add(tickets);
        phase.totalTickets = phase.totalTickets.add(tickets);

        emit LotteryEntered(msg.sender, phaseIndex, tickets);
    }

    // Function for team minting NFTs
    function teamMint(address to, uint256 tokenId) external onlyOwner {
        nftToken.safeTransferFrom(address(this), to, tokenId);
        emit TeamMinted(to, tokenId);
    }

    // Function to get the staked amount of a user
    function getStakedAmount(address user) external view returns (uint256) {
        return stakers[user].amountStaked;
    }

    // Function to get the total tickets in a lottery phase
    function getTotalTickets(uint256 phaseIndex) external view returns (uint256) {
        require(phaseIndex < lotteryPhases.length, "Invalid phase index");
        return lotteryPhases[phaseIndex].totalTickets;
    }
}
```
