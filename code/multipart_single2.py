#!/usr/bin/python
# -*- coding: iso8859_2 -*-

# Prepare the environment
import qgis
from qgis.core import *
import sys

app = QgsApplication([],True, None)
app.setPrefixPath("/usr", True)
app.initQgis()
sys.path.append('/usr/share/qgis/python/plugins')
from processing.core.Processing import Processing
Processing.initialize()
from processing.tools import *

##making the connection with the postgres database
uri = QgsDataSourceURI()
myLayer = "ABSOUYA_p"
myPrimaryKey = "gid"
uri.setConnection("localhost","5432","admin_burkina_v5","postgres","admin")
uri.setDataSource("public",myLayer,"geom","",myPrimaryKey)
vlayer= QgsVectorLayer(uri.uri(),myLayer,"postgres")


# general.runalg("qgis:multiparttosingleparts", vlayer, "tmp.shp")
output = general.runalg("qgis:multiparttosingleparts", vlayer, None)
# from https://docs.qgis.org/2.8/en/docs/user_manual/processing_algs/gdalogr/ogr_conversion.html
# processing.runalg('gdalogr:convertformat', input_layer, format, options, output_layer)
general.runalg('gdalogr:convertformat', output["OUTPUT"], 1, "", "tmp2.geojson")
