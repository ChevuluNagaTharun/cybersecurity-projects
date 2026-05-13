\# Port Defender — Your USB Security Shield



Port Defender is a cybersecurity-based USB protection tool developed using Python and Tkinter.  

It allows users to enable or disable USB ports securely using password authentication and Windows Registry control.



\---



\## Features



\- Disable USB Ports

\- Enable USB Ports

\- Password Protected Access

\- Realistic Hacker-Style GUI

\- Security Log Monitoring

\- Windows Registry-Based USB Control

\- Dark Cybersecurity Theme



\---



\## Technologies Used



\- Python

\- Tkinter

\- Windows Registry

\- Batch Scripting



\---



\## Project Structure



```bash

Port-Defender/

│

├── screenshots/

│   └── gui.png

│

├── main.py

├── block\_usb.bat

├── unblock\_usb.bat

├── run.bat

├── README.md

```



\---



\## How It Works



The tool modifies the Windows Registry path:



```bash

HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Services\\USBSTOR

```



\### Registry Values



| Value | Action |

|------|------|

| 4 | Disable USB Storage |

| 3 | Enable USB Storage |



\---



\## Installation



\### Clone Repository



```bash

git clone https://github.com/ChevuluNagaTharun/cybersecurity-projects.git

```



\### Open Project



```bash

cd cybersecurity-projects/Port-Defender

```



\---



\## Run Project



```bash

python main.py

```



OR



```bash

run.bat

```



\---



\## Important



Run CMD or Python as \*\*Administrator\*\* for proper USB control functionality.



\---



\## Screenshot



!\[Port Defender GUI](screenshots/gui.png)



\---



\## Future Improvements



\- Real-time USB Detection

\- USB Device Logging

\- Encryption Support

\- Admin Dashboard

\- Threat Monitoring

\- Device Whitelisting



\---



\## Author



\### Naga Tharun



Cybersecurity Enthusiast | Python Developer | Ethical Hacking Learner



GitHub:

https://github.com/ChevuluNagaTharun



\---



\## License



This project is developed for educational and cybersecurity learning purposes.

