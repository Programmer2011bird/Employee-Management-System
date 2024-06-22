#-----------------------------#
#           6/22/2024         #
#-----------------------------#
import customtkinter as ctk
import pandas as pd

from typing import Any

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class REMOVE_TAB(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("400x250")
        self.resizable(False, False)
        self.wm_title("Employee management system: REMOVE TAB")

        self.LABEL_EMPLOYEE_NAME: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's name: ")
        self.ENTRY_EMPLOYEE_NAME: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Name")

        self.LABEL_EMPLOYEE_ID: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee's ID: ")
        self.ENTRY_EMPLOYEE_ID: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="ID")

        self.BUTTON_REMOVE_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Remove Employee",
                                                                   command=self.remove_employee, width=300)

        self.LABEL_EMPLOYEE_NAME.grid(row=0, column=0, padx=35, pady=25)
        self.ENTRY_EMPLOYEE_NAME.grid(row=0, column=1, padx=35, pady=25)

        self.LABEL_EMPLOYEE_ID.grid(row=1, column=0, padx=35, pady=25)
        self.ENTRY_EMPLOYEE_ID.grid(row=1, column=1, padx=35, pady=25)

        self.BUTTON_REMOVE_EMPLOYEE.grid(row=2, column=0, padx=35, pady=25, columnspan=2)

    def remove_employee(self) -> None:
        NAME: str = str(self.ENTRY_EMPLOYEE_NAME.get())
        ID: int = int(self.ENTRY_EMPLOYEE_ID.get())

        CSV: pd.DataFrame = pd.read_csv("DATA/EMPLOYEES.csv")
        names: list = list(CSV.get("NAME"))
        ids: list = list(CSV.get("ID"))

        names_and_ids: list[tuple] = list(zip(names, ids))

        for i in range(len(names_and_ids)):
            item: list = list(names_and_ids[i])

            if item[0].lower() == NAME.lower() and item[1] == ID:
                modified_CSV: str | Any = CSV.drop(index=i).to_csv(index=False).replace("\n", "", -1)

                with open("DATA/EMPLOYEES.csv", "w+") as file:
                    file.write(modified_CSV)
