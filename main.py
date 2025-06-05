from numpy import random
import matplotlib.pyplot as plt
from batch import Batch


def send_shreds(batches, FEC_SIZE, flag):
    for batch in batches:
        amount = random.randint(0,int(FEC_SIZE/16))
        if (batch.shreds_snd + amount) >= FEC_SIZE:
            batch.transit_cache = FEC_SIZE - batch.shreds_snd
            batch.shreds_snd = FEC_SIZE
        else:
            batch.send_shreds(amount)

        if flag:
            batch.rcv_shreds()
        batch.transit_cache = 0


def count_repairs(batches):
    repairs = 0
    for batch in batches:
        repairs += batch.count_repairs()
    return repairs

def test(fec_list, nodes):
    for FEC_SIZE in fec_list:
        print(f'FEC Size: {FEC_SIZE}')
        losses = [1] * 32
        for x in range(11, 17):
            losses[x] = 0
        batches = [Batch(FEC_SIZE) for x in range(0, nodes)]
        for x in range(0, 31):
            send_shreds(batches, FEC_SIZE, losses[x])
        print(f'20% repairs:{count_repairs(batches)}')

        losses = [1] * 32
        for x in [5,6,7,21,22,23,24]:
            losses[x] = 0
        batches = [Batch(FEC_SIZE) for x in range(0, nodes)]
        for x in range(0, 31):
            send_shreds(batches, FEC_SIZE, losses[x])
        print('10%-10% repairs:', count_repairs(batches))


def main():
    nodes = 100000
    fec_list = [32,64,128,256,512]
    test(fec_list, nodes)


if __name__ == "__main__":              
    main()