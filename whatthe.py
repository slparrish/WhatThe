#!/usr/bin/env python3
# WhatThe  By: Scott Parrish Ver:0.3 05/09/2023
# A small app to display important information about a system for use when troubleshooting or 
# configuring.
# GitHub: https://github.com/slparrish/WhatThe.git

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog
from hostinfo import HostInfo
import platform


class WhatThe(EasyFrame):
    """Initializes window with a title graphic, 2 text areas for displaying pertinent system information,
    a graphic depicting the operating system for each of the supported systems, a refresh counter with
    label and three buttons with callback functions."""

    counter = 0 # Counter for refreshes.

    def __init__(self,
                title="WhatThe",
                width=700,
                height=600,
                background="white",
                resizable=True): 
               
        super().__init__(title, width, height, background, resizable)
        
        def diskInfo():
            """Callback function for disk info button.  Uses a filedialog to chose the disk the user
            wishes to get info on.  Brings up a messageBox window displaying total disk space, disk 
            used and disk free."""
            pathname = tkinter.filedialog.askdirectory(parent=self) # File dialog to chose disk
            # dirInfo variable to store messageBox text string
            dirInfo = f'Disk Usage: Total:{HostInfo.getDisk(self, pathname)[0]/1000000000:.1f} GB\n\
            Used: {HostInfo.getDisk(self, pathname)[1]/1000000000:.1f} GB\n\
            Free: {HostInfo.getDisk(self, pathname)[2]/1000000000:.1f} GB'
            # display the message box window
            self.messageBox(title=pathname, message=dirInfo, width=30, height=5)

        self.titleImg = PhotoImage(file="whatthe.gif")
        titleLabel = self.addLabel("", row=0, column=0, columnspan=2, sticky="NSEW")
        titleLabel["image"] = self.titleImg

        # General Group
        # Text area containing general system information.  Default text set to show refresh
        # button working as intended.
        genString = "Default text... Hit the refresh\nbutton to show correct info."
        self.genOutputArea = self.addTextArea("", row=1, column=0, width=5, height=5)
        # Sets default text above.  Hitting refresh once will populate genString with the
        # proper information.
        self.genOutputArea.setText(genString)

        # Image group
        self.imgfile = f'{platform.system().lower()}.gif' # (windows/linux/darwin) converted to string for gif filename
        self.imageText = self.addLabel(f'Image for {platform.system()}', row=1, column=1, rowspan=1, sticky="NEW")
        imageLabel = self.addLabel("", row=1, column=1, sticky="SEW") 
        self.image = PhotoImage(file=self.imgfile)
        imageLabel["image"] = self.image

        # Networking group
        self.netLabel = self.addLabel('Networking:', row=3, column=0, sticky="SW")
        self.netOutputArea = self.addTextArea("", row=4, column=0, width=5, height=5)
        netString =  f'Loopback: 127.0.0.1\nIPv4: {HostInfo.getIP2(self)}'
        self.netOutputArea.setText(netString)

        # Refresh group
        # Sets up readonly text field and label to display number of times refresh clicked (counter)
        self.refreshLabel = self.addLabel('Refreshes:', row=3, column=1, sticky="NSEW")
        self.refreshOutField = self.addTextField("", row=4, column=1, rowspan=1, width=3, sticky="N", state="readonly")
        self.refreshOutField.setText(self.counter)

        def refresh():
            """Callback function for the refresh button.  Refreshes all text in the two text areas.
            These areas are intended to display information that can change as the user makes 
            adjustments to their system.  The refresh functionality is demostrated by the default 
            genString text being changed to values from HostInfo functions after hitting the refresh
            button."""
            genString = f'Hostname: {HostInfo.getHostname(self)}\nSystem: {HostInfo.system(self)}\nVersion: {HostInfo.version(self)}'
            netString =  f'Loopback: 127.0.0.1\nIPv4: {HostInfo.getIP2(self)}'
            self.genOutputArea.setText(genString) # Writes text to text areas
            self.netOutputArea.setText(netString) #     ""
            self.counter += 1
            self.refreshOutField.setText(self.counter) # Displays times refresh clicked
            
        # Button Panel with 3 buttons, Refresh, Disk Info and Exit.  Each has corresponding callback
        # functions.  Disk info will bring up a dialog to select the disk to get info on and then 
        # display the disk usage stats in a pop up window.
        buttonPanel = self.addPanel(row=5, column=0, columnspan=2, background="white")
        buttonPanel.addButton('Refresh', row=0, column=0, command=refresh)  # refreshes text in text boxes
        buttonPanel.addButton('Disk Info', row=0, column=1, command=diskInfo)
        buttonPanel.addButton('Exit', row=0, column=2, command=exit)
    



def main() -> None:

    root = WhatThe()
    root.mainloop()


if __name__ == '__main__':
    main()


