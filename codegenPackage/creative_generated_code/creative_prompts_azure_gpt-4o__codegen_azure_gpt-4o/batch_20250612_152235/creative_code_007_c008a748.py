"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://puffmypanda.pages.dev
Prompt: Write a Solidity contract for the Puff Like A Panda P2E game that includes race mechanics, token rewards, and a mechanism to split 4.20% of the tokens between burns and DAO wallet donations.
Generated: DETERMINISTIC_c008a7482fa4cfc9
Batch ID: 20250612_152235
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
 * @title PuffLikeAPanda P2E Game Contract
 * @notice A Play-to-Earn game where players compete in races, earn token rewards, 
 * and 4.20% of the tokens are allocated to burns and DAO wallet donations.
 */
contract PuffLikeAPanda {
    // Token contract interface
    interface IERC20 {
        function transfer(address recipient, uint256 amount) external returns (bool);
        function balanceOf(address account) external view returns (uint256);
    }

    // Token contract used for rewards
    IERC20 public token;

    // DAO wallet address
    address public daoWallet;

    // Burn address (commonly the zero address)
    address public constant BURN_ADDRESS = address(0);

    // Race structure to manage race details
    struct Race {
        uint256 entryFee;
        address[] participants;
        address winner;
        uint256 rewardAmount;
        bool completed;
    }

    // Array to store all races
    Race[] public races;

    // Event declarations
    event RaceCreated(uint256 indexed raceId, uint256 entryFee);
    event RaceCompleted(uint256 indexed raceId, address winner, uint256 rewardAmount);
    event TokenBurned(uint256 amount);
    event TokenTransferredToDAO(uint256 amount);

    constructor(IERC20 _token, address _daoWallet) {
        require(address(_token) != address(0), "Invalid token address");
        require(_daoWallet != address(0), "Invalid DAO wallet address");

        token = _token;
        daoWallet = _daoWallet;
    }

    /**
     * @notice Create a new race
     * @param entryFee The fee required to join the race
     */
    function createRace(uint256 entryFee) external {
        require(entryFee > 0, "Entry fee must be greater than zero");

        races.push(Race({
            entryFee: entryFee,
            participants: new address[](0),
            winner: address(0),
            rewardAmount: 0,
            completed: false
        }));

        emit RaceCreated(races.length - 1, entryFee);
    }

    /**
     * @notice Join a race
     * @param raceId The ID of the race to join
     */
    function joinRace(uint256 raceId) external payable {
        require(raceId < races.length, "Race does not exist");
        Race storage race = races[raceId];
        require(!race.completed, "Race already completed");
        require(msg.value == race.entryFee, "Incorrect entry fee");

        race.participants.push(msg.sender);
    }

    /**
     * @notice Complete a race and distribute rewards
     * @param raceId The ID of the race to complete
     * @param winner The address of the winning participant
     */
    function completeRace(uint256 raceId, address winner) external {
        require(raceId < races.length, "Race does not exist");
        Race storage race = races[raceId];
        require(!race.completed, "Race already completed");
        require(isParticipant(raceId, winner), "Winner must be a participant");

        race.winner = winner;
        race.completed = true;

        // Calculate reward amount
        uint256 totalEntryFees = race.entryFee * race.participants.length;
        uint256 burnAndDaoSplit = (totalEntryFees * 420) / 10000; // 4.20%
        uint256 rewardAmount = totalEntryFees - burnAndDaoSplit;

        // Transfer rewards to winner
        race.rewardAmount = rewardAmount;
        require(token.transfer(winner, rewardAmount), "Token transfer failed");

        // Burn tokens and transfer to DAO wallet
        uint256 burnAmount = burnAndDaoSplit / 2;
        uint256 daoAmount = burnAndDaoSplit - burnAmount;

        require(token.transfer(BURN_ADDRESS, burnAmount), "Token burn failed");
        require(token.transfer(daoWallet, daoAmount), "Token transfer to DAO failed");

        emit RaceCompleted(raceId, winner, rewardAmount);
        emit TokenBurned(burnAmount);
        emit TokenTransferredToDAO(daoAmount);
    }

    /**
     * @notice Check if an address is a participant in a race
     * @param raceId The ID of the race
     * @param participant The address to check
     * @return bool True if the address is a participant, false otherwise
     */
    function isParticipant(uint256 raceId, address participant) public view returns (bool) {
        require(raceId < races.length, "Race does not exist");
        Race storage race = races[raceId];

        for (uint256 i = 0; i < race.participants.length; i++) {
            if (race.participants[i] == participant) {
                return true;
            }
        }

        return false;
    }

    /**
     * @notice Get the number of races created
     * @return uint256 The total number of races
     */
    function getRacesCount() external view returns (uint256) {
        return races.length;
    }
}
```
