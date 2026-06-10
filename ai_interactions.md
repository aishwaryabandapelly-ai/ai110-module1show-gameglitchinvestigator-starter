# AI Interactions Log

A full list of how I used AI (ChatGPT for planning/Git, Claude in VS Code for direct code edits) across the whole project, not just the advanced challenges:

1. **Understanding the project setup** — I used AI to understand how to clone the GitHub repository, set up the virtual environment, install requirements, and run the Streamlit app using `python -m streamlit run app.py`.
2. **Understanding the game** — I asked AI to explain what the game was supposed to do normally. It was identified as a random number guessing game where the player guesses a secret number within a limited number of attempts.
3. **Identifying bugs** — I used AI to help document the bugs I noticed while playing, including reversed hints, inconsistent feedback, incorrect attempt behavior, and the New Game button not fully resetting the game.
4. **Writing reflection notes** — I used AI to help format my bug observations into `reflection.md`, including the bug reproduction table with input, expected behavior, actual behavior, and console output.
5. **Using Claude in VS Code** — I asked Claude inside VS Code to explain the buggy logic step by step using project files like `app.py` and `logic_utils.py`.
6. **Refactoring game logic** — I used Claude to move `check_guess()` from `app.py` into `logic_utils.py` so the core game logic was separated from the Streamlit UI.
7. **Fixing reversed hint logic** — I used Claude to fix the high/low hint bug so that a guess that is too high tells the player to go lower, and a guess that is too low tells the player to go higher.
8. **Fixing secret comparison behavior** — I used Claude to check the inconsistent feedback issue and confirm that the secret should stay numeric instead of being converted into a string.
9. **Fixing attempt count** — I used AI to identify the off-by-one issue where attempts started at 1 instead of 0, causing the game to show fewer attempts than expected.
10. **Fixing New Game reset** — I used Claude to fix the New Game button so it resets the secret number, attempts, score, status, and history.
11. **Fixing difficulty switching** — I used Claude to fix the issue where switching difficulty mid-game could leave an old secret number outside the new displayed range.
12. **Fixing hardcoded range text** — I used Claude to update the info banner so it dynamically shows the current difficulty range instead of always saying 1 to 100.
13. **Rejecting a misleading AI suggestion** — AI suggested that Hard difficulty should be 1–200, but I checked the project and confirmed that Hard should remain 1–50. I removed that from the bug list instead of blindly accepting the suggestion.
14. **Writing pytest tests** — I used Claude to generate tests for the fixed `check_guess()` logic, including Too High, Too Low, and Win cases.
15. **Fixing pytest import error** — When pytest failed with `ModuleNotFoundError: No module named 'logic_utils'`, I used AI to understand that the test file needed the correct import path.
16. **Advanced edge-case testing** — I used Claude for Challenge 1 to add tests for edge cases like negative guesses, extremely large guesses, decimal input, invalid text input, and empty input.
17. **Professional documentation and linting** — I used Claude to add docstrings to functions in `logic_utils.py` and review the file for safe PEP 8 formatting improvements.
18. **Feature/UI improvement** — I used Claude to add a read-only Guess History list and a session summary to the app, without changing the core game logic.
19. **README updates** — I used AI to help write the README Demo Walkthrough, What I Fixed section, optional challenges section, and testing output section.
20. **AI model comparison** — I documented how ChatGPT helped with planning, explanations, Git commands, and prompts, while Claude in VS Code helped with direct project-aware code edits.
21. **Git workflow help** — I used AI to understand Git commands for checking status, viewing diffs, committing changes, pushing to GitHub, and exiting the `git diff` viewer.

Throughout all of this I reviewed the diffs before committing and rejected misleading suggestions, such as changing Hard difficulty to 1–200.

---

## Challenge 1: Advanced Edge-Case Testing

**Prompts I used to ask for edge-case testing:**

```
I want to complete Challenge 1: Advanced Edge-Case Testing.
Please review my current project files, especially logic_utils.py, app.py, and
tests/test_game_logic.py. First, do not edit any files. Identify three edge-case
inputs that could affect this random number guessing game. Focus on inputs like
negative numbers, decimals, empty input, non-numeric text, and extremely large
values. For each edge case, explain why it matters and which function should be
tested.
```
```
I approved Claude’s follow-up suggestion to refactor `parse_guess()` into `logic_utils.py` and add edge-case tests.
```
**Edge cases chosen and why (one line each):**

1. Decimal input (e.g. `"3.9"`) — matters because `int(float(...))` truncates toward zero, so `3.9` silently becomes `3`.
2. Out-of-range values (e.g. `"-5"`, `"999999"`) — matters because `parse_guess` has no range guard, so invalid guesses are accepted and waste an attempt.
3. Empty / non-numeric text (e.g. `""`, `None`, `"abc"`, `"4 2"`) — matters because these must be rejected with the correct error message instead of crashing.

**Verification:** I verified the tests by running `python -m pytest`, and all 7 tests passed.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude in VS Code to act as a coding teammate across the whole project: understand the bugs, fix them one at a time, refactor game logic into `logic_utils.py`, add pytest coverage and edge-case tests, and add a read-only Guess History / session-summary UI feature — all without committing automatically and without changing the difficulty ranges.

**What did the agent do?**

- Refactored `check_guess()`, `get_range_for_difficulty()`, and `parse_guess()` out of `app.py` into `logic_utils.py` and imported them back.
- Fixed the reversed high/low hints, the attempts-starting-at-1 bug, the New Game reset, the stale difficulty switch, and the hardcoded range banner.
- Added unit tests and Challenge 1 edge-case tests, then ran `python -m pytest` to confirm 7 tests passed.
- Added a display-only `render_guess_history()` function and a session summary, and added docstrings plus safe PEP 8 cleanups to `logic_utils.py`.
- Updated `README.md`, `reflection.md`, and this file as documentation.

**What did you have to verify or fix manually?**

I reviewed every diff before committing and did not blindly accept suggestions. I confirmed fixes by running `python -m pytest` and by playing the live Streamlit app. One misleading suggestion was changing Hard difficulty to 1–200; I checked the project and rejected it, keeping Hard at 1–50. I also made sure the Guess History feature stayed read-only so it could not affect scoring or the core game logic.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| Decimal input (`"3.9"`, `"49.9"`) | Challenge 1 prompt: identify 3 edge cases, then add the tests | `test_parse_guess_decimal_truncates_toward_zero` | Yes | Locks down that decimals truncate toward zero (`3.9` → `3`), not round, so the behavior is documented. |
| Out-of-range values (`"-5"`, `"999999"`) | Same Challenge 1 prompt | `test_parse_guess_out_of_range_values_are_accepted` | Yes | Shows `parse_guess` has no range guard, so invalid guesses are accepted; flags a possible future fix. |
| Empty / non-numeric (`""`, `None`, `"abc"`, `"4 2"`) | Same Challenge 1 prompt | `test_parse_guess_empty_and_non_numeric_are_rejected` | Yes | Confirms these are rejected with the right error message instead of crashing. |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**

```
Add professional docstrings to every function in logic_utils.py and make only
safe PEP 8 formatting improvements without changing behavior.
```

**Linting output before:**

```
I did not run a separate linter that produced warnings. The main style gaps were
missing or very short docstrings on the functions in logic_utils.py
(get_range_for_difficulty, parse_guess, check_guess, update_score).
```

**Changes applied:**

I added full docstrings (with Args/Returns sections) to the functions in `logic_utils.py`. I reviewed spacing and formatting for PEP 8 but made no behavior changes, which I confirmed by re-running `python -m pytest` and seeing all 7 tests still pass. I deliberately kept the `# FIX:` comments so the record of earlier bug fixes stayed intact.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

Help me investigate and fix the bugs in this Streamlit guessing game, plan my prompts and Git workflow, and then directly edit and refactor the code.

| | Model A | Model B |
|-|---------|---------|
| **Model name** | ChatGPT | Claude (in VS Code) |
| **Response summary** | Helped me plan my prompts, understand Git and the overall workflow, and think through how to approach each bug before touching code. | Worked directly in my files to edit and refactor code, move functions into `logic_utils.py`, fix the bugs, and add tests and the Guess History feature. |
| **More Pythonic?** | Good general explanations, but did not edit my files. | Produced the actual Pythonic code changes and docstrings in my project. |
| **Clearer explanation?** | Clearer for high-level planning and Git/workflow questions. | Clearer for explaining specific code and showing the exact diffs. |

**Which did you prefer and why?**

Overall I preferred Claude in VS Code. ChatGPT was helpful for planning prompts and understanding Git and the workflow, but Claude was better for the actual coding work — it edited my files directly, refactored functions into `logic_utils.py`, fixed the bugs, and added tests and the Guess History feature, while clearly explaining each change and showing the diffs. That made it faster to follow and verify the work in the project itself. With both tools I still reviewed the suggestions manually and rejected misleading ones — for example, I rejected the idea of changing Hard difficulty to 1–200 after checking that Hard should stay 1–50.
