import time


# def time():
#     start = input("Press 1 to start the timer")
#     print("The Timer has started")
#     begin = time.time()
#     end = input("Press 2 to stop the time")
#     end = time.time()
#     elapsed = end.begin
#     print("The time elapsed is", elapsed, "seconds")


# if __name__ == '__main__':
#     time()

start = input("Press 1 to start the timer :")
print("The Timer has started")
begin = time.time()
end = input("Press 2 to stop the time :")
end = time.time()
elapsed = end-begin
print("The time elapsed is", elapsed, "seconds")

