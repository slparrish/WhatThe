#!/usr/bin/env python3
# WhatThe  By: Scott Parrish Ver:0.2 04/28/2023
# A small app to display important information about a system for use when troubleshooting or 
# configuring.
# GitHub: https://github.com/slparrish/WhatThe.git

from breezypythongui import EasyFrame
from tkinter import PhotoImage
# from tkinter.font import Font
# import sys
import platform
import socket
import shutil

class WhatThe(EasyFrame):
    """Initializes window"""
    
    def __init__(self,
                title="WhatThe",
                width=800,
                height=600,
                background="white",
                resizable=True): 
               
        super().__init__(title, width, height, background, resizable)

        self.imgfile = f'{platform.system().lower()}.gif'

        # Potentially panelize groups
        # General Group
        self.genLabel = self.addLabel('General Information:', row=0, column=0, sticky="SW")
        self.genOutputArea = self.addTextArea("", row=1, column=0, width=5, height=5)
        imageLabel = self.addLabel("", row=1, column=1, sticky="NSEW") 
        self.image = PhotoImage(file=self.imgfile)
        imageLabel["image"] = self.image
        # Networking group
        self.netLabel = self.addLabel('Networking:', row=2, column=0, sticky="SW")
        self.netOutputArea = self.addTextArea("", row=3, column=0, width=5, height=5)

        self.addButton('Refresh', row=3, column=1)  # need function to refresh info in HostInfo
        self.addButton('Exit', row=4, column=1, command=exit)
    
    def setImage(self, imgfile):
        self.imgfile = imgfile


# HostInfo() class to gather info about our machine    
# To do: potentially move some methods into constructor, add more info
# 
class HostInfo(): 
    """Handles gathering host info"""
    def __init__(self) -> None:
        pass
      
    def getHostname(self):
        """get hostname from the more portable platform module.  os.uname() isnt as 
        portable. Returns second element of uname"""
        return platform.uname()[1]
    
    def version(self):
        return platform.version()
    
    def system(self):
        return platform.system()
    
    def getIP(self):
        """Get IPv4 address of the host"""
        hostname = socket.gethostname()     # should be the same as from getHostname() above
        ip_addr = socket.gethostbyname(hostname)
        return ip_addr
    
    def getIP2(self):
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
        return host_ip
    
    def getDisk(self, path: str):
        return shutil.disk_usage(path)



def main() -> None:
    root = WhatThe()
    myHost = HostInfo()
    root.setImage("mac.gif")
    genString = f'Hostname: {myHost.getHostname()}\n\
System: {myHost.system()}\n\
Version: {myHost.version()}\n\
Disk Usage: Total:{myHost.getDisk("/")[0]/1000000000:.1f} GB \n\
            Used: {myHost.getDisk("/")[1]/1000000000:.1f} GB\n\
            Free: {myHost.getDisk("/")[2]/1000000000:.1f} GB'
    # root.image = PhotoImage(file="mac.gif")
    # root.image = PhotoImage(file="mac.gif")
    # imageLabel["Image"] = root.image
    root.genOutputArea.setText(genString)
    netString = f'IPv4 Address: {myHost.getIP2()}'
    root.netOutputArea.setText(netString)
    
    
    root.mainloop()


if __name__ == '__main__':
    main()


