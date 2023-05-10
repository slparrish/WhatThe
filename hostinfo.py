
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
