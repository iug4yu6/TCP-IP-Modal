import socket
import colorama

def _():
    try:
        s = socket.socket()

        print(colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.BRIGHT + "DOM Base Starting...")
        print("")
        s1 = input(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[+] IP> ")
        s2 = input(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[+] PORT> ")
        s3 = input(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[+] LISTEN> ")

        s.bind((s1, int(s2)))
        s.listen(int(s3))

        print("")
        print(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT + "Started...")
        print("")

        obj, cr7 = s.accept()
        print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + f"[+] Connected to {cr7}:{s2}")
        print("")

        l = obj.recv(10000)
        ll = l.decode()
        print(ll)
        print("")

        l1 = input(colorama.Fore.LIGHTYELLOW_EX + colorama.Style.BRIGHT + "Enter File Name Of User Data: ")
        a = open(l1, "w")

        a.write(ll)

    except TypeError:
        None

if __name__ == '__main__':
    _()