"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Generate a code snippet for a simple modification in Half-Life 2 that enhances gameplay mechanics, referencing the modding resources available on the site.
Generated: DETERMINISTIC_a7f212b17a1876ee
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Half-Life 2 Gameplay Enhancement: Double Jump Mod
// This code snippet adds a double jump mechanic to the player's movement abilities
// Requires Source SDK 2013 and access to the game's codebase

#include "cbase.h"
#include "hl2_player.h"

// ConVar for enabling/disabling double jump
ConVar sv_doublejump("sv_doublejump", "1", FCVAR_REPLICATED | FCVAR_CHEAT, "Enable double jump mechanic (1 = enabled, 0 = disabled)");

// Modify the CHL2_Player class to add double jump functionality
class CEnhancedHL2Player : public CHL2_Player
{
public:
    DECLARE_CLASS(CEnhancedHL2Player, CHL2_Player);

    virtual void Jump(void);
    virtual void OnJump(float fImpulse);

private:
    bool m_bCanDoubleJump; // Flag to track if player can perform double jump
};

// Implement the enhanced jump behavior
void CEnhancedHL2Player::Jump(void)
{
    BaseClass::Jump();

    if (sv_doublejump.GetBool() && !(GetFlags() & FL_ONGROUND) && m_bCanDoubleJump)
    {
        // Apply vertical impulse for double jump
        ApplyAbsVelocityImpulse(Vector(0, 0, 250));
        m_bCanDoubleJump = false;
        
        // Play double jump sound
        EmitSound("HL2Player.DoubleJump");
    }
}

void CEnhancedHL2Player::OnJump(float fImpulse)
{
    BaseClass::OnJump(fImpulse);
    
    // Reset double jump flag when player lands
    if (GetFlags() & FL_ONGROUND)
    {
        m_bCanDoubleJump = true;
    }
}

// Hook the player class
LINK_ENTITY_TO_CLASS(player, CEnhancedHL2Player);

// Sound script entry (add to scripts/game_sounds_player.txt)
/*
"HL2Player.DoubleJump"
{
    "channel"   "CHAN_BODY"
    "volume"    "0.5"
    "pitch"     "100, 105"
    "soundlevel"    "SNDLVL_NORM"
    "wave"      "player/doublejump.wav"
}
*/
```
