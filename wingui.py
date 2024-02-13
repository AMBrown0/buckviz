# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:17:42 2020

@author: andy
"""


from pywinauto.application import Application
app = Application().start("notepad.exe")

app.UntitledNotepad.menu_select("Help->About Notepad")
app.AboutNotepad.OK.click()
app.UntitledNotepad.Edit.type_keys("pywinauto Works!", with_spaces = True)