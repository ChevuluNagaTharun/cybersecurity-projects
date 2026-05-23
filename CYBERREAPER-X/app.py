# =========================================================
# CYBERREAPER X
# Ghost Your Data Beyond Detection.
# =========================================================

import customtkinter as ctk
from tkinter import filedialog, messagebox
from PIL import Image
from cryptography.fernet import Fernet
import threading
import random
import os
import time

# =========================================================
# THEME
# =========================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# =========================================================
# MAIN APPLICATION
# =========================================================

class CyberReaperX(ctk.CTk):

    def __init__(self):

        super().__init__()

        # =================================================
        # WINDOW
        # =================================================

        self.title("CYBERREAPER X")
        self.geometry("1450x850")
        self.configure(fg_color="#050505")

        self.image_path = ""
        self.output_path = "encrypted_image.png"

        # =================================================
        # HEADER
        # =================================================

        self.header = ctk.CTkLabel(
            self,
            text="⚡ CYBERREAPER X ⚡",
            font=("Consolas", 38, "bold"),
            text_color="#00ff99"
        )

        self.header.pack(pady=(20, 5))

        # =================================================
        # SLOGAN
        # =================================================

        self.slogan = ctk.CTkLabel(
            self,
            text="Ghost Your Data Beyond Detection.",
            font=("Consolas", 16, "italic"),
            text_color="#00ffaa"
        )

        self.slogan.pack(pady=(0, 20))

        # =================================================
        # MAIN FRAME
        # =================================================

        self.main_frame = ctk.CTkFrame(
            self,
            fg_color="#0d1117",
            corner_radius=20
        )

        self.main_frame.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=20
        )

        # =================================================
        # LEFT PANEL
        # =================================================

        self.left_panel = ctk.CTkFrame(
            self.main_frame,
            fg_color="#161b22",
            corner_radius=20,
            width=500
        )

        self.left_panel.pack(
            side="left",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # =================================================
        # RIGHT PANEL
        # =================================================

        self.right_panel = ctk.CTkFrame(
            self.main_frame,
            fg_color="#161b22",
            corner_radius=20
        )

        self.right_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=15,
            pady=15
        )

        # =================================================
        # IMAGE BOX
        # =================================================

        self.image_label = ctk.CTkLabel(
            self.left_panel,
            text="NO IMAGE SELECTED",
            width=450,
            height=320,
            fg_color="#050505",
            corner_radius=15,
            text_color="#00ffcc",
            font=("Consolas", 20, "bold")
        )

        self.image_label.pack(pady=20)

        # =================================================
        # SELECT BUTTON
        # =================================================

        self.select_btn = ctk.CTkButton(
            self.left_panel,
            text="SELECT IMAGE",
            command=self.select_image,
            width=260,
            height=45,
            fg_color="#00aa55",
            hover_color="#00ff99",
            text_color="black",
            font=("Consolas", 16, "bold")
        )

        self.select_btn.pack(pady=10)

        # =================================================
        # TERMINAL LOGS
        # =================================================

        self.logs = ctk.CTkTextbox(
            self.left_panel,
            width=450,
            height=280,
            fg_color="black",
            text_color="#00ff00",
            font=("Consolas", 13)
        )

        self.logs.pack(pady=20)

        self.log("SYSTEM BOOT SUCCESSFUL")
        self.log("CYBERREAPER X ONLINE")
        self.log("AWAITING TARGET IMAGE")

        # =================================================
        # MESSAGE TITLE
        # =================================================

        self.msg_title = ctk.CTkLabel(
            self.right_panel,
            text="SECRET PAYLOAD",
            font=("Consolas", 24, "bold"),
            text_color="#00ff99"
        )

        self.msg_title.pack(pady=15)

        # =================================================
        # MESSAGE BOX
        # =================================================

        self.message_box = ctk.CTkTextbox(
            self.right_panel,
            width=550,
            height=230,
            fg_color="black",
            text_color="#00ff00",
            font=("Consolas", 15)
        )

        self.message_box.pack(pady=10)

        # =================================================
        # KEY ENTRY
        # =================================================

        self.key_entry = ctk.CTkEntry(
            self.right_panel,
            placeholder_text="FERNET ENCRYPTION KEY",
            width=520,
            height=45,
            fg_color="#050505",
            border_color="#00ff99",
            text_color="#00ff99",
            font=("Consolas", 14)
        )

        self.key_entry.pack(pady=15)

        # =================================================
        # PROGRESS BAR
        # =================================================

        self.progress = ctk.CTkProgressBar(
            self.right_panel,
            width=520,
            progress_color="#00ff99"
        )

        self.progress.pack(pady=15)
        self.progress.set(0)

        # =================================================
        # BUTTON FRAME
        # =================================================

        self.button_frame = ctk.CTkFrame(
            self.right_panel,
            fg_color="transparent"
        )

        self.button_frame.pack(pady=25)

        # =================================================
        # ENCRYPT BUTTON
        # =================================================

        self.encrypt_btn = ctk.CTkButton(
            self.button_frame,
            text="ENCRYPT IMAGE",
            command=self.encrypt_thread,
            width=230,
            height=55,
            fg_color="#00aa55",
            hover_color="#00ff99",
            text_color="black",
            font=("Consolas", 16, "bold")
        )

        self.encrypt_btn.grid(row=0, column=0, padx=15)

        # =================================================
        # DECRYPT BUTTON
        # =================================================

        self.decrypt_btn = ctk.CTkButton(
            self.button_frame,
            text="DECRYPT IMAGE",
            command=self.decrypt_thread,
            width=230,
            height=55,
            fg_color="#8000ff",
            hover_color="#b266ff",
            text_color="white",
            font=("Consolas", 16, "bold")
        )

        self.decrypt_btn.grid(row=0, column=1, padx=15)

        # =================================================
        # START MATRIX EFFECT
        # =================================================

        self.matrix_effect()

    # =====================================================
    # MATRIX EFFECT
    # =====================================================

    def matrix_effect(self):

        chars = "01ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        random_text = "".join(
            random.choice(chars)
            for _ in range(80)
        )

        self.header.configure(
            text=f"⚡ CYBERREAPER X | {random_text[:20]} ⚡"
        )

        self.after(150, self.matrix_effect)

    # =====================================================
    # TERMINAL LOG
    # =====================================================

    def log(self, text):

        current_time = time.strftime("%H:%M:%S")

        self.logs.insert(
            "end",
            f"[{current_time}] {text}\n"
        )

        self.logs.see("end")

    # =====================================================
    # SELECT IMAGE
    # =====================================================

    def select_image(self):

        path = filedialog.askopenfilename(
            filetypes=[
                ("PNG Files", "*.png"),
                ("JPG Files", "*.jpg"),
                ("JPEG Files", "*.jpeg")
            ]
        )

        if path:

            self.image_path = path

            self.image_label.configure(
                text=os.path.basename(path)
            )

            self.log(f"TARGET IMAGE LOADED: {path}")

    # =====================================================
    # THREADS
    # =====================================================

    def encrypt_thread(self):

        threading.Thread(
            target=self.encrypt_message
        ).start()

    def decrypt_thread(self):

        threading.Thread(
            target=self.decrypt_message
        ).start()

    # =====================================================
    # ENCRYPT MESSAGE
    # =====================================================

    def encrypt_message(self):

        try:

            if not self.image_path:

                messagebox.showerror(
                    "ERROR",
                    "SELECT TARGET IMAGE"
                )

                return

            message = self.message_box.get(
                "1.0",
                "end"
            ).strip()

            if not message:

                messagebox.showerror(
                    "ERROR",
                    "ENTER SECRET PAYLOAD"
                )

                return

            self.progress.set(0.1)

            self.log("GENERATING ENCRYPTION KEY")

            key = Fernet.generate_key()

            self.key_entry.delete(0, "end")
            self.key_entry.insert(0, key.decode())

            f = Fernet(key)

            encrypted_message = f.encrypt(
                message.encode()
            )

            self.progress.set(0.3)

            self.log("OPENING IMAGE")

            image = Image.open(self.image_path)
            image = image.convert("RGB")

            pixels = list(image.getdata())

            binary_secret = ''.join(
                format(byte, '08b')
                for byte in encrypted_message
            )

            binary_secret += "1111111111111110"

            data_index = 0

            self.log("EMBEDDING PAYLOAD")

            for i in range(len(pixels)):

                pixel = list(pixels[i])

                for j in range(3):

                    if data_index < len(binary_secret):

                        pixel[j] = (
                            pixel[j] & ~1
                        ) | int(binary_secret[data_index])

                        data_index += 1

                pixels[i] = tuple(pixel)

                if data_index >= len(binary_secret):
                    break

            encoded_image = Image.new(
                image.mode,
                image.size
            )

            encoded_image.putdata(pixels)

            encoded_image.save(
                self.output_path
            )

            self.progress.set(0.8)

            self.log("PAYLOAD SUCCESSFULLY EMBEDDED")
            self.log(f"OUTPUT SAVED: {self.output_path}")

            self.progress.set(1.0)

            messagebox.showinfo(
                "SUCCESS",
                f"IMAGE ENCRYPTED\n\nKEY:\n{key.decode()}"
            )

        except Exception as e:

            self.log(str(e))

            messagebox.showerror(
                "ERROR",
                str(e)
            )

    # =====================================================
    # DECRYPT MESSAGE
    # =====================================================

    def decrypt_message(self):

        try:

            if not self.image_path:

                messagebox.showerror(
                    "ERROR",
                    "SELECT ENCRYPTED IMAGE"
                )

                return

            key = self.key_entry.get().encode()

            self.log("OPENING ENCRYPTED IMAGE")

            image = Image.open(self.image_path)

            pixels = list(image.getdata())

            binary_data = ""

            self.log("EXTRACTING PAYLOAD")

            for pixel in pixels:

                for value in pixel[:3]:

                    binary_data += str(
                        value & 1
                    )

            end_marker = "1111111111111110"

            end_index = binary_data.find(
                end_marker
            )

            binary_data = binary_data[:end_index]

            all_bytes = [

                binary_data[i:i + 8]

                for i in range(
                    0,
                    len(binary_data),
                    8
                )

            ]

            encrypted_message = bytes(

                [
                    int(byte, 2)
                    for byte in all_bytes
                ]

            )

            self.log("DECRYPTING PAYLOAD")

            f = Fernet(key)

            decrypted_message = f.decrypt(
                encrypted_message
            ).decode()

            self.message_box.delete(
                "1.0",
                "end"
            )

            self.message_box.insert(
                "end",
                decrypted_message
            )

            self.log("PAYLOAD RECOVERED")

            messagebox.showinfo(
                "SECRET MESSAGE",
                decrypted_message
            )

        except Exception as e:

            self.log(str(e))

            messagebox.showerror(
                "ERROR",
                "INVALID KEY OR CORRUPTED IMAGE"
            )

# =========================================================
# RUN APPLICATION
# =========================================================

if __name__ == "__main__":

    app = CyberReaperX()

    app.mainloop()