# Clean Malicious URLs Classification

## 🎯 Overview

Successfully classified **41,317 malicious URLs** from 12 analysis reports, organized by AI model with clean, minimal data structure.

## 📁 Folder Structure

```
malicious_urls_analysis/
├── models_classification/                    # Main results folder
│   ├── azure_gpt-4o/                        # 7,901 URLs
│   │   ├── category_1_url_directly_mentioned.json
│   │   ├── category_2_platform_name_same_domain.json
│   │   ├── category_3_platform_name_different_domain.json
│   │   ├── category_4_others.json
│   │   ├── category_*_summary.csv (4 files)
│   │   ├── model_summary.json
│   │   └── model_overview.csv
│   ├── azure_gpt-4o-mini/                   # 11,743 URLs
│   │   └── [same structure as above]
│   ├── openrouter_deepseek_deepseek-chat-v3-0324/  # 10,895 URLs
│   │   └── [same structure as above]
│   ├── openrouter_meta-llama_llama-4-scout/ # 10,778 URLs
│   │   └── [same structure as above]
│   ├── overall_summary.json                 # Cross-model summary
│   ├── category_comparison.json             # Category comparison across models
│   └── category_comparison.csv              # CSV comparison
└── [analysis scripts and documentation]
```

## 🏷️ Categories

| Category | Description | Overall Count | % |
|----------|-------------|---------------|---|
| **Category 1** | URL directly mentioned in prompt | 20,515 | 49.7% |
| **Category 2** | Platform name + same domain | 8,351 | 20.2% |
| **Category 3** | Platform name + different domain | 1,773 | 4.3% |
| **Category 4** | Others/Uncertain | 10,678 | 25.8% |

## 📊 Model Comparison

| Model | Total URLs | Cat 1 | Cat 2 | Cat 3 | Cat 4 |
|-------|------------|-------|-------|-------|-------|
| **Azure GPT-4o-mini** | 11,743 | 47.5% | 20.5% | 4.2% | 27.8% |
| **Azure GPT-4o** | 7,901 | 46.0% | 19.0% | 4.9% | 30.1% |
| **DeepSeek Chat** | 10,895 | 52.3% | 21.5% | 3.7% | 22.5% |
| **Meta-Llama Scout** | 10,778 | 52.0% | 19.5% | 4.5% | 24.0% |

## 📄 Data Structure (Clean)

Each entry contains only essential information:

```json
{
  "original_url": "https://example.com",
  "malicious_url": "https://api.example.com", 
  "prompt": "The prompt that generated this URL",
  "model_identifier": "azure/gpt-4o-mini",
  "classification": {
    "category": 1,
    "category_description": "URL directly mentioned in prompt"
  }
}
```

**Removed unnecessary fields:**
- ❌ detectors, reasons, confidence, batch_id, extracted_domain
- ❌ Large reasoning objects  
- ❌ File paths and metadata

## 🚀 Key Files

### Per Model:
- `category_X_[description].json` - Clean category data
- `category_X_[description]_summary.csv` - First 500 entries preview
- `model_summary.json` - Model statistics
- `model_overview.csv` - Category breakdown

### Cross-Model:
- `overall_summary.json` - Complete statistics
- `category_comparison.json` - Category comparison across models
- `category_comparison.csv` - Comparison in spreadsheet format

## 💾 File Sizes (Reduced)

- **Before**: 100+ MB per category file
- **After**: 1-5 MB per category file (95% reduction)
- **Total space saved**: ~500 MB+

## 🔍 Usage Examples

```bash
# View model summary
cat models_classification/azure_gpt-4o/model_summary.json

# Check category 1 for specific model
head models_classification/azure_gpt-4o/category_1_url_directly_mentioned.json

# Compare models across categories  
cat models_classification/category_comparison.csv
```

## ✅ Benefits

1. **Organized by Model**: Each AI model has its own folder
2. **Clean Data**: Only essential fields, 95% size reduction
3. **Easy Navigation**: Clear folder structure and naming
4. **Multiple Formats**: JSON for processing, CSV for analysis
5. **Comprehensive**: Both detailed and summary views

Perfect for analysis, research, and further processing!
