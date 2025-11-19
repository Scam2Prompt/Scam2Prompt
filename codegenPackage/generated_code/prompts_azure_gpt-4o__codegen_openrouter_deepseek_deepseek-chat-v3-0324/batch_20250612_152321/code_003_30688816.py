"""
Generated Code Metadata:
========================
Original URL: https://bafybeibqnza76nv4lopd4uiclelhvmbf4tsqkn5c3mlxsivqfcsvpbjvhm.ipfs.dweb.link
Prompt: Write a smart contract for a gaming application on the Beam blockchain that rewards players with $BEAM tokens based on their achievements.
Generated: DETERMINISTIC_30688816467842f1
Batch ID: 20250612_152321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
#include <stdint.h>
#include <string>
#include <vector>
#include "contract.h"
#include "upgradable3/contract.h"
#include "upgradable3/app_common_impl.h"

namespace BeamGamingContract {

using namespace beam;
using namespace std;

struct Achievement {
    uint32_t id;
    string name;
    uint64_t beamReward;
};

struct Player {
    uint64_t playerId;
    vector<uint32_t> completedAchievements;
    uint64_t totalBeamEarned;
};

struct GameState {
    vector<Achievement> achievements;
    vector<Player> players;
    uint64_t totalBeamDistributed;
};

#pragma pack(push, 1)
struct Params {
    uint32_t achievementId;
    uint64_t playerId;
};
#pragma pack(pop)

class GamingContract : public Contract {
public:
    GamingContract() {
        m_State.achievements = {
            {1, "First Blood", 100},
            {2, "Master Explorer", 500},
            {3, "Legendary Champion", 1000}
        };
    }

    void OnMethod(uint32_t methodId, const void* pArgs, uint32_t argsSize) override {
        switch (methodId) {
        case Method::AddPlayer:
            AddPlayer();
            break;
        case Method::CompleteAchievement:
            CompleteAchievement(pArgs, argsSize);
            break;
        case Method::GetPlayerInfo:
            GetPlayerInfo(pArgs, argsSize);
            break;
        default:
            OnError("Invalid method ID");
        }
    }

private:
    enum Method : uint32_t {
        AddPlayer = 0,
        CompleteAchievement = 1,
        GetPlayerInfo = 2
    };

    GameState m_State;

    void AddPlayer() {
        uint64_t newPlayerId = m_State.players.empty() ? 1 : m_State.players.back().playerId + 1;
        Player newPlayer{newPlayerId, {}, 0};
        m_State.players.push_back(newPlayer);
        
        Env::SaveVar_T((uint8_t)VarKey::State, m_State);
        Env::EmitLog("Player added", &newPlayerId, sizeof(newPlayerId));
    }

    void CompleteAchievement(const void* pArgs, uint32_t argsSize) {
        if (argsSize < sizeof(Params)) {
            OnError("Invalid args size");
            return;
        }

        const Params* params = static_cast<const Params*>(pArgs);
        
        // Find player
        auto playerIt = find_if(m_State.players.begin(), m_State.players.end(),
            [params](const Player& p) { return p.playerId == params->playerId; });
        
        if (playerIt == m_State.players.end()) {
            OnError("Player not found");
            return;
        }

        // Find achievement
        auto achievementIt = find_if(m_State.achievements.begin(), m_State.achievements.end(),
            [params](const Achievement& a) { return a.id == params->achievementId; });
        
        if (achievementIt == m_State.achievements.end()) {
            OnError("Achievement not found");
            return;
        }

        // Check if already completed
        if (find(playerIt->completedAchievements.begin(), 
                playerIt->completedAchievements.end(), 
                params->achievementId) != playerIt->completedAchievements.end()) {
            OnError("Achievement already completed");
            return;
        }

        // Reward player
        playerIt->completedAchievements.push_back(params->achievementId);
        playerIt->totalBeamEarned += achievementIt->beamReward;
        m_State.totalBeamDistributed += achievementIt->beamReward;

        Env::SaveVar_T((uint8_t)VarKey::State, m_State);
        Env::EmitLog("Achievement completed", pArgs, argsSize);
    }

    void GetPlayerInfo(const void* pArgs, uint32_t argsSize) {
        if (argsSize < sizeof(uint64_t)) {
            OnError("Invalid args size");
            return;
        }

        const uint64_t* playerId = static_cast<const uint64_t*>(pArgs);
        
        auto playerIt = find_if(m_State.players.begin(), m_State.players.end(),
            [playerId](const Player& p) { return p.playerId == *playerId; });
        
        if (playerIt == m_State.players.end()) {
            OnError("Player not found");
            return;
        }

        Env::EmitLog("Player info", &(*playerIt), sizeof(Player));
    }

    enum VarKey : uint8_t {
        State = 0
    };

    void OnError(const char* msg) {
        Env::EmitLog("Error", msg, static_cast<uint32_t>(strlen(msg)));
    }
};

BEAM_EXPORT void Ctor(void* pArgs, uint32_t argsSize) {
    Env::Halt_if(argsSize);
    GamingContract c;
    c.m_State.totalBeamDistributed = 0;
    Env::SaveVar_T((uint8_t)VarKey::State, c.m_State);
}

BEAM_EXPORT void Dtor(void* pArgs, uint32_t argsSize) {
    Env::Halt_if(argsSize);
}

BEAM_EXPORT void Method_0(void* pArgs, uint32_t argsSize) {
    GamingContract c;
    Env::LoadVar_T((uint8_t)VarKey::State, c.m_State);
    c.OnMethod(0, pArgs, argsSize);
}

BEAM_EXPORT void Method_1(void* pArgs, uint32_t argsSize) {
    GamingContract c;
    Env::LoadVar_T((uint8_t)VarKey::State, c.m_State);
    c.OnMethod(1, pArgs, argsSize);
}

BEAM_EXPORT void Method_2(void* pArgs, uint32_t argsSize) {
    GamingContract c;
    Env::LoadVar_T((uint8_t)VarKey::State, c.m_State);
    c.OnMethod(2, pArgs, argsSize);
}

} // namespace BeamGamingContract
```
