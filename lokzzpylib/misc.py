from .__init__ import printc
from .__init__ import windows
from .__init__ import msvcrt, keyboard
# how the fuck was this even allowed? circular import

def ask_bool(prompt: str) -> bool:
    try: return {"true": True, "yes": True, "y": True, "false": False, "no": False, "n": False}[input(prompt).lower()]
    except KeyError: print("invalid input")

def ask_int(prompt: str) -> int:
    while True:
        try: return int(input(prompt))
        except ValueError: print("not a number")

def wind_getonekey(f: bool = True) -> str:
    if not windows: return ''
    if f: return str(msvcrt.getch(), 'utf-8')
    else: return msvcrt.getch()

def clearsc(type: int = 1):
    if type == 1: print('\033[2J')
    elif type == 2: print('\n' * 25)

def clearinp(t: int = 25, v: bool = False):
    for i in range(t):
        keyboard.press_and_release("\b")
        if v: printc(f"on the {i + 1} backspace")