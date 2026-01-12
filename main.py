import requests
import os

# خلك حاط رابط الويبهوك هنا
WEBHOOK_URL = "https://discord.com/api/webhooks/1460029711366492373/TkCFbmplZ1wbur8GTSGCIHeUFpaqbQ44NbdF1PhZbcxqOZeeonOgB_mSUpI7bvoHNY3i"

def send_message():
    os.system("clear")
    print("=== Send Message to Webhook ===")
    msg = input("set your token: ")

    data = {
        "content": msg
    }

    r = requests.post(WEBHOOK_URL, json=data)

    if r.status_code == 204:
        print("تم الإرسال بنجاح!")
    else:
        print("صار خطأ:", r.status_code)

def main():
    while True:
        os.system("clear")
        print("---- OPTIONS ----")
        print("[1] send")
        print("[0] Exit")
        choice = input("Choose: ")

        if choice == "1":
            send_message()
            input("\nاضغط Enter للرجوع للقائمة...")
        elif choice == "0":
            break
        else:
            print("error!")
            input("prees Enter...")

if __name__ == "__main__":
    main()
