#-----------------------------#
#           6/22/2024         #
#-----------------------------#
import customtkinter as ctk
import tkhtmlview as htk
import pandas as pd

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class SHOW_TAB(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("640x385")
        self.resizable(False, False)
        self.wm_title("Employee management system: SHOW TAB")

        self.CSV: pd.DataFrame = pd.read_csv("DATA/EMPLOYEES.csv")
        self.HTML: str = self.CSV.to_html(index=False, border=True)
        self.TABLE: htk.HTMLLabel = htk.HTMLLabel(self, html=f"{self.HTML}")

        self.TABLE.pack()
