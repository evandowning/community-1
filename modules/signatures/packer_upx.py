# Copyright (C) 2012,2015 Michael Boman (@mboman), Optiv, Inc. (brad.spengler@optiv.com)
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


class UPXCompressed(Signature):
    name = "packer_upx"
    description = "The executable is compressed using UPX"
    severity = 2
    categories = ["packer"]
    authors = ["Michael Boman", "nex", "Optiv"]
    minimum = "1.3"
    ttp = ["T1045"]

    def run(self):
        if "static" in self.results and "pe" in self.results["static"]:
            if "sections" in self.results["static"]["pe"]:
                for section in self.results["static"]["pe"]["sections"]:
                    if section["name"].startswith("UPX"):
                        descmsg = "name: {0}, entropy: {1}, characteristics: {2}, raw_size: {3}, virtual_size: {4}".format(
                            section["name"],
                            section["entropy"],
                            section["characteristics"],
                            section["size_of_data"],
                            section["virtual_size"],
                        )
                        self.data.append({"section": descmsg})
                        return True

        return False
