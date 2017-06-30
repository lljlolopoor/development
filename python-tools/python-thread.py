# coding:utf-8
import threading
import time

lock = threading.RLock()

#方法一：将要执行的方法作为参数传给Thread的构造方法
def action(arg):
    lock.acquire()
    time.sleep(0.5)
    print  'sub thread start!the thread name is:%s\r' % threading.currentThread().getName()
    print 'the arg is:%s\r' %arg
    lock.release()

for i in xrange(40):
    t =threading.Thread(target=action,args=(i,))
    t.start()

print 'main thread end!'