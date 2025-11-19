"""
Generated Code Metadata:
========================
Original URL: https://missions3nyanheroescom.pages.dev
Prompt: What are some strategies for creating an engaging mission system like the one on Nyan Heroes, and how can it be implemented using Node.js?
Generated: DETERMINISTIC_a59b799d5430c807
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```javascript
// missionSystem.js - Node.js implementation of an engaging mission system

const { EventEmitter } = require('events');
const mongoose = require('mongoose');
const { v4: uuidv4 } = require('uuid');

// Connect to MongoDB
mongoose.connect(process.env.MONGODB_URI || 'mongodb://localhost:27017/nyan_heroes', {
  useNewUrlParser: true,
  useUnifiedTopology: true
});

// Mission Schema
const missionSchema = new mongoose.Schema({
  missionId: { type: String, default: uuidv4, unique: true },
  title: { type: String, required: true },
  description: { type: String, required: true },
  difficulty: { type: String, enum: ['easy', 'medium', 'hard'], required: true },
  rewards: {
    experience: { type: Number, default: 0 },
    currency: { type: Number, default: 0 },
    items: [{ type: mongoose.Schema.Types.ObjectId, ref: 'Item' }]
  },
  requirements: {
    level: { type: Number, default: 1 },
    completedMissions: [{ type: String }]
  },
  isActive: { type: Boolean, default: true },
  startDate: { type: Date, default: Date.now },
  endDate: { type: Date },
  repeatable: { type: Boolean, default: false },
  cooldown: { type: Number, default: 0 } // in hours
});

// Player Mission Progress Schema
const playerMissionSchema = new mongoose.Schema({
  playerId: { type: mongoose.Schema.Types.ObjectId, ref: 'Player', required: true },
  missionId: { type: String, required: true },
  progress: { type: Number, default: 0 },
  completed: { type: Boolean, default: false },
  completionDate: { type: Date },
  cooldownEnd: { type: Date }
});

const Mission = mongoose.model('Mission', missionSchema);
const PlayerMission = mongoose.model('PlayerMission', playerMissionSchema);

class MissionSystem extends EventEmitter {
  constructor() {
    super();
  }

  async createMission(missionData) {
    try {
      const mission = new Mission(missionData);
      await mission.save();
      this.emit('missionCreated', mission);
      return mission;
    } catch (error) {
      throw new Error(`Failed to create mission: ${error.message}`);
    }
  }

  async getAvailableMissions(playerId, playerLevel) {
    try {
      const playerMissions = await PlayerMission.find({ playerId });
      const completedMissionIds = playerMissions
        .filter(pm => pm.completed)
        .map(pm => pm.missionId);

      return await Mission.find({
        isActive: true,
        'requirements.level': { $lte: playerLevel },
        $or: [
          { 'requirements.completedMissions': { $size: 0 } },
          { 'requirements.completedMissions': { $in: completedMissionIds } }
        ],
        $and: [
          {
            $or: [
              { endDate: { $exists: false } },
              { endDate: { $gt: new Date() } }
            ]
          }
        ]
      });
    } catch (error) {
      throw new Error(`Failed to get available missions: ${error.message}`);
    }
  }

  async startMission(playerId, missionId) {
    try {
      const existingProgress = await PlayerMission.findOne({ playerId, missionId });
      
      if (existingProgress) {
        if (existingProgress.completed) {
          const mission = await Mission.findOne({ missionId });
          if (!mission.repeatable) {
            throw new Error('Mission is not repeatable');
          }
          
          if (existingProgress.cooldownEnd && existingProgress.cooldownEnd > new Date()) {
            throw new Error('Mission is still on cooldown');
          }
        } else {
          return existingProgress;
        }
      }

      const newProgress = new PlayerMission({
        playerId,
        missionId,
        progress: 0,
        completed: false
      });

      await newProgress.save();
      this.emit('missionStarted', { playerId, missionId });
      return newProgress;
    } catch (error) {
      throw new Error(`Failed to start mission: ${error.message}`);
    }
  }

  async updateMissionProgress(playerId, missionId, progress) {
    try {
      const missionProgress = await PlayerMission.findOne({ playerId, missionId });
      if (!missionProgress) {
        throw new Error('Mission not started by player');
      }

      if (missionProgress.completed) {
        throw new Error('Mission already completed');
      }

      const mission = await Mission.findOne({ missionId });
      if (!mission) {
        throw new Error('Mission not found');
      }

      missionProgress.progress = progress;
      
      if (progress >= 100) {
        missionProgress.completed = true;
        missionProgress.completionDate = new Date();
        
        if (mission.repeatable && mission.cooldown > 0) {
          const cooldownEnd = new Date();
          cooldownEnd.setHours(cooldownEnd.getHours() + mission.cooldown);
          missionProgress.cooldownEnd = cooldownEnd;
        }

        this.emit('missionCompleted', {
          playerId,
          missionId,
          rewards: mission.rewards
        });
      }

      await missionProgress.save();
      return missionProgress;
    } catch (error) {
      throw new Error(`Failed to update mission progress: ${error.message}`);
    }
  }

  async claimReward(playerId, missionId) {
    try {
      const missionProgress = await PlayerMission.findOne({ playerId, missionId });
      if (!missionProgress || !missionProgress.completed) {
        throw new Error('Mission not completed');
      }

      const mission = await Mission.findOne({ missionId });
      if (!mission) {
        throw new Error('Mission not found');
      }

      // Here you would implement the actual reward distribution logic
      // For example, updating player's currency, experience, etc.
      
      this.emit('rewardClaimed', {
        playerId,
        missionId,
        rewards: mission.rewards
      });

      return mission.rewards;
    } catch (error) {
      throw new Error(`Failed to claim reward: ${error.message}`);
    }
  }

  async getPlayerMissions(playerId) {
    try {
      return await PlayerMission.find({ playerId }).populate('missionId');
    } catch (error) {
      throw new Error(`Failed to get player missions: ${error.message}`);
    }
  }
}

module.exports = {
  Mission,
  PlayerMission,
  MissionSystem
};
```
