from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns
from batch import Batch

def listmaker(n):
    listofones = [1] * n
    return listofones



def send_shreds(batches, FEC_SIZE):

    for batch in batches:
        amount = random.randint(0,int(FEC_SIZE/10))
        if (FEC_SIZE - 10) <= batch.shreds_rcv:
            batch.shreds_rcv = FEC_SIZE
        else:
            batch.rcv_shreds(amount)


def count_repairs(batches):
    repairs = 0
    for batch in batches:
        repairs += batch.count_repairs()
    return repairs

def main():
    FEC_SIZE = 64
    losses = listmaker(16)
    for x in range(5,8):
        losses[x] = 0
    batches = [Batch(x, FEC_SIZE) for x in range(0,10000)]

    for x in range (0,15):
        if losses[x] : send_shreds(batches,FEC_SIZE)
    print('reps:',count_repairs(batches))

    FEC_SIZE = 128

    plt.show()

    losses = listmaker(16)
    for x in range(5,8):
        losses[x] = 0
    batches = [Batch(x, FEC_SIZE) for x in range(0,10000)]
    
    for x in range (0,15):
        if losses[x] : send_shreds(batches,FEC_SIZE)
    print('reps:',count_repairs(batches))


if __name__ == "__main__":              
    main()