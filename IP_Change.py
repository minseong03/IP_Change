import sys
import os
import socket
import re
import uuid
import time

def main():
    HOST_NAME = socket.gethostname()
    HOST_IP = socket.gethostbyname(HOST_NAME)

    os.system('cls')

    print(" ")
    print("1- 현재 MAC주소와 IP주소 보기")
    print(" ")
    print("2- 자동 할당")
    print(" ")
    print("3- 수동 할당")
    print(" ")
    print("4- 나가기")
    print(" ")
    Menu = input("메뉴를 선택하십시오 ==> ")

    if not Menu: # null check
        os.system('cls')
        os.system('python IP_Change.py')

    if Menu == ('1') : # 현재 MAC 주소와 IP 주소를 보여줌
        print(" ")
        print("현재 MAC 주소 : ", end="")
        print(':'.join(re.findall('..', '%012X' % uuid.getnode())))
        print("현재 IP 주소 : ", end="")
        print(HOST_IP)
        print(" ")
        restart = input('press any key to continue')
        os.system('cls') 
        os.system('python IP_Change.py')

    if Menu == ('2') : # DHCP
        print(" ")
        print("1- 무선 LAN 연결")
        print("2- 이더넷 연결")
        print(" ")
        Connection_Type = input("연결 타입 : ")
        if Connection_Type == ('1') : # 무선 LAN
            print(" ")
            os.system('netsh -c int ip set address name="Wi-Fi" source=dhcp')
            restart = input("press any key to continue")
            os.system('cls')
            os.system('python IP_Change.py')
        if Connection_Type == ('2') : # 이더넷
            print(" ")
            os.system('netsh -c int ip set address name="이더넷" source=dhcp')
            restart = input("press any key to continue")
            os.system('cls')
            os.system('python IP_Change.py')

    if Menu == ('3'): # Static
        print(" ")
        print("1- 무선 LAN 연결")
        print("2- 이더넷 연결")
        print(" ")
        Connection_Type = input("연결 타입 : ")
        if Connection_Type == ('1') :
            print(" ")
            print("ex) 아이피: xxx.xxx.xxx.xxx  서브넷 마스크: xxx.xxx.xxx.x  게이트웨이: xxx.xxx.x.x  DNS: xxx.xxx.xxx.x")
            print('\n')
            Static_IP = input("아이피 입력 : ")
            Subnet_Mask = input("서브넷 마스크 입력 : ")
            Gateway = input("게이트웨이 입력 : ")
            os.system('netsh -c int ip set address name="Wi-Fi" source=static addr={0} mask={1} gateway={2} gwmetric=0'.format(Static_IP, Subnet_Mask, Gateway))
            DNS = input("기본 DNS 입력: ")
            os.system('netsh -c int ip set dns name="Wi-Fi" source=static addr={0} register=PRIMARY'.format(DNS))
            DNS = input("보조 DNS 입력: ")
            os.system('netsh -c int ip add dns name="Wi-Fi" addr={0} index=2'.format(DNS))
            print("done")
        if Connection_Type == ('2') :
            print(" ")
            print("ex) 아이피: xxx.xxx.xxx.xxx  서브넷 마스크: xxx.xxx.xxx.x  게이트웨이: xxx.xxx.x.x  DNS: xxx.xxx.xxx.x")
            print('\n')
            Static_IP = input("아이피 입력 : ")
            Subnet_Mask = input("서브넷 마스크 입력 : ")
            Gateway = input("게이트웨이 입력 : ")
            os.system('netsh -c int ip set address name="이더넷" source=static addr={0} mask={1} gateway={2} gwmetric=0'.format(Static_IP, Subnet_Mask, Gateway))
            DNS = input("기본 DNS 입력: ")
            os.system('netsh -c int ip set dns name="이더넷" source=static addr={0} register=PRIMARY'.format(DNS))
            DNS = input("보조 DNS 입력: ")
            os.system('netsh -c int ip add dns name="이더넷" addr={0} index=2'.format(DNS))
            print("done")

    if Menu == ('4') :
        sys.exit()

if __name__=='__main__':
    main()