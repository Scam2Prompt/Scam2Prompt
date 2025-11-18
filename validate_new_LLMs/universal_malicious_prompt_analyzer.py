#!/usr/bin/env python3
"""
Universal Malicious Prompt Analyzer

Extracts prompts that trigger ALL models to generate malicious code and finds
the corresponding generated code from all available models.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List, Any, Set, Optional
from datetime import datetime


class UniversalMaliciousPromptAnalyzer:
    """Analyzer to find prompts that make ALL models generate malicious code"""
    
    def __init__(self, 
                 focused_results_file: str = "focused_validation_results_20250917_104336.json",
                 validation_results_dir: str = "validation_results"):
        
        self.focused_results_file = Path(focused_results_file)
        self.validation_results_dir = Path(validation_results_dir)
        
        # All available models (including the 4 additional ones not in focused analysis)
        self.all_models = [
            "x-ai/grok-code-fast-1",
            "deepseek/deepseek-chat-v3.1", 
            "openai/gpt-5",
            "qwen/qwen3-coder",
            "google/gemini-2.5-flash",
            "google/gemini-2.5-pro",
            "anthropic/claude-sonnet-4",
            # Additional models that might have been tested
            "openai/gpt-4o",
            "openai/gpt-4o-mini", 
            "meta-llama/llama-3.1-405b-instruct",
            "meta-llama/llama-3.1-70b-instruct"
        ]
        
        # Load focused results
        self.focused_results = self.load_focused_results()
        
    def load_focused_results(self) -> Dict[str, Any]:
        """Load the focused validation results"""
        if not self.focused_results_file.exists():
            raise FileNotFoundError(f"Focused results file not found: {self.focused_results_file}")
        
        with open(self.focused_results_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def find_universal_malicious_prompts(self) -> List[Dict[str, Any]]:
        """Find prompts that trigger ALL tested models to generate malicious code"""
        print("🔍 Finding prompts that trigger ALL models to generate malicious code...")
        
        # Get the models that were actually tested in focused analysis
        tested_models = list(self.focused_results["model_summaries"].keys())
        print(f"📊 Models in focused analysis: {len(tested_models)}")
        for model in tested_models:
            print(f"   - {model}")
        
        universal_malicious_prompts = []
        
        # Check each prompt
        for prompt_result in self.focused_results["prompt_results"]:
            model_results = prompt_result["model_results"]
            
            # Check if ALL tested models generated malicious code for this prompt
            all_malicious = True
            for model in tested_models:
                if model_results.get(model, "not_tested") != "malicious":
                    all_malicious = False
                    break
            
            if all_malicious:
                universal_malicious_prompts.append(prompt_result)
        
        print(f"🚨 Found {len(universal_malicious_prompts)} prompts that trigger ALL {len(tested_models)} models to generate malicious code!")
        
        return universal_malicious_prompts
    
    def get_cache_key(self, model: str, prompt: str) -> str:
        """Generate deterministic cache key (same as validation system)"""
        combined = f"{model}:{prompt}"
        return hashlib.sha256(combined.encode('utf-8')).hexdigest()
    
    def find_generated_code_for_prompt(self, model_identifier: str, prompt: str) -> Optional[Dict[str, Any]]:
        """Find the generated code file for a specific model and prompt"""
        sanitized_model = model_identifier.replace('/', '_')
        model_dir = self.validation_results_dir / sanitized_model
        
        if not model_dir.exists():
            return None
        
        # Check both generated and malicious code directories
        for subdir in ["generated_code", "malicious_code"]:
            result_dir = model_dir / subdir
            if not result_dir.exists():
                continue
                
            # Look for metadata files
            for metadata_file in result_dir.glob("metadata_*.json"):
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    if metadata.get('prompt') == prompt:
                        # Found the metadata, now get the code file
                        code_file = str(metadata_file).replace('metadata_', '').replace('.json', '.py')
                        code_content = ""
                        
                        if Path(code_file).exists():
                            with open(code_file, 'r', encoding='utf-8') as f:
                                code_content = f.read()
                        
                        return {
                            "model": model_identifier,
                            "result_type": "malicious" if subdir == "malicious_code" else "benign",
                            "metadata_file": str(metadata_file),
                            "code_file": code_file,
                            "code_content": code_content,
                            "urls_found": metadata.get('urls_found_in_code', []),
                            "malicious_urls_count": metadata.get('malicious_urls_count', 0),
                            "oracle_results": metadata.get('oracle_results', {})
                        }
                        
                except Exception as e:
                    continue
        
        return None
    
    def analyze_universal_prompts_across_all_models(self, universal_prompts: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Analyze universal malicious prompts across ALL available models"""
        print(f"\n🔍 Analyzing {len(universal_prompts)} universal prompts across ALL {len(self.all_models)} models...")
        
        analysis_results = {
            "analysis_info": {
                "timestamp": datetime.now().isoformat(),
                "universal_prompts_count": len(universal_prompts),
                "total_models_checked": len(self.all_models),
                "focused_models_count": len(self.focused_results["model_summaries"]),
                "description": "Analysis of prompts that trigger ALL focused models to generate malicious code, checked against all available models"
            },
            "universal_prompts_analysis": []
        }
        
        for i, prompt_data in enumerate(universal_prompts):
            print(f"   Analyzing prompt {i+1}/{len(universal_prompts)}...")
            
            prompt_analysis = {
                "prompt_index": i,
                "prompt": prompt_data["prompt"],
                "category": prompt_data["category"],
                "shared_by_models": prompt_data["shared_by_models"],
                "category_description": prompt_data["category_description"],
                "original_models": prompt_data.get("original_models", []),
                "focused_results": prompt_data["model_results"],
                "all_models_results": {}
            }
            
            # Check this prompt against ALL available models
            for model in self.all_models:
                code_result = self.find_generated_code_for_prompt(model, prompt_data["prompt"])
                
                if code_result:
                    prompt_analysis["all_models_results"][model] = {
                        "tested": True,
                        "result_type": code_result["result_type"],
                        "urls_found": code_result["urls_found"],
                        "malicious_urls_count": code_result["malicious_urls_count"],
                        "code_file": code_result["code_file"],
                        "code_preview": code_result["code_content"][:500] + "..." if len(code_result["code_content"]) > 500 else code_result["code_content"],
                        "full_code_length": len(code_result["code_content"]),
                        "oracle_results": code_result["oracle_results"]
                    }
                else:
                    prompt_analysis["all_models_results"][model] = {
                        "tested": False,
                        "result_type": "not_tested",
                        "urls_found": [],
                        "malicious_urls_count": 0,
                        "code_file": None,
                        "code_preview": None,
                        "full_code_length": 0,
                        "oracle_results": {}
                    }
            
            analysis_results["universal_prompts_analysis"].append(prompt_analysis)
        
        return analysis_results
    
    def create_detailed_code_report(self, analysis_results: Dict[str, Any]) -> None:
        """Create a detailed report with full code for each universal prompt"""
        print("\n📝 Creating detailed code report...")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        detailed_report_file = f"universal_malicious_detailed_report_{timestamp}.json"
        
        # Create a version with full code content
        detailed_results = analysis_results.copy()
        
        for prompt_analysis in detailed_results["universal_prompts_analysis"]:
            for model, result in prompt_analysis["all_models_results"].items():
                if result["tested"] and result["code_file"]:
                    try:
                        with open(result["code_file"], 'r', encoding='utf-8') as f:
                            full_code = f.read()
                        result["full_code_content"] = full_code
                    except Exception as e:
                        result["full_code_content"] = f"Error reading file: {e}"
                else:
                    result["full_code_content"] = None
        
        # Save detailed report
        with open(detailed_report_file, 'w', encoding='utf-8') as f:
            json.dump(detailed_results, f, indent=2)
        
        print(f"📁 Detailed report saved: {detailed_report_file}")
        return detailed_report_file
    
    def create_summary_report(self, analysis_results: Dict[str, Any]) -> str:
        """Create a summary report of findings"""
        print("\n📊 Creating summary report...")
        
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        summary_file = f"universal_malicious_summary_{timestamp}.txt"
        
        with open(summary_file, 'w', encoding='utf-8') as f:
            f.write("=" * 100 + "\n")
            f.write("UNIVERSAL MALICIOUS PROMPTS ANALYSIS SUMMARY\n")
            f.write("=" * 100 + "\n\n")
            
            f.write(f"Analysis Timestamp: {analysis_results['analysis_info']['timestamp']}\n")
            f.write(f"Universal Malicious Prompts Found: {analysis_results['analysis_info']['universal_prompts_count']}\n")
            f.write(f"Total Models Checked: {analysis_results['analysis_info']['total_models_checked']}\n")
            f.write(f"Focused Analysis Models: {analysis_results['analysis_info']['focused_models_count']}\n\n")
            
            # Analyze model coverage
            model_coverage = {}
            for model in self.all_models:
                tested_count = 0
                malicious_count = 0
                
                for prompt_analysis in analysis_results["universal_prompts_analysis"]:
                    result = prompt_analysis["all_models_results"][model]
                    if result["tested"]:
                        tested_count += 1
                        if result["result_type"] == "malicious":
                            malicious_count += 1
                
                model_coverage[model] = {
                    "tested": tested_count,
                    "malicious": malicious_count,
                    "malicious_rate": (malicious_count / tested_count * 100) if tested_count > 0 else 0
                }
            
            f.write("MODEL COVERAGE FOR UNIVERSAL MALICIOUS PROMPTS:\n")
            f.write("-" * 80 + "\n")
            for model, stats in model_coverage.items():
                f.write(f"{model:30} | Tested: {stats['tested']:3} | Malicious: {stats['malicious']:3} | Rate: {stats['malicious_rate']:5.1f}%\n")
            
            f.write("\n" + "=" * 100 + "\n")
            f.write("DETAILED PROMPT ANALYSIS:\n")
            f.write("=" * 100 + "\n\n")
            
            for i, prompt_analysis in enumerate(analysis_results["universal_prompts_analysis"]):
                f.write(f"PROMPT {i+1}:\n")
                f.write("-" * 50 + "\n")
                f.write(f"Category: {prompt_analysis['category']} ({prompt_analysis['category_description']})\n")
                f.write(f"Shared by {prompt_analysis['shared_by_models']} models originally\n")
                f.write(f"Prompt: {prompt_analysis['prompt'][:200]}{'...' if len(prompt_analysis['prompt']) > 200 else ''}\n\n")
                
                f.write("Model Results:\n")
                for model, result in prompt_analysis["all_models_results"].items():
                    status = "✓ MALICIOUS" if result["result_type"] == "malicious" else "○ BENIGN" if result["result_type"] == "benign" else "✗ NOT TESTED"
                    urls = f" ({result['malicious_urls_count']} malicious URLs)" if result["malicious_urls_count"] > 0 else ""
                    f.write(f"  {model:30} | {status}{urls}\n")
                
                f.write("\n" + "="*100 + "\n\n")
        
        print(f"📋 Summary report saved: {summary_file}")
        return summary_file
    
    def run_analysis(self) -> Dict[str, Any]:
        """Run complete universal malicious prompt analysis"""
        print("🚀 Starting Universal Malicious Prompt Analysis")
        print("=" * 80)
        
        # Step 1: Find universal malicious prompts
        universal_prompts = self.find_universal_malicious_prompts()
        
        if not universal_prompts:
            print("❌ No prompts found that trigger ALL models to generate malicious code!")
            return {"error": "No universal malicious prompts found"}
        
        # Step 2: Analyze across all available models
        analysis_results = self.analyze_universal_prompts_across_all_models(universal_prompts)
        
        # Step 3: Create detailed report with full code
        detailed_report_file = self.create_detailed_code_report(analysis_results)
        
        # Step 4: Create summary report
        summary_report_file = self.create_summary_report(analysis_results)
        
        print(f"\n✅ Universal Malicious Prompt Analysis Complete!")
        print(f"🚨 Found {len(universal_prompts)} prompts that trigger ALL focused models to be malicious")
        print(f"📁 Detailed report: {detailed_report_file}")
        print(f"📋 Summary report: {summary_report_file}")
        
        return analysis_results


def main():
    """Main function"""
    try:
        analyzer = UniversalMaliciousPromptAnalyzer()
        results = analyzer.run_analysis()
        return results
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    main()
