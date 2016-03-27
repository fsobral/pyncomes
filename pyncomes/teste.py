import util
import td_prefixado
import datetime

if __name__ == "__main__":

    td = td_prefixado.td_prefixado(1000,15.0,datetime.date(2015,01,01),datetime.date(2017,01,01),lambda x: 0.03 / (252 * 100))

    td.venda(1060)

    td.recompra(1200)
