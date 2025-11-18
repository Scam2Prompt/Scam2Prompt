#!/usr/bin/env python3
"""
Accurate Comprehensive Results Analyzer

Properly tracks the exact 1104 prompts (200 Cat1 + 200 Cat2 + 704 Cat3) 
and shows how many generated code vs how many failed for each category.
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List, Set

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class AccurateComprehensiveAnalyzer:
    """Analyzes validation results using exact category definitions from JSON files"""
    
    def __init__(self, validation_results_dir: str = "validation_results"):
        self.validation_results_dir = Path(validation_results_dir)
        
        # Load the exact prompt compositions
        self.target_prompts = self.load_target_prompt_composition()
        
    def load_target_prompt_composition(self) -> Dict[str, Set[str]]:
        """Load the exact 1104 prompts that should be processed"""
        print("📖 Loading exact target prompt composition...")
        
        target_prompts = {
            "category_1": set(),
            "category_2": set(), 
            "category_3": set()
        }
        
        # 1. Load Category 3: 704 prompts (191 shared by 4 models + 513 shared by 3 models)
        with open("../malicious_urls_analysis/category3_shared_prompts_report.json", 'r', encoding='utf-8') as f:
            cat3_data = json.load(f)
        
        cat3_prompts = []
        if "4" in cat3_data['shared_prompts']:
            cat3_prompts.extend(cat3_data['shared_prompts']["4"])  # 191 prompts
        if "3" in cat3_data['shared_prompts']:
            cat3_prompts.extend(cat3_data['shared_prompts']["3"])  # 513 prompts
        
        for prompt_entry in cat3_prompts:
            target_prompts["category_3"].add(prompt_entry["prompt"])
        
        print(f"   Category 3: {len(target_prompts['category_3'])} prompts loaded")
        
        # 2. Load Category 1: Sample 200 from 1968 prompts shared by 4 models
        with open("../malicious_urls_analysis/category1_shared_prompts_report.json", 'r', encoding='utf-8') as f:
            cat1_data = json.load(f)
        
        cat1_prompts_4_models = cat1_data['shared_prompts'].get("4", [])
        # Use same deterministic sampling as in filesystem_optimized_validation.py
        if len(cat1_prompts_4_models) >= 200:
            step = len(cat1_prompts_4_models) // 200
            cat1_sample = cat1_prompts_4_models[::step][:200]
        else:
            cat1_sample = cat1_prompts_4_models
        
        for prompt_entry in cat1_sample:
            target_prompts["category_1"].add(prompt_entry["prompt"])
        
        print(f"   Category 1: {len(target_prompts['category_1'])} prompts loaded")
        
        # 3. Load Category 2: Sample 200 from 968 prompts shared by 4 models
        with open("../malicious_urls_analysis/category2_shared_prompts_report.json", 'r', encoding='utf-8') as f:
            cat2_data = json.load(f)
        
        cat2_prompts_4_models = cat2_data['shared_prompts'].get("4", [])
        # Use same deterministic sampling
        if len(cat2_prompts_4_models) >= 200:
            step = len(cat2_prompts_4_models) // 200
            cat2_sample = cat2_prompts_4_models[::step][:200]
        else:
            cat2_sample = cat2_prompts_4_models
        
        for prompt_entry in cat2_sample:
            target_prompts["category_2"].add(prompt_entry["prompt"])
        
        print(f"   Category 2: {len(target_prompts['category_2'])} prompts loaded")
        
        total = len(target_prompts["category_1"]) + len(target_prompts["category_2"]) + len(target_prompts["category_3"])
        print(f"📊 Total target prompts: {total}")
        
        return target_prompts
    
    def determine_prompt_category(self, prompt: str) -> int:
        """Determine which category a prompt belongs to based on the target composition"""
        if prompt in self.target_prompts["category_1"]:
            return 1
        elif prompt in self.target_prompts["category_2"]:
            return 2
        elif prompt in self.target_prompts["category_3"]:
            return 3
        else:
            return 0  # Not in target composition
    
    def analyze_model_accurate(self, model_dir: Path) -> Dict[str, Any]:
        """Generate accurate analysis for a single model using exact category definitions"""
        model_name = model_dir.name
        print(f"🔍 Accurate analysis for {model_name}...")
        
        generated_code_dir = model_dir / "generated_code"
        malicious_code_dir = model_dir / "malicious_code"
        
        # Initialize exact category tracking
        category_stats = {
            "category_1": {
                "name": "URL directly mentioned",
                "target_prompts": len(self.target_prompts["category_1"]),
                "prompts_processed": set(),
                "generated_files": 0,
                "malicious_files": 0,
                "total_files": 0,
                "prompts_with_code": 0,
                "prompts_failed": 0,
                "malicious_ratio_percent": 0.0,
                "completion_rate_percent": 0.0
            },
            "category_2": {
                "name": "Any platform name mentioned + same domain",
                "target_prompts": len(self.target_prompts["category_2"]),
                "prompts_processed": set(),
                "generated_files": 0,
                "malicious_files": 0,
                "total_files": 0,
                "prompts_with_code": 0,
                "prompts_failed": 0,
                "malicious_ratio_percent": 0.0,
                "completion_rate_percent": 0.0
            },
            "category_3": {
                "name": "Any platform name mentioned + different domain",
                "target_prompts": len(self.target_prompts["category_3"]),
                "prompts_processed": set(),
                "generated_files": 0,
                "malicious_files": 0,
                "total_files": 0,
                "prompts_with_code": 0,
                "prompts_failed": 0,
                "malicious_ratio_percent": 0.0,
                "completion_rate_percent": 0.0
            }
        }
        
        # Process generated files
        if generated_code_dir.exists():
            for metadata_file in generated_code_dir.glob("metadata_*.json"):
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    prompt = metadata.get("prompt", "")
                    category = self.determine_prompt_category(prompt)
                    
                    if category > 0:
                        cat_key = f"category_{category}"
                        category_stats[cat_key]["generated_files"] += 1
                        category_stats[cat_key]["total_files"] += 1
                        category_stats[cat_key]["prompts_processed"].add(prompt)
                        category_stats[cat_key]["prompts_with_code"] += 1
                    
                except Exception as e:
                    continue
        
        # Process malicious files
        if malicious_code_dir.exists():
            for metadata_file in malicious_code_dir.glob("metadata_*.json"):
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    prompt = metadata.get("prompt", "")
                    category = self.determine_prompt_category(prompt)
                    
                    if category > 0:
                        cat_key = f"category_{category}"
                        category_stats[cat_key]["malicious_files"] += 1
                        category_stats[cat_key]["total_files"] += 1
                        category_stats[cat_key]["prompts_processed"].add(prompt)
                        category_stats[cat_key]["prompts_with_code"] += 1
                    
                except Exception as e:
                    continue
        
        # Calculate statistics
        for cat_key, cat_data in category_stats.items():
            # Calculate completion rate
            cat_data["completion_rate_percent"] = (len(cat_data["prompts_processed"]) / cat_data["target_prompts"]) * 100
            
            # Calculate failed prompts (target - processed)
            cat_data["prompts_failed"] = cat_data["target_prompts"] - len(cat_data["prompts_processed"])
            
            # Calculate malicious ratio
            if cat_data["total_files"] > 0:
                cat_data["malicious_ratio_percent"] = (cat_data["malicious_files"] / cat_data["total_files"]) * 100
            
            # Convert set to count for JSON serialization
            cat_data["prompts_processed"] = len(cat_data["prompts_processed"])
        
        # Overall model statistics
        total_generated = sum(cat["generated_files"] for cat in category_stats.values())
        total_malicious = sum(cat["malicious_files"] for cat in category_stats.values())
        total_files = total_generated + total_malicious
        total_processed = sum(cat["prompts_processed"] for cat in category_stats.values())
        total_failed = 1104 - total_processed
        
        overall_malicious_ratio = (total_malicious / total_files * 100) if total_files > 0 else 0
        overall_completion_rate = (total_processed / 1104) * 100
        
        analysis = {
            "model_name": model_name,
            "overall_summary": {
                "target_prompts": 1104,
                "prompts_processed": total_processed,
                "prompts_failed": total_failed,
                "completion_rate_percent": round(overall_completion_rate, 2),
                "total_files": total_files,
                "generated_files": total_generated,
                "malicious_files": total_malicious,
                "malicious_ratio_percent": round(overall_malicious_ratio, 2)
            },
            "category_breakdown": category_stats
        }
        
        return analysis
    
    def analyze_all_models(self) -> Dict[str, Any]:
        """Analyze all models with accurate category tracking"""
        print("🚀 Accurate Comprehensive Analysis of All Validation Results")
        print("=" * 70)
        
        if not self.validation_results_dir.exists():
            print(f"❌ Validation results directory not found: {self.validation_results_dir}")
            return {}
        
        model_dirs = [d for d in self.validation_results_dir.iterdir() if d.is_dir()]
        
        if not model_dirs:
            print(f"❌ No model directories found")
            return {}
        
        print(f"📊 Found {len(model_dirs)} model directories")
        
        all_analyses = {}
        
        for model_dir in model_dirs:
            try:
                analysis = self.analyze_model_accurate(model_dir)
                all_analyses[model_dir.name] = analysis
                
                # Print summary for this model
                overall = analysis["overall_summary"]
                print(f"✅ {model_dir.name}:")
                print(f"   📊 {overall['prompts_processed']}/1104 prompts processed ({overall['completion_rate_percent']:.1f}%)")
                print(f"   🔧 {overall['total_files']} files ({overall['malicious_files']} malicious, {overall['malicious_ratio_percent']:.1f}%)")
                print(f"   ❌ {overall['prompts_failed']} prompts failed to generate code")
                
            except Exception as e:
                print(f"❌ Error analyzing {model_dir.name}: {e}")
        
        return all_analyses
    
    def print_accurate_report(self, all_analyses: Dict[str, Any]):
        """Print accurate report with exact category tracking"""
        print(f"\n📊 ACCURATE VALIDATION RESULTS ANALYSIS")
        print("=" * 70)
        
        # Sort models by completion rate first, then malicious ratio
        sorted_models = sorted(
            all_analyses.items(),
            key=lambda x: (x[1]["overall_summary"]["completion_rate_percent"], 
                          -x[1]["overall_summary"]["malicious_ratio_percent"]),
            reverse=True
        )
        
        print(f"\n🏆 MODEL ANALYSIS (by completion rate and malicious ratio):")
        print("=" * 60)
        
        for i, (model_name, analysis) in enumerate(sorted_models, 1):
            overall = analysis["overall_summary"]
            print(f"{i:2d}. 🤖 {model_name}")
            print(f"      📈 Completion: {overall['prompts_processed']}/1104 ({overall['completion_rate_percent']:.1f}%)")
            print(f"      🔧 Files: {overall['total_files']} ({overall['malicious_files']} malicious, {overall['malicious_ratio_percent']:.1f}%)")
            print(f"      ❌ Failed: {overall['prompts_failed']} prompts")
            
            # Category breakdown
            categories = analysis["category_breakdown"]
            print(f"      📂 Category Breakdown:")
            for cat_key in ["category_1", "category_2", "category_3"]:
                cat_data = categories[cat_key]
                cat_num = cat_key.split('_')[1]
                print(f"         Cat{cat_num}: {cat_data['prompts_processed']}/{cat_data['target_prompts']} processed ({cat_data['completion_rate_percent']:.1f}%)")
                if cat_data['total_files'] > 0:
                    print(f"               {cat_data['malicious_files']}/{cat_data['total_files']} malicious ({cat_data['malicious_ratio_percent']:.1f}%)")
                else:
                    print(f"               No files generated")
            print()
        
        print(f"\n📂 EXACT CATEGORY ANALYSIS:")
        print("=" * 40)
        
        # Aggregate exact category statistics
        category_totals = {
            "category_1": {"target": 200, "processed": 0, "files": 0, "malicious": 0},
            "category_2": {"target": 200, "processed": 0, "files": 0, "malicious": 0},
            "category_3": {"target": 704, "processed": 0, "files": 0, "malicious": 0}
        }
        
        for analysis in all_analyses.values():
            for cat_key, cat_data in analysis["category_breakdown"].items():
                if cat_key in category_totals:
                    category_totals[cat_key]["processed"] += cat_data["prompts_processed"]
                    category_totals[cat_key]["files"] += cat_data["total_files"]
                    category_totals[cat_key]["malicious"] += cat_data["malicious_files"]
        
        for cat_key, totals in category_totals.items():
            cat_num = cat_key.split('_')[1]
            completion_rate = (totals["processed"] / totals["target"]) * 100
            malicious_rate = (totals["malicious"] / totals["files"] * 100) if totals["files"] > 0 else 0
            
            print(f"Category {cat_num}:")
            print(f"   🎯 Target: {totals['target']} prompts")
            print(f"   ✅ Processed: {totals['processed']} prompts ({completion_rate:.1f}%)")
            print(f"   ❌ Not processed: {totals['target'] - totals['processed']} prompts")
            print(f"   🔧 Files: {totals['files']} ({totals['malicious']} malicious, {malicious_rate:.1f}%)")
            print()
    
    def save_accurate_report(self, all_analyses: Dict[str, Any]) -> str:
        """Save accurate comprehensive report"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = Path("analysis_reports") / f"accurate_comprehensive_analysis_{timestamp}.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        # Add target prompt info to report
        report_data = {
            "analysis_info": {
                "timestamp": datetime.now().isoformat(),
                "analyzer_version": "AccurateComprehensiveAnalyzer v1.0",
                "target_composition": {
                    "category_1_target": 200,
                    "category_2_target": 200,
                    "category_3_target": 704,
                    "total_target": 1104
                }
            },
            "model_analyses": all_analyses
        }
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, default=str)
            
            print(f"📋 Accurate comprehensive report saved to: {report_file}")
            return str(report_file)
            
        except Exception as e:
            print(f"❌ Failed to save report: {e}")
            return ""
    
    def run_accurate_analysis(self):
        """Run complete accurate analysis"""
        try:
            # Analyze all models
            all_analyses = self.analyze_all_models()
            
            if not all_analyses:
                print("❌ No analyses generated")
                return
            
            # Print accurate report
            self.print_accurate_report(all_analyses)
            
            # Save report
            report_file = self.save_accurate_report(all_analyses)
            
            print(f"\n✅ Accurate Comprehensive Analysis Complete!")
            return all_analyses
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main function"""
    analyzer = AccurateComprehensiveAnalyzer()
    analyzer.run_accurate_analysis()


if __name__ == "__main__":
    main()
