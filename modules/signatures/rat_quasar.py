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

from lib.cuckoo.common.abstracts import Signature


class QuasarMutexes(Signature):
    name = "rat_quasar_mutexes"
    description = "Creates known Quasar mutexes"
    severity = 3
    categories = ["rat"]
    families = ["QuasarRAT"]
    authors = ["wmetcalf"]
    references = ["6a243d91a8253c474a88a7818c487b5caab65eb7764e2861ee131678a991737a"]
    minimum = "0.5"

    def run(self):
        indicators = [
            "^QSR_MUTEX",
        ]

        for indicator in indicators:
            if self.check_mutex(pattern=indicator, regex=True):
                return True

        return False
