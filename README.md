# 🔎 Simple Port Scanner

A basic Python-based TCP port scanner for educational and internal network use.

## 🚀 Features

- Scans a range of ports on a target host
- Fast, lightweight, and beginner-friendly
- CLI interface with customizable port range

## 🖥️ Demo

```bash
$ python port_scanner.py 127.0.0.1 --start 20 --end 80
[+] Port 22 is open
[+] Port 80 is open
```

## 📦 Requirements

- Python 3.x

## 🔧 Usage

```bash
python port_scanner.py <target> [--start START_PORT] [--end END_PORT]
```

### Example:

```bash
python port_scanner.py 192.168.1.1 --start 1 --end 100
```

