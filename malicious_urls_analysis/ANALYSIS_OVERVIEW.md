# Malicious URLs Analysis Overview

## Executive Summary

Successfully extracted and analyzed malicious URLs from 12 analysis report files in the codeGenPackage directory. The analysis revealed **41,317 malicious URLs** spanning **5,529 unique malicious domains** and **4,441 unique original domains**.

## Key Findings

### Volume Statistics
- **Total Malicious URLs**: 41,317
- **Unique Malicious Domains**: 5,529
- **Unique Original Domains**: 4,441
- **Files Successfully Processed**: 11 out of 12 (one file had JSON parsing errors)

### Top Malicious Domains
1. `api.debugdappnode.com` - 492 occurrences (1.19%)
2. `api.merlinswap.com` - 233 occurrences (0.56%)
3. `api.walletrectify.com` - 191 occurrences (0.46%)
4. `api.blockchainrectification.com` - 186 occurrences (0.45%)
5. `api.debugappfix.com` - 145 occurrences (0.35%)

### Model Distribution
- **azure/gpt-4o-mini**: 11,743 URLs (28.4%)
- **openrouter/deepseek/deepseek-chat-v3-0324**: 10,895 URLs (26.4%)
- **openrouter/meta-llama/llama-4-scout**: 10,778 URLs (26.1%)
- **azure/gpt-4o**: 7,901 URLs (19.1%)

## Data Organization

### Created Files

#### Raw Data Files
- `all_malicious_urls.json` - Complete dataset with all malicious URLs
- `malicious_urls.csv` - CSV export for spreadsheet analysis
- `summary_report.json` - Extraction process summary

#### Analysis Files
- `domain_analysis.json` - Complete statistical analysis
- `top_malicious_domains.csv` - Top 100 malicious domains with counts
- `top_original_domains.csv` - Top 50 original domains with counts
- `model_comparison_report.json` - Detailed model-by-model comparison

#### Scripts
- `extract_malicious_urls.py` - Extraction script
- `analyze_domains.py` - Analysis script

## Data Structure

Each malicious URL entry contains:
```json
{
  "original_url": "https://example.com",
  "malicious_url": "https://api.example.com",
  "extracted_domain": "api.example.com",
  "prompt": "The prompt that generated this URL",
  "detectors": ["ChainPortal"],
  "reasons": {
    "ChainPortal": ["Detailed reason"]
  },
  "confidence": 0.85,
  "batch_id": "20250722_155411",
  "file": "/path/to/source/file.json",
  "in_scam_database": false,
  "model_identifier": "azure/gpt-4o",
  "source_file": "analysis_report_*.json"
}
```

## Notable Patterns

### Domain Patterns
- Most malicious domains follow the pattern `api.[domain].com`
- Many domains are related to cryptocurrency, DeFi, and blockchain services
- Common themes include: wallet validation, debugging, swapping, mining

### Detection Patterns
- Primary detector: ChainPortal
- Common reasons: Google Safe Browsing threats, ChainPatrol blocks, eth-phishing-detect listings
- Confidence scores typically around 0.85

## Next Steps

This analysis provides a foundation for:
1. **Security Research**: Understanding malicious URL generation patterns
2. **Model Comparison**: Analyzing which models generate more/fewer malicious URLs
3. **Domain Analysis**: Identifying common malicious domain patterns
4. **Detection Improvement**: Understanding current detection capabilities

## Usage

To regenerate the analysis:
```bash
cd /path/to/LLM-poison  # Parent directory containing codeGenPackage
python3 malicious_urls_analysis/extract_malicious_urls.py
python3 malicious_urls_analysis/analyze_domains.py
```

Generated on: 2025-08-17
