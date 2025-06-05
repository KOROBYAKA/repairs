class Batch:
    def __init__(self,fec_size):
        self.shreds_snd = 0
        self.transit_cache = 0
        self.shreds_rcv = 0
        self.fec_size = fec_size

    def send_shreds(self, shreds):
        self.shreds_snd += shreds
        self.transit_cache = shreds


    def rcv_shreds(self):
        if self.shreds_rcv + self.transit_cache > self.fec_size: self.shreds_rcv = self.fec_size
        else:
            self.shreds_rcv += self.transit_cache
        self.transit_cache = 0

    def count_repairs(self):
        if (self.shreds_rcv < (self.fec_size/2)):
            return ((self.fec_size/2) - self.shreds_rcv)
        return 0

