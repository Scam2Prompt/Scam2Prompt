#!/usr/bin/env python3
"""
Incomplete Prompts Collector

This script analyzes all validation results and collects prompts that generated incomplete code.
It creates a structured collection similar to problematic_files_collection but specifically
for incomplete prompts only.

Output structure:
incomplete_prompts_collection_TIMESTAMP/
├── model_name/
│   ├── prompts/
│   │   └── model_name_incomplete_prompts.json
│   └── files/
│       └── [incomplete .py files]
└── collection_summary.json
"""

import json
import hashlib
import shutil
from pathlib import Path
from typing import Dict, List, Any, Set
from datetime import datetime
import sys
import os

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the classification logic from focused_validation_analyzer
from focused_validation_analyzer import FocusedValidationAnalyzer


class IncompletePromptsCollector:
    """Collects all incomplete prompts and their corresponding code files"""
    
    def __init__(self, 
                 validation_results_dir: str = "validation_results",
                 output_base_dir: str = "incomplete_prompts_collection"):
        
        self.validation_results_dir = Path(validation_results_dir)
        
        # Create timestamped output directory
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        self.output_dir = Path(f"{output_base_dir}_{timestamp}")
        self.output_dir.mkdir(parents=True, exist_ok=True)
        
        # Available models
        self.models = [
            "x-ai/grok-code-fast-1",
            "deepseek/deepseek-chat-v3.1", 
            "openai/gpt-5",
            "qwen/qwen3-coder",
            "google/gemini-2.5-flash",
            "google/gemini-2.5-pro",
            "anthropic/claude-sonnet-4"
        ]
        
        # Initialize analyzer for classification
        self.analyzer = FocusedValidationAnalyzer()
        
        # Collection statistics
        self.stats = {
            "collection_timestamp": timestamp,
            "total_models": len(self.models),
            "models_processed": 0,
            "total_incomplete_prompts": 0,
            "total_incomplete_files": 0,
            "model_stats": {}
        }
    
    def get_prompt_from_metadata(self, metadata_file: Path) -> Dict[str, Any]:
        """Extract prompt information from metadata file"""
        try:
            with open(metadata_file, 'r', encoding='utf-8') as f:
                metadata = json.load(f)
            
            return {
                "prompt": metadata.get("prompt", ""),
                "prompt_index": metadata.get("prompt_index", -1),
                "model_identifier": metadata.get("model_identifier", ""),
                "timestamp": metadata.get("timestamp", ""),
                "metadata_file": str(metadata_file)
            }
        except Exception as e:
            print(f"Warning: Could not read metadata from {metadata_file}: {e}")
            return None
    
    def find_corresponding_python_file(self, metadata_file: Path) -> Path:
        """Find the corresponding Python file for a metadata file"""
        # Extract the identifier from metadata filename
        # Format: metadata_XXX_YYYYYYYY.json -> model_validation_XXX_YYYYYYYY.py
        parts = metadata_file.stem.split('_')
        if len(parts) >= 3:
            prompt_idx = parts[1]
            prompt_hash = parts[2]
            
            # Get model identifier from parent directory
            model_dir = metadata_file.parent.parent
            sanitized_model = model_dir.name
            
            py_filename = f"{sanitized_model}_validation_{prompt_idx}_{prompt_hash}.py"
            py_file = metadata_file.parent / py_filename
            
            if py_file.exists():
                return py_file
        
        return None
    
    def collect_incomplete_for_model(self, model_identifier: str) -> Dict[str, Any]:
        """Collect all incomplete prompts for a specific model"""
        print(f"🔍 Processing model: {model_identifier}")
        
        sanitized_model = model_identifier.replace('/', '_')
        model_dir = self.validation_results_dir / sanitized_model
        
        if not model_dir.exists():
            print(f"⚠️  Model directory not found: {model_dir}")
            return {"incomplete_prompts": [], "incomplete_files": []}
        
        incomplete_prompts = []
        incomplete_files = []
        
        # Check both generated_code and malicious_code directories
        for subdir in ["generated_code", "malicious_code"]:
            result_dir = model_dir / subdir
            if not result_dir.exists():
                continue
            
            print(f"   📁 Checking {subdir}...")
            
            # Find all metadata files
            metadata_files = list(result_dir.glob("metadata_*.json"))
            print(f"   📄 Found {len(metadata_files)} metadata files")
            
            for metadata_file in metadata_files:
                # Find corresponding Python file
                py_file = self.find_corresponding_python_file(metadata_file)
                
                if py_file and py_file.exists():
                    # Classify the file
                    classification = self.analyzer.categorize_python_file_completion(py_file)
                    
                    if classification == "incomplete":
                        # Get prompt information
                        prompt_info = self.get_prompt_from_metadata(metadata_file)
                        
                        if prompt_info:
                            prompt_info["python_file"] = str(py_file)
                            prompt_info["classification"] = classification
                            prompt_info["directory"] = subdir
                            
                            incomplete_prompts.append(prompt_info)
                            incomplete_files.append(str(py_file))
                            
                            if len(incomplete_prompts) % 50 == 0:
                                print(f"   📊 Found {len(incomplete_prompts)} incomplete prompts so far...")
        
        print(f"   ✅ Found {len(incomplete_prompts)} incomplete prompts for {model_identifier}")
        
        return {
            "incomplete_prompts": incomplete_prompts,
            "incomplete_files": incomplete_files,
            "model_identifier": model_identifier,
            "collection_timestamp": self.stats["collection_timestamp"]
        }
    
    def save_model_collection(self, model_identifier: str, collection_data: Dict[str, Any]) -> None:
        """Save collection data for a specific model"""
        sanitized_model = model_identifier.replace('/', '_')
        model_output_dir = self.output_dir / sanitized_model
        
        # Create directories
        prompts_dir = model_output_dir / "prompts"
        files_dir = model_output_dir / "files"
        prompts_dir.mkdir(parents=True, exist_ok=True)
        files_dir.mkdir(parents=True, exist_ok=True)
        
        # Save prompts JSON
        prompts_file = prompts_dir / f"{sanitized_model}_incomplete_prompts.json"
        with open(prompts_file, 'w', encoding='utf-8') as f:
            json.dump(collection_data, f, indent=2)
        
        print(f"   💾 Saved {len(collection_data['incomplete_prompts'])} prompts to {prompts_file}")
        
        # Copy incomplete Python files
        copied_files = 0
        for file_path in collection_data['incomplete_files']:
            src_file = Path(file_path)
            if src_file.exists():
                dst_file = files_dir / src_file.name
                try:
                    shutil.copy2(src_file, dst_file)
                    copied_files += 1
                except Exception as e:
                    print(f"   ⚠️  Failed to copy {src_file.name}: {e}")
        
        print(f"   📁 Copied {copied_files} incomplete files to {files_dir}")
        
        # Update stats
        self.stats["model_stats"][model_identifier] = {
            "incomplete_prompts": len(collection_data['incomplete_prompts']),
            "incomplete_files": len(collection_data['incomplete_files']),
            "files_copied": copied_files
        }
    
    def collect_all_incomplete(self) -> None:
        """Collect incomplete prompts for all models"""
        print("🚀 Starting Incomplete Prompts Collection")
        print("=" * 60)
        
        for model in self.models:
            try:
                collection_data = self.collect_incomplete_for_model(model)
                
                if collection_data["incomplete_prompts"]:
                    self.save_model_collection(model, collection_data)
                    self.stats["total_incomplete_prompts"] += len(collection_data["incomplete_prompts"])
                    self.stats["total_incomplete_files"] += len(collection_data["incomplete_files"])
                else:
                    print(f"   ℹ️  No incomplete prompts found for {model}")
                
                self.stats["models_processed"] += 1
                
            except Exception as e:
                print(f"❌ Error processing {model}: {e}")
                import traceback
                traceback.print_exc()
        
        # Save collection summary
        self.save_collection_summary()
        
        print(f"\n🎉 Collection Complete!")
        print(f"📊 Summary:")
        print(f"   - Models processed: {self.stats['models_processed']}/{self.stats['total_models']}")
        print(f"   - Total incomplete prompts: {self.stats['total_incomplete_prompts']}")
        print(f"   - Total incomplete files: {self.stats['total_incomplete_files']}")
        print(f"   - Output directory: {self.output_dir}")
        
        # Show per-model breakdown
        print(f"\n📋 Per-Model Breakdown:")
        for model, stats in self.stats["model_stats"].items():
            print(f"   {model}: {stats['incomplete_prompts']} prompts, {stats['files_copied']} files")
    
    def save_collection_summary(self) -> None:
        """Save overall collection summary"""
        summary_file = self.output_dir / "collection_summary.json"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            json.dump(self.stats, f, indent=2)
        
        print(f"📋 Collection summary saved to: {summary_file}")


def main():
    """Main function"""
    try:
        collector = IncompletePromptsCollector()
        collector.collect_all_incomplete()
        
        return collector.output_dir
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    main()
