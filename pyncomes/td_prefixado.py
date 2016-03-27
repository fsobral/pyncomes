import datetime;
import workdays;
import util;

from math import *

class td_prefixado:

    def __init__(self,v,t,dataIni,dataEnd,c,ir=util.ir,iof=util.iof):
        self.v = v
        self.t = pow(1.0 + t / 100.0, 1.0 / util.DIASANO)
        self.c = c
        self.ir = ir
        self.iof = iof
        self.dataIni = dataIni
        self.dataEnd = dataEnd

    def venda(self,valor,data=datetime.date.today()):
        days = workdays.networkdays(self.dataIni, data)

        vf = valor - (valor - self.v) * (self.ir(days) / 100.0) - self.v * self.c(days)

        lucro = (vf - self.v) / self.v

        lucroaa = pow(1.0 + lucro, util.DIASANO / days) - 1

        print("Valor inicial: {0:10.2f}\nValor final: {1:10.2f}\nLucro: {2:10.9f}\nLucro a.a.: {3:10.9f}".format(self.v, vf, lucro,lucroaa))

    def __caso1(self):
    
        fullDays = workdays.networkdays(self.dataIni, self.dataEnd)

        return self.v

    def __caso3(self,valor,dias,taxa,diasRest):

        return (valor * (1.0 - self.ir(dias)) + self.v * \
                (self.ir(dias) - self.c(dias))) * ((1.0 - self.ir(diasRest)) * \
                                                   pow(1.0 + taxa, diasRest) + self.ir(diasRest) - \
                                                   self.c(diasRest))

    def recompra(self,valor):

        data = datetime.date.today()

        days = workdays.networkdays(self.dataIni, data)
        # TODO: verificar se coloco mais 4 dias para compensacao
        nextDays = workdays.networkdays(data,self.dataEnd)

        fullDays = workdays.networkdays(self.dataIni, self.dataEnd)

        rr = pow(self.v * ((1.0 - self.ir(fullDays) / 100.0) * pow(self.t, fullDays) + \
                           self.ir(fullDays) / 100.0 - self.c(fullDays)) / \
                 ((1.0 - self.ir(nextDays) / 100.0) * (valor * (1.0 - self.ir(days) / 100.0) + \
                                                       self.v * (self.ir(days) / 100.0 - self.c(days)))) \
                 - (self.ir(nextDays) / 100.0 - self.c(nextDays)) / (1.0 - self.ir(nextDays) / 100.0), \
                 1.0 / nextDays)

        print("\nDias investidos {0:4d}\nDias restantes {1:4d}\nValor de venda {2:10.2f}\nJuros minimo para recompra {3:10.2f}%\nSe recomprar com tais juros, lucro de {4:10.2f}".format(days, nextDays, valor, (pow(rr, util.DIASANO) - 1.0) * 100.0), 0)
        
        
