# -*- coding: utf-8 -*-
"""
Created on Fri May 29 16:06:33 2020

@author: andy
"""

import win32com.client as win32

from datetime import datetime
outlook = win32.Dispatch('outlook.application')   #get a reference to Outlook
mail = outlook.CreateItem(0)                      #create a new mail item
mail.To = 'executives@bigcompany.com'
#mail.From = "Andyb@accelerate-poeple.co.uk"
mail.Subject = 'Finance Status Report '+datetime.today().strftime('%m/%d')  
mail.Display()
#put today's date in subject line
mail._oleobj_.Invoke(*(64209, 0, 8, 0, 'AndyB@accelerate-people.co.uk'))
mail.SentOnBehalfOfName = 'AndyB@accelerate-people.co.uk' 