"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a guide on how to create a mod for Half-Life using the Source engine, including programming techniques and material creation.
Generated: DETERMINISTIC_a21d69246939221a
Batch ID: 20250612_163915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

Since you're requesting a guide on creating a mod for Half-Life using the Source engine, I'll provide a structured code example for a basic Source mod setup. This will include a sample game code structure, material definition, and build configuration.

```python
# This is a Python script to set up a basic Source mod project structure
# Note: Actual Source mod development is primarily done in C++ and uses Valve's proprietary tools

import os
import shutil

def create_source_mod_project(mod_name):
    """
    Creates a basic directory structure for a Source engine mod.
    """
    try:
        # Create root mod directory
        os.makedirs(f"{mod_name}/game", exist_ok=True)
        
        # Create subdirectories
        dirs = [
            "materials",
            "models",
            "particles",
            "scenes",
            "scripts",
            "sound",
            "src/game/client",
            "src/game/server",
            "src/public",
            "src/common",
            "resource"
        ]
        
        for d in dirs:
            os.makedirs(f"{mod_name}/game/{d}", exist_ok=True)
            
        # Create basic files
        with open(f"{mod_name}/game/scripts/game_sounds_{mod_name.lower()}.txt", "w") as f:
            f.write('"Gamesounds"\n{\n\t"version"\t"1"\n}\n')
            
        with open(f"{mod_name}/game/scripts/materials/{mod_name.lower()}.vmt", "w") as f:
            f.write('"VertexLitGeneric"\n{\n\t"$basetexture" "path/to/your/texture"\n\t"$surfaceprop" "default"\n}\n')
            
        with open(f"{mod_name}/game/src/game/server/{mod_name.lower()}_shared.cpp", "w") as f:
            f.write('#include "cbase.h"\n\n// Your shared game code goes here\n')
            
        with open(f"{mod_name}/game/src/game/server/{mod_name.lower()}.cpp", "w") as f:
            f.write('#include "cbase.h"\n\n// Implement your mod-specific entities here\n')
            
        with open(f"{mod_name}/game/src/game/client/{mod_name.lower()}_client.cpp", "w") as f:
            f.write('#include "cbase.h"\n\n// Client-side implementation goes here\n')
            
        # Create VPC file for project
        with open(f"{mod_name}/src/game/{mod_name}.vpc", "w") as f:
            f.write(f'$Project "{mod_name}"\n{{\n\t"Games"\n\t{{\n\t\t"Half-Life 2"\n\t}}\n\n\t"Configurations"\n\t{{\n\t\t"Release"\n\t\t{{\n\t\t\t$General\n\t\t\t{{\n\t\t\t\t$OutputFile "$SRCDIR\\game\\bin\\{mod_name.lower()}.dll"\n\t\t\t}}\n\t\t}}\n\t}}\n\n\t"Files"\n\t{{\n\t\t"game/server/{mod_name.lower()}.cpp"\n\t\t"game/server/{mod_name.lower()}_shared.cpp"\n\t\t"game/client/{mod_name.lower()}_client.cpp"\n\t}}\n}}\n')
            
        print(f"Successfully created Source mod project: {mod_name}")
        
    except Exception as e:
        print(f"Error creating mod project: {e}")

if __name__ == "__main__":
    mod_name = input("Enter your mod name: ")
    create_source_mod_project(mod_name)
```

```cpp
// Example of a basic entity implementation for Source mod
// File: mod_entity.cpp

#include "cbase.h"
#include "tier0/dbg.h"

// DECLARE_MINIMUM_STEAM_INTERFACE_VERSION();

class CMyModEntity : public CBaseAnimating
{
public:
    DECLARE_CLASS(CMyModEntity, CBaseAnimating);
    DECLARE_DATADESC();

    CMyModEntity();
    virtual ~CMyModEntity();

    void Spawn();
    void Precache();
    void Think();

    void InputEnable(inputdata_t &inputdata);
    void InputDisable(inputdata_t &inputdata);

private:
    bool m_bEnabled;
    float m_flScale;
};

LINK_ENTITY_TO_CLASS(my_mod_entity, CMyModEntity);

BEGIN_DATADESC(CMyModEntity)
    DEFINE_FIELD(m_bEnabled, FIELD_BOOLEAN),
    DEFINE_KEYFIELD(m_flScale, FIELD_FLOAT, "scale"),
    DEFINE_INPUTFUNC(FIELD_VOID, "Enable", InputEnable),
    DEFINE_INPUTFUNC(FIELD_VOID, "Disable", InputDisable),
    DEFINE_THINKFUNC(Think),
END_DATADESC()

CMyModEntity::CMyModEntity()
{
    m_bEnabled = true;
    m_flScale = 1.0f;
}

void CMyModEntity::Spawn()
{
    Precache();
    BaseClass::Spawn();
    
    SetThink(&CMyModEntity::Think);
    SetNextThink(gpGlobals->curtime + 0.1f);
    
    if (m_flScale <= 0)
    {
        Warning("CMyModEntity: Invalid scale value (%f), resetting to 1.0\n", m_flScale);
        m_flScale = 1.0f;
    }
    
    SetModelScale(m_flScale);
}

void CMyModEntity::Precache()
{
    PrecacheModel("models/props_junk/plasticbucket001a.mdl");
    BaseClass::Precache();
}

void CMyModEntity::Think()
{
    if (m_bEnabled)
    {
        // Your entity's think logic here
    }
    
    SetNextThink(gpGlobals->curtime + 0.1f);
}

void CMyModEntity::InputEnable(inputdata_t &inputdata)
{
    m_bEnabled = true;
}

void CMyModEntity::InputDisable(inputdata_t &inputdata)
{
    m_bEnabled = false;
}
```

```vmt
// Example material definition for Source engine
// File: materials/custom_mod_material.vmt

"VertexLitGeneric"
{
    "$basetexture" "custom_mod/custom_texture"
    "$surfaceprop" "metal"
    "$envmap" "env_cubemap"
    "$envmaptint" "[0.3 0.3 0.3]"
    "$normalmap" "custom_mod/custom_normal"
    "$bumpmap" "custom_mod/custom_normal"
    "$phong" "1"
    "$phongexponent" "30"
    "$phongboost" "1"
    "$phongfresnelranges" "[0.5 1 2]"
    "$lightwarptexture" "custom_mod/custom_lightwarp"
}
```

```fgd
// Example FGD definition for custom entity
// File: scripts/entities/my_mod_entity.fgd

@PointClass base(Targetname) studio("models/props_junk/plasticbucket001a.mdl") = my_mod_entity : "My Mod Custom Entity"
[
    scale(float) : "Scale" : 1.0 : "Scale of the model"
    startdisabled(choices) : "Start Disabled" : 0 =
    [
        0 : "No"
        1 : "Yes"
    ]
    input Enable(void) : "Enable the entity's functionality"
    input Disable(void) : "Disable the entity's functionality"
]
```

Note: Actual Source mod development requires Valve's Source SDK, Visual Studio, and other proprietary tools. The above examples provide templates for key files but need to be integrated into a proper Source SDK project.
