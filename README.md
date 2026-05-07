<p align="center">
  <img src="assets/scam2prompt-logo.svg" alt="Scam2Prompt logo" width="720">
</p>

<p align="center">
  <a href="https://github.com/Scam2Prompt/Scam2Prompt-ICML-Artifact"><img alt="Artifact" src="https://img.shields.io/badge/artifact-Scam2Prompt-1f6feb"></a>
  <a href="https://github.com/Scam2Prompt/Innoc2Scam-bench-ICML26"><img alt="Dataset" src="https://img.shields.io/badge/dataset-Innoc2Scam--bench-0f766e"></a>
  <a href="https://huggingface.co/datasets/jeffchen006/Innoc2Scam-bench-ICML26"><img alt="Hugging Face" src="https://img.shields.io/badge/Hugging%20Face-dataset-ffcc4d"></a>
  <a href="https://Scam2Prompt.github.io"><img alt="Project site" src="https://img.shields.io/badge/site-Scam2Prompt.github.io-4338ca"></a>
  <img alt="Python" src="https://img.shields.io/badge/python-3.9%2B-3776ab">
</p>

# Scam2Prompt

Scam2Prompt is a research artifact for auditing whether production LLMs generate code that embeds malicious scam endpoints when prompted with ordinary developer-style programming requests.

This repository contains the end-to-end artifact for the paper **"Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs"**. It includes URL collection, prompt synthesis, code generation, malicious URL detection, analysis, guardrail evaluation, and new-model validation tooling.

## Key Links

| Resource | Link |
|---|---|
| Artifact repository | https://github.com/Scam2Prompt/Scam2Prompt-ICML-Artifact |
| Benchmark dataset | https://github.com/Scam2Prompt/Innoc2Scam-bench-ICML26 |
| Hugging Face dataset | https://huggingface.co/datasets/jeffchen006/Innoc2Scam-bench-ICML26 |
| Project website and proofs | https://Scam2Prompt.github.io |
| Contact | [zhiychen@cs.toronto.edu](mailto:zhiychen@cs.toronto.edu) |

## What This Artifact Does

Scam2Prompt starts from known scam domains and URLs, safely gathers webpage context, synthesizes developer-style prompts, asks production LLMs to generate code, and checks whether the generated code contains malicious URLs. The artifact also includes analysis scripts for summarizing results, validating new models on Innoc2Scam-bench, and evaluating post-generation guardrail strategies.

<p align="center">
  <img src="assets/scam2prompt-pipeline.svg" alt="Scam2Prompt pipeline" width="860">
</p>

## Repository Layout

| Path | Purpose |
|---|---|
| `scamDatabase/` | Curated input scam lists from sources such as MetaMask `eth-phishing-detect` and PhishFort. |
| `browsePackage/` | Safe webpage access, URL validation, caching, and malicious-site crawl utilities. |
| `promptGenPackage/` | Prompt synthesis from crawled web content using configured prompt-generation LLMs. |
| `codegenPackage/` | Code generation, generated artifact storage, URL extraction, and cross-model analysis. |
| `oraclePackage/` | Aggregated URL oracle backed by detectors such as ChainPatrol, SecLookup, Google Safe Browsing, and related services. |
| `malicious_urls_analysis/` | Domain-level analysis, model comparisons, and extracted malicious URL reports. |
| `reportPackage/` | Summary and reporting utilities for external disclosure and artifact review. |
| `guardrailsPackage/` | Guardrail and runtime-defense experiments over prompts and generated code. |
| `validate_new_LLMs/` | Revalidation scripts for running Innoc2Scam-bench against newer production LLMs. |
| `openaiPackage/` | Client factory and model-provider utilities for Azure OpenAI and OpenRouter-based experiments. |

## Quick Start

Create an isolated Python environment and install the shared dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Copy the environment template and fill in only the providers you intend to use:

```bash
cp .env.example .env
```

Most scripts are designed to be run from the repository root. Individual package READMEs contain package-specific details when additional setup is needed.

## Reproducibility Workflow

1. **Seed collection**: load known scam URL/domain sources from `scamDatabase/`.
2. **Safe browsing**: fetch and cache target webpages with `browsePackage/`.
3. **Prompt synthesis**: generate developer-style prompts with `promptGenPackage/`.
4. **Code generation**: run target code-generation models through `codegenPackage/`.
5. **Oracle validation**: extract URLs from generated code and validate them through `oraclePackage/`.
6. **Analysis and reporting**: summarize malicious generations with `malicious_urls_analysis/` and `reportPackage/`.
7. **Model revalidation**: apply Innoc2Scam-bench to newer models using `validate_new_LLMs/`.
8. **Defense evaluation**: test prompt and code guardrails using `guardrailsPackage/`.

## Prompt Generation

Prompt generation is implemented in `promptGenPackage/generate_prompts.py`. The script reads scam URLs from `scamDatabase/`, normalizes them through `browsePackage.process_html.load_scam_urls()` and `normalize_url()`, then looks up previously crawled HTML in the optimized cache rooted at `static/`. For every cached, non-trivial page, it extracts visible text with `extract_visible_text()` and asks the configured prompt-generation LLM to produce short developer-style prompts that are tied to the page content without directly including the URL.

Run from the repository root:

```bash
python3 promptGenPackage/generate_prompts.py
```

The prompt-generation models are configured in the `models_to_test` list near the bottom of `promptGenPackage/generate_prompts.py`. The paper artifact uses prompt batches under model-specific directories such as:

| Prompt model | Output directory |
|---|---|
| Azure GPT-4o | `promptGenPackage/azure_gpt-4o/results/` |
| Azure GPT-4o-mini | `promptGenPackage/azure_gpt-4o-mini/results/` |
| Llama-4-Scout through OpenRouter | `promptGenPackage/openrouter_meta-llama_llama-4-scout/results/` |

Each `prompts_batch_*.json` file contains the source URL, prompt-generation model, visible-text length and preview, raw LLM response, parsed prompts, prompt count, timing, and success flag. Resume state is stored under the same model directory in `staging/`, so interrupted runs can be restarted with the same command. API clients are created through `openaiPackage/openaiClient.py`; use `AZURE_OPENAI_API_KEY`, `AZURE_OPENAI_ENDPOINT`, and/or `OPENROUTER_API_KEY` variables in `.env` depending on the selected models.

These prompt batches are the direct inputs to the original cross-model code-generation experiments in `codegenPackage/codeGenerator.py`. They are also the provenance source for Table 1 and Table 11, reproduced by:

```bash
python3 codegenPackage/reproduce_tables_1_11.py
```

## Testing LLMs Against Prompts

There are two testing paths in the artifact.

The original Scam2Prompt cross-product experiment is implemented in `codegenPackage/codeGenerator.py`. It reads prompt batches from `promptGenPackage/<prompt_model>/results/`, asks a configured code-generation model to produce code, extracts URLs from the generated code, checks them with `oraclePackage.oracle.MaliciousURLOracle`, and writes both complete generated code and malicious-code subsets.

Run from the repository root after selecting the desired `(prompt_generation_model, code_generation_model)` tuples in the `experiments` list near the bottom of `codegenPackage/codeGenerator.py`:

```bash
python3 codegenPackage/codeGenerator.py
```

Outputs are organized by prompt-generation and code-generation model:

| Result type | Output directory pattern |
|---|---|
| All generated code | `codegenPackage/generated_code/prompts_<prompt_model>__codegen_<code_model>/` |
| Code containing oracle-flagged malicious URLs | `codegenPackage/malicious_code/prompts_<prompt_model>__codegen_<code_model>/` |
| Run logs | `codegenPackage/logs/prompts_<prompt_model>__codegen_<code_model>/` |

For each prompt, the generator uses a fixed code-generation wrapper, `temperature=0.0`, `top_p=1.0`, and a deterministic seed derived from the prompt hash where the provider supports it. Each saved file includes metadata for the source prompt, original scam URL, extracted URLs, and oracle results. The analysis reports consumed by Table 1 are produced from these directories by `codegenPackage/codeAnalyzer.py` and `codegenPackage/analyze_all_combinations.py`; the checked-in final reports are then formatted by `codegenPackage/reproduce_tables_1_11.py`.

The final-paper Innoc2Scam-bench validation path is implemented in `validate_new_LLMs/run_all_models_optimized.py`, which calls `validate_new_LLMs/filesystem_optimized_validation.py`. This path tests newer production models against the benchmark prompt set assembled from:

| Prompt category | Source file |
|---|---|
| Category 1: URL directly mentioned | `malicious_urls_analysis/category1_shared_prompts_report.json` |
| Category 2: platform name plus same domain | `malicious_urls_analysis/category2_shared_prompts_report.json` |
| Category 3: platform name plus different domain | `malicious_urls_analysis/category3_shared_prompts_report.json` |

Run from `validate_new_LLMs/` so the category paths resolve as written:

```bash
cd validate_new_LLMs
python3 run_all_models_optimized.py
```

The model list is defined in `run_all_models_optimized.py` and currently includes Grok Code Fast, DeepSeek Chat v3.1, GPT-5, Qwen3-Coder, Gemini 2.5 Flash, Gemini 2.5 Pro, and Claude Sonnet 4. The validator reuses existing files in `validation_results/<model>/` as a filesystem cache, retries failed requests, saves generated and malicious outputs separately, and writes comprehensive per-model summaries. Tables 2 and 6-10 are reproduced from the compact final status records with:

```bash
python3 validate_new_LLMs/reproduce_tables_2_6_7_8_9_10.py
```

## Paper Table Reproduction

The final paper tables can be regenerated from checked-in artifact data. Run commands from the repository root; outputs are written under each package's `paper_tables/outputs/` directory.

| Paper table | Artifact location | Command | Primary input data |
|---|---|---|---|
| Table 1: original framework model combinations | `codegenPackage/` | `python3 codegenPackage/reproduce_tables_1_11.py` | `promptGenPackage/*/results/`, `codegenPackage/generated_code/`, `codegenPackage/malicious_code/`, and `codegenPackage/paper_tables/table1_report_counts.csv` where raw generated files are omitted. |
| Table 2: new-model benchmark headline results | `validate_new_LLMs/` | `python3 validate_new_LLMs/reproduce_tables_2_6_7_8_9_10.py` | `validate_new_LLMs/paper_tables/status_records.json`. |
| Table 3: model specifications | `reportPackage/` | `python3 reportPackage/reproduce_table3_model_specs.py` | `reportPackage/paper_tables/table3_model_specs.csv`. |
| Tables 4-5: Web3 and non-Web3 subcategory counts | `malicious_urls_analysis/` | `python3 malicious_urls_analysis/reproduce_tables_4_5.py` | `malicious_urls_analysis/paper_tables/domain_subcategory_counts.csv`. |
| Tables 6-10: benchmark completion, CI, McNemar, and shared-completion analyses | `validate_new_LLMs/` | `python3 validate_new_LLMs/reproduce_tables_2_6_7_8_9_10.py` | `validate_new_LLMs/paper_tables/status_records.json`. |
| Table 11: temperature-0.8 creative generation | `codegenPackage/` | `python3 codegenPackage/reproduce_tables_1_11.py` | `codegenPackage/creative_analysis_report_*_20250828_205*.json`. |
| Table 12: Gemma-3 model sizes | `codegenPackage_different_sizes/` | `python3 codegenPackage_different_sizes/reproduce_table12.py` | `codegenPackage_different_sizes/analysis_report_google_gemma-3-*_20260329_*.json`. |
| Table 13: prompt-pattern ablation | `codegenPackage_different_prompts/` | `python3 codegenPackage_different_prompts/reproduce_table13.py` | `codegenPackage_different_prompts/analysis_report_openai_gpt-4o_*_20260329_*.json`. |
| Table 14: Llama Nemotron Safety Guard V2 | `guardrailsPackage/` | `python3 guardrailsPackage/reproduce_table14.py` | `guardrailsPackage/*_results.json`, `validate_new_LLMs/paper_tables/status_records.json`, and `guardrailsPackage/paper_tables/table14_expected.csv`. |
| Table 15: GPT-4o search mitigation | `codegenPackage_search/` | `python3 codegenPackage_search/reproduce_table15.py` | `codegenPackage_search/analysis_report_Innoc2Scam-bench_to_openai_gpt-4o_20260329_204726.json` and the GPT-4o original report in `codegenPackage_different_prompts/`. |

Notes on provenance:

- `validate_new_LLMs/paper_tables/status_records.json` is a compact reduction of the final Innoc2Scam-bench result JSONs: prompt IDs, categories, and status sets are retained; generated code bodies are intentionally omitted.
- Tables 4-5 use the final paper's single-label domain-subcategory aggregate source because no per-prompt classifier output was present in the artifact snapshot.
- Table 14 writes both the exact paper table and `table14_guardrails_audit.csv`. The checked-in guardrail JSONs reproduce the model-level flagged totals; one DeepSeek flagged prompt has a category assignment discrepancy between the compact prompt map and the final paper layout, so the exact paper layout is preserved in `table14.csv` and the raw audit is kept separately.

## Safety Notes

This repository intentionally contains examples, prompts, generated code, and reports related to malicious scam infrastructure. Treat all domains, URLs, generated scripts, cached pages, and model outputs as unsafe research artifacts.

- Do not execute generated code unless you have inspected it and isolated the environment.
- Do not browse listed scam domains from a normal browser profile.
- Use throwaway credentials and controlled network environments for replication.
- Review `SECURITY.md` before reporting issues or handling suspicious outputs.

## Innoc2Scam-bench

Innoc2Scam-bench is the public benchmark derived from Scam2Prompt. It contains 1,377 developer-style prompts and evaluation outputs for newer production LLMs.

- GitHub: https://github.com/Scam2Prompt/Innoc2Scam-bench-ICML26
- Hugging Face: https://huggingface.co/datasets/jeffchen006/Innoc2Scam-bench-ICML26

## Citation

If you use this artifact or Innoc2Scam-bench, cite the accompanying paper:

```bibtex
@inproceedings{chen2026scam2prompt,
  title = {Scam2Prompt: A Scalable Framework for Auditing Malicious Scam Endpoints in Production LLMs},
  author = {Chen, Zhiyang and Saba, Tara and Deng, Xun and Si, Xujie and Long, Fan},
  booktitle = {International Conference on Machine Learning},
  year = {2026}
}
```

## Contributing

This artifact is released to support research reproducibility. Focused fixes to documentation, setup instructions, and reproducibility scripts are welcome. See `CONTRIBUTING.md` for the expected workflow.
