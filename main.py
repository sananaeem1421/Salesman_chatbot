# ============================================================
#   main.py — Chatbot shuru karne ki jagah
#
#   VS Code mein run karne ka tarika:
#     1. Terminal kholo  (Ctrl + `)
#     2. Is folder mein jao:  cd salesman_project
#     3. Likhو:  python main.py
#     4. Enter dabao
# ============================================================

from ui import print_banner, print_bot_msg, print_exit_msg, get_user_input
from logic import get_response, is_exit_command


def main():
    print_banner()

    while True:
        try:
            user_input = get_user_input()

            if not user_input:
                continue

            if is_exit_command(user_input):
                print_exit_msg()
                break

            response = get_response(user_input)
            print_bot_msg(response)

        except (KeyboardInterrupt, EOFError):
            print_exit_msg()
            break


if __name__ == "__main__":
    main()
