#!/usr/bin/python
# -*- coding: iso8859_2 -*-

# Prepare the environment
import sys
from qgis.core import *
from PyQt4.QtGui import *
import qgis
import PyQt4.Qsci

# app = QApplication([])
# QgsApplication.setPrefixPath("/usr", True)
# QgsApplication.initQgis()
#
# # Prepare processing framework
# sys.path.append('/usr/share/qgis/python/plugins')
# from processing.core.Processing import Processing
# Processing.initialize()
# from processing.tools import *


app = QgsApplication([],True, None)
app.setPrefixPath("/usr", True)
app.initQgis()
sys.path.append('/usr/share/qgis/python/plugins')
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *

# reading from database
# uri = QgsDataSourceURI()
# # set host name, port, database name, username and password
# uri.setConnection("localhost", "5432", "settlements", "postgres", "admin")

uri = QgsDataSourceURI()
# assign this information before you query the QgsCredentials data store
uri.setConnection("localhost", "5432", "settlements", None, None)
connInfo = uri.connectionInfo()

(success, user, passwd) = QgsCredentials.instance().get(connInfo, None, None)

if success:
    uri.setPassword(passwd)
    uri.setUsername(user)
    uri.setDataSource("public", "est", "geom")
    LYR = QgsVectorLayer(uri.uri(), "est", "postgres")

    # Work with the layer (E.g. get feature count...)
    len( list( LYR.getFeatures() ) )

# layerInput = QgsVectorLayer(uri.uri(), "est", "postgres")

# Run the algorithm
# layerInput = QgsVectorLayer('world_adm0.shp', 'test', 'ogr')
general.runalg("qgis:multiparttosingleparts", LYR, "tmp.shp")
##running multipart to singlepart
# processing.runalg('qgis:multiparttosingleparts', layerInput, 0, "tmp.shp")


# Exit applications
QgsApplication.exitQgis()
QApplication.exit()
