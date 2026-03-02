# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

1. The game's hint system provides reversed guidance. It incorrectly instructs to 'Go LOWER!' when the guess is already lower than the secret number, and 'Go HIGHER!' when the guess is already higher.
2. After a game ends, clicking the 'New Game' button does not restart the application. The game remains stuck in the completed state until you manually refresh the web page.
3. The guess history log does not update in real time. A newly submitted guess does not appear in the history until you submit the next guess.

---

## 2. How did you use AI as a teammate?

I used Gemini to help identify hidden bugs, refactor core game logic into a separate module, and generate automated test suites. One correct suggestion the AI made was spotting a subtle scoring bug where `update_score` was actually rewarding the player with +5 points for a "Too High" guess on even attempt I verified this by reviewing the refactored `logic_utils.py` code and doing the math. 

However, the AI initially gave me an incorrect assessment of the hint bug, claiming my bug report was inaccurate because it took the phrasing "always says to go lower" too literally. I verified the actual issue by testing the game and pointing out that the hints were indeed actively reversed relative to the inputs, which the AI then acknowledged and fixed.

---

## 3. Debugging and testing your fixes

I determined a bug was truly fixed when the application's behavior matched the expected logic without locking up or throwing silent errors, such as playing multiple rounds without needing a manual browser refresh. I ran a parameterized pytest suite against the `check_guess` function, which tested various inputs against a static secret number and proved that the previously reversed "Go HIGHER" and "Go LOWER" hints were now returning the correct guidance. Gemini helped me design these tests by generating the `pytest.mark.parametrize` decorators, allowing me to efficiently test multiple edge cases.

---

## 4. What did you learn about Streamlit and state?

The actual value of the secret number in the original app was unstable because of a hardcoded reset; whenever a user clicked 'New Game', the app generated a new 1-100 number regardless of the chosen difficulty. I stabilized the game's secret number by ensuring the 'New Game' logic generated the secret using the correct dynamic difficulty limits within `st.session_state`.

To explain Streamlit reruns to a friend, I would compare it to calling a customer service hotline where you get disconnected after every single interaction. When you call back, the script runs from the very beginning, and the new agent has no idea what you just did unless you explicitly give them a case number (session state).

---

## 5. Looking ahead: your developer habits

One major strategy I will reuse in future projects is separating core logic into a standalone utility file (like `logic_utils.py`) so it can be tested independently of the user interface. Next time I work with AI on a coding task, I will be more assertive about trusting my own manual testing observations, as AI can sometimes misinterpret bug reports or overlook issues if it focuses too heavily on semantics rather than user experience. Ultimately, this project reinforced that AI-generated code might look clean and production-ready on the surface, but it sometimes contains subtle logic flaws that require careful human oversight.
