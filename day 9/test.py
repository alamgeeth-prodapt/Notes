# from multiprocessing import Process
# import time
# import os

# def worker(name):
#     for i in range(3):
#         print(name, i)
#         time.sleep(1)
#     print(os.getpid())

# if __name__=="__main__":
#     p = Process(target = worker, args=("proc-1",))
#     p1 = Process(target= worker, args=("proc-2",))
#     p.start()
#     p1.start()

#     p.join()
#     p1.join()

#     print("main process")

from multiprocessing import Pool,Process
import time
import os

def sqr(num):
    print(num,os.getpid())
    time.sleep(2)
    return num * num

if __name__ == "__main__":
    ls = [x for x in range(100)]
    with Pool(5) as pool:
        print(pool.map(sqr,ls))
