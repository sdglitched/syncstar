"""
SyncStar
Copyright (C) 2024 Akashdeep Dhar

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
details.

You should have received a copy of the GNU General Public License along with
this program.  If not, see <https://www.gnu.org/licenses/>.

Any Red Hat trademarks that are incorporated in the source code or
documentation are not subject to the GNU General Public License and may only
be used or replicated with the express permission of Red Hat, Inc.
"""

from sys import exit

import os.path

from syncstar.config import standard

from os import urandom

from yaml import safe_load, YAMLError

from syncstar import view


def keep_config(port: int, repair: bool, period: int) -> None:
    # Generate a secret code for the frontend to authenticate with the service
    standard.code = urandom(8).hex().upper()

    # Keep the configuration variables served in the command for consumption
    standard.port = port
    standard.repair = repair
    standard.period = period
    if repair == True:
        standard.logrconf["handlers"]["console"]["level"] = "DEBUG"
        standard.logrconf["root"]["level"] = "DEBUG"


def isos_config(images: str) -> None:
    # Check the validity of the images configuration file before saving the contents
    with open(images, "r") as yamlfile:
        try:
            imdict = safe_load(yamlfile)
            if imdict is not None:
                for indx in imdict:
                    if os.path.exists(imdict[indx]["path"]):
                        view.general(f"Checking image file for '{imdict[indx]['name']}'...")
                        imdict[indx]["size"] = os.path.getsize(imdict[indx]["path"])
                        continue
                    else:
                        view.failure(f"Images file for '{imdict[indx]['name']}' was not found")
                        exit(1)
                standard.images = images
                standard.imdict = imdict
                print(standard.imdict)
            else:
                view.failure("Invalid images configuration file detected")
                exit(1)
        except YAMLError as expt:
            view.failure("Invalid images configuration file detected")
            exit(1)
