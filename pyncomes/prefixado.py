import workdays

import datetime


class prefixado:

    def __init__(self, id, v, d0, ndays, taxa_a):
        self.id = id
        self.v = v
        self.d0 = d0
        self.ndays = ndays
        self.taxa_a = taxa_a

    def now(self):
        return self.at(datetime.date.today())

    def at(self, dt):

        days = workdays.networkdays(self.d0, dt)
        t = pow(1.0 + self.taxa_a / 100, 1.0 / 252)

        vf = self.v * pow(t, days)

        return vf

    def end(self):
        return self.at(self.d0 + datetime.timedelta(days=self.ndays))
