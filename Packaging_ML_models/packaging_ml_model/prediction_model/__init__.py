# this will show the version of package while import
import os
from prediction_model.config import config

with open(os.path.join(config.PACKAGE_ROOT, 'VERSION')) as f:
    __version__ = f.read().strip()
    