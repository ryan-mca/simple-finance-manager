"""Holds all the GUI stuff
"""
# --- Imports ---
from os.path import exists
from os import mkdir
import configparser as confp
import customtkinter as ctk
from appdirs import user_config_dir

# --- Constants
CONFIG_DIR = user_config_dir("simple-finance-manager", False)
win = ctk.CTk()

# --- CustomTKinter stuff
win.title("Simple Finance Manager")
win.geometry("500x350")
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

def main():
    """Runs the login screen
    """
    win.mainloop()

def first_time_setup():
    """Checks things like if files exist and creates default files
    """
    if not exists(CONFIG_DIR):
        mkdir(CONFIG_DIR)
    if not exists(f"{CONFIG_DIR}//settings.conf"):
        with open(f"{CONFIG_DIR}//settings.conf", 'w', encoding="utf-8") as file:
            confp.ConfigParser().write(file)



if __name__ == "__main__":
    main()
