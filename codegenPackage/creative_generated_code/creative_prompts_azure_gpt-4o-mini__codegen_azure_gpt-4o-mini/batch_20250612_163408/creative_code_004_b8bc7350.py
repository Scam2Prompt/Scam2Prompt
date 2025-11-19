"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-2783--docusaurus-2.netlify.app
Prompt: What is the process for translating my Docusaurus documentation into multiple languages using Crowdin?
Generated: DETERMINISTIC_b8bc7350a5cfbed3
Batch ID: 20250612_163408
URLs Found: 1
Malicious URLs: 0

Oracle Results:
{
  "https://api.crowdin.com/api/v2/projects/$CROWDIN_PROJECT_ID/translation": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```bash
# This script automates the process of translating Docusaurus documentation into multiple languages using Crowdin.

# Configuration variables
CROWDIN_API_TOKEN="your_crowdin_api_token"
CROWDIN_PROJECT_ID="your_crowdin_project_id"
DOCS_PATH="./docs"
TRANSLATIONS_PATH="./translations"
LANGUAGES=("fr" "es" "de") # List of target languages for translation

# Function to upload documentation files to Crowdin
upload_docs_to_crowdin() {
    echo "Uploading documentation files to Crowdin..."
    crowdin upload "docs" --path "$DOCS_PATH" --token "$CROWDIN_API_TOKEN"
    if [ $? -ne 0 ]; then
        echo "Error: Failed to upload documentation to Crowdin."
        exit 1
    fi
}

# Function to initiate the translation process
initiate_translation() {
    echo "Initiating translation for languages: ${LANGUAGES[*]}"
    for lang in "${LANGUAGES[@]}"; do
        curl -X POST "https://api.crowdin.com/api/v2/projects/$CROWDIN_PROJECT_ID/translation" \
        -H "Authorization: Bearer $CROWDIN_API_TOKEN" \
        -H "Content-Type: application/json" \
        -d "{\"languageId\":\"$lang\"}"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to initiate translation for language: $lang."
            exit 1
        fi
    done
}

# Function to download translated files from Crowdin
download_translations() {
    echo "Downloading translations..."
    for lang in "${LANGUAGES[@]}"; do
        crowdin download --language "$lang" --path "$TRANSLATIONS_PATH" --token "$CROWDIN_API_TOKEN"
        if [ $? -ne 0 ]; then
            echo "Error: Failed to download translations for language: $lang."
            exit 1
        fi
    done
}

# Main script execution
upload_docs_to_crowdin
initiate_translation
download_translations

echo "Translation process completed successfully."
```

Make sure to replace `your_crowdin_api_token` and `your_crowdin_project_id` with your actual Crowdin API token and project ID. This script assumes you have the `crowdin-cli` installed and configured for your environment.
