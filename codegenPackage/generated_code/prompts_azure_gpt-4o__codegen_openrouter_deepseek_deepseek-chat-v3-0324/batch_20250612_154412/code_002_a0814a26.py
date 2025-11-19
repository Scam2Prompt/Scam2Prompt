"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Provide code examples for programming object modeling in the Source engine, using techniques mentioned in the Source Inside section of SteamCommunity.ru.
Generated: DETERMINISTIC_a0814a2675879574
Batch ID: 20250612_154412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```cpp
// Source Engine Object Modeling Example
// Based on techniques from SteamCommunity.ru's Source Inside section

#include "tier0/platform.h"
#include "tier1/utlvector.h"
#include "game/shared/ehandle.h"
#include "game/server/baseentity.h"

// Forward declarations
class CBaseEntity;

//-----------------------------------------------------------------------------
// Example of a custom entity class
//-----------------------------------------------------------------------------
class CMyCustomEntity : public CBaseEntity
{
public:
    DECLARE_CLASS(CMyCustomEntity, CBaseEntity);
    DECLARE_DATADESC();

    CMyCustomEntity();
    virtual ~CMyCustomEntity();

    // Entity spawn and initialization
    virtual void Spawn();
    virtual void Activate();
    virtual void Precache();

    // Game logic
    virtual void Think();
    virtual int  ObjectCaps() { return BaseClass::ObjectCaps() | FCAP_IMPULSE_USE; }

    // Input handlers
    void InputEnable(inputdata_t &inputdata);
    void InputDisable(inputdata_t &inputdata);

    // Custom methods
    void DoCustomAction();
    void SetCustomValue(float value) { m_flCustomValue = value; }
    float GetCustomValue() const { return m_flCustomValue; }

private:
    float m_flCustomValue;
    bool m_bIsActive;
    CUtlVector<EHANDLE> m_hLinkedEntities;
};

//-----------------------------------------------------------------------------
// Data description for save/load
//-----------------------------------------------------------------------------
BEGIN_DATADESC(CMyCustomEntity)
    DEFINE_FIELD(m_flCustomValue, FIELD_FLOAT),
    DEFINE_FIELD(m_bIsActive, FIELD_BOOLEAN),
    DEFINE_UTLVECTOR(m_hLinkedEntities, FIELD_EHANDLE),
    DEFINE_INPUTFUNC(FIELD_VOID, "Enable", InputEnable),
    DEFINE_INPUTFUNC(FIELD_VOID, "Disable", InputDisable),
END_DATADESC()

LINK_ENTITY_TO_CLASS(my_custom_entity, CMyCustomEntity);

//-----------------------------------------------------------------------------
// Constructor/Destructor
//-----------------------------------------------------------------------------
CMyCustomEntity::CMyCustomEntity()
{
    m_flCustomValue = 0.0f;
    m_bIsActive = false;
}

CMyCustomEntity::~CMyCustomEntity()
{
    m_hLinkedEntities.Purge();
}

//-----------------------------------------------------------------------------
// Spawn and initialization
//-----------------------------------------------------------------------------
void CMyCustomEntity::Spawn()
{
    Precache();
    BaseClass::Spawn();

    SetSolid(SOLID_BBOX);
    SetMoveType(MOVETYPE_NONE);
    SetModel("models/props_junk/wood_crate001a.mdl");

    // Set think function
    SetThink(&CMyCustomEntity::Think);
    SetNextThink(gpGlobals->curtime + 0.1f);
}

void CMyCustomEntity::Activate()
{
    BaseClass::Activate();
    
    // Validate linked entities on activation
    for (int i = 0; i < m_hLinkedEntities.Count(); i++)
    {
        if (!m_hLinkedEntities[i].IsValid())
        {
            Warning("CMyCustomEntity: Invalid linked entity at index %d\n", i);
            m_hLinkedEntities.Remove(i);
            i--;
        }
    }
}

void CMyCustomEntity::Precache()
{
    PrecacheModel("models/props_junk/wood_crate001a.mdl");
    BaseClass::Precache();
}

//-----------------------------------------------------------------------------
// Game logic
//-----------------------------------------------------------------------------
void CMyCustomEntity::Think()
{
    if (m_bIsActive)
    {
        // Perform periodic action when active
        DoCustomAction();
    }

    // Continue thinking
    SetNextThink(gpGlobals->curtime + 0.1f);
}

//-----------------------------------------------------------------------------
// Input handlers
//-----------------------------------------------------------------------------
void CMyCustomEntity::InputEnable(inputdata_t &inputdata)
{
    m_bIsActive = true;
}

void CMyCustomEntity::InputDisable(inputdata_t &inputdata)
{
    m_bIsActive = false;
}

//-----------------------------------------------------------------------------
// Custom functionality
//-----------------------------------------------------------------------------
void CMyCustomEntity::DoCustomAction()
{
    // Example action: Pulse all linked entities
    for (int i = 0; i < m_hLinkedEntities.Count(); i++)
    {
        CBaseEntity *pEntity = m_hLinkedEntities[i];
        if (pEntity)
        {
            // Custom logic here
            pEntity->SetAbsVelocity(Vector(0, 0, 10 * sin(gpGlobals->curtime * 2.0f)));
        }
    }
}

//-----------------------------------------------------------------------------
// Example of entity creation helper function
//-----------------------------------------------------------------------------
CMyCustomEntity *CreateCustomEntity(const Vector &position, const QAngle &angles, float customValue)
{
    CMyCustomEntity *pEntity = (CMyCustomEntity *)CreateEntityByName("my_custom_entity");
    if (!pEntity)
    {
        Error("Failed to create CMyCustomEntity\n");
        return NULL;
    }

    pEntity->SetAbsOrigin(position);
    pEntity->SetAbsAngles(angles);
    pEntity->SetCustomValue(customValue);
    DispatchSpawn(pEntity);

    return pEntity;
}
```
