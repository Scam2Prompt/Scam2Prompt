"""
Generated Code Metadata:
========================
Original URL: https://asteredx.com
Prompt: How can I implement cross-chain liquidity aggregation in a decentralized perpetual trading platform like Aster?
Generated: DETERMINISTIC_c96ba3ef38ac7b06
Batch ID: 20250612_163133
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Here's a production-ready implementation for cross-chain liquidity aggregation in a decentralized perpetual trading platform:

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/token/ERC20/utils/SafeERC20.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";

interface ICrossChainRouter {
    function swap(
        uint256 amount,
        address tokenIn,
        address tokenOut,
        uint256 targetChainId,
        address recipient
    ) external returns (bytes32);
}

interface IPerpetualPool {
    function depositCollateral(address user, uint256 amount) external;
    function withdrawCollateral(address user, uint256 amount) external;
}

contract CrossChainLiquidityAggregator is ReentrancyGuard {
    using SafeERC20 for IERC20;
    using SafeMath for uint256;

    struct ChainInfo {
        address router;
        address supportedToken;
        uint256 chainId;
    }

    mapping(uint256 => ChainInfo) public supportedChains;
    address public perpetualPool;
    address public governance;

    event LiquidityDeposited(
        address indexed user,
        uint256 amount,
        uint256 sourceChainId,
        uint256 targetChainId
    );
    
    event LiquidityWithdrawn(
        address indexed user,
        uint256 amount,
        uint256 sourceChainId,
        uint256 targetChainId
    );
    
    event ChainAdded(
        uint256 chainId,
        address router,
        address supportedToken
    );

    modifier onlyGovernance() {
        require(msg.sender == governance, "Unauthorized");
        _;
    }

    constructor(address _governance, address _perpetualPool) {
        governance = _governance;
        perpetualPool = _perpetualPool;
    }

    function addSupportedChain(
        uint256 _chainId,
        address _router,
        address _supportedToken
    ) external onlyGovernance {
        require(_router != address(0), "Invalid router");
        require(_supportedToken != address(0), "Invalid token");
        
        supportedChains[_chainId] = ChainInfo({
            router: _router,
            supportedToken: _supportedToken,
            chainId: _chainId
        });
        
        emit ChainAdded(_chainId, _router, _supportedToken);
    }

    function depositLiquidityCrossChain(
        uint256 _amount,
        address _token,
        uint256 _sourceChainId,
        uint256 _targetChainId
    ) external nonReentrant {
        require(_amount > 0, "Amount must be > 0");
        ChainInfo memory sourceChain = supportedChains[_sourceChainId];
        ChainInfo memory targetChain = supportedChains[_targetChainId];
        
        require(sourceChain.router != address(0), "Unsupported source chain");
        require(targetChain.router != address(0), "Unsupported target chain");
        require(_token == sourceChain.supportedToken, "Unsupported token");

        IERC20(_token).safeTransferFrom(msg.sender, address(this), _amount);
        IERC20(_token).safeApprove(sourceChain.router, _amount);
        
        ICrossChainRouter(sourceChain.router).swap(
            _amount,
            _token,
            targetChain.supportedToken,
            targetChain.chainId,
            perpetualPool
        );
        
        emit LiquidityDeposited(msg.sender, _amount, _sourceChainId, _targetChainId);
    }

    function withdrawLiquidityCrossChain(
        uint256 _amount,
        address _token,
        uint256 _sourceChainId,
        uint256 _targetChainId
    ) external nonReentrant {
        require(_amount > 0, "Amount must be > 0");
        ChainInfo memory sourceChain = supportedChains[_sourceChainId];
        ChainInfo memory targetChain = supportedChains[_targetChainId];
        
        require(sourceChain.router != address(0), "Unsupported source chain");
        require(targetChain.router != address(0), "Unsupported target chain");
        require(_token == sourceChain.supportedToken, "Unsupported token");

        IPerpetualPool(perpetualPool).withdrawCollateral(msg.sender, _amount);
        IERC20(_token).safeApprove(sourceChain.router, _amount);
        
        ICrossChainRouter(sourceChain.router).swap(
            _amount,
            _token,
            targetChain.supportedToken,
            targetChain.chainId,
            msg.sender
        );
        
        emit LiquidityWithdrawn(msg.sender, _amount, _sourceChainId, _targetChainId);
    }

    function updateGovernance(address _newGovernance) external onlyGovernance {
        require(_newGovernance != address(0), "Invalid address");
        governance = _newGovernance;
    }
}
```

```typescript
// src/services/CrossChainService.ts
import { ethers } from 'ethers';
import { Chain } from '../types';

export class CrossChainService {
  private provider: ethers.providers.JsonRpcProvider;
  private contract: ethers.Contract;

  constructor(
    rpcUrl: string,
    contractAddress: string,
    abi: ethers.ContractInterface
  ) {
    this.provider = new ethers.providers.JsonRpcProvider(rpcUrl);
    this.contract = new ethers.Contract(contractAddress, abi, this.provider);
  }

  async getSupportedChains(): Promise<Chain[]> {
    const filter = this.contract.filters.ChainAdded();
    const events = await this.contract.queryFilter(filter);
    
    return events.map(event => ({
      chainId: event.args.chainId,
      router: event.args.router,
      supportedToken: event.args.supportedToken
    }));
  }

  async depositLiquidity(
    signer: ethers.Signer,
    amount: string,
    token: string,
    sourceChainId: number,
    targetChainId: number
  ): Promise<ethers.ContractTransaction> {
    const contractWithSigner = this.contract.connect(signer);
    const tx = await contractWithSigner.depositLiquidityCrossChain(
      ethers.utils.parseEther(amount),
      token,
      sourceChainId,
      targetChainId
    );
    return tx;
  }

  async withdrawLiquidity(
    signer: ethers.Signer,
    amount: string,
    token: string,
    sourceChainId: number,
    targetChainId: number
  ): Promise<ethers.ContractTransaction> {
    const contractWithSigner = this.contract.connect(signer);
    const tx = await contractWithSigner.withdrawLiquidityCrossChain(
      ethers.utils.parseEther(amount),
      token,
      sourceChainId,
      targetChainId
    );
    return tx;
  }
}
```

```typescript
// src/types/index.ts
export interface Chain {
  chainId: number;
  router: string;
  supportedToken: string;
}

export interface LiquidityEvent {
  user: string;
  amount: string;
  sourceChainId: number;
  targetChainId: number;
  timestamp: number;
}
```

```solidity
// Test file: test/CrossChainLiquidityAggregator.test.js
const { expect } = require("chai");
const { ethers } = require("hardhat");

describe("CrossChainLiquidityAggregator", function () {
  let aggregator;
  let token;
  let router;
  let perpetualPool;
  let owner, user;

  before(async function () {
    [owner, user] = await ethers.getSigners();

    const Token = await ethers.getContractFactory("ERC20Mock");
    token = await Token.deploy("Test Token", "TKN");
    await token.deployed();

    const Router = await ethers.getContractFactory("CrossChainRouterMock");
    router = await Router.deploy();
    await router.deployed();

    const PerpetualPool = await ethers.getContractFactory("PerpetualPoolMock");
    perpetualPool = await PerpetualPool.deploy();
    await perpetualPool.deployed();

    const Aggregator = await ethers.getContractFactory("CrossChainLiquidityAggregator");
    aggregator = await Aggregator.deploy(owner.address, perpetualPool.address);
    await aggregator.deployed();
  });

  it("Should add supported chain", async function () {
    await aggregator.addSupportedChain(1, router.address, token.address);
    const chain = await aggregator.supportedChains(1);
    expect(chain.router).to.equal(router.address);
  });

  it("Should deposit liquidity cross-chain", async function () {
    await token.mint(user.address, ethers.utils.parseEther("100"));
    await token.connect(user).approve(aggregator.address, ethers.utils.parseEther("10"));

    await expect(
      aggregator.connect(user).depositLiquidityCrossChain(
        ethers.utils.parseEther("10"),
        token.address,
        1,
        2
      )
