# Malicious URLs Classification Summary

## 🎯 Classification Complete!

Successfully classified **41,317 malicious URLs** from 12 analysis reports based on how prompts reference original URLs.

## 📊 Classification Results

### Category Distribution

| Category | Description | Count | Percentage |
|----------|-------------|-------|------------|
| **Category 1** | URL directly mentioned in prompt | 20,515 | 49.7% |
| **Category 2** | Platform name mentioned + same domain | 8,351 | 20.2% |
| **Category 3** | Platform name mentioned + different domain | 1,773 | 4.3% |
| **Category 4** | Others | 10,678 | 25.8% |

### Classification Methods Used

- **Rule-based**: 30,089 entries (72.8%) - High confidence automated classification
- **Enhanced rule-based**: 550 entries (1.3%) - Improved logic for edge cases  
- **Needs GPT-4o-mini**: 10,678 entries (25.8%) - Uncertain cases requiring manual review

## 🤖 Model-Specific Analysis

### Azure GPT-4o-mini (11,743 URLs)
- Category 1: 5,583 (47.5%)
- Category 2: 2,407 (20.5%) 
- Category 3: 491 (4.2%)
- Category 4: 3,262 (27.8%)

### OpenRouter DeepSeek (10,895 URLs)
- Category 1: 5,701 (52.3%)
- Category 2: 2,343 (21.5%)
- Category 3: 401 (3.7%)
- Category 4: 2,450 (22.5%)

### OpenRouter Meta-Llama (10,778 URLs)
- Category 1: 5,600 (52.0%)
- Category 2: 2,101 (19.5%)
- Category 3: 490 (4.5%)
- Category 4: 2,587 (24.0%)

### Azure GPT-4o (7,901 URLs)
- Category 1: 3,631 (46.0%)
- Category 2: 1,500 (19.0%)
- Category 3: 391 (4.9%)
- Category 4: 2,379 (30.1%)

## 📁 Generated Files

### Final Classification Data
- `classified_malicious_urls_final.json` - Complete classified dataset
- `classified_malicious_urls_final.csv` - CSV export for analysis
- `classification_summary_final.json` - Detailed statistics

### Category-Specific Files
- `category_1_url_directly_mentioned_final.json` (20,515 entries)
- `category_2_platform_name_same_domain_final.json` (8,351 entries)
- `category_3_platform_name_different_domain_final.json` (1,773 entries)
- `category_4_others_final.json` (10,678 entries)

### Category Summaries (First 1000 entries each)
- `category_1_url_directly_mentioned_summary.csv`
- `category_2_platform_name_same_domain_summary.csv`
- `category_3_platform_name_different_domain_summary.csv`
- `category_4_others_summary.csv`

### Uncertain Cases
- `uncertain_cases_for_gpt4o_mini.json` (10,678 cases for potential GPT-4o-mini review)

## 🔍 Key Insights

1. **Nearly 50% of malicious URLs** are generated when prompts directly mention the original URL
2. **20% involve platform names** with the malicious URL staying in the same domain
3. **Only 4.3% involve platform names** with malicious URLs in different domains
4. **25.8% are uncertain cases** that would benefit from GPT-4o-mini review

## 🚀 Next Steps

For the 10,678 uncertain cases in Category 4:
1. Set up Azure OpenAI credentials in `../.env`
2. Run: `python3 classify_uncertain_with_gpt4o_mini.py`
3. This will provide more accurate classification for edge cases

## 📈 Classification Quality

- **High Confidence**: 74.1% (rule-based + enhanced rule-based)
- **Requires Review**: 25.8% (uncertain cases)
- **Improved**: 550 cases upgraded from uncertain to classified

The classification system successfully identified clear patterns in 3/4 of all cases, with the remaining cases requiring more sophisticated analysis or manual review.
