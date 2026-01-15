# 🔴 Red Team – Python Port Scanner

This project is a simple yet effective **TCP port scanner** developed in Python using the built-in `socket` library.  
It is designed as a **learning-focused cybersecurity project** to understand how port scanning works at a low level.

---

## 🛠 Features

- Scan a target IP address for open TCP ports
- Custom port range input (start & end port)
- Uses TCP (`SOCK_STREAM`) sockets
- Displays open ports in real time
- Summarizes all open ports at the end
- Safe for **local network and lab testing**

---

## 🧠 How It Works

The scanner attempts to establish a TCP connection to each port in the specified range:

- If a connection is successful → **Port is open**
- If not → **Port is closed**

This approach demonstrates the **core logic behind tools like Nmap**, implemented from scratch.

---

## ▶️ Usage

1. Clone the repository:
```bash
git clone https://github.com/YaverGazi/red-team-port-scanner.git
