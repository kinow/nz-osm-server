#!/usr/bin/env python

from owslib.wms import WebMapService

def main():
	wms = WebMapService('http://maps.nzoss.org.nz/mapserv?template=openlayers&service=wms&request=getCapabilities', version='1.1.0')

	layer_name = 'default'
	layer = wms[layer_name]
	
	img = wms.getmap(
		layers=[layer_name],
		srs=layer.crsOptions[0],
		bbox=(layer.boundingBox[0], layer.boundingBox[1], layer.boundingBox[2], layer.boundingBox[3]),
		size=(500,400),
		format='image/png',
		transparent=False
		)

	with open('nz_oss_wms.png', 'wb') as out:
		out.write(img.read())

if __name__ == '__main__':
	main()