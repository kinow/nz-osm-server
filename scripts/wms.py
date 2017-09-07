#!/usr/bin/env python

from owslib.wms import WebMapService

def main():
	wms = WebMapService('http://maps.nzoss.org.nz/mapserv?template=openlayers&service=wms&request=getCapabilities', version='1.3.0')

	layer = 'default'
	crs = wms[layer].crsOptions
	print(crs)
	bbox = wms[layer].boundingBox
	print(bbox)

if __name__ == '__main__':
	main()
