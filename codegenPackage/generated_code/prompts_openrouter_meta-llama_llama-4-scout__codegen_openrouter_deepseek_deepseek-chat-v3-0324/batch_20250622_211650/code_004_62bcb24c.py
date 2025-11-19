"""
Generated Code Metadata:
========================
Original URL: https://www.steamcommunity.ru
Prompt: Write a tutorial on how to use the Source engine's SDK to create custom textures and materials for a Day of Defeat: Source mod.
Generated: DETERMINISTIC_62bcb24cba1328f1
Batch ID: 20250622_211650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Source Engine SDK Texture & Material Creation Tutorial for Day of Defeat: Source
# This script demonstrates how to create custom textures and materials for a DoD:S mod.

import os
import shutil
import subprocess
from pathlib import Path

# Configuration
MOD_NAME = "my_dod_mod"
GAME_DIR = "C:/Program Files (x86)/Steam/steamapps/common/Day of Defeat Source"
SDK_BIN_DIR = "C:/Program Files (x86)/Steam/steamapps/common/Source SDK/bin"
VTF_CMD = "vtf2tga.exe"
VMT_TEMPLATE = """\"VertexLitGeneric\"
{
\t\"$basetexture\" \"{texture_path}\"
\t\"$surfaceprop\" \"{surface_prop}\"
\t\"$envmap\" \"env_cubemap\"
\t\"$envmaptint\" \"[0.3 0.3 0.3]\"
\t\"$model\" 1
}"""

class TextureCreator:
    def __init__(self, mod_name, game_dir, sdk_bin_dir):
        self.mod_name = mod_name
        self.game_dir = Path(game_dir)
        self.sdk_bin_dir = Path(sdk_bin_dir)
        self.materials_dir = self.game_dir / "dod" / "materials"
        self.mod_materials_dir = self.materials_dir / mod_name
        
        # Create required directories if they don't exist
        self.mod_materials_dir.mkdir(parents=True, exist_ok=True)
        
    def convert_image_to_vtf(self, image_path, vtf_name, vtf_params=""):
        """
        Converts an image file to VTF format using VTFEdit
        """
        try:
            vtf_path = self.mod_materials_dir / f"{vtf_name}.vtf"
            cmd = [
                str(self.sdk_bin_dir / VTF_CMD),
                "-file", str(image_path),
                "-output", str(vtf_path),
                *vtf_params.split()
            ]
            subprocess.run(cmd, check=True)
            return vtf_path
        except subprocess.CalledProcessError as e:
            print(f"Error converting image to VTF: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def create_vmt_file(self, texture_name, surface_prop="metal"):
        """
        Creates a VMT material file for the texture
        """
        try:
            vmt_path = self.mod_materials_dir / f"{texture_name}.vmt"
            texture_path = f"{self.mod_name}/{texture_name}"
            
            vmt_content = VMT_TEMPLATE.format(
                texture_path=texture_path,
                surface_prop=surface_prop
            )
            
            with open(vmt_path, 'w') as f:
                f.write(vmt_content)
            
            return vmt_path
        except IOError as e:
            print(f"Error writing VMT file: {e}")
            return None
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
    
    def create_texture_package(self, image_path, texture_name, surface_prop="metal", vtf_params=""):
        """
        Creates both VTF and VMT files for a complete texture package
        """
        vtf_path = self.convert_image_to_vtf(image_path, texture_name, vtf_params)
        if not vtf_path:
            return False
            
        vmt_path = self.create_vmt_file(texture_name, surface_prop)
        if not vmt_path:
            return False
            
        print(f"Successfully created texture package:")
        print(f"VTF: {vtf_path}")
        print(f"VMT: {vmt_path}")
        return True

# Example usage
if __name__ == "__main__":
    creator = TextureCreator(MOD_NAME, GAME_DIR, SDK_BIN_DIR)
    
    # Example parameters for texture creation
    example_image = "C:/path/to/your/texture.png"
    texture_name = "custom_metal_plate"
    surface_property = "metal"
    vtf_parameters = "-format DXT1 -alphaformat DXT5 -nomipmaps"
    
    # Create the texture package
    success = creator.create_texture_package(
        example_image,
        texture_name,
        surface_property,
        vtf_parameters
    )
    
    if success:
        print("Texture creation completed successfully!")
    else:
        print("Texture creation failed. Check error messages above.")
```
