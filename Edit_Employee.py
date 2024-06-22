#-----------------------------#
#           6/22/2024         #
#-----------------------------#
import customtkinter as ctk
from typing import Any
import pandas as pd

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("green")


class EDIT_TAB(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("400x350")
        self.resizable(False, False)
        self.wm_title("Employee management system: EDIT TAB")

        self.LABEL_EMPLOYEE_NAME: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee Name: ")
        self.ENTRY_EMPLOYEE_NAME: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="Name")

        self.LABEL_EMPLOYEE_ID: ctk.CTkLabel = ctk.CTkLabel(self, text="Employee ID: ")
        self.ENTRY_EMPLOYEE_ID: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="ID")

        self.LABEL_SLICER_LINE: ctk.CTkLabel = ctk.CTkLabel(self,
        text="-------------------------------------------------------------------------------")

        self.LABEL_EDIT_EMPLOYEE_NAME: ctk.CTkLabel = ctk.CTkLabel(self, text="New Employee Name: ")
        self.ENTRY_EDIT_EMPLOYEE_NAME: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="New Name")

        self.LABEL_EDIT_EMPLOYEE_ID: ctk.CTkLabel = ctk.CTkLabel(self, text="New Employee ID: ")
        self.ENTRY_EDIT_EMPLOYEE_ID: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="New ID")

        self.LABEL_EDIT_EMPLOYEE_PART: ctk.CTkLabel = ctk.CTkLabel(self, text="New Employee Part: ")
        self.ENTRY_EDIT_EMPLOYEE_PART: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="New part")

        self.LABEL_EDIT_EMPLOYEE_SHIFT: ctk.CTkLabel = ctk.CTkLabel(self, text="New Employee Shift: ")
        self.ENTRY_EDIT_EMPLOYEE_SHIFT: ctk.CTkEntry = ctk.CTkEntry(self, placeholder_text="New Shift")

        self.BUTTON_EDIT_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Edit Employee Info",
                                                                 width=300, command=self.EditEmployee)

        self.LABEL_EMPLOYEE_NAME.grid(row=0, column=0, padx=30, pady=8)
        self.ENTRY_EMPLOYEE_NAME.grid(row=0, column=1, padx=30, pady=8)

        self.LABEL_EMPLOYEE_ID.grid(row=1, column=0, padx=30, pady=8)
        self.ENTRY_EMPLOYEE_ID.grid(row=1, column=1, padx=30, pady=8)

        self.LABEL_SLICER_LINE.grid(row=2, column=0, padx=20, columnspan=2)

        self.LABEL_EDIT_EMPLOYEE_NAME.grid(row=3, column=0, padx=30, pady=8)
        self.ENTRY_EDIT_EMPLOYEE_NAME.grid(row=3, column=1, padx=30, pady=8)

        self.LABEL_EDIT_EMPLOYEE_ID.grid(row=4, column=0, padx=30, pady=8)
        self.ENTRY_EDIT_EMPLOYEE_ID.grid(row=4, column=1, padx=30, pady=8)

        self.LABEL_EDIT_EMPLOYEE_PART.grid(row=5, column=0, padx=30, pady=8)
        self.ENTRY_EDIT_EMPLOYEE_PART.grid(row=5, column=1, padx=30, pady=8)

        self.LABEL_EDIT_EMPLOYEE_SHIFT.grid(row=6, column=0, padx=30, pady=8)
        self.ENTRY_EDIT_EMPLOYEE_SHIFT.grid(row=6, column=1, padx=30, pady=8)

        self.BUTTON_EDIT_EMPLOYEE.grid(row=7, column=0, padx=30, pady=8, columnspan=2)

    def EditEmployee(self) -> None:
        EMPLOYEE_NAME: str = str(self.ENTRY_EMPLOYEE_NAME.get())
        EMPLOYEE_ID: int = int(self.ENTRY_EMPLOYEE_ID.get())
        NEW_EMPLOYEE_NAME: str = str(self.ENTRY_EDIT_EMPLOYEE_NAME.get())
        NEW_EMPLOYEE_ID: str = str(self.ENTRY_EDIT_EMPLOYEE_ID.get())
        NEW_EMPLOYEE_PART: str = str(self.ENTRY_EDIT_EMPLOYEE_PART.get())
        NEW_EMPLOYEE_SHIFT: str = str(self.ENTRY_EDIT_EMPLOYEE_SHIFT.get())

        CSV: pd.DataFrame = pd.read_csv("DATA/EMPLOYEES.csv")
        names: list = list(CSV.get("NAME"))
        ids: list = list(CSV.get("ID"))

        names_and_ids: list[tuple] = list(zip(names, ids))

        for i in range(len(names_and_ids)):
            item: list = list(names_and_ids[i])

            if item[0].lower() == EMPLOYEE_NAME.lower() and item[1] == EMPLOYEE_ID:
                modified_CSV: str | Any = CSV.drop(index=i).to_csv(index=False).replace("\n", "", -1)

                with open("DATA/EMPLOYEES.csv", "w+") as file:
                    file.write(modified_CSV)

                with open("DATA/EMPLOYEES.csv", "a+") as file:
                    file.write(f"{NEW_EMPLOYEE_NAME},{NEW_EMPLOYEE_ID},{NEW_EMPLOYEE_PART},{NEW_EMPLOYEE_SHIFT}\n")
