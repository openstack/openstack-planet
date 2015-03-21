import ConfigParser
import logging
import os

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger("openstack-planet")

cp = ConfigParser.ConfigParser()
cp.read("planet.ini")

assert cp.get('Planet', 'output_dir') == '/srv/planet/openstack'

for i in cp.sections():
    try:
        assert os.path.isfile(os.path.join('images', cp.get(i, 'face')))
    except ConfigParser.NoOptionError:
        pass
    except AssertionError:
        raise IOError('Image not correct for %s' % i)
