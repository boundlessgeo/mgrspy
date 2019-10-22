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

import unittest

from mgrspy import mgrs


class MgrsTest(unittest.TestCase):

    def testSouthPoleCoordinates(self):
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

    def testNorthPoleCoordinates(self):
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
