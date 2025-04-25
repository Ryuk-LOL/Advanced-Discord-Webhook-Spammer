import requests
import time
import random
import os
import threading
from colorama import Fore, Style, init

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print(Fore.MAGENTA + """
╔════════════════════════════════════════════════════════════════════════════╗
║                      🧨  ADVANCED WEBHOOK SPAMMER  🧨                     ║
╠════════════════════════════════════════════════════════════════════════════╣
║  Features:                                                                  ║
║  - Message variants / embeds                                                ║
║  - Rate-limit bypass & delay control                                        ║
║  - Threaded high-speed spam                                                 ║
║  - Random emoji appending after message                                     ║
║  - Supports both direct input & file input                                   ║
╚════════════════════════════════════════════════════════════════════════════╝
""" + Style.RESET_ALL)

def send_message(webhook_url, message, use_embed):
    data = {"content": message}

    if use_embed:
        data = {
            "embeds": [{
                "title": "🔥 Message",
                "description": message,
                "color": 0xff5555
            }]
        }

    try:
        response = requests.post(webhook_url, json=data)
        if response.status_code in [200, 204]:
            print(Fore.GREEN + f"[✓] Sent successfully")
        elif response.status_code == 429:
            retry_after = response.json().get("retry_after", 1)
            print(Fore.YELLOW + f"[!] Rate limited. Retrying in {retry_after} sec")
            time.sleep(retry_after)
            send_message(webhook_url, message, use_embed)  # Retry
        else:
            print(Fore.RED + f"[X] Failed (Status: {response.status_code})")
    except Exception as e:
        print(Fore.RED + f"[X] Error occurred: {str(e)}")

def threaded_spam(webhook, msg, count, delay, use_embed, use_random, thread_count):
    def spam():
        for i in range(count // thread_count):
            text = msg
            if use_random:
                suffix = random.choice(["🔥", "💥", "🚀", "👾", "🧠", "💀"])
                text += f" {suffix}"
            send_message(webhook, text, use_embed)
            time.sleep(delay)

    threads = []
    for _ in range(thread_count):
        t = threading.Thread(target=spam)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def main():
    while True:
        clear()
        banner()

        webhook = input(Fore.CYAN + "🔗 Webhook URL: ").strip()
        if not webhook.startswith("https://discord.com/api/webhooks/"):
            print(Fore.RED + "❌ Invalid webhook URL.")
            return

        msg_source = input(Fore.CYAN + "📄 Use message from (1) input or (2) file? [1/2]: ").strip()
        if msg_source == "2":
            file_path = input("📂 Enter filename (e.g., messages.txt): ").strip()
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    messages = [line.strip() for line in f.readlines() if line.strip()]
                msg = random.choice(messages)
                use_random = True
            except:
                print(Fore.RED + "❌ Failed to load file.")
                continue
        else:
            msg = input(Fore.CYAN + "💬 Message to spam: ").strip()
            use_random = input("🎲 Add random emoji after message? (y/n): ").lower() == "y"

        use_embed = input(Fore.CYAN + "🧱 Send as embed? (y/n): ").lower() == "y"
        count = int(input("🔁 Number of messages to send: "))
        delay = float(input("⏱ Delay between messages (in seconds): "))
        thread_count = int(input("🧵 Number of threads to use: "))

        print(Fore.YELLOW + "\n🚀 Starting spam...\n")
        threaded_spam(webhook, msg, count, delay, use_embed, use_random, thread_count)

        clear()
        print(Fore.GREEN + "🎉 Done! All messages sent.")
        print(Fore.CYAN + "\nMade By ryuk.lyy")
        
        repeat = input(Fore.CYAN + "\nDo you want to spam again? (y/n): ").lower()
        if repeat != 'y':
            print(Fore.GREEN + "Exiting... Have a great day!")
            break

if __name__ == "__main__":
    main()
