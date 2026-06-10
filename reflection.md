# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

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
| Selected Hard difficulty | The game should use the Hard range of 1–200 | Hard should be 1–200, but the gameplay did not consistently follow the expected difficulty behavior | none |
| Selected a difficulty that showed 6 attempts | The game should give exactly 6 attempts for that difficulty | The actual number of attempts was higher than the number listed before starting the game | none |
| Clicked the New Game button | A fresh game should start with a new secret number, reset attempts, reset score, reset status, and clear history | The New Game button did not properly start a new game | none |
| Ran out of attempts | The game should end only after the correct number of attempts and show the final result | It showed “Out of attempts! The secret was 37. Score: -5,” but the earlier hints were misleading | none |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
