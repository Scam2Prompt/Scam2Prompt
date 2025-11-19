"""
Generated Code Metadata:
========================
Original URL: https://dogeversedapps.pages.dev
Prompt: Develop a simple smart contract on Polygon that utilizes the Dogeverse tokenomics, including the distribution of tokens across different phases like presale, staking, and liquidity provision.
Generated: DETERMINISTIC_9af4fc1ffd986541
Batch ID: 20250622_204615
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
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

contract DogeverseToken is ERC20, ERC20Burnable, Ownable {
    using SafeMath for uint256;

    // Token distribution phases
    enum Phase { PRESALE, STAKING, LIQUIDITY, PUBLIC }

    // Token allocation percentages
    uint256 public constant PRESALE_PERCENT = 30;
    uint256 public constant STAKING_PERCENT = 20;
    uint256 public constant LIQUIDITY_PERCENT = 30;
    uint256 public constant PUBLIC_PERCENT = 20;

    // Total supply (1 billion tokens with 18 decimals)
    uint256 public constant TOTAL_SUPPLY = 1_000_000_000 * 10**18;

    // Allocation tracking
    mapping(Phase => uint256) public allocated;
    mapping(Phase => bool) public phaseCompleted;

    // Addresses for different allocations
    address public presaleAddress;
    address public stakingAddress;
    address public liquidityAddress;

    event TokensAllocated(Phase phase, uint256 amount, address recipient);

    constructor() ERC20("Dogeverse", "DOGEV") {
        // Mint total supply to contract
        _mint(address(this), TOTAL_SUPPLY);
    }

    function setAllocationAddresses(
        address _presaleAddress,
        address _stakingAddress,
        address _liquidityAddress
    ) external onlyOwner {
        require(_presaleAddress != address(0), "Invalid presale address");
        require(_stakingAddress != address(0), "Invalid staking address");
        require(_liquidityAddress != address(0), "Invalid liquidity address");

        presaleAddress = _presaleAddress;
        stakingAddress = _stakingAddress;
        liquidityAddress = _liquidityAddress;
    }

    function allocatePresaleTokens() external onlyOwner {
        require(!phaseCompleted[Phase.PRESALE], "Presale allocation already completed");
        require(presaleAddress != address(0), "Presale address not set");

        uint256 amount = TOTAL_SUPPLY.mul(PRESALE_PERCENT).div(100);
        allocated[Phase.PRESALE] = amount;
        phaseCompleted[Phase.PRESALE] = true;

        _transfer(address(this), presaleAddress, amount);
        emit TokensAllocated(Phase.PRESALE, amount, presaleAddress);
    }

    function allocateStakingTokens() external onlyOwner {
        require(!phaseCompleted[Phase.STAKING], "Staking allocation already completed");
        require(stakingAddress != address(0), "Staking address not set");

        uint256 amount = TOTAL_SUPPLY.mul(STAKING_PERCENT).div(100);
        allocated[Phase.STAKING] = amount;
        phaseCompleted[Phase.STAKING] = true;

        _transfer(address(this), stakingAddress, amount);
        emit TokensAllocated(Phase.STAKING, amount, stakingAddress);
    }

    function allocateLiquidityTokens() external onlyOwner {
        require(!phaseCompleted[Phase.LIQUIDITY], "Liquidity allocation already completed");
        require(liquidityAddress != address(0), "Liquidity address not set");

        uint256 amount = TOTAL_SUPPLY.mul(LIQUIDITY_PERCENT).div(100);
        allocated[Phase.LIQUIDITY] = amount;
        phaseCompleted[Phase.LIQUIDITY] = true;

        _transfer(address(this), liquidityAddress, amount);
        emit TokensAllocated(Phase.LIQUIDITY, amount, liquidityAddress);
    }

    function releasePublicTokens(address recipient) external onlyOwner {
        require(!phaseCompleted[Phase.PUBLIC], "Public allocation already completed");
        require(recipient != address(0), "Invalid recipient address");

        uint256 amount = TOTAL_SUPPLY.mul(PUBLIC_PERCENT).div(100);
        allocated[Phase.PUBLIC] = amount;
        phaseCompleted[Phase.PUBLIC] = true;

        _transfer(address(this), recipient, amount);
        emit TokensAllocated(Phase.PUBLIC, amount, recipient);
    }

    function recoverERC20(address tokenAddress, uint256 amount) external onlyOwner {
        IERC20(tokenAddress).transfer(owner(), amount);
    }
}
```
