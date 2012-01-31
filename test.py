import ConfigParser

cp = ConfigParser.ConfigParser()
cp.read("planet.ini")

if cp.get('Planet', 'output_dir') != '/srv/planet':
  sys.exit(1)

