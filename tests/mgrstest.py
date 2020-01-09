# -*- coding: utf-8 -*-
"""
***************************************************************************
    mgrstest.py
    ---------------------
    Date                 : August 2016, October 2019
    Author               : Alex Bruy, Planet Federal
    Copyright            : (C) 2016 Boundless, http://boundlessgeo.com
                         : (C) 2019 Planet Inc, https://planet.com
***************************************************************************
*                                                                         *
*   This program is free software; you can redistribute it and/or modify  *
*   it under the terms of the GNU General Public License as published by  *
*   the Free Software Foundation; either version 2 of the License, or     *
*   (at your option) any later version.                                   *
*                                                                         *
***************************************************************************
"""
__author__ = 'Planet Federal'
__date__ = 'October 2019'
__copyright__ = '(C) 2019 Planet Inc, https://planet.com'

# This will get replaced with a git SHA1 when you do a git archive
__revision__ = '$Format:%H$'

import os
import unittest
import csv
import logging

from mgrspy import mgrs

LOG_LEVEL = os.environ.get('PYTHON_LOG_LEVEL', 'INFO').upper()
FORMAT = "%(levelname)s [%(name)s:%(lineno)s  %(funcName)s()] %(message)s"
logging.basicConfig(level=LOG_LEVEL, format=FORMAT)
log = logging.getLogger(__name__)


class MgrsTest(unittest.TestCase):

    def setUp(self):
        log.debug('\n\n\n--------------- {0}'.format(self.id()))

    def testNorthPoleCoordinates(self):
        self.assertEqual(mgrs.toMgrs(86.598, -156.507), '  YYL4939146492')

        lat, lon = mgrs.toWgs('  YYL4939146492')
        self.assertAlmostEqual(lat, 86.59800323153932)
        self.assertAlmostEqual(lon, -156.50695504226658)

        lat, lon = mgrs.toWgs('    YYL4939146492')
        self.assertAlmostEqual(lat, 86.59800323153932)
        self.assertAlmostEqual(lon, -156.50695504226658)

        lat, lon = mgrs.toWgs('YYL4939146492')
        self.assertAlmostEqual(lat, 86.59800323153932)
        self.assertAlmostEqual(lon, -156.50695504226658)

    def testSouthPoleCoordinates(self):
        self.assertEqual(mgrs.toMgrs(-88.52, -66.49), '  AYN4931665550')

        lat, lon = mgrs.toWgs('  AYN4931665550')
        self.assertAlmostEqual(lat, -88.51999757416547)
        self.assertAlmostEqual(lon, -66.49017323008184)

        lat, lon = mgrs.toWgs('    AYN4931665550')
        self.assertAlmostEqual(lat, -88.51999757416547)
        self.assertAlmostEqual(lon, -66.49017323008184)

        lat, lon = mgrs.toWgs('AYN4931665550')
        self.assertAlmostEqual(lat, -88.51999757416547)
        self.assertAlmostEqual(lon, -66.49017323008184)

    def testSpecialCases(self):
        self.assertEqual(mgrs.toMgrs(-90, 180), '  BAN0000000000')
        lat, lon = mgrs.toWgs('BAN0000000000')
        self.assertAlmostEqual(lat, -90.0)
        self.assertAlmostEqual(lon, 0.0)

    def testWgsCoordinatesCorners(self):
        mgrs_txt = mgrs.toMgrs(11.43995185735899, 23.601038987469863)
        self.assertEqual(mgrs_txt, '34PGT8380865904')

    def testWgsCoordinates(self):
        # to MGRS
        self.assertEqual(mgrs.toMgrs(42.0, -93.0), '15TVG0000049776')
        self.assertEqual(mgrs.toMgrs(42.0, -93.0, 5), '15TVG0000049776')
        self.assertEqual(mgrs.toMgrs(42.0, -93.0, 3), '15TVG000497')
        self.assertEqual(mgrs.toMgrs(42.0, -93.0, 0), '15TVG')

        self.assertEqual(mgrs.toMgrs(38.9072, -77.0369), '18SUJ2338308450')
        self.assertEqual(mgrs.toMgrs(39.9526, -75.1652), '18SVK8588822509')
        self.assertEqual(mgrs.toMgrs(37.6539, 44.0062), '38SMG1233767880')

        # to WGS
        lat, lon = mgrs.toWgs('15TVG0000049776')
        self.assertAlmostEqual(lat, 41.99364855788585)
        self.assertAlmostEqual(lon, -94.20734290469866)

        lat, lon = mgrs.toWgs('15TVG000497')
        self.assertAlmostEqual(lat, 41.99296420261856)
        self.assertAlmostEqual(lon, -94.20732996948512)

        lat, lon = mgrs.toWgs('15TVG')
        self.assertAlmostEqual(lat, 41.545413660388625)
        self.assertAlmostEqual(lon, -94.19896628704795)

        lat, lon = mgrs.toWgs('18SUJ2338308450')
        self.assertAlmostEqual(lat, 38.90719314018781)
        self.assertAlmostEqual(lon, -77.03690158268294)

        lat, lon = mgrs.toWgs('18SVK8588822509')
        self.assertAlmostEqual(lat, 39.95259667537377)
        self.assertAlmostEqual(lon, -75.16520969399382)

        lat, lon = mgrs.toWgs('38SMG1233767880')
        self.assertAlmostEqual(lat, 37.65389907949628)
        self.assertAlmostEqual(lon, 44.00619523636414)

        lat, lon = mgrs.toWgs('4Q FJ 1234 6789')
        self.assertAlmostEqual(lat, 21.409796984165713)
        self.assertAlmostEqual(lon, -157.91612940829197)

    def testPopulatedPlaces(self):
        if os.environ.get('MGRSPY_TEST_PLACES', None) is None:
            return

        # Populated places from Natural Earth project (~2017, 1200+ places)
        with open('populated-places.csv') as populated_places:
            places = [p for p in csv.reader(populated_places, delimiter='\t')]

        lineno = 1
        for place in places:
            name = place[0]
            if name == 'NAMEASCII' or name.startswith('#'):
                log.warning('#{0} skipping'.format(lineno))
                lineno += 1
                continue
            lat = float(place[1])
            lon = float(place[2])
            mgr = place[3]
            zone = int(place[4])
            hemi = place[5].upper()
            easting = float(place[6])
            northing = float(place[7])
            epsg = int(place[8])

            log.warning('#{0} {1} {2} {3} {4} {5} {6} {7} {8} {9}'.format(
                lineno, name, lat, lon, mgr, zone,
                hemi, easting, northing, epsg))

            # verify UTM zone/hemisphere, EPSG code
            hemi2, zone2, epsg2 = mgrs._epsgForWgs(lat, lon)
            self.assertEqual(hemi2, hemi)
            self.assertEqual(zone2, zone)
            self.assertEqual(epsg2, epsg)

            epsg3 = mgrs._epsgForUtm(0 if zone == 61 else zone, hemi)
            self.assertEqual(epsg3, epsg)

            # to MGRS
            self.assertEqual(mgrs.toMgrs(lat, lon).strip(), mgr)

            # # to WGS
            lat2, lon2 = mgrs.toWgs(mgr)
            # Test to only 4 places, as list generated by GeographicLib's
            #   GeoConvert, which may represent MGRS square coord by its center
            # TODO: Generate populated places MGRS using geotrans
            placement = 4
            if name.startswith('Amundsen'):
                # South Pole station that fails MGRS->WGS for placement > 1
                placement = 1
            self.assertAlmostEqual(lat2, lat, places=placement)
            self.assertAlmostEqual(lon2, lon, places=placement)

            lineno += 1
