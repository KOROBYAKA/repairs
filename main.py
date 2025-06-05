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



#Returns results that are used as Data for plotting
#dict format FEC_SIZE:[20%-results,10%-10%-results]
def test(fec_list, nodes):
    results = {}
    for FEC_SIZE in fec_list:
        res = []
        print(f'FEC Size: {FEC_SIZE}')
        losses = [1] * 32
        for x in range(11, 17):
            losses[x] = 0
        batches = [Batch(FEC_SIZE) for x in range(0, nodes)]
        for x in range(0, 31):
            send_shreds(batches, FEC_SIZE, losses[x])
        reps = count_repairs(batches)
        print(f'20% repairs:{reps}')
        res.append(reps)
        losses = [1] * 32
        for x in [5,6,7,21,22,23,24]:
            losses[x] = 0
        batches = [Batch(FEC_SIZE) for x in range(0, nodes)]
        for x in range(0, 31):
            send_shreds(batches, FEC_SIZE, losses[x])
        reps = count_repairs(batches)
        print(f'10%-10% repairs:{reps}')
        res.append(reps)
        results[FEC_SIZE] = res

    return results


def plot_results(data, fec_list,nodes):
    big_blob = []
    small_blob = []
    for item in data.values():
        big_blob.append(item[0])
        small_blob.append(item[1])
    x_positions = range(len(fec_list))
    plt.plot(x_positions, big_blob)
    plt.plot(x_positions, small_blob)
    plt.xticks(ticks=x_positions, labels=fec_list)
    plt.title(f"{nodes} nodes")
    plt.xlabel("FEC Sizes")
    plt.ylabel(f"Total amount of repair requests for {nodes} nodes")
    plt.legend(["20% one loss"," 10%+10% losses"])
    plt.grid()
    plt.show()



def main():
    nodes = 10000
    fec_list = [32,64,128,256,512]
    results = test(fec_list, nodes)
    plot_results(results,fec_list,nodes)


if __name__ == "__main__":              
    main()