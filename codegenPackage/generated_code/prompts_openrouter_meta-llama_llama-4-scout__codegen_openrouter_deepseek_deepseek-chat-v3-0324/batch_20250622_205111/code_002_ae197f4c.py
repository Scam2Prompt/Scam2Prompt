"""
Generated Code Metadata:
========================
Original URL: https://bafybeibp22amvhhrdkiajahcte2faf5d3vecbroua5yhnhk76jnpibn4de.ipfs.dweb.link
Prompt: Design a decentralized application (dApp) that leverages Particle Network's wallet abstraction and dual staking mechanism to enable secure and seamless interactions between users and multiple blockchain ecosystems.
Generated: DETERMINISTIC_ae197f4c94469630
Batch ID: 20250622_205111
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface IParticleWallet {
    function verifySignature(bytes32 messageHash, bytes memory signature) external view returns (bool);
    function getWalletAddress(bytes memory signature) external view returns (address);
}

contract ParticleDApp is Ownable, ReentrancyGuard {
    using SafeMath for uint256;

    // Structs
    struct Stake {
        uint256 amount;
        uint256 timestamp;
        uint256 unlockTime;
    }

    struct DualStake {
        Stake nativeStake;
        Stake tokenStake;
    }

    // State variables
    IParticleWallet public particleWallet;
    IERC20 public stakingToken;
    
    mapping(address => DualStake) public stakes;
    mapping(address => uint256) public rewards;
    
    uint256 public nativeStakingAPY;
    uint256 public tokenStakingAPY;
    uint256 public minStakeDuration;
    uint256 public totalStakedNative;
    uint256 public totalStakedTokens;

    // Events
    event Staked(address indexed user, uint256 nativeAmount, uint256 tokenAmount);
    event Unstaked(address indexed user, uint256 nativeAmount, uint256 tokenAmount);
    event RewardClaimed(address indexed user, uint256 amount);
    event WalletVerified(address indexed user, bytes signature);

    // Constructor
    constructor(
        address _particleWallet,
        address _stakingToken,
        uint256 _nativeAPY,
        uint256 _tokenAPY,
        uint256 _minStakeDuration
    ) {
        require(_particleWallet != address(0), "Invalid Particle Wallet address");
        require(_stakingToken != address(0), "Invalid token address");
        
        particleWallet = IParticleWallet(_particleWallet);
        stakingToken = IERC20(_stakingToken);
        nativeStakingAPY = _nativeAPY;
        tokenStakingAPY = _tokenAPY;
        minStakeDuration = _minStakeDuration;
    }

    // Modifiers
    modifier validStakeDuration(uint256 duration) {
        require(duration >= minStakeDuration, "Stake duration too short");
        _;
    }

    modifier onlyVerifiedUser(bytes memory signature) {
        bytes32 messageHash = keccak256(abi.encodePacked(msg.sender));
        require(particleWallet.verifySignature(messageHash, signature), "Invalid signature");
        _;
    }

    // External functions
    function stake(
        uint256 nativeAmount,
        uint256 tokenAmount,
        uint256 duration,
        bytes memory signature
    ) external payable nonReentrant validStakeDuration(duration) onlyVerifiedUser(signature) {
        require(nativeAmount > 0 || tokenAmount > 0, "Must stake at least one asset");
        
        if (nativeAmount > 0) {
            require(msg.value == nativeAmount, "Incorrect native token amount");
            _stakeNative(nativeAmount, duration);
        }
        
        if (tokenAmount > 0) {
            require(stakingToken.transferFrom(msg.sender, address(this), tokenAmount), "Token transfer failed");
            _stakeToken(tokenAmount, duration);
        }

        emit Staked(msg.sender, nativeAmount, tokenAmount);
    }

    function unstake(bytes memory signature) external nonReentrant onlyVerifiedUser(signature) {
        DualStake storage userStake = stakes[msg.sender];
        require(userStake.nativeStake.amount > 0 || userStake.tokenStake.amount > 0, "No stakes found");
        
        uint256 nativeAmount = 0;
        uint256 tokenAmount = 0;
        
        if (userStake.nativeStake.amount > 0 && block.timestamp >= userStake.nativeStake.unlockTime) {
            nativeAmount = userStake.nativeStake.amount;
            _calculateAndAddReward(nativeAmount, userStake.nativeStake.timestamp, true);
            totalStakedNative = totalStakedNative.sub(nativeAmount);
            userStake.nativeStake.amount = 0;
            
            (bool success, ) = msg.sender.call{value: nativeAmount}("");
            require(success, "Native token transfer failed");
        }
        
        if (userStake.tokenStake.amount > 0 && block.timestamp >= userStake.tokenStake.unlockTime) {
            tokenAmount = userStake.tokenStake.amount;
            _calculateAndAddReward(tokenAmount, userStake.tokenStake.timestamp, false);
            totalStakedTokens = totalStakedTokens.sub(tokenAmount);
            userStake.tokenStake.amount = 0;
            
            require(stakingToken.transfer(msg.sender, tokenAmount), "Token transfer failed");
        }
        
        emit Unstaked(msg.sender, nativeAmount, tokenAmount);
    }

    function claimReward(bytes memory signature) external nonReentrant onlyVerifiedUser(signature) {
        uint256 reward = rewards[msg.sender];
        require(reward > 0, "No rewards to claim");
        
        rewards[msg.sender] = 0;
        require(stakingToken.transfer(msg.sender, reward), "Reward transfer failed");
        
        emit RewardClaimed(msg.sender, reward);
    }

    function verifyWallet(bytes memory signature) external {
        address walletAddress = particleWallet.getWalletAddress(signature);
        require(walletAddress != address(0), "Invalid wallet address");
        emit WalletVerified(msg.sender, signature);
    }

    // Internal functions
    function _stakeNative(uint256 amount, uint256 duration) internal {
        DualStake storage userStake = stakes[msg.sender];
        
        if (userStake.nativeStake.amount > 0) {
            _calculateAndAddReward(userStake.nativeStake.amount, userStake.nativeStake.timestamp, true);
        }
        
        userStake.nativeStake = Stake({
            amount: userStake.nativeStake.amount.add(amount),
            timestamp: block.timestamp,
            unlockTime: block.timestamp.add(duration)
        });
        
        totalStakedNative = totalStakedNative.add(amount);
    }

    function _stakeToken(uint256 amount, uint256 duration) internal {
        DualStake storage userStake = stakes[msg.sender];
        
        if (userStake.tokenStake.amount > 0) {
            _calculateAndAddReward(userStake.tokenStake.amount, userStake.tokenStake.timestamp, false);
        }
        
        userStake.tokenStake = Stake({
            amount: userStake.tokenStake.amount.add(amount),
            timestamp: block.timestamp,
            unlockTime: block.timestamp.add(duration)
        });
        
        totalStakedTokens = totalStakedTokens.add(amount);
    }

    function _calculateAndAddReward(uint256 amount, uint256 timestamp, bool isNative) internal {
        uint256 timeStaked = block.timestamp.sub(timestamp);
        uint256 apy = isNative ? nativeStakingAPY : tokenStakingAPY;
        
        uint256 reward = amount.mul(apy).mul(timeStaked).div(365 days).div(100);
        rewards[msg.sender] = rewards[msg.sender].add(reward);
    }

    // Owner functions
    function updateAPY(uint256 newNativeAPY, uint256 newTokenAPY) external onlyOwner {
        nativeStakingAPY = newNativeAPY;
        tokenStakingAPY = newTokenAPY;
    }

    function updateMinStakeDuration(uint256 newDuration) external onlyOwner {
        minStakeDuration = newDuration;
    }

    function emergencyWithdraw(address tokenAddress) external onlyOwner {
        if (tokenAddress == address(0)) {
            payable(owner()).transfer(address(this).balance);
        } else {
            IERC20 token = IERC20(tokenAddress);
            token.transfer(owner(), token.balanceOf(address(this)));
        }
    }
}
```
