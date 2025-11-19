"""
Generated Code Metadata:
========================
Original URL: https://bondex-app.pages.dev
Prompt: Develop a smart contract for a referral bounty system, enabling recruiters to earn rewards for referring candidates to Web3 job openings on a platform like Bondex.
Generated: DETERMINISTIC_04ee4f98122ea0d7
Batch ID: 20250622_204851
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
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";

contract ReferralBountySystem is Ownable, ReentrancyGuard {
    // Struct to store referral information
    struct Referral {
        address recruiter;
        address candidate;
        uint256 jobId;
        uint256 bountyAmount;
        bool isPaid;
        uint256 timestamp;
    }

    // Mapping to track referrals by ID
    mapping(uint256 => Referral) public referrals;
    
    // Mapping to track recruiter earnings
    mapping(address => uint256) public recruiterEarnings;
    
    // Counter for referral IDs
    uint256 public referralCount;
    
    // The token used for bounty payments
    IERC20 public bountyToken;
    
    // Platform fee percentage (e.g., 1000 = 10%)
    uint256 public platformFee;
    
    // Events
    event ReferralCreated(
        uint256 indexed referralId,
        address indexed recruiter,
        address indexed candidate,
        uint256 jobId,
        uint256 bountyAmount
    );
    
    event BountyPaid(
        uint256 indexed referralId,
        address indexed recruiter,
        uint256 amount,
        uint256 platformFee
    );
    
    event PlatformFeeUpdated(uint256 newFee);
    event BountyTokenUpdated(address newToken);

    /**
     * @dev Constructor
     * @param _bountyToken Address of the ERC20 token used for bounty payments
     * @param _platformFee Platform fee percentage (e.g., 1000 = 10%)
     */
    constructor(address _bountyToken, uint256 _platformFee) {
        require(_bountyToken != address(0), "Invalid token address");
        require(_platformFee <= 10000, "Fee cannot exceed 100%");
        
        bountyToken = IERC20(_bountyToken);
        platformFee = _platformFee;
    }

    /**
     * @dev Create a new referral
     * @param _recruiter Address of the recruiter making the referral
     * @param _candidate Address of the referred candidate
     * @param _jobId ID of the job being referred to
     * @param _bountyAmount Amount of bounty for successful referral
     */
    function createReferral(
        address _recruiter,
        address _candidate,
        uint256 _jobId,
        uint256 _bountyAmount
    ) external onlyOwner {
        require(_recruiter != address(0), "Invalid recruiter address");
        require(_candidate != address(0), "Invalid candidate address");
        require(_bountyAmount > 0, "Bounty amount must be positive");
        
        referralCount++;
        referrals[referralCount] = Referral({
            recruiter: _recruiter,
            candidate: _candidate,
            jobId: _jobId,
            bountyAmount: _bountyAmount,
            isPaid: false,
            timestamp: block.timestamp
        });
        
        emit ReferralCreated(referralCount, _recruiter, _candidate, _jobId, _bountyAmount);
    }

    /**
     * @dev Pay bounty to recruiter for successful referral
     * @param _referralId ID of the referral to pay out
     */
    function payBounty(uint256 _referralId) external nonReentrant {
        require(_referralId > 0 && _referralId <= referralCount, "Invalid referral ID");
        
        Referral storage referral = referrals[_referralId];
        require(!referral.isPaid, "Bounty already paid");
        
        uint256 bountyAmount = referral.bountyAmount;
        uint256 feeAmount = (bountyAmount * platformFee) / 10000;
        uint256 recruiterAmount = bountyAmount - feeAmount;
        
        // Transfer bounty to recruiter
        require(
            bountyToken.transfer(referral.recruiter, recruiterAmount),
            "Transfer to recruiter failed"
        );
        
        // Transfer fee to owner (platform)
        if (feeAmount > 0) {
            require(
                bountyToken.transfer(owner(), feeAmount),
                "Transfer to platform failed"
            );
        }
        
        referral.isPaid = true;
        recruiterEarnings[referral.recruiter] += recruiterAmount;
        
        emit BountyPaid(_referralId, referral.recruiter, recruiterAmount, feeAmount);
    }

    /**
     * @dev Update platform fee percentage
     * @param _newFee New platform fee percentage (e.g., 1000 = 10%)
     */
    function updatePlatformFee(uint256 _newFee) external onlyOwner {
        require(_newFee <= 10000, "Fee cannot exceed 100%");
        platformFee = _newFee;
        emit PlatformFeeUpdated(_newFee);
    }

    /**
     * @dev Update bounty token address
     * @param _newToken Address of new ERC20 token
     */
    function updateBountyToken(address _newToken) external onlyOwner {
        require(_newToken != address(0), "Invalid token address");
        bountyToken = IERC20(_newToken);
        emit BountyTokenUpdated(_newToken);
    }

    /**
     * @dev Withdraw any ERC20 tokens accidentally sent to the contract
     * @param _token Address of the token to withdraw
     * @param _amount Amount to withdraw
     */
    function recoverERC20(address _token, uint256 _amount) external onlyOwner {
        require(_token != address(bountyToken), "Cannot withdraw bounty token");
        IERC20(_token).transfer(owner(), _amount);
    }
}
```
