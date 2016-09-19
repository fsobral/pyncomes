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

    Nhoje = workdays.networkdays(t0, hoje)

    N = workdays.networkdays(t0, tf)

    proxInv = hoje + datetime.timedelta(days=d)

    Nprox = workdays.networkdays(proxInv, tf)

    print N, Nhoje, Nprox

    i1d = math.pow(1.0 + i1, 1.0 / util.DIASANO) - 1.0
    i2d = math.pow(1.0 + i2, 1.0 / util.DIASANO) - 1.0

    t1 = util.ir(N) + (1.0 - util.ir(N)) * math.pow(1.0 + i1d, N)
    t2 = util.ir(Nprox) + (1.0 - util.ir(Nprox)) * math.pow(1.0 + i2d, Nprox)

    vLim = (alpha * t1 / (t2 * (1.0 - util.ir(Nhoje))) -
            util.ir(Nhoje) / (1.0 - util.ir(Nhoje))) * V

    return vLim
