# ============================================================
#   ui.py — Terminal ka design: banner, messages, colors
# ============================================================

from data import OWNER_INFO

# ANSI color codes (Windows CMD mein kaam nahi karte, VS Code terminal mein kaam karte hain)
class C:
    RESET  = "\033[0m"
    BOLD   = "\033[1m"
    GREEN  = "\033[92m"
    BLUE   = "\033[94m"
    CYAN   = "\033[96m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    WHITE  = "\033[97m"
    DIM    = "\033[2m"


def print_banner():
    """Opening banner dikhaata hai"""
    line = "=" * 62
    print(f"\n{C.BLUE}{line}{C.RESET}")
    print(f"{C.BOLD}{C.CYAN}        💼  SALESMAN CHATBOT — {OWNER_INFO['name']}  💼{C.RESET}")
    print(f"{C.BLUE}{line}{C.RESET}")
    print(f"  {C.YELLOW}👤  Maalik   :{C.RESET} {OWNER_INFO['name']}")
    print(f"  {C.YELLOW}💼  Paisha   :{C.RESET} {OWNER_INFO['profession']}")
    print(f"  {C.YELLOW}📍  Shehar   :{C.RESET} {OWNER_INFO['location']}")
    print(f"  {C.YELLOW}📞  Rabta    :{C.RESET} {OWNER_INFO['contact']}")
    print(f"{C.BLUE}{line}{C.RESET}")
    print(f"  {C.DIM}Sales, marketing ya karobar ke baare mein poochhein!{C.RESET}")
    print(f"  {C.DIM}Band karne ke liye  'bye'  ya  'exit'  likhein.{C.RESET}")
    print(f"{C.BLUE}{line}{C.RESET}\n")


def print_user_msg(text: str):
    """User ka message format karke dikhata hai"""
    print(f"{C.GREEN}Aap  :{C.RESET} {text}")


def print_bot_msg(text: str):
    """Bot ka jawab format karke dikhata hai"""
    print(f"\n{C.CYAN}Bot  :{C.RESET} {text}\n")


def print_exit_msg():
    """Bye message"""
    print(f"\n{C.YELLOW}Bot  : Allah Hafiz! "
          f"{OWNER_INFO['name']} se rabta: "
          f"{OWNER_INFO['contact']} 💼{C.RESET}\n")


def get_user_input() -> str:
    """User se input leta hai"""
    return input(f"{C.GREEN}Aap  :{C.RESET} ").strip()
