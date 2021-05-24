import sys

def get_python_version():
    major=sys.version_info.major
    minor=sys.version_info.minor
    micro=sys.version_info.micro
    releaselevel=sys.version_info.releaselevel
    serial=sys.version_info.serial
    version=f"{major}.{minor}.{micro}"
    if releaselevel!="final":
        version+=f"-{releaselevel}.{serial}"
    return version

PLUGIN_METADATA={
    "id":"python",
    "version":get_python_version(),
    "name":f"Python {get_python_version()}",
    "description":f"Python {sys.version}",
    "link":"https://python.org"
}
