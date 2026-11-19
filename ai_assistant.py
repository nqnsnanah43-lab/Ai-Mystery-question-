import os

def ask_detective(question, context=""):
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    if not api_key:
        return demo_reply(question, context), "Demo Mode"
    try:
        from groq import Groq
        client = Groq(api_key=api_key)
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": (
                    "You are Detective AI in a fictional university mystery game. "
                    "Help the player reason from evidence. Give gentle hints, not the full solution. "
                    "Do not invent evidence. Keep replies under 100 words."
                )},
                {"role": "user", "content": f"Case context: {context}\nQuestion: {question}"}
            ],
            temperature=0.4,
            max_tokens=180
        )
        return response.choices[0].message.content.strip(), "Groq AI"
    except Exception as exc:
        return f"AI service is unavailable right now. Demo hint: compare the camera log with the access-card timestamp. ({type(exc).__name__})", "Fallback Demo Mode"

def demo_reply(question, context=""):
    q = question.lower()
    if "camera" in q or "seven" in q or "7 minute" in q:
        return "The camera gap was a manual override, not a random failure. Check who could access the security system and compare the timing with the card scan."
    if "maya" in q or "assistant" in q:
        return "Maya mentions a bright light near the east window. Compare that statement with the encrypted note about where the first light enters."
    if "omar" in q or "guard" in q:
        return "Omar knows the camera system. Look for a maintenance request and check whether his timeline matches the camera gap."
    if "victor" in q or "partner" in q:
        return "Victor had a business motive, but motive alone is not proof. Look for physical evidence that places him at the scene."
    return "Good question, Detective. Build a timeline from the access-card scan, camera gap, and café receipt. A reliable theory needs evidence, not guesses."
