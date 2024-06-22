#-----------------------------#
#           6/22/2024         #
#-----------------------------#
import customtkinter as ctk

import Add_Employee
import Remove_Employee
import Edit_Employee
import Show_Employee

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Application(ctk.CTk):
    def __init__(self) -> None:
        super().__init__()

        self.geometry("400x280")
        self.resizable(False, False)
        self.wm_title("Employee management system")

        self.LABEL_ADD_EMPLOYEE: ctk.CTkLabel = ctk.CTkLabel(self, text="Add An Employee")
        self.BUTTON_ADD_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Add Employee Page",
                                                                command=self.Add_Employee_Tab)

        self.LABEL_REMOVE_EMPLOYEE: ctk.CTkLabel = ctk.CTkLabel(self, text="Remove An Employee")
        self.BUTTON_REMOVE_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Remove Employee Page",
                                                                   command=self.Remove_Employee_Tab)

        self.LABEL_EDIT_EMPLOYEE: ctk.CTkLabel = ctk.CTkLabel(self, text="Edit An Employee Information")
        self.BUTTON_EDIT_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Edit Employee Page",
                                                                 command=self.Edit_Employee_Tab)

        self.LABEL_SHOW_EMPLOYEE: ctk.CTkLabel = ctk.CTkLabel(self, text="Show all Employees info")
        self.BUTTON_SHOW_EMPLOYEE: ctk.CTkButton = ctk.CTkButton(self, text="Show Employees info",
                                                                 command=self.Show_Employee_Tab)

        self.LABEL_ADD_EMPLOYEE.grid(row=0, column=0, pady=20, padx=20)
        self.BUTTON_ADD_EMPLOYEE.grid(row=0, column=1, pady=20, padx=20)

        self.LABEL_REMOVE_EMPLOYEE.grid(row=1, column=0, pady=20, padx=20)
        self.BUTTON_REMOVE_EMPLOYEE.grid(row=1, column=1, pady=20, padx=20)

        self.LABEL_EDIT_EMPLOYEE.grid(row=2, column=0, pady=20, padx=20)
        self.BUTTON_EDIT_EMPLOYEE.grid(row=2, column=1, pady=20, padx=20)

        self.LABEL_SHOW_EMPLOYEE.grid(row=3, column=0, pady=20, padx=20)
        self.BUTTON_SHOW_EMPLOYEE.grid(row=3, column=1, pady=20, padx=20)

    def Add_Employee_Tab(self) -> None:
        TAB_ADD: Add_Employee.ADD_TAB = Add_Employee.ADD_TAB()
        TAB_ADD.mainloop()

    def Remove_Employee_Tab(self) -> None:
        REMOVE_TAB: Remove_Employee.REMOVE_TAB = Remove_Employee.REMOVE_TAB()
        REMOVE_TAB.mainloop()

    def Edit_Employee_Tab(self) -> None:
        EDIT_TAB: Edit_Employee.EDIT_TAB = Edit_Employee.EDIT_TAB()
        EDIT_TAB.mainloop()

    def Show_Employee_Tab(self) -> None:
        SHOW_TAB: Show_Employee.SHOW_TAB = Show_Employee.SHOW_TAB()
        SHOW_TAB.mainloop()


if __name__ == "__main__":
    App = Application()
    App.mainloop()
