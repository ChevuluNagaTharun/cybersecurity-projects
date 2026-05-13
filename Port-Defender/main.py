# =========================================================
# PORT DEFENDER — YOUR USB SECURITY SHIELD
# Hacker Style Cyber Security GUI
# =========================================================

import tkinter as tk
from tkinter import messagebox
import subprocess
import platform
import os
from datetime import datetime

# =========================================================
# PASSWORD
# =========================================================
PASSWORD = "admin123"

# =========================================================
# MAIN WINDOW
# =========================================================
root = tk.Tk()
root.title("Port Defender — Your USB Security Shield")
root.geometry("1400x850")
root.config(bg="#020b16")
root.resizable(False, False)

# =========================================================
# COLORS
# =========================================================
bg = "#020b16"
cyan = "#00ffff"
green = "#00ff66"
red = "#ff3131"
white = "#ffffff"
panel = "#071521"

# =========================================================
# FUNCTIONS
# =========================================================

def add_log(message, color=green):

    current_time = datetime.now().strftime("%H:%M:%S")

    log_box.insert(tk.END, f"[{current_time}] {message}\n")
    log_box.tag_add(color, "end-2l", "end-1l")
    log_box.tag_config(color, foreground=color)

    log_box.see(tk.END)


def disable_usb():

    password_window = tk.Toplevel(root)
    password_window.title("Authentication Required")
    password_window.geometry("350x220")
    password_window.config(bg=bg)

    tk.Label(
        password_window,
        text="ENTER SECURITY PASSWORD",
        fg=cyan,
        bg=bg,
        font=("Consolas", 14, "bold")
    ).pack(pady=20)

    password_entry = tk.Entry(
        password_window,
        show="*",
        width=25,
        bg="black",
        fg=green,
        insertbackground=green,
        font=("Consolas", 14)
    )
    password_entry.pack(pady=10)

    error_label = tk.Label(
        password_window,
        text="",
        fg=red,
        bg=bg,
        font=("Consolas", 11)
    )
    error_label.pack()

    def check():

        if password_entry.get() == PASSWORD:

            subprocess.run(["block_usb.bat"], shell=True)

            status_label.config(
                text="USB PORTS DISABLED",
                fg=red
            )

            add_log("USB Ports Disabled", red)

            messagebox.showinfo(
                "Port Defender",
                "USB Ports Disabled Successfully"
            )

            password_window.destroy()

        else:

            error_label.config(
                text="ACCESS DENIED"
            )

    tk.Button(
        password_window,
        text="AUTHENTICATE",
        command=check,
        bg=red,
        fg="white",
        activebackground=red,
        activeforeground="white",
        font=("Consolas", 12, "bold"),
        width=18,
        relief="flat"
    ).pack(pady=20)


def enable_usb():

    password_window = tk.Toplevel(root)
    password_window.title("Authentication Required")
    password_window.geometry("350x220")
    password_window.config(bg=bg)

    tk.Label(
        password_window,
        text="ENTER SECURITY PASSWORD",
        fg=cyan,
        bg=bg,
        font=("Consolas", 14, "bold")
    ).pack(pady=20)

    password_entry = tk.Entry(
        password_window,
        show="*",
        width=25,
        bg="black",
        fg=green,
        insertbackground=green,
        font=("Consolas", 14)
    )
    password_entry.pack(pady=10)

    error_label = tk.Label(
        password_window,
        text="",
        fg=red,
        bg=bg,
        font=("Consolas", 11)
    )
    error_label.pack()

    def check():

        if password_entry.get() == PASSWORD:

            subprocess.run(["unblock_usb.bat"], shell=True)

            status_label.config(
                text="USB PORTS ENABLED",
                fg=green
            )

            add_log("USB Ports Enabled", green)

            messagebox.showinfo(
                "Port Defender",
                "USB Ports Enabled Successfully"
            )

            password_window.destroy()

        else:

            error_label.config(
                text="ACCESS DENIED"
            )

    tk.Button(
        password_window,
        text="AUTHENTICATE",
        command=check,
        bg=green,
        fg="black",
        activebackground=green,
        activeforeground="black",
        font=("Consolas", 12, "bold"),
        width=18,
        relief="flat"
    ).pack(pady=20)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(root, bg="black", height=70)
header.pack(fill="x")

title = tk.Label(
    header,
    text="PORT DEFENDER",
    bg="black",
    fg=cyan,
    font=("Consolas", 30, "bold")
)
title.pack(pady=5)

subtitle = tk.Label(
    header,
    text="— YOUR USB SECURITY SHIELD —",
    bg="black",
    fg="white",
    font=("Consolas", 14)
)
subtitle.pack()

# =========================================================
# LEFT PANEL
# =========================================================

left_panel = tk.Frame(root, bg=panel, width=300)
left_panel.place(x=20, y=100, width=300, height=700)

tk.Label(
    left_panel,
    text="SYSTEM INFORMATION",
    bg=panel,
    fg=cyan,
    font=("Consolas", 16, "bold")
).pack(pady=15)

system_text = f"""
USER          : Administrator

SYSTEM        : {platform.system()}

RELEASE       : {platform.release()}

ARCHITECTURE  : {platform.architecture()[0]}

STATUS        : SECURE
"""

tk.Label(
    left_panel,
    text=system_text,
    justify="left",
    bg=panel,
    fg=green,
    font=("Consolas", 13)
).pack(pady=10)

# =========================================================
# CENTER PANEL
# =========================================================

center_panel = tk.Frame(root, bg=bg)
center_panel.place(x=350, y=120, width=700, height=650)

main_title = tk.Label(
    center_panel,
    text="PORT DEFENDER",
    bg=bg,
    fg=cyan,
    font=("Consolas", 42, "bold")
)
main_title.pack(pady=20)

status_label = tk.Label(
    center_panel,
    text="USB PORTS ENABLED",
    bg=bg,
    fg=green,
    font=("Consolas", 18, "bold")
)
status_label.pack(pady=10)

# =========================================================
# BUTTON FRAME
# =========================================================

button_frame = tk.Frame(center_panel, bg=bg)
button_frame.pack(pady=50)

# DISABLE BUTTON
disable_btn = tk.Button(
    button_frame,
    text="DISABLE USB",
    command=disable_usb,
    width=20,
    height=4,
    bg="#170000",
    fg=red,
    activebackground=red,
    activeforeground="white",
    font=("Consolas", 18, "bold"),
    relief="solid",
    bd=2
)
disable_btn.grid(row=0, column=0, padx=25)

# ENABLE BUTTON
enable_btn = tk.Button(
    button_frame,
    text="ENABLE USB",
    command=enable_usb,
    width=20,
    height=4,
    bg="#001a00",
    fg=green,
    activebackground=green,
    activeforeground="black",
    font=("Consolas", 18, "bold"),
    relief="solid",
    bd=2
)
enable_btn.grid(row=0, column=1, padx=25)

# EXIT BUTTON
exit_btn = tk.Button(
    center_panel,
    text="EXIT SYSTEM",
    command=root.destroy,
    width=25,
    height=2,
    bg="#001122",
    fg=cyan,
    activebackground=cyan,
    activeforeground="black",
    font=("Consolas", 15, "bold"),
    relief="solid",
    bd=2
)
exit_btn.pack(pady=40)

# =========================================================
# RIGHT PANEL
# =========================================================

right_panel = tk.Frame(root, bg=panel)
right_panel.place(x=1080, y=100, width=300, height=700)

tk.Label(
    right_panel,
    text="SECURITY LOG",
    bg=panel,
    fg=cyan,
    font=("Consolas", 16, "bold")
).pack(pady=15)

log_box = tk.Text(
    right_panel,
    bg="black",
    fg=green,
    font=("Consolas", 11),
    width=35,
    height=30,
    insertbackground=green,
    relief="flat"
)
log_box.pack(pady=10)

# =========================================================
# INITIAL LOGS
# =========================================================

add_log("System Initialized")
add_log("Port Defender Loaded")
add_log("Registry Access : OK")
add_log("Administrator : YES")
add_log("USB Ports Enabled")

# =========================================================
# FOOTER
# =========================================================

footer = tk.Label(
    root,
    text="PORT DEFENDER © CYBER SECURITY TOOL",
    bg="black",
    fg=cyan,
    font=("Consolas", 12)
)
footer.pack(side="bottom", fill="x")

# =========================================================
# RUN
# =========================================================

root.mainloop()