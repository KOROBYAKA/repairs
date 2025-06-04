class Batch:
    def __init__(self,id,fec_size):
        self.id = id
        self.shreds_rcv = 0
        self.fec_size = fec_size

    def send_shreds(self, shreds):
        self.shreds_sent += shreds

    def rcv_shreds(self, shreds):
        self.shreds_rcv += shreds

    def count_repairs(self):
        if (self.shreds_rcv < (self.fec_size/2)):
            return ((self.fec_size/2) - self.shreds_rcv)
        return 0

