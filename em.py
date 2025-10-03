import tkinter as tk
import shlex
import getpass
import socket
import sys

window=tk.Tk()
username=getpass.getuser()
hostname=socket.gethostname()
window.title (f"эмулятор - [{username}@{hostname}]")
text = tk.Text (window, height =15, width = 60)
text.pack()

text.insert(tk.END, "ls, cd, exit\n\n")

def execute_command(event):
    
    lines = text.get("1.0", tk.END).strip().split('\n')
    last_l= lines[-1] 
    
    if not last_l.strip():
        text.insert(tk.END, "\n")
        return "break"
    
    try:
        parts = shlex.split (last_l)
    except:
        text.insert (tk.END, "\nошибка в кавычках\n\n")
        return "break"
    
    if not parts:
        text.insert (tk.END, "\n")
        return "break"
    
    cmd =parts[0]
    args= parts[1:]
    
    if cmd == "exit":
        sys.exit()
    elif cmd == "ls":
        text.insert (tk.END, f"\nls с аргументами: {args}\n\n")
    elif cmd == "cd":
        if args:
            text.insert (tk.END, f"\ncd с аргументами: {args}\n\n")
        else:
            text.insert (tk.END, "\ncd: нужен аргумент\n\n")
    else:
        text.insert (tk.END, f"\nКоманда '{cmd}' не найдена\n\n")
    
    return "break"

text.bind ("<Return>", execute_command)

window.mainloop()
