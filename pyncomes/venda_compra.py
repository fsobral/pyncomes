import datetime
import workdays
import util
import math


def vc(V, i1, i2, t0, d, tf):

    """
    Calculates the limit value for selling a title
    """

    return vc_alpha(1.0, V, i1, i2, t0, d, tf)


def vc_alpha(alpha, V, i1, i2, t0, d, tf):

    """
    Calculates the limit value for selling a title, given a
    percentage 'alpha'
    """

    hoje = datetime.date.today()

    Nhoje = (hoje - t0).days

    N = workdays.networkdays(t0, tf)
    Nc = (tf - t0).days

    proxInv = hoje + datetime.timedelta(days=d)

    Nprox = workdays.networkdays(proxInv, tf)
    Nproxc = (tf - proxInv).days

    print "\nN: {0:4d}, N Corr: {1:4d}, N Hoje: {2:4d}, " \
        "N Prox: {3:4d}, N Prox Corr: {4:4d}\n".format(
            N, Nc, Nhoje, Nprox, Nproxc)

    i1d = math.pow(1.0 + i1, 1.0 / util.DIASANO) - 1.0
    i2d = math.pow(1.0 + i2, 1.0 / util.DIASANO) - 1.0

    t1 = util.ir(Nc) + (1.0 - util.ir(Nc)) * math.pow(1.0 + i1d, N)
    t2 = util.ir(Nproxc) + (1.0 - util.ir(Nproxc)) * math.pow(1.0 + i2d, Nprox)

    vLim = (alpha * t1 / (t2 * (1.0 - util.ir(Nhoje))) -
            util.ir(Nhoje) / (1.0 - util.ir(Nhoje))) * V

    return vLim
