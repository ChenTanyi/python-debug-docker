import os
import sys
import time
import ptvsd
ptvsd.enable_attach("my_secret", address=('0.0.0.0', 3000))

if __name__ == '__main__':
  count = 0
  while 1:
    print('Hello {0}'.format(count))
    count += 1
    time.sleep(1) 