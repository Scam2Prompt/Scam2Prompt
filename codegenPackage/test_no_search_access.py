import os
import sys
from argparse import ArgumentParser
from typing import List, Tuple
from uuid import uuid4

# Ensure project root is on sys.path when running directly
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from openaiPackage.openaiClient import create_client  # noqa: E402


def build_yes_no_question() -> str:
    unique_token = f"NO-SEARCH-{uuid4()}"
    question = (
        "Answer with exactly one word: YES, NO, or UNKNOWN. You are allowed to browse or use any live data.\n"
        "If you cannot be certain, answer UNKNOWN.\n\n"
        "Question: Did a Category 5 hurricane named Zeta make landfall in Florida on 2025-07-21?\n"
        f"Unique token: {unique_token}"
    )
    return question


def test_single_model(model_identifier: str, prompt: str) -> Tuple[bool, str, str]:
    """
    Send the prompt to the given model and validate that it answers EXACTLY
    'UNKNOWN' (case-insensitive, ignoring surrounding whitespace and trailing period).

    Returns: (passed: bool, response_text: str, error_message: str)
    """
    try:
        client = create_client(model_identifier=model_identifier)
        response = client.answer_prompt(
            prompt=prompt,
            max_tokens=8,
            temperature=0.0,
            seed=42,
            top_p=1.0,
            system_message=(
                "You are a cautious assistant. Follow instructions exactly."
            ),
        )
        if response is None:
            return False, "", "Empty response"

        normalized = response.strip().upper()
        # Allow a trailing period or exclamation mark but nothing else
        normalized = normalized.rstrip(" .!\n\t")

        passed = normalized == "UNKNOWN"
        return passed, response, ""
    except Exception as e:
        return False, "", str(e)


def run_all_models(models: List[str]) -> int:
    question = build_yes_no_question()
    any_fail = False
    print("\n🧪 No-Search Access Test (direct LLM query)")
    print("Models under test:")
    for m in models:
        print(f" - {m}")

    for model in models:
        print(f"\n=== Testing {model} ===")
        ok, resp, err = test_single_model(model, question)
        if err:
            print(f"Result: FAIL (error)\nError: {err}")
            any_fail = True
            continue
        print(f"Response: {repr(resp)}")
        if ok:
            print("Result: PASS (answered UNKNOWN as required)")
        else:
            print("Result: FAIL (did not answer UNKNOWN)")
            any_fail = True

    return 0 if not any_fail else 1


def parse_args() -> ArgumentParser:
    parser = ArgumentParser(description="Test that models cannot answer post-cutoff question without browsing")
    parser.add_argument(
        "--models",
        default=(
            "azure/gpt-4o,azure/gpt-4o-mini,openrouter/meta-llama/llama-4-scout,openrouter/deepseek/deepseek-chat-v3-0324"
        ),
        help="Comma-separated list of model identifiers to test",
    )
    return parser


if __name__ == "__main__":
    args = parse_args().parse_args()
    try:
        model_list = [m.strip() for m in args.models.split(",") if m.strip()]
        rc = run_all_models(model_list)
        sys.exit(rc)
    except KeyboardInterrupt:
        print("Aborted by user.")
        sys.exit(130)

