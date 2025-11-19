"""
Generated Code Metadata:
========================
Original URL: https://crudo-protocol.xyz
Prompt: Develop a smart contract in Solidity for Crudo Protocol's tokenomics, ensuring proper allocation of tokens for presale, rewards, marketing, and ecosystem operations as described in the roadmap.
Generated: DETERMINISTIC_9470c3f5f5cf9f3a
Batch ID: 20250612_154902
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
 * @title Crudo Protocol Token
 * @author [Your Name]
 * @notice Token contract for Crudo Protocol
 */
contract CrudoToken is ERC20, ERC20Burnable, ReentrancyGuard {
    using SafeMath for uint256;

    // Tokenomics parameters
    uint256 public constant PRESALE_ALLOCATION = 15; // 15%
    uint256 public constant REWARDS_ALLOCATION = 20; // 20%
    uint256 public constant MARKETING_ALLOCATION = 10; // 10%
    uint256 public constant ECOSYSTEM_ALLOCATION = 55; // 55%

    // Presale parameters
    uint256 public presaleStart;
    uint256 public presaleEnd;
    uint256 public presaleTokens;
    mapping(address => uint256) public presaleBalances;

    // Rewards parameters
    uint256 public rewardsStart;
    uint256 public rewardsEnd;
    uint256 public rewardsTokens;
    mapping(address => uint256) public rewardsBalances;

    // Marketing parameters
    address public marketingWallet;
    uint256 public marketingTokens;

    // Ecosystem parameters
    address public ecosystemWallet;
    uint256 public ecosystemTokens;

    // Roles
    mapping(address => bool) public isPresaleParticipant;
    mapping(address => bool) public isRewardsParticipant;

    /**
     * @notice Constructor
     * @param name Token name
     * @param symbol Token symbol
     */
    constructor(string memory name, string memory symbol) ERC20(name, symbol) {
        // Initialize tokenomics
        uint256 totalSupply = 100 * 10**18; // 100 million tokens

        // Presale allocation
        presaleTokens = totalSupply.mul(PRESALE_ALLOCATION).div(100);
        _mint(msg.sender, presaleTokens);

        // Rewards allocation
        rewardsTokens = totalSupply.mul(REWARDS_ALLOCATION).div(100);
        _mint(msg.sender, rewardsTokens);

        // Marketing allocation
        marketingTokens = totalSupply.mul(MARKETING_ALLOCATION).div(100);
        marketingWallet = msg.sender;

        // Ecosystem allocation
        ecosystemTokens = totalSupply.mul(ECOSYSTEM_ALLOCATION).div(100);
        ecosystemWallet = msg.sender;
    }

    /**
     * @notice Start presale
     * @param start Presale start time
     * @param end Presale end time
     */
    function startPresale(uint256 start, uint256 end) public onlyOwner {
        require(presaleStart == 0, "Presale already started");
        presaleStart = start;
        presaleEnd = end;
    }

    /**
     * @notice Participate in presale
     * @param amount Token amount to purchase
     */
    function participateInPresale(uint256 amount) public {
        require(presaleStart > 0, "Presale not started");
        require(block.timestamp >= presaleStart && block.timestamp <= presaleEnd, "Presale not active");
        require(amount > 0, "Invalid amount");

        presaleBalances[msg.sender] = presaleBalances[msg.sender].add(amount);
        isPresaleParticipant[msg.sender] = true;

        // Transfer tokens from presale allocation
        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Claim presale tokens
     */
    function claimPresaleTokens() public {
        require(isPresaleParticipant[msg.sender], "Not a presale participant");
        require(presaleBalances[msg.sender] > 0, "No presale tokens to claim");

        uint256 tokens = presaleBalances[msg.sender];
        presaleBalances[msg.sender] = 0;

        _transfer(address(this), msg.sender, tokens);
    }

    /**
     * @notice Start rewards
     * @param start Rewards start time
     * @param end Rewards end time
     */
    function startRewards(uint256 start, uint256 end) public onlyOwner {
        require(rewardsStart == 0, "Rewards already started");
        rewardsStart = start;
        rewardsEnd = end;
    }

    /**
     * @notice Participate in rewards
     */
    function participateInRewards() public {
        require(rewardsStart > 0, "Rewards not started");
        require(block.timestamp >= rewardsStart && block.timestamp <= rewardsEnd, "Rewards not active");

        isRewardsParticipant[msg.sender] = true;
    }

    /**
     * @notice Claim rewards tokens
     * @param amount Token amount to claim
     */
    function claimRewardsTokens(uint256 amount) public {
        require(isRewardsParticipant[msg.sender], "Not a rewards participant");
        require(rewardsBalances[msg.sender].add(amount) <= rewardsTokens, "Insufficient rewards tokens");

        rewardsBalances[msg.sender] = rewardsBalances[msg.sender].add(amount);

        _transfer(msg.sender, address(this), amount);
    }

    /**
     * @notice Transfer marketing tokens
     * @param amount Token amount to transfer
     */
    function transferMarketingTokens(uint256 amount) public onlyOwner {
        require(marketingTokens >= amount, "Insufficient marketing tokens");

        _transfer(address(this), marketingWallet, amount);
    }

    /**
     * @notice Transfer ecosystem tokens
     * @param amount Token amount to transfer
     */
    function transferEcosystemTokens(uint256 amount) public onlyOwner {
        require(ecosystemTokens >= amount, "Insufficient ecosystem tokens");

        _transfer(address(this), ecosystemWallet, amount);
    }

    modifier onlyOwner {
        require(msg.sender == owner(), "Only the owner can call this function");
        _;
    }
}
```
