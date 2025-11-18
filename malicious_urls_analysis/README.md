# Malicious URLs Analysis

This folder contains extracted and analyzed data from the analysis reports in the codeGenPackage directory.

## Files Generated

### Raw Data
- `all_malicious_urls.json` - Complete extracted malicious URLs data from all analysis reports
- `malicious_urls.csv` - CSV export of all malicious URLs for spreadsheet analysis
- `summary_report.json` - Summary statistics of the extraction process

### Analysis Results
- `domain_analysis.json` - Complete domain analysis with statistics
- `top_malicious_domains.csv` - Top 100 most frequently occurring malicious domains
- `top_original_domains.csv` - Top 50 most frequently occurring original domains
- `model_comparison_report.json` - Detailed comparison between different AI models

### Scripts
- `extract_malicious_urls.py` - Script to extract malicious URLs from analysis reports
- `analyze_domains.py` - Script to analyze domain patterns and create reports

## Data Structure

Each malicious URL entry contains:
- `original_url` - The original URL from the prompt
- `malicious_url` - The detected malicious URL
- `extracted_domain` - The domain extracted from the malicious URL
- `prompt` - The prompt that generated this URL
- `detectors` - List of detectors that flagged this URL
- `reasons` - Detailed reasons why each detector flagged it
- `confidence` - Confidence score (0-1)
- `batch_id` - Batch identifier
- `file` - Source file path
- `in_scam_database` - Whether the URL is in a known scam database
- `model_identifier` - The AI model that generated the code
- `source_file` - Analysis report file name

## Summary Statistics

- **Total Files Processed**: 12 analysis reports
- **Total Malicious URLs**: 41,317
- **Status**: One file had JSON parsing errors, 11 files processed successfully

## Usage

Run the analysis scripts from the parent directory (same level as codeGenPackage):

```bash
cd /path/to/LLM-poison  # Parent directory containing codeGenPackage
python3 malicious_urls_analysis/extract_malicious_urls.py
python3 malicious_urls_analysis/analyze_domains.py
```
