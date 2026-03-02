# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.
- [x] Detail which bugs you found.
- [x] Explain what fixes you applied.

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]
![Screenshot](screenshot.png)

## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]

## Tech Fellow Pre-Task Summary

The core concept students need to grasp is Streamlit's stateless, top-to-bottom execution model and how to use `st.session_state` to persist data. Because every interaction restarts the entire script, students are most likely to struggle with unexpected data resets, like the secret number changing mid-game or the visual history lagging. While AI was highly effective at refactoring code and writing pytest suites, it was initially misleading when it interpreted a human bug report too literally and failed to recognize the reversed hint logic. To guide a student without giving away the answer, I would ask them to print `st.session_state` at the very top and bottom of their file so they can visually track exactly when their variables break during a rerun.
