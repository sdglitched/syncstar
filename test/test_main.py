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

"""
from os.path import abspath, realpath
from tempfile import TemporaryDirectory

import pytest
from click.testing import CliRunner

from syncstar.main import main


@pytest.mark.parametrize(
    "work, code, text",
    [
        pytest.param(
            False,
            1,
            [
                "Images file for 'AAAAAAAAAAAAAAAA' was not found"
            ],
            id="Negative parameters",
        ),
    ]
)
def test_main(caplog, work, code, text):
    runner = CliRunner()
    with TemporaryDirectory(prefix="syncstar-test-") as tempdrct:
        temppath = f"{tempdrct}/images.yml"
        yamlpath = abspath(realpath(__file__)).replace("test_main.py", "data/images.yml")
        with open(yamlpath) as yamlfile:
            yamldata = yamlfile.read().replace("LOCATION", temppath if work else "LOCATION")
        with open(temppath, "w") as yamlfile:
            yamlfile.write(yamldata)
        result = runner.invoke(main, f"--images {temppath}")
        if work:
            raise KeyboardInterrupt
        print(result.output)
        assert result.exit_code == code
        for indx in text:
            assert indx in caplog.text
"""
