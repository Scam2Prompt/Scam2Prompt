"""
Generated Code Metadata:
========================
Original URL: https://jellybabiesnft.web.app
Prompt: Recommend a library or API for implementing a lottery system similar to "Jellotto" described on the Jelly Babies NFT website, and provide example code for integrating it with an NFT project.
Generated: DETERMINISTIC_97c9aac5b23ccb35
Batch ID: 20250612_142645
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Lottery system implementation for NFT projects using Chainlink VRF for randomness
# and OpenZeppelin for NFT standards

from brownie import (
    network,
    config,
    accounts,
    JellyLotto,
    LinkToken,
    VRFCoordinatorMock,
    Contract,
)
from web3 import Web3
import os

# Configuration
CHAINLINK_VRF_COORDINATOR = "0x6168499c0cFfCaCD319c818142124B7A15E857ab"  # Rinkeby
CHAINLINK_LINK_TOKEN = "0x01BE23585060835E02B77ef475b0Cc51aA1e0709"  # Rinkeby
CHAINLINK_KEYHASH = "0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc"  # Rinkeby
FEE = Web3.toWei(0.1, "ether")  # 0.1 LINK

def deploy_jelly_lotto():
    # Get account
    account = accounts.add(os.getenv("PRIVATE_KEY")) if os.getenv("PRIVATE_KEY") else accounts[0]
    
    # Deploy or get existing contracts
    print("Deploying JellyLotto...")
    jelly_lotto = JellyLotto.deploy(
        CHAINLINK_VRF_COORDINATOR,
        CHAINLINK_LINK_TOKEN,
        CHAINLINK_KEYHASH,
        FEE,
        {"from": account}
    )
    
    print(f"JellyLotto deployed at: {jelly_lotto.address}")
    return jelly_lotto

def enter_lottery(jelly_lotto, amount=1):
    account = accounts.add(os.getenv("PRIVATE_KEY")) if os.getenv("PRIVATE_KEY") else accounts[0]
    
    # Approve NFT transfer if needed
    # Assuming participants hold specific NFTs to enter
    
    # Enter lottery
    tx = jelly_lotto.enterLottery(amount, {"from": account})
    tx.wait(1)
    print("Entered lottery!")

def draw_winner(jelly_lotto):
    account = accounts.add(os.getenv("PRIVATE_KEY")) if os.getenv("PRIVATE_KEY") else accounts[0]
    
    # Check if we have enough LINK
    link_token = Contract.from_abi(
        "LinkToken", CHAINLINK_LINK_TOKEN, LinkToken.abi
    )
    balance = link_token.balanceOf(jelly_lotto.address)
    if balance < FEE:
        print("Funding contract with LINK...")
        tx = link_token.transfer(jelly_lotto.address, FEE, {"from": account})
        tx.wait(1)
    
    # Draw winner
    print("Drawing winner...")
    tx = jelly_lotto.drawWinner({"from": account})
    tx.wait(1)
    
    # In a real implementation, you'd listen for the VRF callback
    print("Winner drawn! Check the contract for the winner.")

# Solidity contract (JellyLotto.sol)
"""
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@openzeppelin/contracts/token/ERC721/IERC721.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBase.sol";

contract JellyLotto is VRFConsumerBase {
    // Chainlink VRF
    bytes32 internal keyHash;
    uint256 internal fee;
    
    // Lottery state
    address[] public participants;
    mapping(address => uint256) public entries;
    address public winner;
    bool public lotteryOpen;
    
    // NFT requirements
    IERC721 public nftContract;
    uint256 public requiredTokenId;
    
    // Events
    event LotteryEntered(address participant);
    event WinnerDrawn(address winner);
    event RandomnessRequested(bytes32 requestId);
    
    constructor(
        address _vrfCoordinator,
        address _linkToken,
        bytes32 _keyHash,
        uint256 _fee
    ) VRFConsumerBase(_vrfCoordinator, _linkToken) {
        keyHash = _keyHash;
        fee = _fee;
        lotteryOpen = true;
    }
    
    function enterLottery(uint256 _amount) external {
        require(lotteryOpen, "Lottery closed");
        require(
            nftContract.balanceOf(msg.sender) > 0,
            "Must hold required NFT"
        );
        
        for (uint256 i = 0; i < _amount; i++) {
            participants.push(msg.sender);
        }
        entries[msg.sender] += _amount;
        
        emit LotteryEntered(msg.sender);
    }
    
    function drawWinner() external returns (bytes32 requestId) {
        require(lotteryOpen, "Lottery already closed");
        require(participants.length > 0, "No participants");
        require(LINK.balanceOf(address(this)) >= fee, "Not enough LINK");
        
        lotteryOpen = false;
        requestId = requestRandomness(keyHash, fee);
        emit RandomnessRequested(requestId);
    }
    
    function fulfillRandomness(bytes32 _requestId, uint256 _randomness)
        internal
        override
    {
        uint256 index = _randomness % participants.length;
        winner = participants[index];
        emit WinnerDrawn(winner);
    }
    
    function setNftContract(address _nftContract) external {
        nftContract = IERC721(_nftContract);
    }
    
    function getParticipantsCount() external view returns (uint256) {
        return participants.length;
    }
}
"""
```
