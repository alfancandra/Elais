#!C:\Users\alfan\AppData\Local\Programs\Python\Python38\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'autosub3==0.1.0','console_scripts','autosub'
__requires__ = 'autosub3==0.1.0'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('autosub3==0.1.0', 'console_scripts', 'autosub')()
    )
