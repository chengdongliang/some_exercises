

"""
threading
创建Thread实例，传给它一个可以调用的类实例
"""

import threading
from time import ctime, sleep

loops = [4, 2]

class ThreadFunc(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args
        print(self.name)
    # 实现了__call__方法的对象，相当于重载了（），可以实现调用功能
    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at: ', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at: ', ctime())

def main():
    print('starting at: ', ctime)
    threads = []
    nloops = range(len(loops))
    for i in nloops:
        t = threading.Thread(target=ThreadFunc(loop, (i, loops[i]), loop.__name__))
        threads.append(t)
    
    for i in nloops:
        threads[i].start()
    
    for i in nloops: # 等待锁释放
        threads[i].join()
    print('all done at: ', ctime())

if __name__=='__main__':
    main()