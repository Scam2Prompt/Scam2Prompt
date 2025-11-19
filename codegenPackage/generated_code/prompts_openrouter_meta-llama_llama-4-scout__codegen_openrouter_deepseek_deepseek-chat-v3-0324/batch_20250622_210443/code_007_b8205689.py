"""
Generated Code Metadata:
========================
Original URL: https://memekombat-in.pages.dev
Prompt: Create a blockchain-based betting system for a gaming platform, using a library like Web3.js and a smart contract written in Solidity.
Generated: DETERMINISTIC_b820568962c79823
Batch ID: 20250622_210443
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

contract BettingPlatform {
    struct Bet {
        address bettor;
        uint256 amount;
        uint256 gameId;
        uint256 prediction;
        bool settled;
    }

    struct Game {
        uint256 id;
        string name;
        uint256 startTime;
        uint256 endTime;
        uint256 result;
        bool isResultSet;
    }

    address public owner;
    uint256 public feePercentage; // Platform fee in percentage (e.g., 5 for 5%)
    uint256 public nextGameId;
    uint256 public nextBetId;

    mapping(uint256 => Game) public games;
    mapping(uint256 => Bet) public bets;
    mapping(uint256 => uint256[]) public gameBets;

    event GameCreated(uint256 gameId, string name, uint256 startTime, uint256 endTime);
    event BetPlaced(uint256 betId, address bettor, uint256 gameId, uint256 amount, uint256 prediction);
    event GameResultSet(uint256 gameId, uint256 result);
    event BetSettled(uint256 betId, address winner, uint256 amountWon);

    modifier onlyOwner() {
        require(msg.sender == owner, "Only owner can call this function");
        _;
    }

    modifier gameExists(uint256 gameId) {
        require(games[gameId].id != 0, "Game does not exist");
        _;
    }

    modifier betExists(uint256 betId) {
        require(bets[betId].bettor != address(0), "Bet does not exist");
        _;
    }

    constructor(uint256 _feePercentage) {
        owner = msg.sender;
        feePercentage = _feePercentage;
    }

    function createGame(
        string memory _name,
        uint256 _startTime,
        uint256 _endTime
    ) external onlyOwner {
        require(_startTime < _endTime, "Start time must be before end time");
        require(_endTime > block.timestamp, "End time must be in the future");

        uint256 gameId = nextGameId++;
        games[gameId] = Game({
            id: gameId,
            name: _name,
            startTime: _startTime,
            endTime: _endTime,
            result: 0,
            isResultSet: false
        });

        emit GameCreated(gameId, _name, _startTime, _endTime);
    }

    function placeBet(uint256 _gameId, uint256 _prediction) external payable gameExists(_gameId) {
        Game memory game = games[_gameId];
        require(block.timestamp >= game.startTime, "Game has not started yet");
        require(block.timestamp < game.endTime, "Game has ended");
        require(msg.value > 0, "Bet amount must be greater than 0");

        uint256 betId = nextBetId++;
        bets[betId] = Bet({
            bettor: msg.sender,
            amount: msg.value,
            gameId: _gameId,
            prediction: _prediction,
            settled: false
        });

        gameBets[_gameId].push(betId);
        emit BetPlaced(betId, msg.sender, _gameId, msg.value, _prediction);
    }

    function setGameResult(uint256 _gameId, uint256 _result) external onlyOwner gameExists(_gameId) {
        Game storage game = games[_gameId];
        require(block.timestamp >= game.endTime, "Game has not ended yet");
        require(!game.isResultSet, "Result already set");

        game.result = _result;
        game.isResultSet = true;

        emit GameResultSet(_gameId, _result);
    }

    function settleBet(uint256 _betId) external betExists(_betId) {
        Bet storage bet = bets[_betId];
        require(!bet.settled, "Bet already settled");

        Game memory game = games[bet.gameId];
        require(game.isResultSet, "Game result not set yet");

        bet.settled = true;

        if (bet.prediction == game.result) {
            uint256 fee = (bet.amount * feePercentage) / 100;
            uint256 winnings = bet.amount * 2 - fee;
            payable(bet.bettor).transfer(winnings);
            emit BetSettled(_betId, bet.bettor, winnings);
        }
    }

    function withdrawFees() external onlyOwner {
        uint256 balance = address(this).balance;
        require(balance > 0, "No fees to withdraw");
        payable(owner).transfer(balance);
    }

    function getGameBets(uint256 _gameId) external view returns (uint256[] memory) {
        return gameBets[_gameId];
    }
}
```

```javascript
const Web3 = require('web3');
const contractABI = require('./BettingPlatformABI.json');

class BettingSystem {
    constructor(web3Provider, contractAddress) {
        this.web3 = new Web3(web3Provider);
        this.contract = new this.web3.eth.Contract(
            contractABI,
            contractAddress
        );
        this.account = null;
    }

    async connectAccount() {
        const accounts = await this.web3.eth.requestAccounts();
        this.account = accounts[0];
        return this.account;
    }

    async createGame(name, startTime, endTime) {
        try {
            const result = await this.contract.methods
                .createGame(name, startTime, endTime)
                .send({ from: this.account });
            return result;
        } catch (error) {
            console.error("Error creating game:", error);
            throw error;
        }
    }

    async placeBet(gameId, prediction, amount) {
        try {
            const result = await this.contract.methods
                .placeBet(gameId, prediction)
                .send({ from: this.account, value: amount });
            return result;
        } catch (error) {
            console.error("Error placing bet:", error);
            throw error;
        }
    }

    async setGameResult(gameId, result) {
        try {
            const resultTx = await this.contract.methods
                .setGameResult(gameId, result)
                .send({ from: this.account });
            return resultTx;
        } catch (error) {
            console.error("Error setting game result:", error);
            throw error;
        }
    }

    async settleBet(betId) {
        try {
            const result = await this.contract.methods
                .settleBet(betId)
                .send({ from: this.account });
            return result;
        } catch (error) {
            console.error("Error settling bet:", error);
            throw error;
        }
    }

    async getGameDetails(gameId) {
        try {
            return await this.contract.methods.games(gameId).call();
        } catch (error) {
            console.error("Error getting game details:", error);
            throw error;
        }
    }

    async getBetDetails(betId) {
        try {
            return await this.contract.methods.bets(betId).call();
        } catch (error) {
            console.error("Error getting bet details:", error);
            throw error;
        }
    }

    async getGameBets(gameId) {
        try {
            return await this.contract.methods.getGameBets(gameId).call();
        } catch (error) {
            console.error("Error getting game bets:", error);
            throw error;
        }
    }
}

module.exports = BettingSystem;
```
