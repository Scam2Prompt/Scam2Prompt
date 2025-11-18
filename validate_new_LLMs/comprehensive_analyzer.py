#!/usr/bin/env python3
"""
Comprehensive Results Analyzer

Analyzes ALL existing validation results and provides complete breakdown by categories.
This addresses the issue where summary files only show current run results.
"""

import json
import sys
import os
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Add parent directory to path for imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class ComprehensiveAnalyzer:
    """Analyzes all existing validation results with complete category breakdown"""
    
    def __init__(self, validation_results_dir: str = "validation_results"):
        self.validation_results_dir = Path(validation_results_dir)
        
        # Load the exact prompt compositions
        self.target_prompts = self.load_target_prompt_composition()
    
    def load_target_prompt_composition(self) -> Dict[str, Any]:
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
        """Determine which category a prompt belongs to based on exact JSON definitions"""
        if prompt in self.target_prompts["category_1"]:
            return 1
        elif prompt in self.target_prompts["category_2"]:
            return 2
        elif prompt in self.target_prompts["category_3"]:
            return 3
        else:
            return 0  # Not in target composition
    
    def infer_category_from_prompt(self, prompt: str) -> int:
        """Infer category from prompt content with improved logic"""
        prompt_lower = prompt.lower()
        
        # Category 1: URL directly mentioned (explicit URLs in prompt)
        if any(indicator in prompt_lower for indicator in [".com", ".org", ".net", "http://", "https://", "www."]):
            return 1
        
        # Category 2: Platform name mentioned + same domain patterns
        # Look for patterns that suggest same-domain scenarios
        cat2_indicators = [
            "integrate", "api", "services", "platform", "account", "registration", 
            "login", "setup", "configure", "connect to", "use the", "access"
        ]
        
        # Category 3: Platform name + different domain patterns  
        cat3_indicators = [
            "decentralized", "blockchain", "crypto", "defi", "nft", "web3",
            "smart contract", "dapp", "token", "wallet", "bridge", "swap"
        ]
        
        cat2_score = sum(1 for indicator in cat2_indicators if indicator in prompt_lower)
        cat3_score = sum(1 for indicator in cat3_indicators if indicator in prompt_lower)
        
        # If more Category 2 indicators, classify as Category 2
        if cat2_score > cat3_score and cat2_score >= 2:
            return 2
        
        # Default to Category 3 for blockchain/crypto related prompts
        return 3
    
    def analyze_model_comprehensive(self, model_dir: Path) -> Dict[str, Any]:
        """Generate comprehensive analysis for a single model using exact category definitions"""
        model_name = model_dir.name
        print(f"🔍 Comprehensive analysis for {model_name}...")
        
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
                "completion_rate_percent": 0.0,
                "urls_found": 0,
                "malicious_urls": 0,
                "sample_prompts": []
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
                "completion_rate_percent": 0.0,
                "urls_found": 0,
                "malicious_urls": 0,
                "sample_prompts": []
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
                "completion_rate_percent": 0.0,
                "urls_found": 0,
                "malicious_urls": 0,
                "sample_prompts": []
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
                    
                    if category > 0:  # Only count prompts in our target composition
                        cat_key = f"category_{category}"
                        category_stats[cat_key]["generated_files"] += 1
                        category_stats[cat_key]["total_files"] += 1
                        category_stats[cat_key]["urls_found"] += len(metadata.get("urls_found_in_code", []))
                        category_stats[cat_key]["prompts_processed"].add(prompt)
                        category_stats[cat_key]["prompts_with_code"] += 1
                        
                        # Collect sample prompts
                        if len(category_stats[cat_key]["sample_prompts"]) < 3:
                            category_stats[cat_key]["sample_prompts"].append(prompt[:100] + "...")
                    
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
                    
                    if category > 0:  # Only count prompts in our target composition
                        cat_key = f"category_{category}"
                        category_stats[cat_key]["malicious_files"] += 1
                        category_stats[cat_key]["total_files"] += 1
                        category_stats[cat_key]["urls_found"] += len(metadata.get("urls_found_in_code", []))
                        category_stats[cat_key]["malicious_urls"] += metadata.get("malicious_urls_count", 0)
                        category_stats[cat_key]["prompts_processed"].add(prompt)
                        category_stats[cat_key]["prompts_with_code"] += 1
                        
                        # Collect sample prompts
                        if len(category_stats[cat_key]["sample_prompts"]) < 3:
                            category_stats[cat_key]["sample_prompts"].append(prompt[:100] + "...")
                    
                except Exception as e:
                    continue
        
        # Calculate statistics
        for cat_key, cat_data in category_stats.items():
            # Calculate completion rate
            cat_data["completion_rate_percent"] = (len(cat_data["prompts_processed"]) / cat_data["target_prompts"]) * 100
            
            # Calculate failed prompts
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
                "malicious_ratio_percent": round(overall_malicious_ratio, 2),
                "total_urls": sum(cat["urls_found"] for cat in category_stats.values()),
                "malicious_urls": sum(cat["malicious_urls"] for cat in category_stats.values())
            },
            "category_breakdown": category_stats
        }
        
        return analysis
    
    def analyze_all_models(self) -> Dict[str, Any]:
        """Analyze all models comprehensively"""
        print("🚀 Comprehensive Analysis of All Validation Results")
        print("=" * 60)
        
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
                analysis = self.analyze_model_comprehensive(model_dir)
                all_analyses[model_dir.name] = analysis
                
                # Print summary for this model
                overall = analysis["overall_summary"]
                print(f"✅ {model_dir.name}:")
                print(f"   📊 {overall['prompts_processed']}/1104 prompts processed ({overall['completion_rate_percent']:.1f}%)")
                print(f"   🔧 {overall['total_files']} files ({overall['malicious_files']} malicious, {overall['malicious_ratio_percent']:.1f}%)")
                print(f"   ❌ {overall['prompts_failed']} prompts failed to generate code")
                
                # Show category breakdown
                categories = analysis["category_breakdown"]
                for cat_key in ["category_1", "category_2", "category_3"]:
                    cat_data = categories[cat_key]
                    cat_num = cat_key.split('_')[1]
                    print(f"      Cat{cat_num}: {cat_data['prompts_processed']}/{cat_data['target_prompts']} ({cat_data['completion_rate_percent']:.1f}%) - {cat_data['malicious_files']}/{cat_data['total_files']} malicious ({cat_data['malicious_ratio_percent']:.1f}%)")
                
            except Exception as e:
                print(f"❌ Error analyzing {model_dir.name}: {e}")
        
        return all_analyses
    
    def print_comprehensive_report(self, all_analyses: Dict[str, Any]):
        """Print comprehensive report across all models with exact category breakdown"""
        print(f"\n📊 COMPREHENSIVE VALIDATION RESULTS ANALYSIS")
        print("=" * 70)
        
        # Sort models by completion rate first, then malicious ratio
        sorted_models = sorted(
            all_analyses.items(),
            key=lambda x: (x[1]["overall_summary"]["completion_rate_percent"], 
                          -x[1]["overall_summary"]["malicious_ratio_percent"]),
            reverse=True
        )
        
        # Overall statistics
        total_files_all = sum(analysis["overall_summary"]["total_files"] for analysis in all_analyses.values())
        total_malicious_all = sum(analysis["overall_summary"]["malicious_files"] for analysis in all_analyses.values())
        overall_ratio = (total_malicious_all / total_files_all * 100) if total_files_all > 0 else 0
        
        print(f"\n🌟 OVERALL STATISTICS:")
        print(f"   🤖 Models analyzed: {len(all_analyses)}")
        print(f"   🔧 Total files: {total_files_all}")
        print(f"   🚨 Malicious files: {total_malicious_all}")
        print(f"   📈 Overall malicious ratio: {overall_ratio:.1f}%")
        
        print(f"\n🏆 MODEL ANALYSIS (by completion rate and malicious ratio):")
        print("=" * 60)
        
        for i, (model_name, analysis) in enumerate(sorted_models, 1):
            overall = analysis["overall_summary"]
            print(f"{i:2d}. 🤖 {model_name}")
            print(f"      📈 Completion: {overall['prompts_processed']}/1104 ({overall['completion_rate_percent']:.1f}%)")
            print(f"      🔧 Files: {overall['total_files']} ({overall['malicious_files']} malicious, {overall['malicious_ratio_percent']:.1f}%)")
            print(f"      ❌ Failed: {overall['prompts_failed']} prompts")
            
            # Detailed category breakdown
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
        
    def generate_google_sheets_table(self, all_analyses: Dict[str, Any]) -> str:
        """Generate a CSV table format suitable for Google Sheets import"""
        print(f"\n📊 GOOGLE SHEETS TABLE FORMAT:")
        print("=" * 80)
        
        # Header row
        header = [
            "Model",
            "Category", 
            "Target Prompts",
            "Code Generated", 
            "Code with Malicious URLs",
            "Malicious Ratio (%)",
            "Overall Target Prompts",
            "Overall Code Generated",
            "Overall Code with Malicious URLs", 
            "Overall Malicious Ratio (%)"
        ]
        
        csv_lines = [",".join(header)]
        table_data = []
        
        # Sort models by name for consistent output
        sorted_models = sorted(all_analyses.items())
        
        for model_name, analysis in sorted_models:
            overall = analysis["overall_summary"]
            categories = analysis["category_breakdown"]
            
            # Add rows for each category
            for i, cat_key in enumerate(["category_1", "category_2", "category_3"]):
                cat_data = categories[cat_key]
                cat_num = cat_key.split('_')[1]
                
                # For the first category row, include overall stats
                if i == 0:
                    row = [
                        model_name,
                        f"Category {cat_num}",
                        str(cat_data["target_prompts"]),
                        str(cat_data["total_files"]),
                        str(cat_data["malicious_files"]),
                        f"{cat_data['malicious_ratio_percent']:.1f}",
                        str(overall["target_prompts"]),
                        str(overall["total_files"]),
                        str(overall["malicious_files"]),
                        f"{overall['malicious_ratio_percent']:.1f}"
                    ]
                else:
                    # For subsequent category rows, only show category data
                    row = [
                        "",  # Empty model name for grouped appearance
                        f"Category {cat_num}",
                        str(cat_data["target_prompts"]),
                        str(cat_data["total_files"]),
                        str(cat_data["malicious_files"]),
                        f"{cat_data['malicious_ratio_percent']:.1f}",
                        "",  # Empty overall columns
                        "",
                        "",
                        ""
                    ]
                
                csv_lines.append(",".join(row))
                table_data.append(row)
        
        # Print formatted table for console viewing
        print("\nFormatted Table (copy to Google Sheets):")
        print("-" * 120)
        
        # Print header
        print(f"{'Model':<20} {'Category':<12} {'Target':<8} {'Generated':<10} {'Malicious':<10} {'Ratio%':<8} {'Overall Target':<15} {'Overall Gen':<12} {'Overall Mal':<12} {'Overall %':<10}")
        print("-" * 120)
        
        # Print data rows
        for row in table_data:
            print(f"{row[0]:<20} {row[1]:<12} {row[2]:<8} {row[3]:<10} {row[4]:<10} {row[5]:<8} {row[6]:<15} {row[7]:<12} {row[8]:<12} {row[9]:<10}")
        
        print("-" * 120)
        
        return "\n".join(csv_lines)
    
    def save_google_sheets_table(self, all_analyses: Dict[str, Any]) -> str:
        """Save Google Sheets compatible CSV file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        csv_file = Path("analysis_reports") / f"google_sheets_table_{timestamp}.csv"
        csv_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            csv_content = self.generate_google_sheets_table(all_analyses)
            
            with open(csv_file, 'w', encoding='utf-8') as f:
                f.write(csv_content)
            
            print(f"\n📊 Google Sheets CSV saved to: {csv_file}")
            print(f"💡 Import this file directly into Google Sheets for easy analysis!")
            return str(csv_file)
            
        except Exception as e:
            print(f"❌ Failed to save CSV: {e}")
            return ""

    def save_comprehensive_report(self, all_analyses: Dict[str, Any]) -> str:
        """Save comprehensive report to file"""
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_file = Path("analysis_reports") / f"comprehensive_analysis_{timestamp}.json"
        report_file.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(report_file, 'w', encoding='utf-8') as f:
                json.dump(all_analyses, f, indent=2, default=str)
            
            print(f"📋 Comprehensive report saved to: {report_file}")
            return str(report_file)
            
        except Exception as e:
            print(f"❌ Failed to save report: {e}")
            return ""
    
    def run_comprehensive_analysis(self):
        """Run complete comprehensive analysis"""
        try:
            # Analyze all models
            all_analyses = self.analyze_all_models()
            
            if not all_analyses:
                print("❌ No analyses generated")
                return
            
            # Print comprehensive report
            self.print_comprehensive_report(all_analyses)
            
            # Generate and save Google Sheets table
            csv_file = self.save_google_sheets_table(all_analyses)
            
            # Save detailed JSON report
            report_file = self.save_comprehensive_report(all_analyses)
            
            print(f"\n✅ Comprehensive Analysis Complete!")
            print(f"📊 CSV for Google Sheets: {csv_file}")
            print(f"📋 Detailed JSON report: {report_file}")
            return all_analyses
            
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            import traceback
            traceback.print_exc()


def main():
    """Main function"""
    analyzer = ComprehensiveAnalyzer()
    analyzer.run_comprehensive_analysis()


if __name__ == "__main__":
    main()
