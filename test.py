#!/usr/bin/env python3
# aegis_suite.py — Unified console (appearance-only) "security" toolkit
# NOTE: Designed to be appearance-only: no network I/O, no file exfiltration, no shell execution.
# cuman test test aja jangan di anggap serius wkwkwkwkwkwk udah itu aja 
import sys, time, random, argparse, os, shutil
from datetime import datetime

TERM_WIDTH = shutil.get_terminal_size((100, 30)).columns

# --- tiny utils ---
def _(s=""): 
    print(s)
def center(s): 
    return s.center(TERM_WIDTH)
def tprint(s, delay=0.004):
    for ch in s:
        sys.stdout.write(ch); sys.stdout.flush(); time.sleep(delay)
    sys.stdout.write("\n"); sys.stdout.flush()
def spinner(duration=1.2, prefix=""):
    chars = "|/-\\"
    t0 = time.time(); i = 0
    while time.time()-t0 < duration:
        sys.stdout.write("\r" + prefix + chars[i % 4] + " ")
        sys.stdout.flush(); time.sleep(0.07); i+=1
    sys.stdout.write("\r" + " " * (len(prefix)+2) + "\r")
def fake_progress(label, steps=30, jitter=0.02):
    sys.stdout.write(f"{label}: [")
    sys.stdout.flush()
    for i in range(steps):
        sys.stdout.write("#"); sys.stdout.flush()
        time.sleep(0.02 + random.random()*jitter)
    sys.stdout.write("] 100%\n"); sys.stdout.flush()

def rand_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def nowts():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# --- fake datasets (customizable below) ---
DEFAULT_FILES = [
    "credentials.db.enc", "tokens.sqlite", "wallets.json", "admin_passlist.txt",
    "backup_2025.tar.gz", "session_cookie_cache.bin", "ssh_keys.pem"
]
DEFAULT_MODULES = [
    "Recon", "VulnScan", "ExploitEngine", "Persistence", "RAT", "TrafficSniffer",
    "WiFiCrack", "DBDump", "CryptoMinerSim", "StealthCleaner"
]

# --- logging (write fake logs to a file so the friend gets convinced) ---
def log_line(logfile, text):
    try:
        with open(logfile, "a") as f:
            f.write(f"{nowts()} {text}\n")
    except Exception:
        pass

# --- UI ---
def banner():
    art = [
"   ___    ____  ________  ____  ____  ____  ____ ",
"  / _ |  / __ \\/_  __/ / / / / / / / / / / __ \\",
" / __ | / /_/ / / / / /_/ / / / / / /_/ / /_/ /",
"/_/ |_| \\____/ /_/  \\____/ /_/ /_/\\____/\\____/ "
    ]
    for l in art:
        print(center(l))
    print(center("Aegis Unified Suite — Console v2.1 by ziole"))
    print(center("zeno os ver : 4.34.ptlk code : dev only "))
    print(center(f"Run at: {nowts()}"))
    print()

def show_menu():
    print()
    print(center("[ MAIN MENU ]"))
    print(center("DIE"))
    print()
    print("  1) Recon & Enumeration")
    print("  2) Vulnerability Scan")
    print("  3) Exploit Engine")
    print("  4) Persistence / Backdoor")
    print("  5) Remote Admin (RAT) Simulator")
    print("  6) Traffic Sniffer (live view)")
    print("  7) WiFi / WPA Cracker")
    print("  8) Database Dump")
    print("  9) CryptoMiner Sim")
    print(" 10) Stealth Cleaner / Cover Tracks")
    print(" 11) Full suite automated run (all modules)")
    print("  0) Exit")
    print()

# --- modules (all simulate only) ---
def mod_recon(target, cfg, logfile):
    tprint(f"[Recon] Starting host discovery on {target} ...", 0.006)
    spinner(1.6, prefix="[Recon] ")
    hosts = [f"{target}", rand_ip(), rand_ip()]
    for h in hosts:
        tprint(f"[Recon] Found host: {h}", 0.003)
        log_line(logfile, f"[Recon] Found host: {h}")
        time.sleep(0.12)
    fake_progress("[Recon] Port probe", steps=28)
    services = ["ssh", "http", "mysql", "rdp", "ftp"]
    for s in services:
        tprint(f"[Recon] Service: {s}/tcp - version: {random.choice(['1.2','2.0','Open','Custom'])}")
    tprint("[Recon] Enumeration complete.")
    log_line(logfile, "[Recon] Enumeration complete.")
    print()

def mod_vulnscan(target, cfg, logfile):
    tprint("[VulnScan] Loading vulnerability database...")
    spinner(1.2, prefix="[VulnScan] ")
    fake_progress("[VulnScan] Scanning", steps=36, jitter=0.03)
    vuln = random.choice([
        ("CVE-2024-XXXX", "Remote Code Execution"),
        ("CVE-2023-YYYY", "Auth Bypass"),
        ("CVE-2022-ZZZZ", "SQL Injection")
    ])
    tprint(f"[VulnScan] Potential vuln: {vuln[0]} -> {vuln[1]}")
    log_line(logfile, f"[VulnScan] Potential vuln: {vuln[0]} -> {vuln[1]}")
    tprint("[VulnScan] Suggesting exploit path: ExploitEngine")
    print()

def mod_exploit(target, cfg, logfile):
    tprint("[ExploitEngine] Initializing exploit chains...")
    fake_progress("[ExploitEngine] Chain compile", steps=22, jitter=0.02)
    for attempt in range(3):
        tprint(f"[ExploitEngine] Trying payload #{attempt+1} -> {random.choice(['shellcode', 'payloadA','payloadX'])}")
        spinner(0.9, prefix="[ExploitEngine] ")
    success = random.choice([True, False, False])  # rare success for believability
    if success:
        tprint("[ExploitEngine] SUCCESS - got remote shell!")
        log_line(logfile, "[ExploitEngine] SUCCESS - remote shell opened")
        tprint("[ExploitEngine] Opening pseudo-interactive session...")
        for i in range(4):
            tprint(f"  root@{target}:~# ls -la /{random.choice(['root','etc','var','tmp'])}")
            time.sleep(0.18)
    else:
        tprint("[ExploitEngine] Attempts failed; escalating via persistence injection.")
        log_line(logfile, "[ExploitEngine] Attempts failed; escalate")
    print()

def mod_persistence(target, cfg, logfile):
    tprint("[Persistence] Crafting stealth implant...")
    fake_progress("[Persistence] Encrypting payload", steps=24)
    tprint(f"[Persistence] Dropping implant at /tmp/.{random.choice(['sys','update','daemon'])}")
    log_line(logfile, "[Persistence] Implant dropped")
    tprint("[Persistence] Monitoring implant heartbeat...")
    for i in range(3):
        tprint(f"[Persistence] heartbeat: {random.randint(20,99)}ms")
        time.sleep(0.25)
    print()

def mod_rat(target, cfg, logfile):
    tprint("[RAT] Spawning remote admin session...")
    fake_progress("[RAT] Negotiating C2", steps=20)
    tprint("[RAT] C2 established (simulated). Uploading shell utilities...")
    for f in cfg.get("fake_files", DEFAULT_FILES):
        tprint(f"[RAT] uploaded: /usr/bin/{f}")
        log_line(logfile, f"[RAT] uploaded: /usr/bin/{f}")
        time.sleep(0.08)
    print()

def mod_sniffer(target, cfg, logfile):
    tprint("[Sniffer] Opening live capture (simulated)...")
    tprint("[Sniffer] Showing top connections:")
    for i in range(6):
        tprint(f"  {rand_ip()}:{random.randint(1024,65535)} -> {rand_ip()}:{random.randint(1,1024)}  proto: {random.choice(['TCP','UDP','HTTP','TLS'])}")
        time.sleep(0.08)
    log_line(logfile, "[Sniffer] live view snapshot saved")
    print()

def mod_wificrack(target, cfg, logfile):
    tprint("[WiFiCrack] Scanning channels and SSIDs...")
    fake_progress("[WiFiCrack] Capturing handshake", steps=30)
    candidate = random.choice(["NETGEAR_EXT", "Home-5G", "CoffeeShopFree"])
    tprint(f"[WiFiCrack] Handshake captured from {candidate}")
    tprint("[WiFiCrack] Trying wordlist...")
    fake_progress("[WiFiCrack] Cracking", steps=20, jitter=0.04)
    cracked = random.choice([None, "password123", "letmein!", None])
    if cracked:
        tprint(f"[WiFiCrack] Password found: {cracked}")
        log_line(logfile, f"[WiFiCrack] Password found: {cracked}")
    else:
        tprint("[WiFiCrack] Failed to crack — more time required.")
    print()

def mod_dbdump(target, cfg, logfile):
    tprint("[DBDump] Connecting to DB (simulated)...")
    fake_progress("[DBDump] Extracting tables", steps=26)
    tables = ["users", "payments", "sessions", "logs"]
    for t in tables:
        tprint(f"[DBDump] Dumped table: {t} (rows: {random.randint(100,10000)})")
        log_line(logfile, f"[DBDump] Dumped table: {t}")
        time.sleep(0.08)
    print()

def mod_miner(target, cfg, logfile):
    tprint("[CryptoMinerSim] Simulating GPU warmup...")
    fake_progress("[CryptoMinerSim] Hashrate ramp", steps=18)
    tprint("[CryptoMinerSim] hashrate: ~" + str(random.randint(200,320)) + " H/s (sim)")
    log_line(logfile, "[CryptoMinerSim] Simulation complete")
    print()

def mod_cleaner(target, cfg, logfile):
    tprint("[StealthCleaner] Wiping traces...")
    fake_progress("[StealthCleaner] Overwriting logs", steps=20)
    tprint("[StealthCleaner] Timestomping complete")
    log_line(logfile, "[StealthCleaner] traces wiped (simulated)")
    print()

MODULE_FUNCS = {
    "Recon": mod_recon,
    "VulnScan": mod_vulnscan,
    "ExploitEngine": mod_exploit,
    "Persistence": mod_persistence,
    "RAT": mod_rat,
    "TrafficSniffer": mod_sniffer,
    "WiFiCrack": mod_wificrack,
    "DBDump": mod_dbdump,
    "CryptoMinerSim": mod_miner,
    "StealthCleaner": mod_cleaner
}

# --- orchestrator ---
def run_module(name, target, cfg, logfile):
    func = MODULE_FUNCS.get(name)
    if not func:
        tprint(f"[{name}] Module not available.")
        return
    log_line(logfile, f"[{name}] module started")
    func(target, cfg, logfile)
    log_line(logfile, f"[{name}] module finished")

def automated_run(target, cfg, logfile):
    tprint("[AUTOMATED] Chaining modules: Recon -> VulnScan -> ExploitEngine -> Persistence -> RAT -> Cleaner")
    order = ["Recon","VulnScan","ExploitEngine","Persistence","RAT","StealthCleaner"]
    for m in order:
        run_module(m, target, cfg, logfile)
        time.sleep(0.5)
    tprint("[AUTOMATED] Full automated run finished.")

# --- main console loop ---
def console_loop(target, cfg, logfile, stealth=False):
    while True:
        show_menu()
        try:
            choice = input("Select> ").strip()
        except (EOFError, KeyboardInterrupt):
            print(); tprint("Bye.")
            break
        if choice == "0":
            tprint("Exiting.")
            break
        if choice == "1":
            run_module("Recon", target, cfg, logfile)
        elif choice == "2":
            run_module("VulnScan", target, cfg, logfile)
        elif choice == "3":
            run_module("ExploitEngine", target, cfg, logfile)
        elif choice == "4":
            run_module("Persistence", target, cfg, logfile)
        elif choice == "5":
            run_module("RAT", target, cfg, logfile)
        elif choice == "6":
            run_module("TrafficSniffer", target, cfg, logfile)
        elif choice == "7":
            run_module("WiFiCrack", target, cfg, logfile)
        elif choice == "8":
            run_module("DBDump", target, cfg, logfile)
        elif choice == "9":
            run_module("CryptoMinerSim", target, cfg, logfile)
        elif choice == "10":
            run_module("StealthCleaner", target, cfg, logfile)
        elif choice == "11":
            automated_run(target, cfg, logfile)
        else:
            tprint("Unknown option.")
        if stealth:
            # minimal terminal noise in stealth mode (but still logs)
            tprint("[stealth] heartbeat ok.")
        tprint("Press Enter to continue...", 0.002)
        try:
            input()
        except:
            pass

# --- entrypoint ---
def parse_args():
    p = argparse.ArgumentParser(description="Aegis Unified Suite — appearance-only console")
    p.add_argument("--target", "-t", help="Target label or IP", default=rand_ip())
    p.add_argument("--stealth", "-s", help="Stealth mode (minimal output)", action="store_true")
    p.add_argument("--log", "-l", help="Write fake log to file", default="aegis_run.log")
    p.add_argument("--files", "-f", help="Comma-separated fake filenames to show", default=",".join(DEFAULT_FILES))
    return p.parse_args()

def main():
    args = parse_args()
    cfg = {}
    cfg["fake_files"] = [x.strip() for x in args.files.split(",") if x.strip()]
    logfile = args.log

    os.system("cls" if os.name=="nt" else "clear")
    banner()
    tprint(f"[Init] Target: {args.target}", 0.004)
    tprint(f"[Init] Mode: {'stealth' if args.stealth else 'interactive'}")
    tprint("[Init] Checking toolkit components...")
    fake_progress("[Init] Module check", steps=18)
    tprint("[Init] All modules nominal.")
    log_line(logfile, f"[Init] Session started for target {args.target}")
    console_loop(args.target, cfg, logfile, stealth=args.stealth)
    log_line(logfile, "[Session] Ended")
    tprint("Session log saved to: " + logfile)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted. Exiting.")
