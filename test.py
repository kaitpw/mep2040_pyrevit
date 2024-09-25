"""
Finds all schedules in a revit document/project and prepares them to be sent to the Pocketbase database.k

This file is shared on www.revitapidocs.com
For more information visit http://github.com/gtalarico/revitapidocs
"""

from Autodesk.Revit.DB import FilteredElementCollector, ViewSchedule, ViewScheduleExportOptions # not entirely sure how to use this last onbe

import os
import subprocess

#i think __revit__ is a global variableInThe pyrevit environlment
doc = __revit__.ActiveUIDocument.Document
schedules = FilteredElementCollector(doc).OfClass(ViewSchedule)

# add schedules to pocketbase? 