# MutMOL-plugin/mutmol_gui.py

from pymol.Qt import QtWidgets
from pymol import cmd
import requests

dialog = None 

def pdb_to_uniprot(pdb_id):
    pdb = pdb_id.lower()
    url = f"https://www.ebi.ac.uk/pdbe/api/mappings/uniprot/{pdb}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    entry = data.get(pdb.upper(), {})
    uniprot_dict = entry.get('UniProt', {})
    return list(uniprot_dict.keys())


def run_plugin_gui():

    global dialog

    if dialog is None:
        dialog = QtWidgets.QDialog()
        dialog.setWindowTitle("MutMOL Plugin")
        layout = QtWidgets.QVBoxLayout(dialog)

     # Text entry for PDB 
        layout.addWidget(QtWidgets.QLabel("PDB ID:"))
        pdb_input = QtWidgets.QLineEdit()
        layout.addWidget(pdb_input)
    
    dialog.show()
