#Setup Logging
import logging
log = logging.getLogger(__name__)

#Python Modules
import sys
import csv
from sympy.geometry import Point, Polygon

class Geofence(object):	

	def __init__(self, coordinates):	
		log.info("Creating geofence...")
		self.polygon = None
		points = []
                for coordinate in coordinates:
                        if len(coordinate) != 2:
                                log.info("Invalid point specificed: " + coordinate)
                                continue
                        p = Point(float(coordinate[0]), float(coordinate[1]), evaluate=False)
                        points.append(p)
                if len(points) == 2:
			p1 = Point(points[0].x, points[0].y, evaluate=False)
			p2 = Point(points[1].x, points[0].y, evaluate=False)
			p3 = Point(points[1].x, points[1].y, evaluate=False)
			p4 = Point(points[0].x, points[1].y, evaluate=False)
			self.polygon = Polygon(p1, p2, p3, p4)
			log.info(self.polygon)
		elif len(points) > 2:
			self.polygon = Polygon(*points)
		log.debug(self.polygon)
		log.info("Geofence established!")

	#Return true if x,y points are inside geofence
	def contains(self, x, y):
		if self.polygon is not None:
			return self.polygon.encloses_point(Point(x,y))
		else:
			return False
