# this sets up the environment for usingThe revitpythonshell. the importnat thing thqt it creates/gets is the uidoc which ia rewuired param for one the of the filterelementcollector class which we ill use to get all ofThe schedules
# it may also make sense to changeThis to not getThe acivedocumne but maybe a listOf other documents, depends on wehher wee will runAny production scripts fromThis shell
# these commands get executed in the current scope
# of each new shell (but not for canned commands)
#pylint: disable=all
import clr
clr.AddReferenceByPartialName('PresentationCore')
clr.AddReferenceByPartialName('AdWindows')
clr.AddReferenceByPartialName("PresentationFramework")
clr.AddReferenceByPartialName('System')
clr.AddReferenceByPartialName('System.Windows.Forms')

from Autodesk.Revit import DB
from Autodesk.Revit import UI #these dont seem to be necessary because the ui doesnt need to be accessed to add a button to. lookMoreInto the runtime environment of the batch processor to see whats up.

import Autodesk.Windows as aw

# creates variables for selected elements in global scope
# e1, e2, ...
max_elements = 5
gdict = globals()
uiapp = __revit__
uidoc = uiapp.ActiveUIDocument
if uidoc:
    doc = uiapp.ActiveUIDocument.Document
    selection = [doc.GetElement(x) for x in uidoc.Selection.GetElementIds()]
    for idx, el in enumerate(selection):
        if idx < max_elements:
            gdict['e{}'.format(idx+1)] = el
        else:
            break

# alert function
def alert(msg):
    TaskDialog.Show('RPS', msg)

# quit function
def quit():
    __window__.Close()