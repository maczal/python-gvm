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

from ...gmpv208 import Gmpv208TestCase
from ...gmpv208.entities.port_lists import (
    GmpClonePortListTestMixin,
    GmpCreatePortListTestMixin,
    GmpCreatePortRangeTestMixin,
    GmpDeletePortListTestMixin,
    GmpDeletePortRangeTestMixin,
    GmpGetPortListsTestMixin,
    GmpGetPortListTestMixin,
    GmpModifyPortListTestMixin,
)


class Gmpv208ClonePortListTestCase(GmpClonePortListTestMixin, Gmpv208TestCase):
    pass


class Gmpv208CreatePortListTestCase(
    GmpCreatePortListTestMixin, Gmpv208TestCase
):
    pass


class Gmpv208CreatePortRangeListTestCase(
    GmpCreatePortRangeTestMixin, Gmpv208TestCase
):
    pass


class Gmpv208DeletePortListTestCase(
    GmpDeletePortListTestMixin, Gmpv208TestCase
):
    pass


class Gmpv208DeletePortRangeTestCase(
    GmpDeletePortRangeTestMixin, Gmpv208TestCase
):
    pass


class Gmpv208GetPortListTestCase(GmpGetPortListTestMixin, Gmpv208TestCase):
    pass


class Gmpv208GetPortListsTestCase(GmpGetPortListsTestMixin, Gmpv208TestCase):
    pass


class Gmpv208ModifyPortListTestCase(
    GmpModifyPortListTestMixin, Gmpv208TestCase
):
    pass
