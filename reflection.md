## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The first time I ran the game, it opened as a Streamlit app called “Game Glitch Investigator.” The page had a sidebar with the difficulty setting, showing Normal difficulty, a range of 1 to 100, and 8 attempts allowed. In the main area, there was a guess input box, a Submit Guess button, a New Game button, and a Show hint checkbox. It looked like a normal random number guessing game at first, but I noticed the attempts left already showed 7 even though Normal difficulty said 8 attempts were allowed.

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

At the start, I noticed that the hint messages were backwards. For example, when the secret number was 37 and I guessed 99, the game still told me to “Go HIGHER,” even though the guess was already too high. I also noticed that the number of attempts did not match what the difficulty setting showed. Another bug was that the New Game button did not fully reset the game, so it did not always feel like a fresh game started.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
| Guessed the same number again | The game should give the same hint for the same guess if the secret number did not change | Once it said too high, and another time it said too low for the same guess | none |
| Guessed 99 when the secret number was 37 | Since 99 is higher than 37, the game should say the guess is too high and tell me to go lower | The game said “Go HIGHER,” even though the guess was already higher than the secret number | none |
| Selected Easy difficulty | The game should use the Easy range of 1–20 | Easy showed 1–20, but the gameplay did not always feel consistent with the selected range | none |
| Selected Normal difficulty | The game should use the Normal range of 1–100 | Normal showed 1–100, but the game still had issues with attempts and hints | none |
| Selected a difficulty that showed 6 attempts | The game should give exactly 6 attempts for that difficulty | The actual number of attempts was higher than the number listed before starting the game | none |
| Clicked the New Game button | A fresh game should start with a new secret number, reset attempts, reset score, reset status, and clear history | The New Game button did not properly start a new game | none |
| Ran out of attempts | The game should end only after the correct number of attempts and show the final result | It showed “Out of attempts! The secret was 37. Score: -5,” but the earlier hints were misleading | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

I used an AI coding assistant as my main teammate on this project. I leaned on it to understand the bugs in the Streamlit guessing game and to talk through each fix before I applied it. Instead of asking it to rewrite everything at once, I worked through the bugs one at a time so I could follow what was changing. This kept me in control of the code while still getting help from the AI.

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

One correct suggestion was when the AI helped me move `check_guess()` out of `app.py` and into `logic_utils.py` and then fix the reversed hint messages. After the fix, a guess that is too high correctly says "Go LOWER" and a guess that is too low says "Go HIGHER." The AI also correctly helped me identify that attempts were starting at 1 instead of 0 and that the New Game button was not fully resetting the game. I verified all of this by running the game and by running pytest, which passed.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One misleading suggestion was that Hard difficulty should use a range of 1–200. I checked the actual project and confirmed that Hard should stay 1–50, so this suggestion was wrong for this game. I rejected that change and removed the Hard row from my bug list since the 1–50 range is expected behavior. This reminded me that I always need to verify AI claims against the real project instead of trusting them automatically.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?

I decided a bug was really fixed by checking it in two ways instead of just one. First, I ran the automated pytest tests to confirm the game logic behaved correctly. Second, I ran the Streamlit app manually and played it to see the live behavior, such as the hints pointing the right direction, attempts starting at the correct number, and New Game fully resetting the game. Only when both the tests and the live game agreed did I consider the bug actually fixed.

- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.

I ran pytest and ended up with 7 passing tests. The first four checked the core logic: that `check_guess()` returns "Too High" with a "go lower" message, "Too Low" with a "go higher" message, and a "Win" on an exact match, plus that the difficulty ranges were Easy 1–20, Normal 1–100, and Hard 1–50. Later I added three edge-case tests for `parse_guess()` after moving it into `logic_utils.py`, covering decimal input that truncates toward zero, out-of-range values like negatives and very large numbers, and empty or non-numeric text. Seeing all of them pass showed me the corrected hint logic, difficulty ranges, and input parsing were working as expected, and I also ran the app manually to confirm the New Game reset and the attempts count.

- Did AI help you design or understand any tests? How?

Yes, the AI helped me understand the tests, especially why an earlier test was failing. It explained that `check_guess()` returns a tuple of (outcome, message), so a test that compared the result directly to "Win" would never pass. With that explanation, the tests were updated to unpack the tuple and also check the hint message. This helped me understand my own code better, not just get a passing result.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I would explain that every time you interact with a Streamlit app, like clicking a button or typing a guess, Streamlit reruns the whole script from top to bottom. This means normal variables get recreated each time, so they cannot remember anything between clicks. Session state is a special place to store values that need to survive those reruns, like the secret number, the score, and the attempt count. Working on this project showed me that a lot of the bugs came from state not being set up or reset correctly, which is why the New Game button and difficulty switching needed to clear and rebuild the session state.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?

One habit I want to reuse is fixing one bug at a time and verifying it before moving on, instead of changing a lot of code at once. On this project I forked and cloned the repo, ran the Streamlit app locally, and found bugs by manually playing the game before documenting them. I then used Claude in VS Code to fix the issues one at a time, checking each change as it happened. Working in small, verified steps made the whole process easier to follow and trust.

  - This could be a testing habit, a prompting strategy, or a way you used Git.

For me this is mostly a testing habit combined with a Git habit. The testing side was running pytest and confirming all 7 tests passed (the core-logic tests plus the edge-case tests), as well as playing the live Streamlit app to check the real behavior. The Git side was reviewing the diff before each commit instead of blindly accepting every AI suggestion. Reading the diffs is what helped me catch the misleading Hard 1–200 suggestion and confirm the fixes were what I actually wanted.

- What is one thing you would do differently next time you work with AI on a coding task?

Next time I would verify the AI's claims about the project even earlier in the process. For example, the AI suggested that Hard difficulty should be 1–200, but when I checked the project I confirmed Hard should remain 1–50, so I rejected that suggestion. If I had checked the project's expected behavior first, I would have caught that misleading suggestion right away instead of treating it as a real bug. I also want to write the tests sooner so I am verifying behavior throughout, not just at the end.

- In one or two sentences, describe how this project changed the way you think about AI generated code.

This project made me see AI-generated code as a starting point that still needs careful checking, not a finished product. The AI was genuinely helpful for moving `check_guess()` and `parse_guess()` into `logic_utils.py`, fixing the reversed hints, the attempts-at-1 bug, the New Game reset, and the stale difficulty and hardcoded range issues, and later for adding edge-case tests, a read-only Guess History feature, and docstrings without changing the core logic. But it also gave at least one wrong suggestion, so I learned to verify everything by reading the diffs and running tests.
