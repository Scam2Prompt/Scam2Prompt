"""
Generated Code Metadata:
========================
Original URL: https://synspad.firebaseapp.com
Prompt: "Create a smart contract in Solidity for launching IDOs on multiple blockchain platforms with validation and non-custodial features."
Generated: DETERMINISTIC_b14d65aa1843833f
Batch ID: 20250622_212859
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

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract MultiChainIDO is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    struct IDOInfo {
        uint256 id;
        address tokenAddress;
        uint256 tokenPrice;
        uint256 hardCap;
        uint256 softCap;
        uint256 minContribution;
        uint256 maxContribution;
        uint256 startTime;
        uint256 endTime;
        uint256 totalRaised;
        uint256 totalTokensSold;
        bool isActive;
        bool isWhitelistEnabled;
    }

    struct Contribution {
        address contributor;
        uint256 amount;
        uint256 tokensBought;
        bool claimed;
    }

    mapping(uint256 => IDOInfo) public idos;
    mapping(uint256 => mapping(address => bool)) public whitelist;
    mapping(uint256 => mapping(address => Contribution)) public contributions;
    mapping(address => bool) public validTokens;
    mapping(uint256 => bool) public chainSupported;

    uint256 public idoCount;
    uint256 public feePercentage; // Platform fee percentage (1 = 1%)
    address public feeWallet;

    event IDOCreated(
        uint256 id,
        address tokenAddress,
        uint256 tokenPrice,
        uint256 hardCap,
        uint256 softCap,
        uint256 startTime,
        uint256 endTime
    );
    event Contributed(uint256 idoId, address contributor, uint256 amount, uint256 tokens);
    event TokensClaimed(uint256 idoId, address contributor, uint256 amount);
    event FundsWithdrawn(uint256 idoId, uint256 amount);
    event WhitelistUpdated(uint256 idoId, address[] addresses, bool isWhitelisted);
    event IDOStatusChanged(uint256 idoId, bool isActive);

    constructor(uint256 _feePercentage, address _feeWallet) {
        require(_feePercentage <= 100, "Fee percentage cannot exceed 100");
        require(_feeWallet != address(0), "Invalid fee wallet address");
        
        feePercentage = _feePercentage;
        feeWallet = _feeWallet;
    }

    modifier onlyActiveIDO(uint256 _idoId) {
        require(idos[_idoId].isActive, "IDO is not active");
        _;
    }

    modifier onlyValidIDO(uint256 _idoId) {
        require(_idoId <= idoCount && _idoId != 0, "Invalid IDO ID");
        _;
    }

    modifier onlyDuringIDO(uint256 _idoId) {
        require(block.timestamp >= idos[_idoId].startTime && block.timestamp <= idos[_idoId].endTime, "IDO not active");
        _;
    }

    function createIDO(
        address _tokenAddress,
        uint256 _tokenPrice,
        uint256 _hardCap,
        uint256 _softCap,
        uint256 _minContribution,
        uint256 _maxContribution,
        uint256 _startTime,
        uint256 _endTime,
        bool _isWhitelistEnabled
    ) external onlyOwner {
        require(_tokenAddress != address(0), "Invalid token address");
        require(_tokenPrice > 0, "Token price must be greater than 0");
        require(_hardCap > _softCap, "Hard cap must be greater than soft cap");
        require(_minContribution <= _maxContribution, "Min contribution must be <= max contribution");
        require(_startTime > block.timestamp, "Start time must be in the future");
        require(_endTime > _startTime, "End time must be after start time");

        idoCount++;
        idos[idoCount] = IDOInfo({
            id: idoCount,
            tokenAddress: _tokenAddress,
            tokenPrice: _tokenPrice,
            hardCap: _hardCap,
            softCap: _softCap,
            minContribution: _minContribution,
            maxContribution: _maxContribution,
            startTime: _startTime,
            endTime: _endTime,
            totalRaised: 0,
            totalTokensSold: 0,
            isActive: true,
            isWhitelistEnabled: _isWhitelistEnabled
        });

        emit IDOCreated(
            idoCount,
            _tokenAddress,
            _tokenPrice,
            _hardCap,
            _softCap,
            _startTime,
            _endTime
        );
    }

    function contribute(uint256 _idoId) external payable onlyValidIDO(_idoId) onlyActiveIDO(_idoId) onlyDuringIDO(_idoId) nonReentrant {
        IDOInfo storage ido = idos[_idoId];
        require(msg.value >= ido.minContribution, "Contribution below minimum");
        require(msg.value <= ido.maxContribution, "Contribution exceeds maximum");
        require(ido.totalRaised.add(msg.value) <= ido.hardCap, "Hard cap reached");
        
        if (ido.isWhitelistEnabled) {
            require(whitelist[_idoId][msg.sender], "Address not whitelisted");
        }

        uint256 tokensToBuy = msg.value.div(ido.tokenPrice);
        ido.totalRaised = ido.totalRaised.add(msg.value);
        ido.totalTokensSold = ido.totalTokensSold.add(tokensToBuy);

        Contribution storage userContribution = contributions[_idoId][msg.sender];
        userContribution.contributor = msg.sender;
        userContribution.amount = userContribution.amount.add(msg.value);
        userContribution.tokensBought = userContribution.tokensBought.add(tokensToBuy);

        emit Contributed(_idoId, msg.sender, msg.value, tokensToBuy);
    }

    function claimTokens(uint256 _idoId) external onlyValidIDO(_idoId) nonReentrant {
        IDOInfo storage ido = idos[_idoId];
        require(block.timestamp > ido.endTime, "IDO not ended yet");
        require(ido.totalRaised >= ido.softCap, "Soft cap not reached");
        
        Contribution storage userContribution = contributions[_idoId][msg.sender];
        require(userContribution.tokensBought > 0, "No tokens to claim");
        require(!userContribution.claimed, "Tokens already claimed");

        userContribution.claimed = true;
        IERC20 token = IERC20(ido.tokenAddress);
        require(token.transfer(msg.sender, userContribution.tokensBought), "Token transfer failed");

        emit TokensClaimed(_idoId, msg.sender, userContribution.tokensBought);
    }

    function withdrawFunds(uint256 _idoId) external onlyOwner onlyValidIDO(_idoId) {
        IDOInfo storage ido = idos[_idoId];
        require(block.timestamp > ido.endTime, "IDO not ended yet");
        require(ido.totalRaised >= ido.softCap, "Soft cap not reached");

        uint256 balance = address(this).balance;
        uint256 feeAmount = balance.mul(feePercentage).div(100);
        uint256 remainingAmount = balance.sub(feeAmount);

        (bool feeSuccess, ) = feeWallet.call{value: feeAmount}("");
        require(feeSuccess, "Fee transfer failed");

        (bool success, ) = owner().call{value: remainingAmount}("");
        require(success, "Funds transfer failed");

        emit FundsWithdrawn(_idoId, remainingAmount);
    }

    function refund(uint256 _idoId) external onlyValidIDO(_idoId) nonReentrant {
        IDOInfo storage ido = idos[_idoId];
        require(block.timestamp > ido.endTime, "IDO not ended yet");
        require(ido.totalRaised < ido.softCap, "Soft cap reached - no refunds");

        Contribution storage userContribution = contributions[_idoId][msg.sender];
        require(userContribution.amount > 0, "No contribution to refund");
        require(!userContribution.claimed, "Already refunded");

        userContribution.claimed = true;
        (bool success, ) = msg.sender.call{value: userContribution.amount}("");
        require(success, "Refund failed");
    }

    function updateWhitelist(uint256 _idoId, address[] calldata _addresses, bool _isWhitelisted) external onlyOwner onlyValidIDO(_idoId) {
        IDOInfo storage ido = idos[_idoId];
        require(ido.isWhitelistEnabled, "Whitelist not enabled for this IDO");

        for (uint256 i = 0; i < _addresses.length; i++) {
            whitelist[_idoId][_addresses[i]] = _isWhitelisted;
        }

        emit WhitelistUpdated(_idoId, _addresses, _isWh
