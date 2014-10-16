# -*- coding: utf-8 -*-
#    Copyright (C) 2013  Christian Ledermann
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301  USA
import csv
import unittest
from .counter import count_search, count_user, save_csv

class BasicTestCase(unittest.TestCase):

    def test_count_user(self):
        self.assertTrue(len(count_user('christian.ledermann')) > 0)
        self.assertTrue(len(count_user('christian.ledermann', 'Maintainer')) > 0)

    def test_count_search(self):
        self.assertTrue(len(count_search(name='collective.geo')) > 0)

    def test_save_csv(self):
        package_list= [(1547, 244, 40, 12857, 9, u'2012-06-27T11:26:39', 'fastkml')]
        save_csv(package_list, 'test')






def test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(BasicTestCase))
    return suite

if __name__ == '__main__':
    unittest.main()
