# ============================================================
# CYBERSCAN PROFESSIONAL EDITION
# Educational / Authorized Security Testing Only
# ============================================================

import socket
import concurrent.futures
import threading
import csv
import platform
from datetime import datetime

import customtkinter as ctk
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText

from PIL import Image

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

# ============================================================
# APP STYLE
# ============================================================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")

# ============================================================
# MAIN APPLICATION
# ============================================================

class CyberReconScanner:

    def __init__(self):

        self.root = ctk.CTk()

        self.root.title("CyberScan Professional Edition")
        self.root.geometry("1500x900")

        # ====================================================
        # BACKGROUND IMAGE
        # ====================================================

        self.bg_image = ctk.CTkImage(
            light_image=Image.open("background.png"),
            dark_image=Image.open("background.png"),
            size=(1500, 900)
        )

        self.bg_label = ctk.CTkLabel(
            self.root,
            image=self.bg_image,
            text=""
        )

        self.bg_label.place(
            x=0,
            y=0,
            relwidth=1,
            relheight=1
        )

        # ====================================================
        # VARIABLES
        # ====================================================

        self.results = []
        self.stop_scan = False
        self.open_port_count = 0
        self.scanned_ports = 0

        self.build_gui()

        self.update_clock()

    # ========================================================
    # GUI
    # ========================================================

    def build_gui(self):

        # ====================================================
        # HEADER
        # ====================================================

        header = ctk.CTkFrame(
            self.root,
            fg_color="#12263f",
            corner_radius=25,
            border_width=1,
            border_color="#00e5ff",
            height=90
        )

        header.pack(
            fill="x",
            padx=20,
            pady=15
        )

        title = ctk.CTkLabel(
            header,
            text="CYBERSCAN",
            font=("Orbitron", 36, "bold"),
            text_color="#00e5ff"
        )

        title.pack(
            side="left",
            padx=25,
            pady=20
        )

        self.status_header = ctk.CTkLabel(
            header,
            text="SYSTEM STATUS : READY",
            font=("Consolas", 16),
            text_color="#7ce7ff"
        )

        self.status_header.pack(
            side="left",
            padx=20
        )

        self.clock = ctk.CTkLabel(
            header,
            text="",
            font=("Consolas", 16, "bold"),
            text_color="#00ffff"
        )

        self.clock.pack(
            side="right",
            padx=30
        )

        # ====================================================
        # MAIN AREA
        # ====================================================

        main = ctk.CTkFrame(
            self.root,
            fg_color="transparent"
        )

        main.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        # ====================================================
        # LEFT PANEL
        # ====================================================

        left_panel = ctk.CTkFrame(
            main,
            width=340,
            fg_color="#11263b",
            corner_radius=25,
            border_width=1,
            border_color="#00d9ff"
        )

        left_panel.pack(
            side="left",
            fill="y",
            padx=10,
            pady=10
        )

        # ====================================================
        # TITLE
        # ====================================================

        section = ctk.CTkLabel(
            left_panel,
            text="TARGET CONFIGURATION",
            font=("Orbitron", 18, "bold"),
            text_color="#00e5ff"
        )

        section.pack(
            pady=(25, 20)
        )

        # ====================================================
        # INPUTS
        # ====================================================

        self.target_entry = ctk.CTkEntry(
            left_panel,
            placeholder_text="Target IP / Hostname",
            width=280,
            height=45,
            font=("Consolas", 14),
            fg_color="#0d1f33",
            border_color="#00d9ff",
            corner_radius=15
        )

        self.target_entry.pack(pady=10)

        self.start_port = ctk.CTkEntry(
            left_panel,
            width=280,
            height=45,
            font=("Consolas", 14),
            fg_color="#0d1f33",
            border_color="#00d9ff",
            corner_radius=15
        )

        self.start_port.pack(pady=10)
        self.start_port.insert(0, "1")

        self.end_port = ctk.CTkEntry(
            left_panel,
            width=280,
            height=45,
            font=("Consolas", 14),
            fg_color="#0d1f33",
            border_color="#00d9ff",
            corner_radius=15
        )

        self.end_port.pack(pady=10)
        self.end_port.insert(0, "1024")

        # ====================================================
        # COMBO BOX
        # ====================================================

        self.scan_mode = ctk.CTkComboBox(
            left_panel,
            values=[
                "Quick Scan",
                "Accurate Scan",
                "Service Scan"
            ],
            width=280,
            height=45,
            font=("Consolas", 14),
            fg_color="#0d1f33",
            border_color="#00d9ff",
            button_color="#009dff",
            button_hover_color="#00c8ff",
            corner_radius=15
        )

        self.scan_mode.pack(pady=10)
        self.scan_mode.set("Quick Scan")

        # ====================================================
        # BUTTONS
        # ====================================================

        self.start_button = ctk.CTkButton(
            left_panel,
            text="START SCAN",
            width=280,
            height=50,
            fg_color="#009dff",
            hover_color="#00c8ff",
            font=("Orbitron", 16, "bold"),
            corner_radius=18,
            command=self.start_scan_thread
        )

        self.start_button.pack(
            pady=(25, 12)
        )

        self.stop_button = ctk.CTkButton(
            left_panel,
            text="STOP SCAN",
            width=280,
            height=50,
            fg_color="#c1121f",
            hover_color="#ef233c",
            font=("Orbitron", 16, "bold"),
            corner_radius=18,
            command=self.stop_scanning
        )

        self.stop_button.pack(pady=12)

        self.csv_button = ctk.CTkButton(
            left_panel,
            text="EXPORT CSV",
            width=280,
            height=50,
            fg_color="#1d4ed8",
            hover_color="#2563eb",
            font=("Orbitron", 16, "bold"),
            corner_radius=18,
            command=self.export_csv
        )

        self.csv_button.pack(pady=12)

        self.pdf_button = ctk.CTkButton(
            left_panel,
            text="EXPORT PDF",
            width=280,
            height=50,
            fg_color="#3a86ff",
            hover_color="#4895ef",
            font=("Orbitron", 16, "bold"),
            corner_radius=18,
            command=self.export_pdf
        )

        self.pdf_button.pack(pady=12)

        # ====================================================
        # STATS PANEL
        # ====================================================

        stats = ctk.CTkFrame(
            left_panel,
            fg_color="#132a44",
            corner_radius=20,
            border_width=1,
            border_color="#00d9ff"
        )

        stats.pack(
            fill="x",
            padx=20,
            pady=25
        )

        stats_title = ctk.CTkLabel(
            stats,
            text="LIVE ANALYTICS",
            font=("Orbitron", 16, "bold"),
            text_color="#00e5ff"
        )

        stats_title.pack(pady=15)

        self.ports_label = ctk.CTkLabel(
            stats,
            text="Ports Scanned : 0",
            font=("Consolas", 14),
            text_color="#7ce7ff"
        )

        self.ports_label.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        self.open_label = ctk.CTkLabel(
            stats,
            text="Open Ports : 0",
            font=("Consolas", 14),
            text_color="#7ce7ff"
        )

        self.open_label.pack(
            anchor="w",
            padx=20,
            pady=5
        )

        self.risk_label = ctk.CTkLabel(
            stats,
            text="Threat Level : LOW",
            font=("Consolas", 14, "bold"),
            text_color="#00ff99"
        )

        self.risk_label.pack(
            anchor="w",
            padx=20,
            pady=10
        )

        # ====================================================
        # RISK BAR
        # ====================================================

        self.risk_bar = ctk.CTkProgressBar(
            stats,
            width=250,
            progress_color="#00ff99",
            fg_color="#0d1f33"
        )

        self.risk_bar.pack(
            pady=(5, 20)
        )

        self.risk_bar.set(0.2)

        # ====================================================
        # RIGHT PANEL
        # ====================================================

        right_panel = ctk.CTkFrame(
            main,
            fg_color="#11263b",
            corner_radius=25,
            border_width=1,
            border_color="#00d9ff"
        )

        right_panel.pack(
            side="right",
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        output_title = ctk.CTkLabel(
            right_panel,
            text="LIVE CYBER TERMINAL",
            font=("Orbitron", 22, "bold"),
            text_color="#00e5ff"
        )

        output_title.pack(
            anchor="w",
            padx=25,
            pady=(25, 15)
        )

        # ====================================================
        # PROGRESS BAR
        # ====================================================

        self.progress = ctk.CTkProgressBar(
            right_panel,
            width=950,
            progress_color="#00e5ff",
            fg_color="#0d1f33"
        )

        self.progress.pack(
            padx=25,
            pady=10
        )

        self.progress.set(0)

        # ====================================================
        # TERMINAL
        # ====================================================

        self.output = ScrolledText(
            right_panel,
            bg="#0b1d30",
            fg="#7ce7ff",
            insertbackground="#00ffff",
            font=("Consolas", 12),
            relief="flat",
            highlightthickness=1,
            highlightbackground="#00d9ff"
        )

        self.output.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=15
        )

        # ====================================================
        # FOOTER
        # ====================================================

        footer = ctk.CTkLabel(
            right_panel,
            text="CyberScan Professional Edition v3.0  |  Authorized Security Testing Only",
            font=("Consolas", 12),
            text_color="#7ce7ff"
        )

        footer.pack(
            pady=(0, 15)
        )

        # ====================================================
        # STARTUP LOGS
        # ====================================================

        self.animated_log("[ INITIALIZING CYBERSCAN CORE ]")
        self.animated_log("[ LOADING NETWORK MODULES ]")
        self.animated_log("[ ESTABLISHING SECURE ENVIRONMENT ]")
        self.animated_log("[ ACCESS GRANTED ]")
        self.animated_log("")

    # ========================================================
    # CLOCK
    # ========================================================

    def update_clock(self):

        current = datetime.now().strftime("%H:%M:%S")

        self.clock.configure(
            text=current
        )

        self.root.after(1000, self.update_clock)

    # ========================================================
    # ANIMATED LOG
    # ========================================================

    def animated_log(self, text):

        for char in text:

            self.output.insert("end", char)
            self.output.update()

        self.output.insert("end", "\n")
        self.output.see("end")

    # ========================================================
    # NORMAL LOG
    # ========================================================

    def log(self, text):

        self.output.insert("end", text + "\n")
        self.output.see("end")

    # ========================================================
    # STOP SCAN
    # ========================================================

    def stop_scanning(self):

        self.stop_scan = True
        self.log("[ STOPPING SCAN ]")

    # ========================================================
    # START THREAD
    # ========================================================

    def start_scan_thread(self):

        self.stop_scan = False

        scan_thread = threading.Thread(
            target=self.scan_ports
        )

        scan_thread.daemon = True
        scan_thread.start()

    # ========================================================
    # SCAN SINGLE PORT
    # ========================================================

    def scan_single_port(self, target, port, timeout):

        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(timeout)

        try:

            result = sock.connect_ex(
                (target, port)
            )

            if result == 0:
                return port, True

            return port, False

        except:
            return port, False

        finally:
            sock.close()

    # ========================================================
    # MAIN SCAN
    # ========================================================

    def scan_ports(self):

        self.output.delete("1.0", "end")

        self.results.clear()

        self.open_port_count = 0
        self.scanned_ports = 0

        target = self.target_entry.get().strip()

        try:

            start = int(self.start_port.get())
            end = int(self.end_port.get())

        except:

            self.log("[ ERROR ] Invalid Port Range")
            return

        try:

            target_ip = socket.gethostbyname(target)

        except:

            self.log("[ ERROR ] Invalid Target")
            return

        self.log("=" * 70)
        self.log(f"Target : {target} ({target_ip})")
        self.log(f"Host OS : {platform.system()}")
        self.log(f"Scan Started : {datetime.now()}")
        self.log("=" * 70)

        mode = self.scan_mode.get()

        if mode == "Quick Scan":

            timeout = 0.5
            workers = 300

        elif mode == "Accurate Scan":

            timeout = 2
            workers = 100

        else:

            timeout = 1
            workers = 200

        total_ports = end - start + 1

        with concurrent.futures.ThreadPoolExecutor(
            max_workers=workers
        ) as executor:

            futures = []

            for port in range(start, end + 1):

                if self.stop_scan:
                    break

                futures.append(
                    executor.submit(
                        self.scan_single_port,
                        target_ip,
                        port,
                        timeout
                    )
                )

            for future in concurrent.futures.as_completed(futures):

                if self.stop_scan:
                    break

                self.scanned_ports += 1

                progress = self.scanned_ports / total_ports

                self.progress.set(progress)

                self.ports_label.configure(
                    text=f"Ports Scanned : {self.scanned_ports}"
                )

                port, is_open = future.result()

                self.status_header.configure(
                    text=f"SCANNING PORT : {port}"
                )

                if is_open:

                    self.open_port_count += 1

                    self.open_label.configure(
                        text=f"Open Ports : {self.open_port_count}"
                    )

                    try:
                        service = socket.getservbyport(port)

                    except:
                        service = "Unknown"

                    self.log(f"[ OPEN ] Port {port} ({service})")

                    self.results.append({
                        "port": port,
                        "service": service
                    })

        self.progress.set(1)

        self.status_header.configure(
            text="SCAN COMPLETE"
        )

        self.log("")
        self.log("[ COMPLETE ] Scan Finished")
        self.log(f"[ SUMMARY ] Open Ports : {self.open_port_count}")

        # ====================================================
        # THREAT LEVEL
        # ====================================================

        if self.open_port_count >= 10:

            self.risk_label.configure(
                text="Threat Level : HIGH",
                text_color="red"
            )

            self.risk_bar.set(1)

        elif self.open_port_count >= 5:

            self.risk_label.configure(
                text="Threat Level : MEDIUM",
                text_color="orange"
            )

            self.risk_bar.set(0.6)

        else:

            self.risk_label.configure(
                text="Threat Level : LOW",
                text_color="#00ff99"
            )

            self.risk_bar.set(0.2)

    # ========================================================
    # EXPORT CSV
    # ========================================================

    def export_csv(self):

        if not self.results:

            self.log("[ ERROR ] No Results")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV Files", "*.csv")]
        )

        if not file_path:
            return

        with open(file_path, "w", newline="") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=["port", "service"]
            )

            writer.writeheader()
            writer.writerows(self.results)

        self.log(f"[ EXPORT ] CSV Saved : {file_path}")

    # ========================================================
    # EXPORT PDF
    # ========================================================

    def export_pdf(self):

        if not self.results:

            self.log("[ ERROR ] No Results")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".pdf",
            filetypes=[("PDF Files", "*.pdf")]
        )

        if not file_path:
            return

        doc = SimpleDocTemplate(
            file_path,
            pagesize=letter
        )

        styles = getSampleStyleSheet()

        elements = []

        title = Paragraph(
            "CyberScan Professional Report",
            styles['Title']
        )

        elements.append(title)
        elements.append(Spacer(1, 15))

        generated = Paragraph(
            f"Generated : {datetime.now()}",
            styles['Normal']
        )

        elements.append(generated)
        elements.append(Spacer(1, 20))

        for result in self.results:

            text = f'''
            <b>Port:</b> {result['port']}<br/>
            <b>Service:</b> {result['service']}<br/><br/>
            '''

            para = Paragraph(
                text,
                styles['BodyText']
            )

            elements.append(para)
            elements.append(Spacer(1, 12))

        doc.build(elements)

        self.log(f"[ EXPORT ] PDF Saved : {file_path}")

    # ========================================================
    # RUN APP
    # ========================================================

    def run(self):

        self.root.mainloop()

# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app = CyberReconScanner()
    app.run()