import os, time

#BASIC
YW = "\033[1;36;40m"
RD = "\033[1;31;40m"
WT = "\033[1;37;40m"
GR = "\033[1;32;40m"

os.system ('cls')
time.sleep(2)
def banner():
    print (f"{RD}══════════════════╗")
    print (f"{YW}      {GR} _.-;;-._  {RD}╔══ {GR}--------------------- {RD}══╗")
    print (f"{YW}'-..-'{GR}|   ||   | {RD}║ {YW}> {WT}The Windows Activation  {RD}║")
    print (f"{YW}'-..-'{GR}|_.-;;-._| {RD}║   {WT}Tools.                  {RD}║")
    print (f"{YW}'-..-'{GR}|   ||   | {RD}║ {YW}> {GR}Author {YW}: {WT}Keyw00rd       {RD}║")
    print (f"{YW}'-..-'{GR}|_.-''-._| {RD}╚══ {GR}--------------------- {RD}══╝")
    print (f"{RD}══════════════════╝")

def option_yes():
    os.system('cls')
    time.sleep(2)
    banner()
    time.sleep(1)
    print (f" {YW}[ {WT}! {YW}] {WT}Run Tools Windows Activate...")
    time.sleep(1.5)
    print (f" {YW}[ {WT}! {YW}] {WT}Try IPK License...")
    os.system('slmgr.vbs /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    time.sleep(1.5)
    print (f" {YW}[ {WT}! {YW}] {WT}Wait A Few Second...")
    time.sleep(0.5)
    os.system('slmgr.vbs /skms kms.lotro.cc')
    time.sleep(1.5)
    print (f" {YW}[ {WT}! {YW}] {WT}Try ATO...")
    time.sleep(0.5)
    os.system('slmgr.vbs /ato')
    time.sleep(2)
    print (f" {YW}[ {GR}! {YW}] {WT}Windows Has Actived... {WT}")

def option_no():
    os.system('cls')
    time.sleep(2)
    banner()
    time.sleep(2.5)
    print (f" {YW}[ {RD}! {YW}] {WT}Windows Not Actived... {WT}")

def option():
    banner()
    time.sleep(2)
    opt = input(f" {YW}[ {WT}? {YW}] {WT}Run This Tools [ {GR}Y {WT}or {RD}N {WT}] \n{YW}./{WT}windact{YW}@{WT}option{YW}~${WT} ")
    if opt=='y' and 'Y':
      option_yes()
    elif opt=='n' and 'N':
      option_no()
    else:
        print (f" {YW}[ {RD}! {YW}] {WT}Error Option For {RD}> {opt}{WT}")
    time.sleep(0.2)
option()
