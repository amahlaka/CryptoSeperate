"""
Simply tool to split bulk wallets.

Save the bulk wallet text from:
https://walletgenerator.net
https://ryepdx.github.io/ethaddress.org/#/bulkWallets
or similar sites that providfe it in format: id, publickey, privatekey
Every wallet has to be on its own line, save to file wallets.txt
Place the script and wallets.txt in same folder and run this script

Made by Arttu Mahlakaarto
Feel free to donate:
BTC: 1PhfraqhnPt9B91WE4Ve5FVkJrxEiyenu1
ETH: 0xa34ad58c8213c2e473f2faf0ea521c59e9400915
ZEC: t1PYTokShkUHCUv6oeqwwHizXbjj7UQnX5c
"""
import os
import errno

def failure(code):
    if(code == 1):
        errormsg = "Could not find file wallets.txt"
        errormsg += "\nPlease check that file exists and try again"
    errlog = open('error.log', 'w')
    errlog.write(errormsg)
    errlog.close()
    print(errormsg)
    input("Press Enter to exit")
    exit()

if(not os.path.isfile('wallets.txt')):
    failure(1)

f = open('wallets.txt')  # Open the wallets.txt file
listA = []
for line in iter(f):
    listA.append(line)  # Turn it into a list
f.close()

for i, v in enumerate(listA):  # Process each wallet individually
    os.system("mkdir Wallet-"+str(i))  # Make folder Wallet-#
    fa = v.replace('"', "").replace("\n", "").split(',')  # Process public key
    fileb = open('Wallet-'+str(i)+'\\public.txt', 'w')
    fileb.write("Public key for Wallet"+str(i)+":\n"+fa[1])
    fileb.close()
    filea = open('Wallet-'+str(i)+'\\private.txt', 'w')
    filea.write("Private key for Wallet-"+str(i)+":\n"+fa[2])
    filea.close()

guide = open('Instructions.txt', 'w')
gt = "To Recieve coins, use your public address\n"
gt += "NEVER share your private key until you are ready to spend the coins\n"
gt += "Anyone with your private key can withdraw your money, so keep it safe\n"
gt += "Feel free to donate:\n"
gt += "BTC: 1PhfraqhnPt9B91WE4Ve5FVkJrxEiyenu1\n"
gt += "ETH: 0xa34ad58c8213c2e473f2faf0ea521c59e9400915\n"
gt += "ZEC: t1PYTokShkUHCUv6oeqwwHizXbjj7UQnX5c\n"
guide.write(gt)
guide.close()
os.remove('wallets.txt')
