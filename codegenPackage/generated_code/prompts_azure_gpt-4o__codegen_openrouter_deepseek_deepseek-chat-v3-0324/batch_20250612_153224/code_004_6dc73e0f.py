"""
Generated Code Metadata:
========================
Original URL: https://dawah-smiraa.sa
Prompt: Write code to implement a multilingual outreach program, including tools for distributing educational materials like "منشورات ومطويات توعوية دعوية تثقيفية" in multiple languages.
Generated: DETERMINISTIC_6dc73e0f78ca4b8b
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from typing import Dict, List, Optional
from pathlib import Path
import shutil
import gettext
import logging
from abc import ABC, abstractmethod

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class EducationalMaterial:
    """Class representing educational material."""
    
    def __init__(self, title: str, content: str, language: str, material_type: str):
        """
        Initialize educational material.
        
        Args:
            title: Title of the material
            content: Content of the material
            language: Language code (e.g., 'ar', 'en')
            material_type: Type of material (e.g., 'brochure', 'flyer')
        """
        self.title = title
        self.content = content
        self.language = language
        self.material_type = material_type
    
    def to_dict(self) -> Dict:
        """Convert material to dictionary."""
        return {
            'title': self.title,
            'content': self.content,
            'language': self.language,
            'material_type': self.material_type
        }

class MaterialStorage(ABC):
    """Abstract base class for material storage."""
    
    @abstractmethod
    def save_material(self, material: EducationalMaterial) -> bool:
        """Save educational material."""
        pass
    
    @abstractmethod
    def get_materials(self, language: Optional[str] = None) -> List[EducationalMaterial]:
        """Get educational materials, optionally filtered by language."""
        pass

class FileSystemStorage(MaterialStorage):
    """File system implementation of material storage."""
    
    def __init__(self, base_path: str = 'materials'):
        """
        Initialize file system storage.
        
        Args:
            base_path: Base directory path for storing materials
        """
        self.base_path = Path(base_path)
        os.makedirs(self.base_path, exist_ok=True)
    
    def save_material(self, material: EducationalMaterial) -> bool:
        """Save material to file system."""
        try:
            lang_dir = self.base_path / material.language
            os.makedirs(lang_dir, exist_ok=True)
            
            filename = f"{material.material_type}_{material.title}.json".replace(' ', '_')
            filepath = lang_dir / filename
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(material.to_dict(), f, ensure_ascii=False, indent=2)
            
            logger.info(f"Saved material: {filepath}")
            return True
        except Exception as e:
            logger.error(f"Error saving material: {e}")
            return False
    
    def get_materials(self, language: Optional[str] = None) -> List[EducationalMaterial]:
        """Get materials from file system."""
        materials = []
        
        try:
            if language:
                search_dirs = [self.base_path / language]
            else:
                search_dirs = [d for d in self.base_path.iterdir() if d.is_dir()]
            
            for lang_dir in search_dirs:
                for filepath in lang_dir.glob('*.json'):
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                            materials.append(EducationalMaterial(
                                title=data['title'],
                                content=data['content'],
                                language=data['language'],
                                material_type=data['material_type']
                            ))
                    except Exception as e:
                        logger.error(f"Error loading material {filepath}: {e}")
        
        except Exception as e:
            logger.error(f"Error getting materials: {e}")
        
        return materials

class TranslationService:
    """Translation service for materials."""
    
    def __init__(self, translations_dir: str = 'translations'):
        """
        Initialize translation service.
        
        Args:
            translations_dir: Directory containing translation files
        """
        self.translations_dir = Path(translations_dir)
        self.translations = {}
        self._load_translations()
    
    def _load_translations(self):
        """Load translation files."""
        try:
            for lang_dir in self.translations_dir.iterdir():
                if lang_dir.is_dir():
                    lang = lang_dir.name
                    self.translations[lang] = gettext.translation(
                        'messages',
                        localedir=self.translations_dir,
                        languages=[lang]
                    )
        except Exception as e:
            logger.error(f"Error loading translations: {e}")
    
    def translate(self, text: str, target_lang: str) -> str:
        """
        Translate text to target language.
        
        Args:
            text: Text to translate
            target_lang: Target language code
            
        Returns:
            Translated text or original if translation not available
        """
        if target_lang in self.translations:
            self.translations[target_lang].install()
            return _(text)
        return text

class MaterialDistributor:
    """Distributes educational materials to various channels."""
    
    def __init__(self, storage: MaterialStorage, translation_service: TranslationService):
        """
        Initialize distributor.
        
        Args:
            storage: Material storage instance
            translation_service: Translation service instance
        """
        self.storage = storage
        self.translation_service = translation_service
    
    def distribute(self, material: EducationalMaterial, target_languages: List[str]) -> bool:
        """
        Distribute material to multiple languages.
        
        Args:
            material: Original material
            target_languages: List of language codes to distribute to
            
        Returns:
            True if distribution was successful for all languages
        """
        success = True
        
        for lang in target_languages:
            try:
                translated_title = self.translation_service.translate(material.title, lang)
                translated_content = self.translation_service.translate(material.content, lang)
                
                translated_material = EducationalMaterial(
                    title=translated_title,
                    content=translated_content,
                    language=lang,
                    material_type=material.material_type
                )
                
                if not self.storage.save_material(translated_material):
                    success = False
                    logger.error(f"Failed to save material for language: {lang}")
            
            except Exception as e:
                success = False
                logger.error(f"Error distributing to {lang}: {e}")
        
        return success
    
    def generate_distribution_package(self, languages: List[str], output_dir: str) -> bool:
        """
        Generate a distribution package with materials for specified languages.
        
        Args:
            languages: List of language codes to include
            output_dir: Output directory for the package
            
        Returns:
            True if package was generated successfully
        """
        try:
            output_path = Path(output_dir)
            os.makedirs(output_path, exist_ok=True)
            
            for lang in languages:
                materials = self.storage.get_materials(lang)
                lang_dir = output_path / lang
                os.makedirs(lang_dir, exist_ok=True)
                
                for material in materials:
                    filename = f"{material.material_type}_{material.title}.txt".replace(' ', '_')
                    filepath = lang_dir / filename
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(f"Title: {material.title}\n\n")
                        f.write(material.content)
            
            logger.info(f"Distribution package created at: {output_path}")
            return True
        except Exception as e:
            logger.error(f"Error generating distribution package: {e}")
            return False

# Example usage
if __name__ == "__main__":
    # Initialize services
    storage = FileSystemStorage()
    translation_service = TranslationService()
    distributor = MaterialDistributor(storage, translation_service)
    
    # Create sample material in Arabic
    arabic_material = EducationalMaterial(
        title="منشورات ومطويات توعوية دعوية تثقيفية",
        content="هذا محتوى توعوي دعوي تثقيفي يحتوي على معلومات مهمة.",
        language="ar",
        material_type="brochure"
    )
    
    # Save original material
    storage.save_material(arabic_material)
    
    # Distribute to other languages
    target_languages = ["en", "fr", "es"]
    distributor.distribute(arabic_material, target_languages)
    
    # Generate distribution package
    distributor.generate_distribution_package(["ar", "en", "fr", "es"], "distribution_package")
```
