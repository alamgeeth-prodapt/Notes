# import threading

# def worker():
#     print("thread's doing his job")

# t0 = threading.Thread(target=worker)

# t0.start()
# t0.join()

# import threading
# import time

# def worker(name):
#     for i in range(5):
#         print(name,i)
#         time.sleep(1)
# if __name__ == "__main__":
#     t1 = threading.Thread(target=worker,args=("t1",))
#     t2 = threading.Thread(target=worker,args=("t2",))

#     t1.start()
#     t2.start()

#     t1.join()
#     print("t1 joined")
#     t2.join()
#     print("t2 joined")

#     print("finished")

# from concurrent.futures import ThreadPoolExecutor
# import threading
# import time
# def sqr(x):
#     print(threading.get_ident())
#     time.sleep(2)
#     return x*x

# with ThreadPoolExecutor(max_workers=5) as exec:
#     res = exec.map(sqr,[1,2,3,4,5])

# print(list(res))

# import unittest

# class testcals(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(3+3,5)

# if __name__ == "__main__":
#     unittest.main()
