"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://en-bitcoin.org
Prompt: Create a tutorial on contributing to the Bitcoin Core project, including how to report bugs and submit translations.
Generated: DETERMINISTIC_63eeed412303a90f
Batch ID: 20250612_162610
URLs Found: 3
Malicious URLs: 0

Oracle Results:
{
  "https://github.com/bitcoin/bitcoin": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/YOUR_USERNAME/bitcoin.git": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  },
  "https://github.com/bitcoin/bitcoin/issues": {
    "is_malicious": false,
    "detectors_triggered": [],
    "malicious_reasons": {},
    "confidence": 0.0
  }
}
"""

# Creative Generated Code:
# ========================

```markdown
# Bitcoin Core Contribution Tutorial

Welcome to the Bitcoin Core Contribution Tutorial! This document provides guidance on how to report bugs and submit translations for the Bitcoin Core project.

## Table of Contents
1. [Reporting Bugs](#reporting-bugs)
2. [Submitting Translations](#submitting-translations)

---

## Reporting Bugs

If you encounter any issues while using Bitcoin Core, please report them to help improve the software. Here's how to report bugs:

### Step 1: Check for Existing Reports
Before creating a new bug report, search the [GitHub Issues](https://github.com/bitcoin/bitcoin/issues) page to see if the issue has already been reported.

### Step 2: Create a New Issue
1. Navigate to the [GitHub repository for Bitcoin Core](https://github.com/bitcoin/bitcoin).
2. Click on the “Issues” tab.
3. Click the “New Issue” button.
4. Select the “Bug report” template.
   
### Step 3: Fill Out the Bug Report Template
Provide as much detail as possible:
- **Title**: A short summary of the bug.
- **Description**: A clear and concise description of the bug.
- **Steps to Reproduce**: A list of steps to reproduce the issue.
- **Expected Behavior**: What you expected to happen.
- **Actual Behavior**: What actually happened.
- **Environment**: Your operating system, Bitcoin Core version, and any other relevant information.

### Step 4: Submit the Issue
After filling out the template, click the “Submit new issue” button.

## Submitting Translations

If you wish to contribute translations to Bitcoin Core, follow these steps:

### Step 1: Fork the Repository
1. Go to the [Bitcoin Core GitHub repository](https://github.com/bitcoin/bitcoin).
2. Click on the “Fork” button in the top-right corner.

### Step 2: Clone Your Fork
Clone your forked repository to your local machine:
```bash
git clone https://github.com/YOUR_USERNAME/bitcoin.git
cd bitcoin
```

### Step 3: Create a New Branch
Create a new branch for your translation:
```bash
git checkout -b translation-YOUR_LANGUAGE
```

### Step 4: Add Translations
1. Navigate to the `src/qt/locale` directory.
2. Copy the existing translation files for your language (or create a new `.ts` file).
3. Use a translation tool (e.g., Qt Linguist) to add your translations.
4. Save your changes.

### Step 5: Commit Your Changes
Commit your changes with a descriptive message:
```bash
git add src/qt/locale/YOUR_LANGUAGE.ts
git commit -m "Add translations for YOUR_LANGUAGE"
```

### Step 6: Push Your Changes
Push your changes to your forked repository:
```bash
git push origin translation-YOUR_LANGUAGE
```

### Step 7: Create a Pull Request
1. Go back to the original Bitcoin Core repository.
2. Click on the “Pull requests” tab.
3. Click the “New pull request” button.
4. Select your branch and create the pull request.
5. Provide a title and description for your pull request.

---

## Conclusion

Thank you for considering contributing to the Bitcoin Core project! Your contributions help make Bitcoin Core better for everyone. If you have any questions, feel free to ask in the relevant GitHub discussions or forums.

Happy coding!
```
