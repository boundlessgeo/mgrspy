# -*- coding: utf-8 -*-
"""
***************************************************************************
    __init__.py
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

from tests.mrgstest import MgrsTest
from tests.utilstest import UtilsTest


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(UtilsTest, 'test'))
    suite.addTests(unittest.makeSuite(MgrsTest, 'test'))

    return suite
