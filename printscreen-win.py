import ctypes
import os
from datetime import datetime
from PIL import ImageGrab

try:
   userHome = os.path.expanduser('~')
   desktopPath = userHome + '/Desktop/'

   im = ImageGrab.grab()
   dt = datetime.today().strftime("%y%m%d-%H%M%S")
   imgPath = 'screen-%s.png' % dt
   srcPath = os.path.join(desktopPath, 'screen')
   if not os.path.exists(srcPath):
     os.makedirs(scrPath)
   imgPath = os.path.join(srcPath, imgPath)
   im.save(imgPath,'PNG')
   print('Saved to: %s' % imgPath)
   ctypes.windll.user32.MessageBoxA(0, "Stored as: %s" % imgPath, "Print Screen", 0)
except Exception as e:
   print('Error: %s' % str(e))
