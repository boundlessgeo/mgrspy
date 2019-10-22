# -*- coding: utf-8 -*-
"""
***************************************************************************
    utilstest.py
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

import unittest

from mgrspy import mgrs


class UtilsTest(unittest.TestCase):

    def testEpgsFromWgsCoordinates(self):
        hemisphere, zone, epsg = mgrs._epsgForWgs(0, 0)
        self.assertEqual(hemisphere, 'N')
        self.assertEqual(zone, 31)
        self.assertEqual(epsg, 32631)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, 0)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 31)
        self.assertEqual(epsg, 32731)

        hemisphere, zone, epsg = mgrs._epsgForWgs(45, 0)
        self.assertEqual(hemisphere, 'N')
        self.assertEqual(zone, 31)
        self.assertEqual(epsg, 32631)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, -180)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 1)
        self.assertEqual(epsg, 32701)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, 180)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 1)
        self.assertEqual(epsg, 32701)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, -60)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 21)
        self.assertEqual(epsg, 32721)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, 60)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 41)
        self.assertEqual(epsg, 32741)

        hemisphere, zone, epsg = mgrs._epsgForWgs(-45, 185)
        self.assertEqual(hemisphere, 'S')
        self.assertEqual(zone, 1)
        self.assertEqual(epsg, 32701)

        with self.assertRaises(mgrs.MgrsException):
            hemisphere, zone, epsg = mgrs._epsgForWgs(-95, 60)


    def testEpsgFromUtmParameters(self):
        epsg = mgrs._epsgForUtm(31, 'N')
        self.assertEqual(epsg, 32631)

        epsg = mgrs._epsgForUtm(31, 'S')
        self.assertEqual(epsg, 32731)

        epsg = mgrs._epsgForUtm(1, 'S')
        self.assertEqual(epsg, 32701)

        epsg = mgrs._epsgForUtm(1, 'N')
        self.assertEqual(epsg, 32601)

        epsg = mgrs._epsgForUtm(21, 'S')
        self.assertEqual(epsg, 32721)

        epsg = mgrs._epsgForUtm(41, 'S')
        self.assertEqual(epsg, 32741)

        epsg = mgrs._epsgForUtm(0, 'S')
        self.assertEqual(epsg, 32761)

        epsg = mgrs._epsgForUtm(0, 'N')
        self.assertEqual(epsg, 32661)

        # invaid hemisphere
        with self.assertRaises(mgrs.MgrsException):
            epsg = mgrs._epsgForUtm(31, 'K')

        # invaid zone
        with self.assertRaises(mgrs.MgrsException):
            epsg = mgrs._epsgForUtm(62, 'S')


    def testCheckZone(self):
        self.assertTrue(mgrs._checkZone('02HKK5607125582'), True)
        self.assertTrue(mgrs._checkZone('02HKK560255'), True)
        self.assertTrue(mgrs._checkZone('02HKK'), True)

        self.assertTrue(mgrs._checkZone('18SUJ2338308450'), True)
        self.assertTrue(mgrs._checkZone('18SUJ233084'), True)
        self.assertTrue(mgrs._checkZone('18SUJ'), True)

        self.assertFalse(mgrs._checkZone('  YYB4951249156'), False)
        self.assertFalse(mgrs._checkZone('YYB4951249156'), False)
        self.assertFalse(mgrs._checkZone('YYB495491'), False)
        self.assertFalse(mgrs._checkZone('YYB'), False)

        self.assertFalse(mgrs._checkZone('00YYB4951249156'), False)
        self.assertFalse(mgrs._checkZone('00YYB4951249156'), False)
        self.assertFalse(mgrs._checkZone('0YYB495491'), False)
        self.assertFalse(mgrs._checkZone('0YYB'), False)

        # zone with 3 digits
        with self.assertRaises(mgrs.MgrsException):
            mgrs._checkZone('181SUJ2338308450')


    def testMgrsStringBreak(self):
        zone, letters, easting, northing, precision = mgrs._breakMgrsString('18SUJ2338308450')
        self.assertEqual(zone, 18)
        self.assertEqual(letters, [18, 20, 9])
        self.assertEqual(easting, 23383.0)
        self.assertEqual(northing, 8450.0)
        self.assertEqual(precision, 5)

        zone, letters, easting, northing, precision = mgrs._breakMgrsString('18SUJ233084')
        self.assertEqual(zone, 18)
        self.assertEqual(letters, [18, 20, 9])
        self.assertEqual(easting, 23300.0)
        self.assertEqual(northing, 8400.0)
        self.assertEqual(precision, 3)

        zone, letters, easting, northing, precision = mgrs._breakMgrsString('18SUJ')
        self.assertEqual(zone, 18)
        self.assertEqual(letters, [18, 20, 9])
        self.assertEqual(easting, 0.0)
        self.assertEqual(northing, 0.0)
        self.assertEqual(precision, 0)

        zone, letters, easting, northing, precision = mgrs._breakMgrsString('  YYB4951249156')
        self.assertEqual(zone, 0)
        self.assertEqual(letters, [24, 24, 1])
        self.assertEqual(easting, 49512.0)
        self.assertEqual(northing, 49156.0)
        self.assertEqual(precision, 5)

        zone, letters, easting, northing, precision = mgrs._breakMgrsString('    YYB4951249156')
        self.assertEqual(zone, 0)
        self.assertEqual(letters, [24, 24, 1])
        self.assertEqual(easting, 49512.0)
        self.assertEqual(northing, 49156.0)
        self.assertEqual(precision, 5)

        zone, letters, easting, northing, precision = mgrs._breakMgrsString('YYB4951249156')
        self.assertEqual(zone, 0)
        self.assertEqual(letters, [24, 24, 1])
        self.assertEqual(easting, 49512.0)
        self.assertEqual(northing, 49156.0)
        self.assertEqual(precision, 5)
