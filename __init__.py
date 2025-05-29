# file MutMOL-plugin/__init__.py
import os, sys
this_dir = os.path.dirname(__file__)
if this_dir not in sys.path:
    sys.path.insert(0, this_dir)

from pymol.plugins import addmenuitemqt
from mutmol_gui import run_plugin_gui

def __init_plugin__(app=None):
    addmenuitemqt('MutMOL', run_plugin_gui)
    print("MutMOL plugin initialised")  

dialog = None

