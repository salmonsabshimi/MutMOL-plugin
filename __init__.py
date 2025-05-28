# file MutMOL-plugin/__init__.py
from pymol.plugins import addmenuitemqt

def __init_plugin__(app=None):
    addmenuitemqt('MutMOL', run_plugin_gui)

dialog = None

def run_plugin_gui():
    from pymol.Qt import QtWidgets

    global dialog

    if dialog is None:
        dialog = QtWidgets.QDialog()
        # TO DO fill dialog with widgets 
    
    dialog.show()