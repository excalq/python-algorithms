import os
import glob
import humansize
from pprint import pprint

dir = '/Users/arthur/Hacking/Android/AndroidSDK/samples/android-23/legacy/ApiDemos/res/layout/'
path = os.path.join(dir, '*.xml')
xml = [(humansize.approximate_size(os.stat(f).st_size), f) for f in glob.glob(path)] 
pprint(xml, width=260)
