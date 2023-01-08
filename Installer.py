import requests
import os
from tkinter import messagebox
os.mkdir("OnlineBanking")
with open("bankaccounts.py", "w") as bankAccMN: bankAccMN.write(requests.get("https://github.com/Viswas-Programs/ParodyBank/raw/v5/bankaccounts.py", timeout=10).content.decode(encoding='utf-8'))
with open("bankaccountsdatabase.py", "w") as bankAccDbMN: bankAccDbMN.write(requests.get("https://github.com/Viswas-Programs/ParodyBank/raw/v5/bankaccountdatabase.py", timeout=10).content.decode(encoding='utf-8'))
messagebox.showinfo("Installation successful", "Installation completed successfully. check console for possible errors")
