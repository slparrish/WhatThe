#!/usr/bin/env python3
# WhatThe  By: Scott Parrish Ver:0.2 04/28/2023
# A small app to display important information about a system for use when troubleshooting or 
# configuring.
# GitHub: https://github.com/slparrish/WhatThe.git

from breezypythongui import EasyFrame
from tkinter import PhotoImage
import tkinter.filedialog
from hostinfo import HostInfo
import platform


class WhatThe(EasyFrame):
    """Initializes window"""
    counter = 0
    def __init__(self,
                title="WhatThe",
                width=700,
                height=600,
                background="white",
                resizable=True): 
               
        super().__init__(title, width, height, background, resizable)
        
        def diskInfo():
            pathname = tkinter.filedialog.askdirectory(parent=self)
            # print(pathname)
            dirInfo = f'Disk Usage: Total:{HostInfo.getDisk(self, pathname)[0]/1000000000:.1f} GB\n\
            Used: {HostInfo.getDisk(self, pathname)[1]/1000000000:.1f} GB\n\
            Free: {HostInfo.getDisk(self, pathname)[2]/1000000000:.1f} GB'
            self.messageBox(title=pathname, message=dirInfo, width=30, height=5)


        self.imgfile = f'{platform.system().lower()}.gif'
        self.titleImg = PhotoImage(file="whatthe.gif")
        titleLabel = self.addLabel("", row=0, column=0, columnspan=2, sticky="NSEW")
        titleLabel["image"] = self.titleImg

        # General Group
        genString = "Default text... Hit the refresh\nbutton to show correct info."
        self.genOutputArea = self.addTextArea("", row=1, column=0, width=5, height=5)
        self.genOutputArea.setText(genString)

        # Image group
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
        self.refreshLabel = self.addLabel('Refreshes:', row=3, column=1, sticky="NSEW")
        self.refreshOutField = self.addTextField("", row=4, column=1, rowspan=1, width=3, sticky="N", state="readonly")
        self.refreshOutField.setText(self.counter)

        def refresh():
            genString = f'Hostname: {HostInfo.getHostname(self)}\nSystem: {HostInfo.system(self)}\nVersion: {HostInfo.version(self)}'
            netString =  f'Loopback: 127.0.0.1\nIPv4: {HostInfo.getIP2(self)}'
            self.genOutputArea.setText(genString)
            self.netOutputArea.setText(netString)
            self.counter += 1
            self.refreshOutField.setText(self.counter)
            

        buttonPanel = self.addPanel(row=5, column=0, columnspan=2, background="white")
        buttonPanel.addButton('Refresh', row=0, column=0, command=refresh)  # refreshes text in text boxes
        buttonPanel.addButton('Disk Info', row=0, column=1, command=diskInfo)
        buttonPanel.addButton('Exit', row=0, column=2, command=exit)
    



def main() -> None:
    root = WhatThe()

    root.mainloop()


if __name__ == '__main__':
    main()


