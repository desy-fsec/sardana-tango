#!/usr/bin/env python

from setuptools import setup
from datetime import datetime

release = datetime.today().strftime('%Y.%m.%d.%H.%M').replace(".0", ".")

package_dir = {"sardana.PoolController.sardana_tango": "sardana_tango/ctrl"}

packages = ["sardana.PoolController.sardana_tango"]

provides = ['sardana_tango']


setup(name='sardana_tango',
      version=release,
      author="Sardana Controller Developers",
      author_email="sardana-devel@lists.sourceforge.net",
      maintainer="ALBA",
      maintainer_email="sardana-devel@lists.sourceforge.net",
      url="https://github.com/ALBA-Synchrotron/sardana-tango",
      packages=packages,
      package_dir=package_dir,
      include_package_data=True,
      provides=provides,
      )
