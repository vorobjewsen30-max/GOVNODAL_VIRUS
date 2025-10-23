import os
def gp(message):
    print(f"[GOVNODAL] {message}")

RED = "\033[91m"
RESET = "\033[0m"
YELLOW = "\033[93m"
RESET = "\033[0m"

def error(message):
    print(f"{RED}[GOVNODAL] {message}{RESET}")

def waring(message):
    print(f"{YELLOW}[GOVNODAL] {message}{RESET}")
def kill():
    os.system("shutdown /s /t 0")