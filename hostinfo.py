# hostinfo.py  By: Scott Parrish Ver: 0.2 05/09/2023
# Module to gather information about the local computer.
import platform
import socket
import shutil

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
        """returns version of operating system"""
        return platform.version()
    
    def system(self):
        """Returns Operating system name (Windows, Linux, Darwin for Mac)"""
        return platform.system()
    
    # Not as reliable as below but does not ping the network or require a network connection.
    def getIP(self):
        """Get IPv4 address of the host, not always reliable"""
        hostname = socket.gethostname()     # should be the same as from getHostname() above
        ip_addr = socket.gethostbyname(hostname)
        return ip_addr
    
    # Reliably returns the machine IP but briefly connects to google DNS
    def getIP2(self):
        """Reliably returns the machine IP but briefly connects to google DNS on port 80"""
        s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host_ip = s.getsockname()[0]
        s.close()
        return host_ip
    
    def getDisk(self, path: str):
        """Returns a tuple with [0] total disk space, [1] disk used, and [2] disk free."""
        return shutil.disk_usage(path)
