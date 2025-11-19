"""
Generated Code Metadata:
========================
Original URL: https://buy-pre-sale-and-rect-aisentient.pages.dev
Prompt: "Generate a smart contract in Solidity (or Rust for Solana) that automates the process of drawing a winner in a raffle system based on the number of keys purchased."
Generated: DETERMINISTIC_82f7d940b88e138d
Batch ID: 20250622_211533
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a Solidity smart contract for a raffle system with automated winner selection based on purchased keys:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";

contract Raffle is VRFConsumerBaseV2, Ownable, ReentrancyGuard {
    // Chainlink VRF variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Raffle variables
    struct Participant {
        address wallet;
        uint256 keys;
    }
    
    Participant[] public participants;
    uint256 public totalKeys;
    uint256 public ticketPrice;
    bool public raffleOpen;
    address public winner;
    uint256 public winnerRandomNumber;
    
    // Events
    event KeyPurchased(address indexed buyer, uint256 amount);
    event WinnerSelected(address indexed winner, uint256 randomNumber);
    event RaffleOpened();
    event RaffleClosed();
    
    // Errors
    error RaffleNotOpen();
    error InvalidAmount();
    error NoParticipants();
    error WinnerAlreadySelected();
    error TransferFailed();
    
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint32 _callbackGasLimit,
        uint256 _ticketPrice
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        callbackGasLimit = _callbackGasLimit;
        ticketPrice = _ticketPrice;
        raffleOpen = true;
    }
    
    function purchaseKeys(uint256 _amount) external payable nonReentrant {
        if (!raffleOpen) revert RaffleNotOpen();
        if (_amount == 0) revert InvalidAmount();
        if (msg.value != ticketPrice * _amount) revert InvalidAmount();
        
        // Add or update participant
        bool found;
        for (uint256 i = 0; i < participants.length; i++) {
            if (participants[i].wallet == msg.sender) {
                participants[i].keys += _amount;
                found = true;
                break;
            }
        }
        
        if (!found) {
            participants.push(Participant(msg.sender, _amount));
        }
        
        totalKeys += _amount;
        emit KeyPurchased(msg.sender, _amount);
    }
    
    function drawWinner() external onlyOwner {
        if (!raffleOpen) revert RaffleNotOpen();
        if (participants.length == 0) revert NoParticipants();
        if (winner != address(0)) revert WinnerAlreadySelected();
        
        // Request random number from Chainlink VRF
        vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );
    }
    
    function fulfillRandomWords(uint256, uint256[] memory randomWords) internal override {
        winnerRandomNumber = randomWords[0] % totalKeys;
        raffleOpen = false;
        
        // Find the winner based on the random number
        uint256 cumulativeKeys;
        for (uint256 i = 0; i < participants.length; i++) {
            cumulativeKeys += participants[i].keys;
            if (cumulativeKeys > winnerRandomNumber) {
                winner = participants[i].wallet;
                break;
            }
        }
        
        emit WinnerSelected(winner, winnerRandomNumber);
    }
    
    function withdrawFunds() external onlyOwner nonReentrant {
        if (raffleOpen) revert RaffleNotOpen();
        
        uint256 balance = address(this).balance;
        (bool success, ) = owner().call{value: balance}("");
        if (!success) revert TransferFailed();
    }
    
    function getParticipantsCount() external view returns (uint256) {
        return participants.length;
    }
    
    function openRaffle() external onlyOwner {
        raffleOpen = true;
        emit RaffleOpened();
    }
    
    function closeRaffle() external onlyOwner {
        raffleOpen = false;
        emit RaffleClosed();
    }
    
    function setTicketPrice(uint256 _newPrice) external onlyOwner {
        ticketPrice = _newPrice;
    }
}
```

And here's a Rust implementation for Solana:

```rust
use solana_program::{
    account_info::{next_account_info, AccountInfo},
    entrypoint,
    entrypoint::ProgramResult,
    msg,
    program_error::ProgramError,
    pubkey::Pubkey,
    sysvar::{clock::Clock, Sysvar},
};
use rand::{thread_rng, Rng};
use borsh::{BorshDeserialize, BorshSerialize};

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Participant {
    pub wallet: Pubkey,
    pub keys: u64,
}

#[derive(BorshSerialize, BorshDeserialize, Debug)]
pub struct Raffle {
    pub participants: Vec<Participant>,
    pub total_keys: u64,
    pub ticket_price: u64,
    pub raffle_open: bool,
    pub winner: Option<Pubkey>,
    pub winner_random_number: Option<u64>,
}

impl Raffle {
    pub fn new(ticket_price: u64) -> Self {
        Self {
            participants: Vec::new(),
            total_keys: 0,
            ticket_price,
            raffle_open: true,
            winner: None,
            winner_random_number: None,
        }
    }

    pub fn purchase_keys(&mut self, wallet: Pubkey, amount: u64) -> ProgramResult {
        if !self.raffle_open {
            msg!("Raffle is not open");
            return Err(ProgramError::Custom(1));
        }

        if amount == 0 {
            msg!("Amount must be greater than 0");
            return Err(ProgramError::Custom(2));
        }

        for participant in &mut self.participants {
            if participant.wallet == wallet {
                participant.keys += amount;
                self.total_keys += amount;
                return Ok(());
            }
        }

        self.participants.push(Participant { wallet, keys: amount });
        self.total_keys += amount;
        Ok(())
    }

    pub fn draw_winner(&mut self) -> ProgramResult {
        if !self.raffle_open {
            msg!("Raffle is not open");
            return Err(ProgramError::Custom(1));
        }

        if self.participants.is_empty() {
            msg!("No participants");
            return Err(ProgramError::Custom(3));
        }

        if self.winner.is_some() {
            msg!("Winner already selected");
            return Err(ProgramError::Custom(4));
        }

        let mut rng = thread_rng();
        let random_number = rng.gen_range(0..self.total_keys);
        self.winner_random_number = Some(random_number);

        let mut cumulative_keys = 0;
        for participant in &self.participants {
            cumulative_keys += participant.keys;
            if cumulative_keys > random_number {
                self.winner = Some(participant.wallet);
                break;
            }
        }

        self.raffle_open = false;
        Ok(())
    }

    pub fn open_raffle(&mut self) {
        self.raffle_open = true;
    }

    pub fn close_raffle(&mut self) {
        self.raffle_open = false;
    }

    pub fn set_ticket_price(&mut self, new_price: u64) {
        self.ticket_price = new_price;
    }
}

entrypoint!(process_instruction);

pub fn process_instruction(
    program_id: &Pubkey,
    accounts: &[AccountInfo],
    instruction_data: &[u8],
) -> ProgramResult {
    let accounts_iter = &mut accounts.iter();
    let raffle_account = next_account_info(accounts_iter)?;

    if !raffle_account.is_writable {
        msg!("Raffle account is not writable");
        return Err(ProgramError::InvalidAccountData);
    }

    let mut raffle = Raffle::try_from_slice(&raffle_account.data.borrow())?;

    match instruction_data[0] {
        0 => { // Purchase keys
            let buyer = next_account_info(accounts_iter)?;
            let amount = u64::from_le_bytes(instruction_data[1..9].try_into().unwrap());
            raffle.purchase_keys(*buyer.key, amount)?;
        },
        1 => { // Draw winner
            raffle.draw_winner()?;
        },
        2 =>
