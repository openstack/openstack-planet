import ConfigParser

cp = ConfigParser.ConfigParser()
cp.read("planet.ini")

assert cp.get('Planet', 'output_dir') == '/srv/planet/openstack'
