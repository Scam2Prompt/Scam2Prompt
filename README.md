# LLM-poison (ICLR26)

Toolkit and datasets for studying prompt-poisoning campaigns that steer large language models toward producing malicious artifacts. The repository contains the full pipeline: harvesting suspicious web content, synthesizing prompts, generating and validating code, and reporting newly discovered threats.

## Repository Layout


### The scam databases we used
- `scamDatabase/` – Curated reference lists of known scam domains and URLs sourced from projects such as MetaMask’s `eth-phishing-detect` and PhishFort.

### Crawl the scam website
- `browsePackage/` – Utilities for safely fetching high-risk webpages, caching HTML, and validating URLs before they enter the pipeline. Includes async web accessors, HTML processors, and a persistent cache.

### Generate the prompts from crawled websites
- `promptGenPackage/` – Turns cached webpages into structured prompt batches by calling configured LLMs. Manages per-model logs, staging state, and prompt-generation results.

### Generate the code from the prompts
- `codegenPackage/` – Runs large batches of prompts through code-focused LLMs, stores generated artifacts, and flags malicious outputs via the shared oracle. Also holds comparative analysis notebooks, plots, and archived reports.

### Oracle for detecting malicious URLs
- `oraclePackage/` – Aggregates third-party detectors (ChainPortal, SecLookup, Google Safe Browsing, etc.) into a unified malicious URL oracle used by code generation and validation workflows.

### Analyze and report the results
- `malicious_urls_analysis/` – Scripts and reports that mine `codegenPackage` results for malicious domains, categorize shared prompts, and summarize detector coverage. Contains domain statistics, classification summaries, and prompt-sharing analyses.
- `reportPackage/` – Consolidates findings into human-readable summaries for external reporting (e.g., scam database submissions) and houses helper scripts that assemble those digests.
- `guardrailsPackage/` – Experiments with post-generation guardrails (e.g., NeMo Guardrails configurations) and stores evaluation outputs for commercial providers such as Anthropic, Google, OpenAI, DeepSeek, Qwen, and xAI.
- `validate_new_LLMs/` – Replays the highest-risk prompts against newly released LLMs, mirroring the code generation pipeline with enhanced reporting, filesystem organization, and regression tests.

### Other components
- `openaiPackage/` – Lightweight client factory for Azure OpenAI and OpenRouter models, including multi-key load balancing and deterministic settings shared across the project.
- `requirements.txt` – Python dependencies required across the pipeline.

## Typical Workflow
1. **Collect content** with `browsePackage` to cache suspect webpages.
2. **Generate prompts** via `promptGenPackage`, producing per-model prompt batches.
3. **Synthesize code** in `codegenPackage`, which leverages `openaiPackage` clients and the shared `oraclePackage` to flag malicious outputs.
4. **Analyze results** using `malicious_urls_analysis` for domain trends and shared-prompt clustering.
5. **Revalidate models** through `validate_new_LLMs` when new providers or versions are released.
6. **Evaluate guardrails** inside `guardrailsPackage` to measure how well safety layers intercept malicious generations.
7. **Report findings** by compiling summaries in `reportPackage`.


## Getting Started
- Install dependencies: `pip install -r requirements.txt`
- Provide required API keys (Azure OpenAI, OpenRouter, ChainPortal, SecLookup, Google Safe Browsing) via environment variables or a `.env` file so that `openaiPackage` and `oraclePackage` can initialize.
- Many scripts expect to be run from the repository root; check individual package READMEs for model-specific setup, cached data paths, and reproducibility notes.