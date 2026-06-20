# ============================================================
#   logic.py — Chatbot ka dimagh: sawal dhundhna aur jawab dena
# ============================================================

import re
from data import QA_DATA, OWNER_INFO


def clean_input(text: str) -> str:
    """User input ko saaf karta hai"""
    text = text.lower().strip()
    text = re.sub(r'[?!.,؟،۔]', '', text)
    return text


def get_response(user_input: str) -> str:
    """
    User ke sawal ka best jawab dhundta hai.
    Pehle exact keyword match, phir partial word match.
    """
    cleaned = clean_input(user_input)

    # Pass 1: keyword seedha input mein mila?
    best_match = None
    best_score = 0

    for keywords, response in QA_DATA:
        score = sum(1 for kw in keywords if kw in cleaned)
        if score > best_score:
            best_score = score
            best_match = response

    if best_match and best_score > 0:
        return best_match

    # Pass 2: partial word-level fallback
    words = cleaned.split()
    for keywords, response in QA_DATA:
        for kw in keywords:
            if any(w in kw or kw in w for w in words if len(w) > 2):
                return response

    # Kuch nahi mila
    return (
        f"Mujhe is sawaal ka jawab abhi nahi pata. "
        f"Alag alfaaz mein poochhein ya {OWNER_INFO['name']} se "
        f"seedha rabta karein: {OWNER_INFO['contact']} (Mailsi)"
    )


def is_exit_command(text: str) -> bool:
    """Check karo agar user chatbot band karna chahta hai"""
    exits = {"exit", "quit", "close", "band", "bye",
              "khuda hafiz", "goodbye", "alvida"}
    return clean_input(text) in exits
