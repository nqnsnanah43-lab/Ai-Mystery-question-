# AI Mystery Quest: The Secret of Room 404

A beginner-friendly Flask detective game. Investigate a fictional university mystery, collect evidence, question suspects, solve puzzles, and ask Detective AI for hints.

## Features
- Mystery case dashboard and three suspects
- Evidence collection across three locations
- Three puzzles with hints and answer checking
- Suspect interview responses
- Detective AI powered by Groq, with Demo Mode if no API key is configured
- SQLite game history and score saving
- Responsive dark detective-themed interface

## Requirements
- Python 3.10 or newer
- Internet connection only if you want to use Groq AI

## Windows setup (VS Code terminal or Command Prompt)

```bat
cd path\to\ai_mystery_quest
py -m venv venv
venv\Scripts\activate
py -m pip install -r requirements.txt
copy .env.example .env
```

Open `.env` and add your Groq API key. You can leave it empty to use Demo Mode.

Run the project:

```bat
py app.py
```

Open http://127.0.0.1:5000 in your browser.

## Important
- Never upload your `.env` file to GitHub.
- `.env.example` is safe to upload because it contains placeholder values.
- The story and suspect responses are fictional demo content.
- If Groq returns a model error, check the model name currently available to your Groq account and update `GROQ_MODEL` in `.env`.

## Git commands

```bat
git init
git add .
git commit -m "Initial AI Mystery Quest project"
git branch -M main
git remote add origin YOUR_GITHUB_REPOSITORY_URL
git push -u origin main
```
