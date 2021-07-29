import time, sys, itertools,threading

done = False
def animate():
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rcalculating pp ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)

length = float(input("What is the length of the pp(inches): "))

time.sleep(1)

if(length>5.2):
    longEnough = "big"
else:
    longEnough = "not big"

t.start()

time.sleep(3)
done = True

time.sleep(1)

print("This pp is " + longEnough)

time.sleep(5)


