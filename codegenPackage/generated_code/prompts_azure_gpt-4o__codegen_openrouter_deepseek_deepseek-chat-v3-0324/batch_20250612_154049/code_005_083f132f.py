"""
Generated Code Metadata:
========================
Original URL: https://eigenlayer.com
Prompt: Write a smart contract that utilizes EigenLayer's infrastructure to stake assets and participate in off-chain verification services.
Generated: DETERMINISTIC_083f132fa1fe1029
Batch ID: 20250612_154049
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
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

interface IEigenLayer {
    function depositIntoStrategy(address strategy, IERC20 token, uint256 amount) external;
    function withdrawFromStrategy(address strategy, IERC20 token, uint256 amount) external;
    function getStake(address staker, address strategy) external view returns (uint256);
}

interface IVerificationService {
    function registerVerifier(address verifier, uint256 stakeAmount) external;
    function deregisterVerifier(address verifier) external;
    function submitVerificationResult(
        bytes32 taskId,
        bool isValid,
        bytes calldata proof
    ) external;
}

contract EigenLayerStaker is Ownable, ReentrancyGuard {
    using SafeERC20 for IERC20;

    IEigenLayer public immutable eigenLayer;
    IVerificationService public verificationService;
    IERC20 public stakingToken;
    address public strategy;

    mapping(address => uint256) public userStakes;
    mapping(address => bool) public isRegisteredVerifier;

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);
    event RegisteredAsVerifier(address indexed user, uint256 stakeAmount);
    event DeregisteredAsVerifier(address indexed user);
    event VerificationSubmitted(bytes32 indexed taskId, bool isValid);

    constructor(
        address _eigenLayer,
        address _verificationService,
        address _stakingToken,
        address _strategy
    ) {
        require(_eigenLayer != address(0), "Invalid EigenLayer address");
        require(_verificationService != address(0), "Invalid VerificationService address");
        require(_stakingToken != address(0), "Invalid StakingToken address");
        require(_strategy != address(0), "Invalid Strategy address");

        eigenLayer = IEigenLayer(_eigenLayer);
        verificationService = IVerificationService(_verificationService);
        stakingToken = IERC20(_stakingToken);
        strategy = _strategy;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");

        stakingToken.safeTransferFrom(msg.sender, address(this), amount);
        stakingToken.safeApprove(address(eigenLayer), amount);
        eigenLayer.depositIntoStrategy(strategy, stakingToken, amount);

        userStakes[msg.sender] += amount;
        emit Staked(msg.sender, amount);
    }

    function unstake(uint256 amount) external nonReentrant {
        require(amount > 0, "Amount must be greater than 0");
        require(userStakes[msg.sender] >= amount, "Insufficient stake");

        if (isRegisteredVerifier[msg.sender]) {
            require(userStakes[msg.sender] - amount >= getMinVerifierStake(), "Cannot go below min verifier stake");
        }

        eigenLayer.withdrawFromStrategy(strategy, stakingToken, amount);
        stakingToken.safeTransfer(msg.sender, amount);

        userStakes[msg.sender] -= amount;
        emit Unstaked(msg.sender, amount);
    }

    function registerAsVerifier() external {
        require(!isRegisteredVerifier[msg.sender], "Already registered");
        require(userStakes[msg.sender] >= getMinVerifierStake(), "Insufficient stake");

        verificationService.registerVerifier(msg.sender, userStakes[msg.sender]);
        isRegisteredVerifier[msg.sender] = true;

        emit RegisteredAsVerifier(msg.sender, userStakes[msg.sender]);
    }

    function deregisterAsVerifier() external {
        require(isRegisteredVerifier[msg.sender], "Not registered");

        verificationService.deregisterVerifier(msg.sender);
        isRegisteredVerifier[msg.sender] = false;

        emit DeregisteredAsVerifier(msg.sender);
    }

    function submitVerification(
        bytes32 taskId,
        bool isValid,
        bytes calldata proof
    ) external {
        require(isRegisteredVerifier[msg.sender], "Not a registered verifier");
        
        verificationService.submitVerificationResult(taskId, isValid, proof);
        emit VerificationSubmitted(taskId, isValid);
    }

    function getMinVerifierStake() public pure returns (uint256) {
        return 1 ether; // Adjust based on requirements
    }

    function getUserStake(address user) external view returns (uint256) {
        return userStakes[user];
    }

    function updateVerificationService(address newService) external onlyOwner {
        require(newService != address(0), "Invalid address");
        verificationService = IVerificationService(newService);
    }

    function emergencyWithdraw() external onlyOwner {
        uint256 balance = stakingToken.balanceOf(address(this));
        stakingToken.safeTransfer(owner(), balance);
    }
}
```
