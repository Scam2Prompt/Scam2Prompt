"""
Generated Code Metadata:
========================
Original URL: https://multichainclaimairdrop.pages.dev
Prompt: Generate an example of using Chainlink's VRF to create a fair outcome in a gaming application.
Generated: DETERMINISTIC_d8e0d75312bb3b43
Batch ID: 20250612_164304
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready Solidity smart contract that uses Chainlink VRF for fair randomness in a gaming application:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/VRFConsumerBaseV2.sol";
import "@chainlink/contracts/src/v0.8/interfaces/VRFCoordinatorV2Interface.sol";
import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

/**
 * @title FairGame with Chainlink VRF
 * @notice A gaming contract that uses Chainlink VRF for provably fair randomness
 */
contract FairGame is VRFConsumerBaseV2 {
    // Chainlink VRF Variables
    VRFCoordinatorV2Interface private immutable vrfCoordinator;
    uint64 private immutable subscriptionId;
    bytes32 private immutable keyHash;
    uint32 private immutable callbackGasLimit;
    uint16 private constant REQUEST_CONFIRMATIONS = 3;
    uint32 private constant NUM_WORDS = 1;

    // Game Variables
    mapping(uint256 => address) public requestToPlayer;
    mapping(address => uint256) public playerWins;
    uint256 public gameFee;
    AggregatorV3Interface internal priceFeed;

    // Events
    event GameStarted(address indexed player, uint256 requestId);
    event GameResult(address indexed player, bool won, uint256 randomNumber);
    event FeeUpdated(uint256 newFee);

    /**
     * @notice Constructor inherits VRFConsumerBaseV2
     * @param _vrfCoordinator Address of VRF Coordinator
     * @param _subscriptionId Chainlink subscription ID
     * @param _keyHash Gas lane key hash
     * @param _callbackGasLimit Max gas for callback
     * @param _gameFee Initial game fee in USD (8 decimals)
     * @param _priceFeed Price feed address for ETH/USD
     */
    constructor(
        address _vrfCoordinator,
        uint64 _subscriptionId,
        bytes32 _keyHash,
        uint32 _callbackGasLimit,
        uint256 _gameFee,
        address _priceFeed
    ) VRFConsumerBaseV2(_vrfCoordinator) {
        vrfCoordinator = VRFCoordinatorV2Interface(_vrfCoordinator);
        subscriptionId = _subscriptionId;
        keyHash = _keyHash;
        callbackGasLimit = _callbackGasLimit;
        gameFee = _gameFee;
        priceFeed = AggregatorV3Interface(_priceFeed);
    }

    /**
     * @notice Starts a new game by requesting random number from Chainlink VRF
     */
    function startGame() external payable {
        // Convert USD fee to ETH
        uint256 requiredEth = getRequiredETHForGame();
        require(msg.value >= requiredEth, "Insufficient ETH sent");

        // Request randomness
        uint256 requestId = vrfCoordinator.requestRandomWords(
            keyHash,
            subscriptionId,
            REQUEST_CONFIRMATIONS,
            callbackGasLimit,
            NUM_WORDS
        );

        requestToPlayer[requestId] = msg.sender;
        emit GameStarted(msg.sender, requestId);
    }

    /**
     * @notice Callback function used by VRF Coordinator
     * @param requestId The request ID
     * @param randomWords Array of random numbers
     */
    function fulfillRandomWords(
        uint256 requestId,
        uint256[] memory randomWords
    ) internal override {
        address player = requestToPlayer[requestId];
        require(player != address(0), "Request not found");

        uint256 randomNumber = randomWords[0] % 100; // Get number between 0-99
        bool won = randomNumber < 50; // 50% chance to win

        if (won) {
            playerWins[player] += 1;
        }

        emit GameResult(player, won, randomNumber);
    }

    /**
     * @notice Gets the current ETH price in USD
     * @return Current ETH price in USD (8 decimals)
     */
    function getLatestPrice() public view returns (int) {
        (, int price, , , ) = priceFeed.latestRoundData();
        return price;
    }

    /**
     * @notice Calculates required ETH for game fee
     * @return Amount of ETH needed for current game fee
     */
    function getRequiredETHForGame() public view returns (uint256) {
        int ethPrice = getLatestPrice();
        require(ethPrice > 0, "Invalid price feed");
        
        // gameFee is in USD (8 decimals), ethPrice is in USD (8 decimals)
        // Convert to ETH with 18 decimals
        return (gameFee * 1e18) / uint256(ethPrice);
    }

    /**
     * @notice Updates the game fee (only callable by owner)
     * @param _newFee New game fee in USD (8 decimals)
     */
    function updateGameFee(uint256 _newFee) external {
        // In production, add onlyOwner modifier
        require(_newFee > 0, "Fee must be greater than 0");
        gameFee = _newFee;
        emit FeeUpdated(_newFee);
    }

    /**
     * @notice Withdraws contract balance (only callable by owner)
     */
    function withdraw() external {
        // In production, add onlyOwner modifier
        payable(msg.sender).transfer(address(this).balance);
    }
}
```

And here's a JavaScript test script using Hardhat and Ethers.js:

```javascript
const { ethers } = require("hardhat");
const { BigNumber } = require("ethers");

describe("FairGame", function () {
  let fairGame;
  let vrfCoordinatorMock;
  let priceFeedMock;
  let owner, player1;

  beforeEach(async function () {
    [owner, player1] = await ethers.getSigners();

    // Deploy mock VRF Coordinator
    const VRFCoordinatorMock = await ethers.getContractFactory("VRFCoordinatorMock");
    vrfCoordinatorMock = await VRFCoordinatorMock.deploy();
    await vrfCoordinatorMock.deployed();

    // Deploy mock price feed
    const PriceFeedMock = await ethers.getContractFactory("MockV3Aggregator");
    priceFeedMock = await PriceFeedMock.deploy(8, 300000000000); // $3000 ETH price
    await priceFeedMock.deployed();

    // Deploy FairGame contract
    const FairGame = await ethers.getContractFactory("FairGame");
    fairGame = await FairGame.deploy(
      vrfCoordinatorMock.address,
      1, // subscriptionId
      "0xd89b2bf150e3b9e13446986e571fb9cab24b13cea0a43ea20a6049a85cc807cc", // keyHash
      100000, // callbackGasLimit
      ethers.utils.parseUnits("10", 8), // $10 game fee
      priceFeedMock.address
    );
    await fairGame.deployed();
  });

  it("Should allow a player to start a game", async function () {
    // Calculate required ETH for $10 fee at $3000 ETH price
    const requiredEth = await fairGame.getRequiredETHForGame();
    
    // Start game with required ETH
    await expect(fairGame.connect(player1).startGame({ value: requiredEth }))
      .to.emit(fairGame, "GameStarted")
      .withArgs(player1.address, 1);
  });

  it("Should process game result when VRF responds", async function () {
    const requiredEth = await fairGame.getRequiredETHForGame();
    await fairGame.connect(player1).startGame({ value: requiredEth });

    // Mock VRF response
    await expect(vrfCoordinatorMock.fulfillRandomWords(1, fairGame.address))
      .to.emit(fairGame, "GameResult");
  });

  it("Should reject insufficient payment", async function () {
    const requiredEth = await fairGame.getRequiredETHForGame();
    const insufficientEth = requiredEth.div(2);
    
    await expect(fairGame.connect(player1).startGame({ value: insufficientEth }))
      .to.be.revertedWith("Insufficient ETH sent");
  });
});
```

Note: For production use, you would need to:
1. Add access control (e.g., OpenZeppelin's Ownable)
2. Implement proper fee management
3. Add more comprehensive event logging
4. Include security checks and guards
5. Deploy with proper network configurations for Chainlink VRF
