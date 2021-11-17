# -*- coding: utf-8 -*-
# Copyright (C) 2021 Greenbone Networks GmbH
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from ...gmpv2110 import Gmpv2110TestCase
from ...gmpv208.entities.scanners import (
    GmpCloneScannerTestMixin,
    GmpDeleteScannerTestMixin,
    GmpGetScannerTestMixin,
    GmpGetScannersTestMixin,
)
from .scanners import (
    GmpCreateScannerTestMixin,
    GmpModifyScannerTestMixin,
)


class Gmpv2110DeleteScannerTestCase(
    GmpDeleteScannerTestMixin, Gmpv2110TestCase
):
    pass


class Gmpv2110GetScannerTestCase(GmpGetScannerTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110GetScannersTestCase(GmpGetScannersTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110CloneScannerTestCase(GmpCloneScannerTestMixin, Gmpv2110TestCase):
    pass


class Gmpv2110CreateScannerTestCase(
    GmpCreateScannerTestMixin, Gmpv2110TestCase
):
    pass


class Gmpv2110ModifyScannerTestCase(
    GmpModifyScannerTestMixin, Gmpv2110TestCase
):
    pass