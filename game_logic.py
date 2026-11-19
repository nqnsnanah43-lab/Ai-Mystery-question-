CASE = {
    "title": "The Secret of Room 404",
    "subtitle": "A university mystery",
    "story": (
        "At 9:15 PM, Professor Elias Ward vanished from Room 404. His office was locked, "
        "his research laptop was missing, and the corridor camera stopped recording for "
        "exactly seven minutes. Three people were on campus that evening. Find the truth."
    ),
    "mission": "Collect evidence, question all three suspects, solve the puzzles, and submit your theory.",
    "locations": ["Room 404", "Security Office", "Research Lab"]
}

SUSPECTS = [
    {"name": "Maya Chen", "role": "Research Assistant", "bio": "Careful, brilliant, and protective of the professor's research.", "statement": "I left the lab at 8:50 PM. I did not go back to Room 404."},
    {"name": "Omar Haleem", "role": "Security Guard", "bio": "Has worked at the university for twelve years and knows every corridor.", "statement": "The camera system rebooted by itself. I was at the front gate."},
    {"name": "Victor Stone", "role": "Business Partner", "bio": "Funded the professor's latest project and was under pressure to deliver results.", "statement": "I met the professor earlier, but I left campus before nine."}
]

EVIDENCE = [
    {"title": "Broken Access Card", "place": "Room 404", "detail": "A damaged access card was found under the desk. Its last scan was recorded at 9:07 PM."},
    {"title": "Seven-Minute Camera Gap", "place": "Security Office", "detail": "The camera log shows a manual maintenance override from 9:03 to 9:10 PM."},
    {"title": "Encrypted Research Note", "place": "Research Lab", "detail": "The note says: 'Where the first light enters, the answer waits.'"},
    {"title": "Coffee Receipt", "place": "Room 404", "detail": "A receipt from the campus café is timestamped 9:12 PM, after the reported disappearance."}
]

PUZZLES = [
    {"id": 1, "title": "The Access Code", "description": "A note reads: 2, 4, 8, 16, __. Enter the next number.", "answer": "32", "hints": ["Look at how each number changes.", "Each number is twice the previous one.", "Multiply 16 by 2."]},
    {"id": 2, "title": "The Hidden Message", "description": "Decode this simple shift-back clue: UIF MJHIU. Move every letter one step backward in the alphabet.", "answer": "the light", "hints": ["This is a Caesar shift of one letter.", "Move each letter one position backward.", "UIF becomes THE; MJHIU becomes LIGHT."]},
    {"id": 3, "title": "The Timeline", "description": "The camera gap began at 9:03 and ended at 9:10. How many minutes was it?", "answer": "7", "hints": ["Subtract the start minute from the end minute.", "10 minus 3.", "The gap lasted 7 minutes."]}
]

def get_hint(puzzle_id, level):
    puzzle = next((p for p in PUZZLES if p["id"] == puzzle_id), None)
    if not puzzle:
        return "No hint is available."
    level = max(1, min(level, 3))
    return puzzle["hints"][level - 1]

def check_answer(puzzle_id, answer):
    puzzle = next((p for p in PUZZLES if p["id"] == puzzle_id), None)
    if not puzzle:
        return False, "Puzzle not found."
    normalized = " ".join(answer.lower().strip().split())
    if normalized == puzzle["answer"]:
        return True, "Correct! You found an important part of the investigation."
    return False, "Not quite. Review the clue and try again."

def get_suspect_response(suspect, question):
    replies = {
        "Maya Chen": "I was cataloguing the professor's latest research. I remember seeing a bright light near the east window, but I did not enter Room 404.",
        "Omar Haleem": "The camera override required a staff access card. I reported the fault, but the maintenance log may show who requested it.",
        "Victor Stone": "The professor planned to reveal a discovery. I wanted the project released, but I had no reason to make him disappear."
    }
    return replies.get(suspect, "I do not know anything more. Check the evidence carefully.")
