import subprocess, sys
import tkinter
from tkinter import *
import tkinter as tk
from tkinter import messagebox
import os



def org():
    subprocess.Popen(["powershell.exe",".\Data\Windows10Debloater-master\Windows10DebloaterGUI.ps1"],stdout=sys.stdout)
def stop_up():
    try:
        os.system("net stop wuauserv")
        os.system("net stop bits")
        os.system("net stop dosvc")
        messagebox.showinfo("Attention","sucessfully Disabled_Windows_Update")
    except Exception as e:
        messagebox.showinfo("Attention",e)
def start_up():
    try:
        os.system("net start wuauserv")
        os.system("net start bits")
        os.system("net start dosvc")
        messagebox.showinfo("Attention","sucessfully Enabled_Windows_Update")
    except Exception as e:
        messagebox.showinfo("Attention",e)
def clear_temp():
    try:
        os.system("del /q/f/s %TEMP%\*")
        messagebox.showinfo("Attention","Temp files deleted")
    except Exception as e:
        messagebox.showinfo("Attention",e)

def install_choco():
    try:
        subprocess.Popen(["powershell.exe",".\Data\choco-develop\setup.ps1"],stdout=sys.stdout)
        os.system("choco install chocolateygui")
        messagebox.showinfo("Attention","Installing! Please check the terminal window")
    except Exception as e:
        messagebox.showinfo("Attention",e)

def uninstall_choco():
    try:
        subprocess.run(["powershell.exe","choco uninstall chocolateygui"], capture_output=True)
        os.system("ECHO Y |RMDIR /S C:\ProgramData\chocolatey")
        messagebox.showinfo("Attention","Uninstalled Chocolatey")
    except Exception as e:
        subprocess.run(["powershell.exe","choco uninstall nodejs -y --remove-dependencies"], capture_output=True)
    except Exception as e:
        messagebox.showinfo("Attention",e)

def online_de():
    try:
        subprocess.run(["powershell.exe", "iwr -useb https://git.io/debloat|iex"], capture_output=True)
    except Exception as e:
        messagebox.showinfo("Attention",e)
def uninstall_store():
    try:
        p=messagebox.askyesno("Attention","Are you sure you want to delete MS store")
        if(p==True):
            subprocess.Popen(["powershell.exe",".\\Data\\uninstall_store.ps1"],stdout=sys.stdout)
        if(p==False):
            return;
    except Exception as e:
        messagebox.showinfo("Attention",e)

def reset():
    os.system("systemreset --factoryreset")

def stop_defender():
    try:
        subprocess.run(["powershell", "Set-MpPreference -DisableRealtimeMonitoring $true"], capture_output=True)
    except Exception as e:
        messagebox.showinfo("Attention",e)
def start_defender():
    try:
        subprocess.run(["powershell", "Set-MpPreference -DisableRealtimeMonitoring $false"], capture_output=True)
    except Exception as e:
        messagebox.showinfo("Attention",e)

def chrome():
    messagebox.showinfo("Attension","This requires mordern version of windows with App Installer installed. Check terminal !")
    os.system("winget install -e --id Google.Chrome")

def brave():
    messagebox.showinfo("Attension","This requires mordern version of windows with App Installer installed. Check terminal ! ")
    os.system("winget install -e --id BraveSoftware.BraveBrowser")

def utility():
    messagebox.showinfo("Attension","This requires mordern version of windows with App Installer installed. And this can also install Chocolatey. Check terminal !")
    subprocess.Popen(["powershell.exe",".\Data\Win-Debloat-Tools-main\Win10ScriptGUI.ps1"],stdout=sys.stdout)

def health():
    os.system("DISM /Online /Cleanup-Image /ScanHealth")
def cerdits():
    messagebox.showinfo("Credits","Developed by Mithlesh ,")
def credits():
    messagebox.showinfo("Credits","Developed by Mithlesh \n Instagram - @mithlesh1144 \n Github - github.com/llllmithulllll \n linkedin -www.linkedin.com/in/mithlesh1144/")
def ms():
    messagebox.showinfo("Attension","A new window will open up shortly!")
    os.startfile(".\Data\Microsoft_toolkit_setup\Microsoft Toolkit.exe")

p=subprocess.run(["powershell", "Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned"], capture_output=True)
print(p)
win=Tk()
win.geometry("700x600")
win['background']='#202124'
win.resizable(0,0)
tk.Label(win,text="Mutility",bg='#202124',fg="white",font=('Eras Bold ITC','30')).place(x=275,y=30)
tk.Button(win,text="Enable_Windows_Update",command=start_up,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=50,y=100)
tk.Button(win,text="Disable_Windows_Update",command=stop_up,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=50,y=200)
tk.Button(win,text="Disable_Defender",command=stop_defender,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=50,y=300)
tk.Button(win,text="Enable_Defender",command=start_defender,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=50,y=400)
tk.Button(win,text="Uninstall_MS_Store",command=uninstall_store,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=50,y=500)
tk.Button(win,text="Install_chocolatey",command=install_choco,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=250,y=100)
tk.Button(win,text="Uninstall_chocolatey",command=uninstall_choco,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=250,y=200)
tk.Button(win,text="clear_temp_Files",command=clear_temp,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=250,y=300)
tk.Button(win,text="Offline debloater",bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),command=org,width=25,height=5).place(x=250,y=400)
tk.Button(win,text="Online_Debloater(Latest)",command=online_de,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=250,y=500)
tk.Button(win,text="Reset_Windows",command=reset,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=450,y=100)
tk.Button(win,text="Install_Chrome",command=chrome,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=450,y=200)
tk.Button(win,text="Install_Brave",command=brave,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=450,y=300)
tk.Button(win,text="Download_Applications",command=utility,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=450,y=400)
tk.Button(win,text="Online_System_Restore",command=health,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=5).place(x=450,y=500)
tk.Button(win,text="Credits",command=credits,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=2).place(x=50,y=50)
tk.Button(win,text="MS_Tool_Kit(Activation)",command=ms,bg='#202124',activebackground='#1eacff',fg="white",font=('Eras Medium ITC',10),width=25,height=2).place(x=450,y=50)
win.mainloop()
