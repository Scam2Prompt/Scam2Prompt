"""
Generated Code Metadata:
========================
Original URL: https://rexas-de.web.app
Prompt: Create an NFT generation algorithm using Rexas GenAI, producing unique, high-quality digital artworks for artists and creators.
Generated: DETERMINISTIC_1701448c61d2cb11
Batch ID: 20250622_210046
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import random
import json
from datetime import datetime
from typing import List, Dict, Optional
from PIL import Image, ImageDraw, ImageFont
import numpy as np
import requests
from rexas_genai import RexasGenAI

class NFTGenerator:
    """
    NFT Generator using Rexas GenAI to create unique digital artworks.
    Handles generation, metadata creation, and file storage.
    """
    
    def __init__(self, api_key: str, output_dir: str = "nft_output"):
        """
        Initialize NFT Generator with Rexas GenAI API key.
        
        Args:
            api_key: Rexas GenAI API key
            output_dir: Directory to store generated NFTs
        """
        self.genai = RexasGenAI(api_key=api_key)
        self.output_dir = output_dir
        self._setup_directories()
        
    def _setup_directories(self) -> None:
        """Create necessary directories if they don't exist."""
        os.makedirs(self.output_dir, exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "images"), exist_ok=True)
        os.makedirs(os.path.join(self.output_dir, "metadata"), exist_ok=True)
    
    def _generate_unique_id(self) -> str:
        """Generate a unique ID for each NFT."""
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        random_str = ''.join(random.choices('abcdef0123456789', k=8))
        return f"nft_{timestamp}_{random_str}"
    
    def _generate_artwork(self, prompt: str, style: str) -> Image.Image:
        """
        Generate artwork using Rexas GenAI.
        
        Args:
            prompt: Description of the artwork
            style: Artistic style to apply
            
        Returns:
            Generated PIL Image object
            
        Raises:
            RuntimeError: If generation fails
        """
        try:
            response = self.genai.generate_image(
                prompt=prompt,
                style=style,
                resolution="1024x1024",
                quality="high"
            )
            
            if not response.success:
                raise RuntimeError(f"Generation failed: {response.error_message}")
                
            return Image.open(requests.get(response.image_url, stream=True).raw)
        except Exception as e:
            raise RuntimeError(f"Artwork generation failed: {str(e)}")
    
    def _apply_signature(self, image: Image.Image, creator: str) -> Image.Image:
        """
        Apply creator's signature to the artwork.
        
        Args:
            image: PIL Image object
            creator: Name of the creator
            
        Returns:
            Signed PIL Image object
        """
        try:
            draw = ImageDraw.Draw(image)
            font = ImageFont.load_default()
            text = f"© {creator}"
            text_width, text_height = draw.textsize(text, font=font)
            
            margin = 20
            x = image.width - text_width - margin
            y = image.height - text_height - margin
            
            draw.text((x, y), text, fill="white", font=font)
            return image
        except Exception as e:
            raise RuntimeError(f"Failed to apply signature: {str(e)}")
    
    def _generate_metadata(
        self,
        nft_id: str,
        creator: str,
        prompt: str,
        style: str,
        attributes: Dict[str, str],
        image_path: str
    ) -> Dict:
        """
        Generate NFT metadata following OpenSea standards.
        
        Args:
            nft_id: Unique NFT identifier
            creator: Creator name
            prompt: Generation prompt
            style: Art style
            attributes: Additional attributes
            image_path: Path to the image file
            
        Returns:
            Dictionary containing NFT metadata
        """
        metadata = {
            "name": f"GenAI Art #{nft_id}",
            "description": f"AI-generated artwork created by {creator}",
            "image": image_path,
            "external_url": "",
            "attributes": [
                {
                    "trait_type": "Artist",
                    "value": creator
                },
                {
                    "trait_type": "Style",
                    "value": style
                },
                {
                    "trait_type": "Prompt",
                    "value": prompt
                }
            ]
        }
        
        for key, value in attributes.items():
            metadata["attributes"].append({
                "trait_type": key,
                "value": value
            })
            
        return metadata
    
    def generate_nft(
        self,
        prompt: str,
        creator: str,
        style: str = "digital art",
        attributes: Optional[Dict[str, str]] = None,
        save_files: bool = True
    ) -> Dict:
        """
        Generate a complete NFT with artwork and metadata.
        
        Args:
            prompt: Description for artwork generation
            creator: Creator name
            style: Artistic style
            attributes: Additional NFT attributes
            save_files: Whether to save files to disk
            
        Returns:
            Dictionary containing NFT data and paths
            
        Raises:
            RuntimeError: If generation fails
        """
        try:
            if attributes is None:
                attributes = {}
                
            nft_id = self._generate_unique_id()
            
            # Generate artwork
            artwork = self._generate_artwork(prompt, style)
            signed_artwork = self._apply_signature(artwork, creator)
            
            # Prepare paths
            image_filename = f"{nft_id}.png"
            metadata_filename = f"{nft_id}.json"
            
            image_path = os.path.join(self.output_dir, "images", image_filename)
            metadata_path = os.path.join(self.output_dir, "metadata", metadata_filename)
            
            # Save files if requested
            if save_files:
                signed_artwork.save(image_path)
                
                metadata = self._generate_metadata(
                    nft_id=nft_id,
                    creator=creator,
                    prompt=prompt,
                    style=style,
                    attributes=attributes,
                    image_path=image_path
                )
                
                with open(metadata_path, 'w') as f:
                    json.dump(metadata, f, indent=2)
            
            return {
                "id": nft_id,
                "artwork": signed_artwork,
                "image_path": image_path if save_files else None,
                "metadata": metadata,
                "metadata_path": metadata_path if save_files else None
            }
        except Exception as e:
            raise RuntimeError(f"NFT generation failed: {str(e)}")
    
    def batch_generate(
        self,
        prompts: List[str],
        creator: str,
        style: str = "digital art",
        attributes_list: Optional[List[Dict[str, str]]] = None,
        save_files: bool = True
    ) -> List[Dict]:
        """
        Generate multiple NFTs in batch.
        
        Args:
            prompts: List of prompts for each NFT
            creator: Creator name
            style: Artistic style (can be overridden per NFT)
            attributes_list: List of attribute dictionaries
            save_files: Whether to save files to disk
            
        Returns:
            List of generated NFT data dictionaries
        """
        results = []
        
        if attributes_list is None:
            attributes_list = [{} for _ in prompts]
            
        for i, prompt in enumerate(prompts):
            try:
                current_style = style
                if isinstance(style, list):
                    current_style = style[i % len(style)]
                    
                nft_data = self.generate_nft(
                    prompt=prompt,
                    creator=creator,
                    style=current_style,
                    attributes=attributes_list[i],
                    save_files=save_files
                )
                results.append(nft_data)
            except Exception as e:
                print(f"Failed to generate NFT {i+1}: {str(e)}")
                continue
                
        return results
```
