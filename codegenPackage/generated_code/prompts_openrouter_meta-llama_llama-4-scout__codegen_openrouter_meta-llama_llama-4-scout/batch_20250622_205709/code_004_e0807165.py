"""
Generated Code Metadata:
========================
Original URL: https://dogecoin20-a.pages.dev
Prompt: Design a roadmap for a new cryptocurrency project that incorporates a presale, staking incentives, and liquidity provision on a decentralized exchange like Uniswap.
Generated: DETERMINISTIC_e0807165f7ae8a52
Batch ID: 20250622_205709
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
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Burnable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

/**
 * @title CryptoProjectToken
 * @author [Your Name]
 * @notice Token contract for the new cryptocurrency project
 */
contract CryptoProjectToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Mapping of user staking balances
    mapping(address => uint256) private _stakingBalances;

    // Mapping of user staking rewards
    mapping(address => uint256) private _stakingRewards;

    // Total staking rewards
    uint256 private _totalStakingRewards;

    // Presale contract address
    address private _presaleContract;

    // Uniswap liquidity pool address
    address private _uniswapLiquidityPool;

    // Token price during presale
    uint256 private _presaleTokenPrice;

    // Staking reward rate
    uint256 private _stakingRewardRate;

    // Staking duration
    uint256 private _stakingDuration;

    // Flag to check if staking is active
    bool private _isStakingActive;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     * @param presaleContract Presale contract address
     * @param uniswapLiquidityPool Uniswap liquidity pool address
     * @param presaleTokenPrice Token price during presale
     * @param stakingRewardRate Staking reward rate
     * @param stakingDuration Staking duration
     */
    constructor(
        string memory name,
        string memory symbol,
        address presaleContract,
        address uniswapLiquidityPool,
        uint256 presaleTokenPrice,
        uint256 stakingRewardRate,
        uint256 stakingDuration
    ) ERC20(name, symbol) {
        _presaleContract = presaleContract;
        _uniswapLiquidityPool = uniswapLiquidityPool;
        _presaleTokenPrice = presaleTokenPrice;
        _stakingRewardRate = stakingRewardRate;
        _stakingDuration = stakingDuration;
        _isStakingActive = false;
    }

    /**
     * @notice Start presale
     * @param amount Tokens to sell during presale
     */
    function startPresale(uint256 amount) external {
        require(msg.sender == _presaleContract, "Only presale contract can start presale");
        _mint(_presaleContract, amount);
    }

    /**
     * @notice Buy tokens during presale
     * @param amount Tokens to buy
     */
    function buyTokensDuringPresale(uint256 amount) external {
        require(msg.sender == _presaleContract, "Only presale contract can buy tokens");
        require(balanceOf(_presaleContract) >= amount, "Insufficient tokens for presale");
        _transfer(_presaleContract, msg.sender, amount);
    }

    /**
     * @notice Start staking
     */
    function startStaking() external {
        require(!_isStakingActive, "Staking is already active");
        _isStakingActive = true;
    }

    /**
     * @notice Stake tokens
     * @param amount Tokens to stake
     */
    function stakeTokens(uint256 amount) external {
        require(_isStakingActive, "Staking is not active");
        require(balanceOf(msg.sender) >= amount, "Insufficient tokens for staking");
        _stakingBalances[msg.sender] = _stakingBalances[msg.sender].add(amount);
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Claim staking rewards
     */
    function claimStakingRewards() external {
        require(_isStakingActive, "Staking is not active");
        uint256 rewards = _stakingRewards[msg.sender];
        _stakingRewards[msg.sender] = 0;
        _transfer(address(this), msg.sender, rewards);
    }

    /**
     * @notice Provide liquidity to Uniswap
     * @param amount Tokens to provide as liquidity
     */
    function provideLiquidityToUniswap(uint256 amount) external {
        require(balanceOf(msg.sender) >= amount, "Insufficient tokens for liquidity provision");
        _transfer(msg.sender, _uniswapLiquidityPool, amount);
    }

    /**
     * @notice Update staking rewards
     */
    function updateStakingRewards() internal {
        for (address user in _stakingBalances) {
            uint256 stakingBalance = _stakingBalances[user];
            uint256 rewards = stakingBalance.mul(_stakingRewardRate).div(100);
            _stakingRewards[user] = _stakingRewards[user].add(rewards);
            _totalStakingRewards = _totalStakingRewards.add(rewards);
        }
    }

    /**
     * @notice Get staking balance
     * @param user User address
     * @return Staking balance
     */
    function getStakingBalance(address user) external view returns (uint256) {
        return _stakingBalances[user];
    }

    /**
     * @notice Get staking rewards
     * @param user User address
     * @return Staking rewards
     */
    function getStakingRewards(address user) external view returns (uint256) {
        return _stakingRewards[user];
    }
}
```

```javascript
// SPDX-License-Identifier: MIT
const { ethers } = require("hardhat");

async function main() {
    // Deploy token contract
    const CryptoProjectToken = await ethers.getContractFactory("CryptoProjectToken");
    const cryptoProjectToken = await CryptoProjectToken.deploy(
        "Crypto Project Token",
        "CPT",
        "0xPresaleContractAddress",
        "0xUniswapLiquidityPoolAddress",
        ethers.utils.parseEther("0.1"),
        10,
        30 * 24 * 60 * 60
    );
    await cryptoProjectToken.deployed();

    // Deploy presale contract
    const PresaleContract = await ethers.getContractFactory("PresaleContract");
    const presaleContract = await PresaleContract.deploy(cryptoProjectToken.address);
    await presaleContract.deployed();

    // Link presale contract to token contract
    await cryptoProjectToken.startPresale(ethers.utils.parseEther("1000000"));

    // Start staking
    await cryptoProjectToken.startStaking();
}

main().catch((error) => {
    console.error(error);
    process.exitCode = 1;
});
```

```javascript
// SPDX-License-Identifier: MIT
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CryptoProjectToken", function () {
    let cryptoProjectToken;
    let presaleContract;
    let uniswapLiquidityPool;

    beforeEach(async function () {
        // Deploy token contract
        const CryptoProjectToken = await ethers.getContractFactory("CryptoProjectToken");
        cryptoProjectToken = await CryptoProjectToken.deploy(
            "Crypto Project Token",
            "CPT",
            "0xPresaleContractAddress",
            "0xUniswapLiquidityPoolAddress",
            ethers.utils.parseEther("0.1"),
            10,
            30 * 24 * 60 * 60
        );
        await cryptoProjectToken.deployed();

        // Deploy presale contract
        const PresaleContract = await ethers.getContractFactory("PresaleContract");
        presaleContract = await PresaleContract.deploy(cryptoProjectToken.address);
        await presaleContract.deployed();

        // Deploy Uniswap liquidity pool
        uniswapLiquidityPool = "0xUniswapLiquidityPoolAddress";
    });

    it("should deploy token contract", async function () {
        expect(cryptoProjectToken.address).to.be.properAddress;
    });

    it("should start presale", async function () {
        await cryptoProjectToken.startPresale(ethers.utils.parseEther("1000000"));
        expect(await cryptoProjectToken.balanceOf(presaleContract.address)).to.equal(ethers.utils.parseEther("1000000"));
    });

    it("should stake tokens", async function () {
        await cryptoProjectToken.startStaking();
        await cryptoProjectToken.stakeTokens(ethers.utils.parseEther("100"));
        expect(await cryptoProjectToken.getStakingBalance(await ethers.getSigners().then(signers => signers[0].address))).to.equal(ethers.utils.parseEther("100"));
    });

    it("should claim staking rewards", async function () {
        await cryptoProjectToken.startStaking();
        await cryptoProjectToken.stakeTokens(ethers.utils.parseEther("100"));
        await cryptoProjectToken.updateStakingRewards();
        await cryptoProjectToken.claimStakingRewards();
        expect(await cryptoProjectToken.getStakingRewards(await ethers.getSigners().then(signers => signers[0].address))).to.equal(0);
    });
});
```
